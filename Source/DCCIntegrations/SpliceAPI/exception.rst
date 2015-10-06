
.. _exception:

FabricSplice::Exception
=========================

The Exception is used to catch any errors happening within Fabric:Splice or the Fabric Core from a host application. You may wrap any call to the :dfn:`SPLICECAPI` like this:

Example
---------------------------------

.. code-block:: c++

    try
    {
      ... call to SPLICECAPI ...
    }
    catch(FabricSplice::Exception e)
    {
      printf("Splice Error %s\n", e.what());
    }

It's recommended to wrap the try and catch calls into macros, so that you can deploy them easily anywhere you use the :dfn:`SPLICECAPI`.

Class Outline
---------------------------------

.. code-block:: c++

    namespace FabricSplice
    {
      class Exception
      {
      public:

        // returns the description of the Exception
        char const * what() const;

        // returns the description of the Exception
        operator const char *() const;
      };
    };
