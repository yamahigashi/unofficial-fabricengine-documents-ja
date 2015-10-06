
.. _scripting:

FabricSplice::Scripting
===============================

The Scripting class provides static methods for parsing script arguments. This can be useful within Splice integrations. Options are provided as json strings typically, and the following helper functions simplify parsing these.

Class Outline
---------------------------------

.. code-block:: c++

    namespace FabricSplice
    {
      class Scripting
      {
      public:

        // decodes a flat list of scripting arguments into a dictionary of 
        // argument values. this also assume one of the arguments (index 1 or 2)
        // to contain a json structure with additional values
        static FabricCore::Variant parseScriptingArguments(const char * action, const char * reference, const char * data, const char * auxiliary);

        // returns a bool argument of a given parsed dictionary
        static bool consumeBooleanArgument(FabricCore::Variant & argsDict, const char * name, bool defaultValue = false, bool optional = false);

        // returns a int argument of a given parsed dictionary
        static int consumeIntegerArgument(FabricCore::Variant & argsDict, const char * name, int defaultValue = 0, bool optional = false);

        // returns a float argument of a given parsed dictionary
        static float consumeScalarArgument(FabricCore::Variant & argsDict, const char * name, float defaultValue = 0.0, bool optional = false);

        // returns a string argument of a given parsed dictionary (string variant)
        static std::string consumeStringArgument(FabricCore::Variant & argsDict, const char * name, const char * defaultValue = "", bool optional = false);

        // returns a variant argument of a given parsed dictionary
        static FabricCore::Variant consumeVariantArgument(FabricCore::Variant & argsDict, const char * name, const FabricCore::Variant & defaultValue = FabricCore::Variant(), bool optional = false);
      };
    };
