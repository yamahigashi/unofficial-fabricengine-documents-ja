
.. _klparser:

FabricSplice::KLParser
=========================

The KLParser class provides functionality to parse KL files. It also implements sub-classes for accessing contextual symbols for constants, structs, operators and functions. Using the :ref:`klparser` you can implement code completion tools, analytic tools for KL code, doxygen style documentation generation tools etc.

.. note:: The KLParser will be deprecated after 1.13.0 and replaced by a proper AST representation.

Example
---------------------------------

The sample below shows how to use the :ref:`klparser` for iterating over all defined symbols within a KL file.

.. code-block:: c++

    #include <FabricSplice.h>

    using namespace FabricSplice;

    int main( int argc, const char* argv[] )
    {
      std::string klCode;
      klCode += "struct MyType {\n";
      klCode += "  Float32 x;\n";
      klCode += "  Float32 y;\n";
      klCode += "}\n";
      klCode += "\n";
      klCode += "function MyType(Float64 x, Float64 y) {\n";
      klCode += "  this.x = x;\n";
      klCode += "  this.y = y;\n";
      klCode += "}\n";

      KLParser parser = KLParser::getParser("MyType", "MyType", klCode.c_str());
      for(unsigned int j=0;j<parser.getNbKLSymbols();j++)
      {
        KLParser::KLSymbol s = parser.getKLSymbol(j);
        printf("%03d: '%s' '%s'\n", (int)i, s.typeName(), s.str().c_str());
      }
      return 0;
    }

Class Outline
---------------------------------

.. code-block:: c++

    namespace FabricSplice
    {
      class KLParser
      {
      public:

        class KLSymbol
        {
        public:

          enum Type {
            Type_none,

            Type_separator,
            Type_semicolon,
            Type_comma,
            Type_period,
            Type_comment,

            Type_firstkeyword,
            Type_in,
            Type_io,
            Type_if,
            Type_else,
            Type_switch,
            Type_case,
            Type_default,
            Type_for,
            Type_while,
            Type_do,
            Type_break,
            Type_continue,
            Type_this,
            Type_alias,
            Type_require,
            Type_return,
            Type_const,
            Type_function,
            Type_operator,
            Type_struct,
            Type_object,
            Type_interface,
            Type_lastkeyword,

            Type_rt,
            Type_name,
            Type_number,
            Type_string,

            Type_assignment,
            Type_arithmetic,
            Type_brace1,
            Type_brace2,
            Type_bracket1,
            Type_bracket2,
            Type_curly1,
            Type_curly2,
            Type_pex1,
            Type_pex2,

            Type_maxtypes
          };

        public:

          // copy constructor
          KLSymbol(KLSymbol const & other);

          // copy operator
          KLSymbol & operator =( KLSymbol const & other );

          // returns true if the object is valid
          bool isValid() const;

          // bool conversion operator
          operator bool() const;

          // returns the index of this symbol
          unsigned int index() const;

          // returns the char position within the code
          unsigned int pos() const;

          // returns the length of this symbol
          unsigned int length() const;

          // returns the type of this symbol
          Type type() const;

          // returns true of this symbol is a keyword
          bool isKeyword() const;

          // returns
          const char * typeName() const;

          // returns a char from the front (given an index);
          char front(unsigned int index = 0) const;

          // returns a char from the back (given an index);
          char back(unsigned int index = 0) const;

          // returns the contained string
          std::string str() const;

          // returns true if this contains a given char
          bool contains(char c) const;

          // returns the index of a given char, or UINT_MAX if not found
          unsigned int find(char c) const;

          // returns the previous symbol before this one, or an invalid one
          KLSymbol prev(bool skipComments = true, unsigned int offset = 1) const;

          // returns the next symbol after this one, or an invalid one
          KLSymbol next(bool skipComments = true, unsigned int offset = 1) const;

          // returns the name of the parser this symbol belongs to
          const char * parser() const;
        };

        class KLConstant
        {
        public:
          // copy constructor
          KLConstant(KLConstant const & other);

          // copy operator
          KLConstant & operator =( KLConstant const & other );

          // returns true if the object is valid
          bool isValid() const;

          // bool conversion operator
          operator bool() const;

          // returns the symbol of this KLConstant
          KLSymbol symbol() const;

          // returns the comments of this KLConstant
          const char * comments() const;

          // returns the type of this KLConstant
          const char * type() const;

          // returns the name of this KLConstant
          const char * name() const;

          // returns the value of this KLConstant
          const char * value() const;
        };

        class KLVariable
        {
        public:
          // copy constructor
          KLVariable(KLVariable const & other);

          // copy operator
          KLVariable & operator =( KLVariable const & other );

          // returns true if the object is valid
          bool isValid() const;

          // bool conversion operator
          operator bool() const;

          // returns the symbol of this KLVariable
          KLSymbol symbol() const;

          // returns the type of this KLVariable
          const char * type() const;

          // returns the name of this KLVariable
          const char * name() const;
        };

        class KLStruct
        {
        public:
          // copy constructor
          KLStruct(KLStruct const & other);

          // copy operator
          KLStruct & operator =( KLStruct const & other );

          // returns true if the object is valid
          bool isValid() const;

          // bool conversion operator
          operator bool() const;

          // returns the symbol of this KLStruct
          KLSymbol symbol() const;

          // returns the comments of this KLStruct
          const char * comments() const;

          // returns the type of this KLStruct
          const char * type() const;

          // returns the name of this KLStruct
          const char * name() const;

          // returns number of interfaces in this KLStruct
          unsigned int nbInterfaces() const;

          // returns name of an interface of a given index
          const char * getInterface(unsigned int index) const;

          // returns number of members in this KLStruct
          unsigned int nbMembers() const;

          // returns the type of a member of this KLStruct with a given index
          const char * memberType(unsigned int index) const;

          // returns the type of a member of this KLStruct with a given index
          const char * memberName(unsigned int index) const;
        };

        class KLArgumentList
        {
        public:
          // copy constructor
          KLArgumentList(KLArgumentList const & other);

          // copy operator
          KLArgumentList & operator =( KLArgumentList const & other );

          // returns true if the object is valid
          bool isValid() const;

          // bool conversion operator
          operator bool() const;

          // returns number of arguments in this KLArgumentList
          unsigned int nbArgs() const;

          // returns the mode of an argument with a given index
          const char * mode(unsigned int index) const;

          // returns the type of an argument with a given index
          const char * type(unsigned int index) const;

          // returns the name of an argument with a given index
          const char * name(unsigned int index) const;
        };

        class KLOperator
        {
        public:
          // copy constructor
          KLOperator(KLOperator const & other);

          // copy operator
          KLOperator & operator =( KLOperator const & other );

          // returns true if the object is valid
          bool isValid() const;

          // bool conversion operator
          operator bool() const;

          // returns the symbol of this KLOperator
          KLSymbol symbol() const;

          // returns the comments of this KLOperator
          const char * comments() const;

          // returns the name of this KLOperator
          const char * name() const;

          // returns true if this KLOperator uses a PEX notation
          bool isPex() const;

          // returns the pexArgument of this KLOperator
          const char * pexArgument() const;

          // returns the argument list of this KLOperator
          KLArgumentList arguments() const;

          // returns the symbol starting the body of this KLOperator
          KLSymbol bodyStart() const;

          // returns the symbol ending the body of this KLOperator
          KLSymbol bodyEnd() const;
        };

        class KLFunction
        {
        public:
          // copy constructor
          KLFunction(KLFunction const & other);

          // copy operator
          KLFunction & operator =( KLFunction const & other );

          // returns true if the object is valid
          bool isValid() const;

          // bool conversion operator
          operator bool() const;

          // returns the symbol of this KLFunction
          KLSymbol symbol() const;

          // returns the comments of this KLFunction
          const char * comments() const;

          // returns the type of this KLFunction (or "" if it is a void);
          const char * type() const;

          // returns the name of this KLFunction
          const char * name() const;

          // returns the owner of this KLFunction (or "" if it's not a method);
          const char * owner() const;

          // returns the argument list of this KLFunction
          KLArgumentList arguments() const;

          // returns the symbol starting the body of this KLFunction
          KLSymbol bodyStart() const;

          // returns the symbol ending the body of this KLFunction
          KLSymbol bodyEnd() const;
        };

        class KLInterface
        {
        public:
          // returns the symbol of this KLInterface
          KLSymbol symbol() const;

          // returns the comments of this KLInterface
          const char * comments() const;

          // returns the name of this KLInterface
          const char * name() const;

          // returns the number of functions on this KLInterface
          unsigned int nbFunctions() const;

          // returns a function of this KLInterface by index
          KLFunction function(unsigned int index) const;
        };

        // default constructor
        KLParser();

        // copy constructor
        KLParser(KLParser const & other);

        // copy operator
        KLParser & operator =( KLParser const & other );

        // default destructor
        ~KLParser();

        // returns true if the object is valid
        bool isValid() const;

        // bool conversion operator
        operator bool() const;

        // returns the owner of the parser
        const char * owner() const ;

        // returns the name of the parser
        const char * name() const ;

        // returns the contained sourcecode of the parser
        const char * code() const ;

        // returns the number of current parsers
        static unsigned int getNbParsers();

        // returns a parser given an index
        static KLParser getParser(unsigned int index);

        // returns a parser given a name an optional klCode
        // if the parser doesn't exist yet - it will be created.
        static KLParser getParser(const char * owner, const char * name, const char * klCode = NULL);

        // parse new KL code in this parser
        bool parse(const char * klCode);

        // returns the number of KL symbols
        unsigned int getNbKLSymbols() const;

        // returns a specific KL symbol
        KLSymbol getKLSymbol(unsigned int symbolIndex) const;

        // returns the symbol for a special character index in the KL code
        KLSymbol getKLSymbolFromCharIndex(unsigned int charIndex) const;

        // returns the number of required KL types / extensions
        unsigned int getNbKLRequires() const;

        // returns the name of the required KL type / extension given an index
        const char * getKLRequire(unsigned int index) const;

        // returns the number of KL constants
        unsigned int getNbKLConstants() const;

        // returns the KL constant given an index
        KLConstant getKLConstant(unsigned int index) const;

        // returns the number of KL variables
        unsigned int getNbKLVariables() const;

        // returns the KL variable given an index
        KLVariable getKLVariable(unsigned int index) const;

        // returns the number of KL interfaces
        unsigned int getNbKLInterfaces() const;

        // returns the KL interface given an index
        KLInterface getKLInterface(unsigned int index) const;

        // returns the number of KL structs / objects
        unsigned int getNbKLStructs() const;

        // returns the KL struct / object given an index
        KLStruct getKLStruct(unsigned int index) const;

        // returns the number of KL operators
        unsigned int getNbKLOperators() const;

        // returns the KL operator given an index
        KLOperator getKLOperator(unsigned int index) const;

        // returns the number of KL functions / methods
        unsigned int getNbKLFunctions() const;

        // returns the KL function given an index
        KLFunction getKLFunction(unsigned int index) const;

        // returns the KL type for a given name symbol (or "" if unknown)
        const char * getKLTypeForSymbol(const KLSymbol & symbol) const;

        // returns the KL type for a member or method below a given owner type
        static const char * getKLTypeForSymbol(const char * owner, const char * member);
      };
    };
