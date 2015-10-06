.. _GPUPG:

GPU Compute Programming Guide
=============================

.. contents:: Table of Contents
  :local:

This document provides an outline of KL programing with GPU Compute (currently for Nvidia CUDA hardware) covering some details of its implementation in addition to explaining how it can be used in KL code. Everything in this document assumes that the user has correctly enabled CUDA GPU compute support as outlined in the :ref:`GPUCompute`.

As GPU compute is still a relatively new feature there may be additional changes in its API as it evolves and we are always interested in feedback and suggestions from end users.

.. _gpupg-example:

KL Example
++++++++++

The following is an example of KL code using GPU compute and is provided as a starting point to further discussion. This particular code shows the syntax used to invoke an operator on the GPU but is not an example of an algorithm that is particularly well-suited to GPU execution.

.. kl-example:: GPU Compute
  :no-output:

  operator myComputeKernel<<<index>>>(Scalar input[], io Scalar output[])
  {
    output[index] = input[index] + Scalar(log(index));
  }

  operator entry()
  {
    Boolean runOnGPU = true;

    Scalar input[];
    input.resize(1024);
    for (Integer i=0; i<1024; i++)
      input[i] = i*i;
    input.convertToSVM();

    Scalar output[];
    output.convertToGPU();
    output.resize(1024);
    myComputeKernel<<<1024@runOnGPU>>>(input, output);
    output.convertToCPU();
    report(output);
  }

Invoking a GPU Operator
+++++++++++++++++++++++

GPU compute functionality is accessed in KL via the standard :ref:`KLPG.parallel-execution-statement` syntax on an operator plus an @ followed by a Boolean that evaluates to ``true``. Passing no parameter or ``false`` after the @ symbol will invoke the operator on the CPU.

On machines with no CUDA support, or where CUDA support has not been enabled or failed to load, passing an @true parameter to a :ref:`KLPG.parallel-execution-statement` call will invoke the operator in a simulated GPU environment on the CPU, which can sometimes be useful for testing. A message will be printed each time an operator is invoked in this way to ensure that the user is aware that this code is not running on the GPU despite the @true PEX call:

.. code-block:: none

  [FABRIC:MT] Falling back to running GPU operator on CPU

Type Support
++++++++++++

Not all KL types are supported on the GPU and in particular ``object``, ``interface``, and ``MapReduce`` operators are currently unsupported. KL will output an error if a user tries to run an operator that uses one of these types on the GPU. In addition ``Dict`` and ``String`` types cannot currently be passed as parameters to a GPU operator, though a GPU operator may make use of them internally. These limitations around types may be removed in an upcoming version based on feedback and relevant use cases.

The KL type that is most relevant to running operators on the GPU is the Variable Array as this maps most directly to use cases where the GPU operates in parallel on a large set (or sets) of input data. These variable arrays will often contain elements of a complex struct type, such as a :kl-ref:`Vec3` or an :kl-ref:`Xfo`. See the ``input`` and ``output`` arrays in the :ref:`gpupg-example`.

Memory Management
+++++++++++++++++

There are four types of memory made available in GPU compute so that the user can choose the type most suited to their needs. The three types are:

- *CPU*: Standard CPU memory, allocated on the heap via malloc(). This is the default backing memory for all types created on the CPU.

- *GPU*: Standard GPU-allocated memory. This type of memory is accessible only on the GPU and attempting to access it on the CPU will result in an error (in ``guarded`` mode) or a crash (in ``unguarded`` mode).

- *SVM*: SVM stands for Shared Virtual Memory and in the CUDA case represents what is referred to as CUDA Managed Memory. This type of memory is accessible both on the CPU and the GPU and data transfers are managed transparently by the Nvidia driver. This type of memory is easiest for new users as it does not require the user to track where memory lives. More experienced users however may require more fine-grained control.

- *GLBuffer*: GLBuffer is memory that was loaded into an OpenGL buffer and then bound for use in GPU compute operators. This type of memory will be discussed further in the "GL Binding" section.

Changing Memory Backing
^^^^^^^^^^^^^^^^^^^^^^^

All KL types support several methods to change where their backing memory lives. For most types (including all shallow types) these methods are a no-op as their backing memory is not owned by them. However in the case of Variable Arrays these methods change where the member elements of the Variable Array are stored. The three relevant methods are:

- ``myVar.convertToCPU()``

- ``myVar.convertToGPU()``

- ``myVar.convertToSVM()``

These methods convert the backing memory of the type to one of the three types of memory discussed above.

GL Binding
^^^^^^^^^^

There is an additional conversion method convertToGLBuffer() on Variable Arrays that allows converting their backing memory into a GL buffer which can be used in rendering in addition to GPU compute. This method requires that a valid GL context be bound at the time it's called and will otherwise result in an exception:

.. code-block:: none

  Exception: glewInit() call failed; is there a valid GL context bound?

A short example of using GL binding is provided here:

.. kl-example:: GL binding in KL
  :no-output:

  require FabricOGL;

  operator entry()
  {
    Scalar input[];
    input.resize(1024);

    // the convertToGLBuffer() call returns the GL buffer ID
    Integer bufferId = input.convertToGLBuffer(GL_ARRAY_BUFFER, GL_DYNAMIC_DRAW);

    // the GL buffer ID can also be retrieved later via the getBufferId() method
    bufferId = input.getBufferId();

    report('GL buffer ID is: '+bufferId);
    myGPUOperator<<<1024@true>>>(input);
  }

The parameters passed to convertToGLBuffer() are the same as the `target` and `usage` parameters normally passed to a `glBufferData()` call and can have the same values.

Determining Array Memory Location
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

KL provides a mechanism to determine where a given Variable Array's elements currently live using the getElementsMemType() method. A short example of its use is outlined here:

.. kl-example:: Variable Array Memory Types in KL
  :no-output:

  function printMemoryType(Vec3 myArray[])
  {
    if (myArray.getElementsMemType() == Fabric_MemType_CPU)
      report('Array elements are in CPU memory.');
    else if (myArray.getElementsMemType() == Fabric_MemType_GPU)
      report('Array elements are in GPU memory.');
    else if (myArray.getElementsMemType() == Fabric_MemType_SVM)
      report('Array elements are in Shared Virtual memory.');
    else if (myArray.getElementsMemType() == Fabric_MemType_GLBuffer)
      report('Array elements are stored in a GL buffer.');
  }

Memory and Resizing Arrays
^^^^^^^^^^^^^^^^^^^^^^^^^^

When using GPU compute the array resize() method resizes the allocated memory on the device where the memory resides. GL buffer-bound arrays can not be resized via the resize() method and will throw an error.

For memory types that are accessible on the CPU (CPU and SVM), the elements in a newly-resized array will be initialized using the default constructor for the element type of the array (for example initialized with the Vec3() constructor). For GPU memory the elements in a newly-resized array will be initialized to zeros. This is an important distinction to be aware of as it represents a difference in behavior between CPU and GPU arrays.

.. kl-example:: The resize() method
  :no-output:

  operator entry()
  {
    Vec3 a[];

    // array is resized to 1024 elements in CPU memory, all elements are
    // initialized with the Vec3() constructor
    a.resize(1024);

    // all 1024 elements are removed from CPU memory and transferred to GPU
    a.convertToGPU();

    // the array in GPU memory is resized to 2048 elements, the first 1024
    // hold their previous values while the new elements are initialized with 0s
    a.resize(2048);
  }


The copyTo() Array Method
^^^^^^^^^^^^^^^^^^^^^^^^^

The copyTo() method can be used to transfer data between arrays, regardless of where their memory is located. The method will resize the destination array to be of the same size as the source array. Memory location for the destination array will remain unchanged.

.. kl-example:: The copyTo() method
  :no-output:

  operator entry()
  {
    Vec3 a[];
    a.resize(1024);
    // ... fill 'a' with data ...

    Vec3 b[];
    b.resize(128);
    // ... fill 'b' with data ...
    b.convertToGPU();

    // resizes 'b' to 1024 elements (on GPU) and copies the values from 'a'
    a.copyTo(b);
  }

Parameter Passing
+++++++++++++++++

Parameters to a KL GPU operator can be of any supported type and as with any normal KL operator they can be passed as ``in`` (the default) or ``io`` parameters. Shallow type parameters (such as an ``Integer`` or a ``struct``) will have their values copied to and from the GPU before and after each parallel operator invocation. Variable Arrays on the other hand will only have a pointer to their values passed into the operator. The backing memory for the Variable Array elements must live in memory accessible to the target device.

In ``guarded`` mode, KL will perform checks on Variable Array parameters to ensure that their backing memory currently lives in an accessible memory space. If not a KL exception will be thrown to inform the user. As an example, the following KL code:

.. kl-example:: GPU Compute - Memory
  :no-output:

  operator entry()
  {
    Integer input[];
    input.resize(1024);
    Integer output[];
    output.resize(1024);
    myComputeKernel<<<1024@true>>>(input, output);
  }

Will result in the error message:

.. code-block:: none

  Error: input: data not available in GPU memory

Adding a ``convertToGPU()`` or ``convertToSVM()`` method call to the ``input`` and ``output`` parameters will resolve the error, as seen in the :ref:`gpupg-example`.

In ``unguarded`` mode KL code that uses device and CPU memory incorrectly will crash.


