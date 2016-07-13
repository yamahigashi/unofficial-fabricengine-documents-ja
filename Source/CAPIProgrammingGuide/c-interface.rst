


.. c:function:: void FEC_Initialize()

  Initializes the CAPI interface. This function must be called before any other CAPI functions; it is often called immediately at application startup.






.. c:function:: void FEC_Finalize()

  Shuts down the CAPI interface. This function must be called right once all use of CAPI has finished; this is often at application exit.






.. c:function:: void FEC_EnableDebug( int runServer )

  This enables the Core debugger, turning off code optimization and embedding Dwarf debug info into all compiled code. If runServer is non-zero then the debug server process is also launched to take control of the Core process. Set runServer to 0 if you will use an external debugger like gdb.





.. _c-interface:

The C Language Interface
=========================

This chapter describes in detail the general practices that are required of an application that uses CAPI through the C language interface.  This chapter is not required reading if you do not plan on using the C language interface.

Namespacing
----------------------------

All types and function calls in the C language interface begin with the prefix :samp:`FEC_{...}`; for instance, :c:func:`FEC_ClientCreate`.  This both makes it easier to identify CAPI-related code as well minimizes the chance of namespace clashes with other code.

Object Lifecycles
----------------------------

Since the C language does not have an automatic mechanism for objects that go out-of-scope, the CAPI programmer using the C interface is responsible for manually managing the lifecycle of most of the objects returned from the C interface.

Reference-Counted Objects
^^^^^^^^^^^^^^^^^^^^^^^^^

All of the high-level objects in the C interface are reference-counted objects.  These objects include:

- Clients (:c:type:`FEC_ClientRef`; see :ref:`clients`)

- Nodes, Operators, Bindings, Events and EventHandlers (:c:type:`FEC_NodeRef`, :c:type:`FEC_BindingRef`, etc.; see :ref:`dg-objects`)

All of the reference-counted objects are all "instances" of a base object of type :c:type:`FEC_Ref`, and they all have ``Ref`` at the end of their names.  Reference counted objects are always created using a call that ends in *Create* or *CreateWith...* (eg. :c:func:`FEC_ClientCreate`).  It is the responsibility of the programmer to call the function :c:func:`FEC_RefRelease` on the object once the object is no longer needed; failing to call :c:func:`FEC_RefRelease` on all your reference-counted objects will result in memory and resource leaks at runtime!

API Reference
"""""""""""""

.. c:type:: FEC_Ref

  The type of a generic reference in CAPI.  Many CAPI functions return references that are "derived" from this type (see eg. :c:type:`FEC_ClientRef` and :c:type:`FEC_DGNodeRef`).  When using the C interface, the references must be manually managed by the programmer.  Not releasing references once they are no longer in use will cause your program to leak memory and resources and/or hang on exit.






.. c:var:: FEC_Ref FEC_NULL_REF

  The NULL reference value.  CAPI functions that fail will return this value for references they would otherwise return.  Passing this value to CAPI functions will result in an exception.






.. c:function:: void FEC_RefRetain(FEC_Ref ref)

  Retain a reference; this adds one to the reference count of an reference, so that :c:func:`FEC_RefRelease` will have to be called an additional time for the reference to be freed.  Calling this function on a FEC_NULL_REF reference does nothing.

  This function is not usually needed.





.. c:function:: void FEC_RefRelease(FEC_Ref ref)

  Releases a reference; this subtracts one to the reference count of an reference; if the reference count is then zero, the reference is freed.  Calling this function on a FEC_NULL_REF reference does nothing.

  Many CAPI functions return reference types; it is the responsibility of the programmer when using the C interface to call this function on those references once they are no longer needed.




.. c:function:: int FEC_RefIsNull(FEC_Ref ref)

  Determines whether or not the given reference is null, ie. if its value is FEC_NULL_REF.






Variants
^^^^^^^^^^^^^^^^^^^^^^^^^

In addition to reference-counted objects, there is a separate class of objects that require manual lifecycle management when using the C interface.  A :dfn:`variant` is a generic container for heterogenous data.  Variants are used in many calls to pass data in and out of the Fabric Core, and are covered in detail in :ref:`variants`.

Variants are always created using a call that begins with ``FEC_VariantInit...`` and variants must always be destroyed when they are no longer used by calling ``FEC_VariantDispose()``; as with reference-counted objects, not calling ``FEC_VariantDispose`` when variants are no longer needed will result in memory and resource leaks.

.. note:: There is one important exception to this rule: if a variant is null (ie. ``FEC_VariantIsNull()`` returns true) then it is not necessary (but still safe) to call ``FEC_VariantDispose``.  This makes error-handling code simpler.

.. _CAPI.c-interface.error-handling:

Error Handling
^^^^^^^^^^^^^^

Since the C language does not have a (good) generic exception mechanism, the
CAPI C language interface provides an exception mechanism that requires that
the programmer query for exceptions after every call into CAPI that could
fail.  "Exceptions" in CAPI are simply C string that describe the exception.
The entry function for obtaining the last exception; is
:c:func:`FEC_GetLastExceptionCString`; this function returns NULL if there is
no last exception.

API Reference
^^^^^^^^^^^^^

.. c:function:: char const *FEC_GetLastExceptionCString()

  Return the last exception as a C string.  If there is no exception, returns NULL.

  .. warning::

    The value returned by this function is no longer value after a call to
    most CAPI functions, including :c:func:`FEC_ClearLastException`.




.. c:function:: uint32_t FEC_GetLastExceptionLength()

  Return the length of the last exception string.  If there is no exception, returns 0.




.. c:function:: void FEC_ClearLastException( void )

  Clear the last exception so that :c:func:`FEC_GetLastExceptionCString`
  returns NULL.  If there is currently no exception, this function
  does nothing.

  .. note:: The value returned from :c:func:`FEC_GetLastExceptionCString` is no longer valid after a call to this function.





C Interface Example
----------------------------

The following example code shows the use of the C language interface to CAPI.

.. code-block:: c
  :linenos:

  #include <FabricCore.h>

  #include <stdio.h>
  #include <stdlib.h>

  int main( int argc, char **argv )
  {
    char const *exceptionCString;
    FEC_ClientCreateOptions createOptions;
    FEC_ClientRef client;
    FEC_KLSourceFile sourceFiles[1] = {
      "vec3.kl",
      "\
  struct Vec3 {\n\
    Float32 x, y, z;\n\
  };\n\
  function Float32 Vec3.normSq() {\n\
    return this.x*this.x + this.y*this.y + this.z*this.z;\n\
  }\n\
  function Float32 Vec3.norm() {\n\
    return sqrt(this.normSq());\n\
  }\n\
  "
    };
    FEC_DGOperatorRef dgOperator;
    char const *parameterLayout[2] = { "self.vec3", "self.norm" };
    FEC_DGBindingRef dgBinding;
    FEC_DGNodeRef dgNode;
    float vec3Data[1024*3];
    float normData[1024];
    uint32_t i;

    FEC_Initialize();

    memset( &createOptions, 0, sizeof(createOptions) );
    createOptions.guarded = 1;

    client = FEC_ClientCreate( NULL, NULL, &createOptions );
    exceptionCString = FEC_GetLastExceptionCString();
    if ( exceptionCString )
    {
      printf( "Caught exception: %s\n", exceptionCString );
      exit( 1 );
    }

    FEC_RegisterKLExtension(
      client,
      "Vec3",
      "1.0.0",
      "",
      1,
      sourceFiles,
      true,
      false
      );
    exceptionCString = FEC_GetLastExceptionCString();
    if ( exceptionCString )
    {
      printf( "Caught exception: %s\n", exceptionCString );
      exit( 1 );
    }

    dgOperator = FEC_DGOperatorCreate(
      client,
      "testOperator1",
      "test.kl",
      "\
  require Vec3;\n\
  \n\
  operator testOp(Vec3 vec3, io Float32 norm) {\n\
    norm = vec3.norm();\n\
  }\n\
  ",
      "testOp"
      );

    dgBinding = FEC_DGBindingCreate(
      dgOperator,
      2,
      parameterLayout
      );
    exceptionCString = FEC_GetLastExceptionCString();
    if ( exceptionCString )
    {
      printf( "Caught exception: %s\n", exceptionCString );
      exit( 1 );
    }

    dgNode = FEC_DGNodeCreate( client, "testNode1" );
    FEC_DGContainerAddMember_Variant( dgNode, "vec3", "Vec3", NULL );
    FEC_DGContainerAddMember_Variant( dgNode, "norm", "Float32", NULL );
    FEC_DGContainerSetSize( dgNode, 1024 );
    for ( i=0; i<1024; ++i )
    {
      vec3Data[3*i+0] = (float)(i+0);
      vec3Data[3*i+1] = (float)(2*i+1);
      vec3Data[3*i+2] = (float)(i+2);
    }
    FEC_DGContainerSetMemberAllSlicesData( dgNode, "vec3", sizeof(vec3Data), vec3Data );
    FEC_DGNodeAppendBinding( dgNode, dgBinding );
    exceptionCString = FEC_GetLastExceptionCString();
    if ( exceptionCString )
    {
      printf( "Caught exception: %s\n", exceptionCString );
      exit( 1 );
    }

    FEC_DGNodeEvaluate( dgNode );
    FEC_DGContainerGetMemberAllSlicesData( dgNode, "norm", sizeof(normData), normData );
    for ( i=0; i<8; ++i )
      printf( "norm[%u] = %g\n", (unsigned)i, normData[i] );
    printf( "...\n" );
    for ( i=1016; i<1024; ++i )
      printf( "norm[%u] = %g\n", (unsigned)i, normData[i] );

    FEC_RefRelease( dgNode );
    FEC_RefRelease( dgBinding );
    FEC_RefRelease( dgOperator );
    FEC_RefRelease( client );

    FEC_Finalize();

    return 0;
  }


