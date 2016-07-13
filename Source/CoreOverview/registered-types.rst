Registered Types
=================

|FABRIC_PRODUCT_NAME| provides a method for defining types that are used in KL operators and dependency graph nodes. Once a custom type is registered, the data type can be used to populate nodes and can be used in KL operators.  This type system enables the types used in the KL source code to be defined before compilation.

Using only a small number of basic atomic types, users can register custom types that combine these types into new complex types. Types can be defined using existing complex types, allowing the definition of complex nested data structures.  Types can have KL functions associated with them, enabling object method syntax to be used with the type in KL. 

Complete documentation for working with registered types is provided in the :ref:`DGPG`.