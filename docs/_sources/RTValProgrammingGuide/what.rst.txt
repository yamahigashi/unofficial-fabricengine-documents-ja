.. _RTVG.what-is:

What is an RTVal?
===================

An :dfn:`RTVal` is a container for data that is managed by the KL programming language.  The term "RTVal" is a mnemonic for "Registered Type Value"; "Registered Type" is the historical name in |FABRIC_PRODUCT_NAME| for KL types.

An RTVal has three key attributes: they have a type, they have a value, and they are reference-counted.

RTVals have Types
-----------------

Every RTVal has a fixed KL type.  The type is specified when the RTVal is created and cannot be changed.

An RTVal can be of almost [#almost]_ any KL type.  The type can be an internal, predefined type or a user-defined type such as a structure or an object.

.. [#almost] The exceptions are types that "internal" types for interacting with other, non-KL parts of the system, such as ``Container``.

RTVals have Values
------------------

Every RTVal has a value.  The initial value of the RTVal is determined when the RTVal is created.

Since RTVals are values in the KL programming language, they follow the same lifecycle process as any other data.  When the RTVal is created, one of the :ref:`contructors <KLPG.constructor>` for its type is called; similarly, when an RTVal is destroyed, its :ref:`destructor <KLPG.destructor>` is called.

The value of an RTVal can change, usually through one of two mechanisms:
  
  - A (:ref:`read-write <KLPG.method.this-type>`) method of the RTVal's type is called on the RTVal; or
  
  - The RTVal is passed to another method or function call taking an `io` argument.

RTVals are Reference-Counted
----------------------------

RTVals are reference-counted objects that are owned by the |FABRIC_PRODUCT_NAME| client.  When the last reference to the RTVal is dropped, it is destroyed.  In both Python and C++, assigning one RTVal value to another simply copies a reference to the same underlying object.