.. _GPUCompute:

GPU Compute Guide
=================

.. image:: /images/FE_logo_345_60.*
   :width: 345px
   :height: 60px

| |FABRIC_PRODUCT_NAME| version |FABRIC_VERSION|
| |FABRIC_COPYRIGHT|

.. contents:: Table of Contents
  :local:

**Important - Read Me First**
-----------------------------

- GPU compute is not enabled by default in Fabric Engine applications and must be specifically enabled in the environment before it can be used.

- See the :ref:`GPUPG` for information on how KL code can be made to take advantage of GPU compute.

- Please look over the list of :ref:`gpu-known-issues`.

- It's important to be aware of guarded vs. unguarded mode when running on the GPU as its effects can be even more pronounced that on the CPU. Once code is debugged and known to be working there can sometimes be significant performance gains achieved by running in unguarded mode.

- GPU compute currently works on Windows 7 or higher and Linux (CentOS 6.x) 64-bit platforms with supported Nvidia hardware (see below).

Installation
------------

Nvidia Hardware Support
+++++++++++++++++++++++

KL GPU compute requires supported Nvidia hardware in order to run. Please ensure that your Nvidia card is supported by verifying the following:

- A card with Compute Capability of at least 3.0 is required. A list of GPUs and their compute capabilities is available here: https://developer.nvidia.com/cuda-gpus

- For supported cards the latest stable Nvidia driver must be installed: http://www.nvidia.com/Download/index.aspx?lang=en-us

- CUDA toolkit 6 or later must be installed from https://developer.nvidia.com/cuda-downloads The current version was built against CUDA 6.0 but should work up to CUDA toolkit 7.5


Enabling GPU Compute
++++++++++++++++++++

By default Fabric will not try to load Nvidia libraries and enable GPU compute unless the environment variable ``FABRIC_FEATURE_CUDA_COMPUTE=1`` is set. Once this is set Fabric will try to load the required libraries on startup and any errors encountered will be output to the console. 

GPU compute requires that the Nvidia libraries either be present in global system library locations or else be explicitly added to the PATH or LD_LIBRARY_PATH.

On Windows the required libraries are ``nvvm64_20_0.dll`` and ``nvcuda.dll`` and by default are installed in ``C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v6.0\bin`` and ``C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v6.0\nvvm\bin``. You may need to add these directories to your system PATH variable like this:

  ``PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v6.0\bin;C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v6.0\nvvm\bin;%PATH%``

On Linux the required libraries are ``libcuda.so`` and ``libnvvm.so`` and are usually found in ``/usr/local/cuda/lib64`` and ``/usr/local/cuda/nvvm/lib64``. You may want to update your LD_LIBRARY_PATH like this:

  ``LD_LIBRARY_PATH=/usr/local/cuda/lib64:/usr/local/cuda/nvvm/lib64:$LD_LIBRARY_PATH``

The ``CUDA_PATH`` environment variable must also be present on your system, though this is often set automatically by the CUDA toolkit.

A sample environment setup for CUDA compute on Linux might look like this:

.. code-block:: none

  export FABRIC_FEATURE_CUDA_COMPUTE=1
  export CUDA_PATH=/usr/local/cuda
  export LD_LIBRARY_PATH=$CUDA_PATH/lib64:$CUDA_PATH/nvvm/lib64:$LD_LIBRARY_PATH


Testing GPU Compute
+++++++++++++++++++

A GPU-enabled sample can be found under ``Samples/Canvas`` with the name nbody-gpu.canvas. As noted above, significant performance improvements can often be seen on the GPU by running canvas in unguarded mode with the -u flag.

KL Programming
--------------

See the :ref:`GPUPG` for more information on how to use GPU compute in KL.

.. _gpu-known-issues:

Known Issues
------------

- Kernels that take longer than 10 seconds to execute on the GPU will be terminated by the driver and return with CUDA_ERROR_LAUNCH_TIMEOUT. This timeout may be disabled in an upcoming release.

- Nvidia's compiler can take a very long time to compile large KL operators, especially in guarded mode. Compilation time in the Nvidia compiler (generating PTX assembly from the input LLVM IR) and CUDA operator loading (preparing the PTX code to be run on the GPU) are printed to the Fabric log when GPU compute is used. This is an area we are investigating to determine which types of operators slow down Nvidia's compiler the most and how we can mitigate this.

- On Linux an occasional hang in the Nvidia driver has been encountered that requires a full reboot in order to recover. This is a bug in the Nvidia driver and an issue has been filed with Nvidia. The bug appears related to running multiple KL applications in separate processes where all are using GPU compute simultaneously. For this reason it is recommended to run only a single Fabric process at a time with GPU compute.

- Using many Integer atomic functions in a single KL GPU operator may sometimes cause the operator to hang and not return (the Integer.atomic*() methods in KL).

