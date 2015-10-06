.. _cconv:

Calling Convention for Exported Functions
==========================================

.. warning::
  
  The use of the :command:`kl2edk` tool to generate the header file with the types and function prototypes corresponding to KL code has mostly made this section irrelevant, since you can now guarantee that you use the right calling convention for your extension functions by just copying the function prototypes from the generated header file.  However, we retain this section for reference and to help those looking for a deeper understanding of how KL interfaces with C++.

We saw in the :ref:`EAG.sample` section that to return a string from a function exported to KL it was necessary to declare the C++ function signature with the return value as a first parameter and with the C++ function returning ``void``.  In KL the function declaration was::

  function String GetHelloWorldString() = "GetHelloWorldString";

whereas the function definition in C++ was::

  FABRIC_EXT_EXPORT void GetHelloWorldString(
    Fabric::EDK::KL::String &result
    )
  {
    // ...
  }

In order to have the extension function called correctly from KL it is necessary in some cases to adjust the C++ function parameters and return type.  We refer to this as the *calling convention* for exported functions.

The rules for the calling convention are dependent on the types of the function parameters and the return type.  For the purpose of the calling convention, there are two kinds of types: *simple* types and *complex* types.

.. _cconv.simple:

Calling Convention for Simple Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The simple types are the small, predefined types; they are:

- ``Boolean``;
- The integer types: ``UInt8``, ``SInt8``, ``UInt16``, ``SInt16``, ``UInt32``, ``SInt32``, ``UInt64`` and ``SInt64``;
- The floating-point types: ``Float32`` and ``Float64``; and
- The aliases for simple types: ``Integer``, ``Byte``, ``Index``, ``Size`` and ``Scalar``.

See :ref:`types.simple` for more information about the simple types.

Simple types are directly returned from C++ functions and are directly passed by value as ``in`` parameters:

- When a KL function returns a simple type the corresponding C++ function should also return the same simple type.

- When a KL function takes a simple type as an ``in`` parameter the C++ function should also take the same simple type by value.

- When a KL function takes a simple type as an ``io`` parameter the C++ function should take the same simple type by reference.

For example, the KL function::

  // KL code
  
  function Boolean SimpleTypeFunc(
    UInt32 inParam,
    io Float32 ioParam
    ) = "SimpleTypeFuncImpl";

should have the C++ definition::

  // C++ code
  
  FABRIC_EXT_EXPORT Fabric::EDK::KL::Boolean SimpleTypeFuncImpl(
    Fabric::EDK::KL::UInt32 inParam,
    Fabric::EDK::KL::Float32 &ioParam
    )
  {
    // ...
    return true; // directly return value
  }

.. _cconv.complex:

Calling Convention for Complex Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The :ref:`complex types <types.complex>` are all the types that are not simple types.  They include:

- :ref:`KL::String <types.string>`
- All container types; see :ref:`types.container`
- All user-defined types; see :ref:`types.user-defined`

Complex types are always passed by reference.  Furthermore, in the case they are returned from functions the return value should be stored into a hidden first reference parameter; the resulting function should return void.  In order to simplify the use of this convention, the typedefs ``INParam``, ``IOParam`` and ``RetVal`` are provided for each built-in complex type; see 

In order to facilitate this, predefined complex types provide typedefs that help with this calling convention:

``KL::<ComplexType>::INParam``
  
  The type of an ``in`` parameter from KL.

``KL::<ComplexType>::IOParam``
  
  The type of an ``io`` parameter from KL.

``KL::<ComplexType>::Result``
  
  The type of a "hidden return parameter" in KL.
  
  .. note:: A hidden return parameter must always be the first parameter of the C++ function in which it is used.  This condition cannot be enforced by the ``FabricEDK.h`` header, therefore it is the programmer's responsibility to ensure it is met.

If you wish to provide these same typedefs in your custom structure definitions, use the ``FABRIC_EDK_COMPLEX_TYPE(TypeName)`` macro as demonstrated below.

For example, the following KL function declaration:

.. code-block:: kl
  
  struct MyType {
    String st;
  };
  
  function String myFunc(
    UInt32 uint32s[],
    io String dict[UInt32],
    MyType myType
    ) = "MyFunc";

should be represented by the following C++ function:

.. code-block:: c
  
  struct MyType
  {
    FABRIC_EDK_COMPLEX_TYPE(MyType)
    
    KL::String st;
  };
  
  FABRIC_EDK_EXPORT void MyFunc(
    KL::String::Result result, // hidden return parameter
    KL::VariableArray<KL::UInt32>::INParam uint32s,
    KL::Dict<KL::UInt32, KL::String>::IOParam dict,
    MyType::INParam myType
    )
  {
    // ...
  }

Mixing Simple and Complex Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is perfectly acceptable (and common) to mix simple and complex types in extension functions; you must simply follow the rules for each type individually.

