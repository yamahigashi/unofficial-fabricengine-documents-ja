


.. _cpp-interface:

The C++ Language Interface
===========================

This chapter describes in detail the general practices that are required of an application that uses CAPI through the C++ language interface.  This chapter is not required reading if you do not plan on using the C++ language interface.

Since C++ provides both object lifecycle management and exception features, there is much less work for a programmer to do when using CAPI's C++ interface.

Namespacing
------------------

All of the C++ interface objects (classes) and functions are namespaced within the C++ namespace ``FabricCore``.  As a programmer, you can choose to use explicit namespacing by prefixing all usage of CAPI objects and functions with ``FabricCore::...``, for instance :cpp:class:`FabricCore::DGNode`, or you can choose to omit the prefix (assuming the resulting symbol name does not conflict with other symbols in your program at compile time) by adding

.. code-block:: c

  using namespace FabricCore;

at the top of each source file that uses the CAPI C++ interface.

Object Lifecycles
------------------

Both reference-counted objects and variants are automatically released when they go out of scope when using the C++ interface to CAPI.  Scoping rules for CAPI C++ objects are the same as for any other C++ object.

Error Handling
------------------

The C++ interface uses standard C++ exception handling for its error handling features.  When using the CAPI C++ interface, any errors that occur are thrown as C++ exceptions of type :cpp:class:`FabricCore::Exception`, and can be caught using a standard ``catch ( FabricCore::Exception e ) { ... }`` statement.  For more information, see :ref:`exceptions`.

Example
------------------

The following example code shows the use of the C++ language interface to CAPI.

.. code-block:: c
  :linenos:

  #include <FabricCore.h>

  #include <stdio.h>

  int main( int argc, char **argv )
  {
    FabricCore::Initialize();

    FabricCore::Client::CreateOptions createOptions;
    memset( &createOptions, 0, sizeof(createOptions) );
    createOptions.guarded = true;

    FabricCore::Client client( NULL, NULL, &createOptions );

    FabricCore::KLSourceFile sourceFiles[1] = {
      {
        "vec3.kl", "\
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
      }
    };
    FabricCore::RegisterKLExtension(
      client,
      "Vec3",
      "1.0.0",
      "", // override
      1,
      sourceFiles,
      true, // load
      false // reload
      );

    FabricCore::DGOperator dgOperator(
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

    char const *parameterLayout[2] = { "self.vec3", "self.norm" };
    FabricCore::DGBinding dgBinding(
      dgOperator,
      2,
      parameterLayout
      );

    FabricCore::DGNode dgNode( client, "testNode1" );
    dgNode.addMember( "vec3", "Vec3" );
    dgNode.addMember( "norm", "Float32" );
    dgNode.setSize( 1024 );
    float vec3Data[1024*3];
    for ( uint32_t i=0; i<1024; ++i )
    {
      vec3Data[3*i+0] = float(i+0);
      vec3Data[3*i+1] = float(2*i+1);
      vec3Data[3*i+2] = float(i+2);
    }
    dgNode.setMemberAllSlicesData( "vec3", sizeof(vec3Data), vec3Data );
    dgNode.appendBinding( dgBinding );
    dgNode.evaluate();
    float normData[1024];
    dgNode.getMemberAllSlicesData( "norm", sizeof(normData), normData );
    for ( uint32_t i=0; i<8; ++i )
      printf( "norm[%u] = %g\n", unsigned(i), normData[i] );
    printf( "...\n" );
    for ( uint32_t i=1016; i<1024; ++i )
      printf( "norm[%u] = %g\n", unsigned(i), normData[i] );

    FabricCore::Finalize();

    return 0;
  }


