.. _KLPG.types:

The KL Type System
==================

Unlike most languages, KL has a dynamic type system that is inherited from the Fabric environment.  In most cases, compound types are registered from the Fabric environment running in a dynamic language (eg. JavaScript or Python); those types are then automatically made available to KL programs running in that environment.  This does not, however, affect the semantics of the language; the KL type system can still be explained purely from the point of view of the language itself.

Like most programming languages, KL has support for both a fixed set of base types from which other types are derived as well as different kinds of derived types.

.. index::
  single: base types

Base Types
----------

The base types in KL are the following:

:code:`Boolean`
  can be either :code:`true` or :code:`false`

``UInt8``
  an 8-bit unsigned integer

``Byte``
  an alias for ``UInt8``

``SInt8``
  an 8-bit signed integer

``UInt16``
  a 16-bit unsigned integer

``SInt16``
  a 16-bit signed integer

``UInt32``
  a 32-bit unsigned integer

``Count``
  an alias for ``UInt32``; used to represent cardinal numbers

``Index``
  an alias for ``UInt32``; used to represent ordinal numbers

``Size``
  an alias for ``UInt32``

``SInt32``
  a 32-bit signed integer

``Integer``
  an alias for ``SInt32``

``UInt64``
  a 64-bit unsigned integer

``DataSize``
  an alias for ``UInt64``; used to represent sizes of blocks of memory

``SInt64``
  a 64-bit signed integer

``Float32``
  a 32-bit IEEE floating point

``Scalar``
  an alias for ``Float32``

``Float64``
  a 64-bit IEEE floating point

``String``
  a sequence of zero or more characters

.. index::
  single: Boolean type
  pair: Boolean; type

The :code:`Boolean` Type
^^^^^^^^^^^^^^^^^^^^^^^^

The value of an expression of :code:`Boolean` type is either logical true or logical false.  The type has the following properties:

- The constants :code:`true` and :code:`false` are :code:`Boolean` values with logical values true and false, respectively.

- All other base types cast to Boolean as follows:
  
  - All values of integer type (eg. ``UInt32``, ``Byte``) cast to true if and only if the value is non-zero
  
  - All values of floating-point type (ie. ``Float32`` and ``Float64``) cast true if and only if the value is not equal to ``0.0`` or ``-0.0``
  
  - ``String`` values cast to true if and only if their length is greater than zero
  
  - Arrays and dictionaries cast to true if and only if they are non-empty
  
  - By default, structures do not cast to :code:`Boolean`, but you can implement the cast if desired by creating a :code:`Boolean` constructor that takes the structure as a parameter; see :ref:`KLPG.constructor`

- For operators:

  - None of the arithmetic operators (binary ``+``, ``-``, ``*``, ``/``, ``%`` as well as unary ``-`` and ``+``) are valid for :code:`Boolean` values
  - Only the ``==`` and ``!=`` comparison operators are valid for :code:`Boolean` values
  - All of the bitwise binary operators (``|``, ``&amp;``, ``^`` and ``~``) are valid for :code:`Boolean` values and treat the value as if it were a single bit

The following example shows the use of the :code:`Boolean` type::

  operator entry() {
    Boolean a = true;
    report(a);
    Boolean b = a & false;
    report(b);
    report(a != b);
  }

Output::

  true
  false
  true

.. index::
  single: integer types
  pair: UInt8; type
  pair: SInt8; type
  pair: UInt16; type
  pair: SInt16; type
  pair: UInt32; type
  pair: SInt32; type
  pair: UInt64; type
  pair: SInt64; type
  pair: Size; type
  pair: Count; type
  pair: Index; type
  pair: DataSize; type
  pair: Integer; type
  pair: Byte; type

Integer Types
^^^^^^^^^^^^^

The ``UInt8``, ``SInt8``, ``UInt16``, ``SInt16``, ``UInt32``, ``SInt32``, ``UInt64`` and ``SInt64`` types, as well as their aliases (``Byte``, ``Integer``, ``Size``, ``Count``, ``Index`` and ``DataSize``), are collectively known as the :index:`integer types` and represent whole integers.  These types differ only in their bit width and whether they are signed or unsigned, as follows:

``UInt8``
  an 8-bit unsigned integer

``Byte``
  an alias for ``UInt8``

``SInt8``
  an 8-bit signed integer

``UInt16``
  a 16-bit unsigned integer

``SInt16``
  a 16-bit signed integer

``UInt32``
  a 32-bit unsigned integer

``SInt32``
  a 32-bit signed integer

``Integer``
  an alias for ``SInt32``

``UInt64``
  a 64-bit unsigned integer

``SInt64``
  a 64-bit signed integer

``Count``
  an alias for ``UInt32``.  ``Size`` is usually used to count the number of elements in an array

``Index``
  an alias for ``UInt32``.  ``Index`` is usually used to index into an array

``DataSize``
  an alias for ``UInt64``.  ``DataSize`` is used to represent the size of a block of memory and is the return type for the ``dataSize`` method of types.

``Size``
  an alias for ``UInt32``.

Integer types behave as follows:

- All of the :ref:`arithmetic <arithmetic-ops>`, :ref:`logical <logical-ops>` and :ref:`bitwise <bitwise-ops>` operators work as expected for all integer types.

- Integer constants are typed using the suffixes ``s32`` for ``SInt32``, ``u64`` for ``UInt64``, and so on; if a suffix is omitted, the type is ``SInt32``.  For more details, see :ref:`integer-constants`.

The following shows the use of integer types::

  operator entry() {
    Byte b = 64;
    report(b);
    Size s = 45 * Size(b) + 32;
    report(s);
    Integer i = -75 * Integer(s) + 18;
    report(i);
  }

Output::

  64
  2912
  -218382

.. index::
  single: integer atomics
  pair: atomics; integer

Integer Atomic Methods
""""""""""""""""""""""

The integer types have a set of built-in :ref:`methods` that perform atomic 
operations on a value of the type.  Atomic operations are used to implement
lock-free algorithms; for more information on atomic operations, see
http://en.wikipedia.org/wiki/Linearizability.

.. kl:function::
  UInt8 UInt8.atomicAdd(UInt8 val)
  SInt8 SInt8.atomicAdd(SInt8 val)
  UInt16 UInt16.atomicAdd(UInt16 val)
  SInt16 SInt16.atomicAdd(SInt16 val)
  UInt32 UInt32.atomicAdd(UInt32 val)
  SInt32 SInt32.atomicAdd(SInt32 val)
  UInt64 UInt64.atomicAdd(UInt64 val)
  SInt64 SInt64.atomicAdd(SInt64 val)
  
  Atomically add a value to the integer
  
  :param val: The value to add
  :returns: the old value of the integer

.. kl:function::
  UInt8 UInt8.atomicInc()
  SInt8 SInt8.atomicInc()
  UInt16 UInt16.atomicInc()
  SInt16 SInt16.atomicInc()
  UInt32 UInt32.atomicInc()
  SInt32 SInt32.atomicInc()
  UInt64 UInt64.atomicInc()
  SInt64 SInt64.atomicInc()
  
  Atomically increments the integer
  
  :returns: the old value of the integer

.. kl:function::
  UInt8 UInt8.atomicSub(UInt8 val)
  SInt8 SInt8.atomicSub(SInt8 val)
  UInt16 UInt16.atomicSub(UInt16 val)
  SInt16 SInt16.atomicSub(SInt16 val)
  UInt32 UInt32.atomicSub(UInt32 val)
  SInt32 SInt32.atomicSub(SInt32 val)
  UInt64 UInt64.atomicSub(UInt64 val)
  SInt64 SInt64.atomicSub(SInt64 val)
  
  Atomically subtracts a value from the integer
  
  :param val: The value to add
  :returns: the old value of the integer

.. kl:function::
  UInt8 UInt8.atomicDec()
  SInt8 SInt8.atomicDec()
  UInt16 UInt16.atomicDec()
  SInt16 SInt16.atomicDec()
  UInt32 UInt32.atomicDec()
  SInt32 SInt32.atomicDec()
  UInt64 UInt64.atomicDec()
  SInt64 SInt64.atomicDec()
  
  Atomically decrements the integer
  
  :returns: the old value of the integer

.. kl:function::
  UInt8 UInt8.atomicOr(UInt8 val)
  SInt8 SInt8.atomicOr(SInt8 val)
  UInt16 UInt16.atomicOr(UInt16 val)
  SInt16 SInt16.atomicOr(SInt16 val)
  UInt32 UInt32.atomicOr(UInt32 val)
  SInt32 SInt32.atomicOr(SInt32 val)
  UInt64 UInt64.atomicOr(UInt64 val)
  SInt64 SInt64.atomicOr(SInt64 val)
  
  Atomically perform a bitwise or on the integer
  
  :param val: The value to or with the integer
  :returns: the old value of the integer

.. kl:function::
  UInt8 UInt8.atomicAnd(UInt8 val)
  SInt8 SInt8.atomicAnd(SInt8 val)
  UInt16 UInt16.atomicAnd(UInt16 val)
  SInt16 SInt16.atomicAnd(SInt16 val)
  UInt32 UInt32.atomicAnd(UInt32 val)
  SInt32 SInt32.atomicAnd(SInt32 val)
  UInt64 UInt64.atomicAnd(UInt64 val)
  SInt64 SInt64.atomicAnd(SInt64 val)
  
  Atomically perform a bitwise and on the integer
  
  :param val: The value to and with the integer
  :returns: the old value of the integer

.. kl:function::
  UInt8 UInt8.atomicXor(UInt8 val)
  SInt8 SInt8.atomicXor(SInt8 val)
  UInt16 UInt16.atomicXor(UInt16 val)
  SInt16 SInt16.atomicXor(SInt16 val)
  UInt32 UInt32.atomicXor(UInt32 val)
  SInt32 SInt32.atomicXor(SInt32 val)
  UInt64 UInt64.atomicXor(UInt64 val)
  SInt64 SInt64.atomicXor(SInt64 val)
  
  Atomically perform a bitwise xor on the integer
  
  :param val: The value to xor with the integer
  :returns: the old value of the integer

.. kl:function::
  UInt8 UInt8.atomicCAS(UInt8 oldVal, UInt8 newVal)
  SInt8 SInt8.atomicCAS(SInt8 oldVal, SInt8 newVal)
  UInt16 UInt16.atomicCAS(UInt16 oldVal, UInt16 newVal)
  SInt16 SInt16.atomicCAS(SInt16 oldVal, SInt16 newVal)
  UInt32 UInt32.atomicCAS(UInt32 oldVal, UInt32 newVal)
  SInt32 SInt32.atomicCAS(SInt32 oldVal, SInt32 newVal)
  UInt64 UInt64.atomicCAS(UInt64 oldVal, UInt64 newVal)
  SInt64 SInt64.atomicCAS(SInt64 oldVal, SInt64 newVal)
  
  Atomically perform a compare-and-swap operation: if the integer's value
  is ``oldVal``, change it to ``newVal``.  Returns ``oldVal`` if and only
  if the value was changed.
  
  :param oldVal: The value to compare with the integer
  :param newVal: The value to set the integer to if the comparison succeeds
  :returns: the old value of the integer

.. index::
  single: floating-point types
  pair: Float32; type
  pair: Float64; type
  pair: Scalar; type

Floating-Point Types
^^^^^^^^^^^^^^^^^^^^

The ``Float32`` and ``Float64`` types (as well as ``Scalar``, an alias for ``Float32``) are collectively known as :dfn:`floating-point types` and represent :abbr:`IEEE` floating-point numbers.  These types differ only in their bit width, as follows:

``Float32``
  a 32-bit :abbr:`IEEE` floating-point number

``Float64``
  a 64-bit :abbr:`IEEE` floating-point number

``Scalar``
  an alias for ``Float32``

Floating-point types behave as follows:

- Floating-point constants have the same syntax as in JavaScript and C, and are of type ``Float64``.  For more details, see :ref:`floating-point-constants`.

- All of the :ref:`arithmetic <arithmetic-ops>` and :ref:`logical <logical-ops>` operators are valid for floating-point values.  None of the bitwise operators are valid for floating-point values.

The following example shows the use of floating-point types::

  operator entry() {
    Float32 x = 3.141;
    report(x);
    Float64 y = 2.718;
    report(y);
    Float32 z = x*x + y*y;
    report(z);
  }

Output::

  3.141
  2.718
  17.2534

.. index::
  single: string type
  pair: String; type

The ``String`` Type
^^^^^^^^^^^^^^^^^^^

The ``String`` type represents a text string, ie. a sequence of zero or more characters.  A value of type ``String`` is referred to as a :index:`string value`.

The semantics of the ``String`` type in KL are important to understand.  Strings have the following key properties:

- A string is a sequence of zero or more characters.

- The length of a string is value of type ``Size``, and the maximum length of a string is :math:`2^31-1`.

- String constants can be specified inline in KL source files using single- or double-quotation marks, just as in Python and JavaScript.  For more details and examples of string constants, see :ref:`string-constants`.

- Strings support the following operations and properties:
  
  - They have a ``.length`` property which returns the number of characters in the string
  
  - The ``+=`` assignment operator is used to append another string to a given string
  
  - A new string can be created by concatenating two other strings using the ``+`` binary operation
  
  - Strings can be compared using the usual ``==``, ``!=``, ``<``, ``<=``, ``>`` and ``>=`` logical operators.  Additionally, they support the :samp:`{string}.compare({otherString})` method that returns -1, 0 or 1 depending on whether :samp:`{string}` is less than, equal to or greater than :samp:`{otherString}`, respectively.

  - Strings can be indexed into using the :samp:`{string}[{index}]`.  The result is a string containing the single character at the given index.  :samp:`{index}` must be in the range :math:`[0...2^31-1]`.

  - A 32-bit hash value for the string can be obtained with the :samp:`{string}.hash()` method.

- Unlike C or C++, strings can contain the null character (ASCII 0).

- Strings have no notion of encoding; they are just sequences of bytes.  String encodings are determined by the application space where the strings are used.  Note that everything in Fabric itself uses the UTF-8 encoding, but Fabric extensions may need to convert strings into other encodings.

- All other types in KL can be converted to strings through a cast; this conversion simply creates a string that is a human-readable version of the value.  This conversion can be overridden for custom types by writing a custom :samp:`function {Type}.appendDesc(io String string)` method; see :ref:`conversion-funcs`.

Example use of the ``String`` type::

  operator entry() {
    String a = "A string";
    report(a);
    report("a has length " + a.length);
    String b = "Another string";
    report(b);
    String c = a + " and " + b;
    report(c);
    b += " now includes " + a;
    report(b);
  }

Output::

  A string
  a has length 8
  Another string
  A string and Another string
  Another string now includes A string

.. index::
  single: derived types
  pair: type; derived

.. _KLPG.types.derived:

Derived Types
-------------

In addition to the base types, KL supports three classes of derived types: structures, arrays and dictionaries.

.. index::
  single: structures
  pair: structure; type

.. _KLPG.types.structures:

Structures
^^^^^^^^^^

A :dfn:`structure` is a collection of typed values that are placed together in memory.

Structures are usually defined outside of KL using Fabric's :index:`registered type system`, but they can also be declared in KL source code itself using the ``struct`` keyword::

  struct NewType {
    Float32 firstMember;
    String secondMember;
    Integer thirdMemberVarArray[], fourthMemberFixedArray[3];
  };

Note the use of the variable-size array as the last member; derived types can nest arbitrarily.

.. note:: All structure declarations in KL must be in the global scope; it is not possible to declare a structure within a function scope.

More details about structures:

- Access to structure members is through the ``.`` (dot) operator, as in JavaScript.

- Currently, the structure members are using C-like alignment (see :ref:`structure-alignment`).

- It is possible to overload operators and add :dfn:`methods` to structures; see :ref:`methods`.

- It is possible to control access to members and methods of structures using the ``public``, ``private``, ``protected`` and ``permits`` keywords; see :ref:`KLPG.types.member-access`.

Example use of structures::

  struct MyNewType {
    Integer i;
    String s, t;
  };

  function entry() {
    MyNewType mnt;
    mnt.s = "Hello!";
    mnt.i = 42;
    mnt.t = "there!";
    report(mnt);
  }

Output::

  {i:42,s:"Hello!",t:"there!"}


.. index::
  single: structure alignment

.. _structure-alignment:

Structure Member Alignment
""""""""""""""""""""""""""

The alignment of members of structures is identical to that of the C
programming language.  Therefore, EDK code that interfaces with the
|FABRIC_PRODUCT_NAME| does not need to use any special alignment
specification to match the KL structure alignment.

For reference, the rules of KL structure alignment (the same as the C default)
are:

- Every type has a size and an alignment

- The alignment of base types is the same as their size

- The alignment of structures (as a whole) is the largest alignment of any of
  its member types

- The byte position of a member within a structure is chosen by rounding up
  the next available offset in the structure to the alignment of the member
  type

.. index::
  single: structure inheritance

.. _KPLG.structure.inheritance:

Structure Inheritance
"""""""""""""""""""""

.. versionadded:: 1.13.0

A structure can inherit (or `derive`) from a single base structure. The specialized structure then inherits from all members and methods of the base structure.

The :samp:`struct {SpecializedType} : {BaseType}` syntax is used to declare the inheritance relationship. A specialized structure can be `cast` to its base structure type at no cost. The :samp:`.parent` accessor allows to perform that cast explicitly.

.. kl-example::

  struct Shape {
    Float32 centerX, centerY;
  };

  struct Circle : Shape {
    Float32 radius;
  };

  operator entry() {
    Circle c;
    c.centerX = 1;
    c.centerY = 2;
    c.radius = 3;

    report( c );
    report( c.parent );
  }

.. note::

  When cast to its base type, a structure looses all its specialized behavior, which is different from :ref:`objects <KPLG.object.inheritance>`:

  .. kl-example::

    struct Shape {
      Float32 centerX, centerY;
    };

    struct Circle : Shape {
      Float32 radius;
    };

    function printShape( Shape s ) {
      report( s.type() + ": " + s );
    }

    operator entry() {
      Circle c;
      printShape( c );
    }

.. index::
  single: objects
  pair: object; type

.. _KLPG.types.objects:

Objects
^^^^^^^

.. versionchanged:: 1.12.0
  Can no longer do "empty construction" of variables of object type

An :dfn:`object` is similar to a :ref:`structure <KLPG.types.structures>` in that it is a collection of typed values placed together in memory, except that objects are copy-by-reference rather than copy-by-value; objects must be :dfn:`constructed` and are internally reference-counted.  Additionally, objects can support :ref:`interfaces <KLPG.types.interfaces>`, which are a collection of methods that the object is guaranteed to support.

Objects are used in much the same way as structures, with the major difference being that they are copy-by-reference and must be constructed.  KL internally keeps track of the number of references to each object and when the last reference to an object is dropped the memory holding the object is freed.  Objects drop their references when they go out of scope, or when they have :code:`null` assigned to them.

Objects are defined using the :code:`object` keyword in KL.  The syntax is very similar to the definition of :ref:`structures <KLPG.types.structures>`:

.. code-block:: kl
  
  // An object with two members
  object Obj {
    String s;
    UInt32 n;
  };

Optionally, the object can derive from one base object, and implement one or more :ref:`interfaces <KLPG.types.interfaces>`.  There are indicated after the name of the object:

.. code-block:: kl
  
  // An object with two members that implements two interfaces
  object MyObjType : BaseObjType, IntOne, IntTwo {
    String s;
    UInt32 n;
  };

Variables whose type is that of a given object are declared with the name of the object.

.. code-block:: kl
  
  // A variable of type MyObjType
  MyObjType obj = null;
  report(obj); // reports: null
  
The value :code:`null` refers to a non-existent object.  You can report an object that is :code:`null`, but trying to reference its members or call methods on it will result in a runtime error.

Any variable of Object type can be set to :code:`null`.  Doing almost anything with a :code:`null` object will result in a runtime error.  To create a valid object it must be constructed.  There are two syntaxes for constructing objects:

.. code-block:: kl
  
  MyObjType obj = MyObjType(); // calls the default constructor
  report(obj); // reports: {s:"",n:0}
  MyObjType obj2(); // also calls the default constructor
  report(obj2); // reports: {s:"",n:0}
  obj2 = null; // releases the object referenced by obj2
  report(obj2); // throws an error

.. note::
  Objects cannot be "empty constructed"; you must explicitly construct objects or explicitly set their values to :code:`null`.

:ref:`Constructors <KLPG.constructor>` and :ref:`destructors <KLPG.destructor>` can be specified for objects just as they are for structures:

.. code-block:: kl
  
  // Provide a default constructor
  function MyObjType() {
    this.s = "hello";
    this.n = 42;
  }
  
  // Provide a constructor that takes parameters
  function MyObjType(String s, UInt32 n) {
    this.s = s;
    this.n = n;
  }
  
  // later..
  MyObjType obj = MyObjType();
  report(obj); // reports: {s:"hello",n:42}
  obj = MyObjType("foo", 7);
  report(obj); // reports: {s:"foo",n:7}

Constructing a specific object from another object of the same type makes the new object a reference to the old object.  In this case, a new object is not created; if the object is modified through one of the references to it then the other see the modifications as well.

.. code-block:: kl
  
  MyObjType o1("bar", 3);
  MyObjType o2 = o1;
  o2.s = "baz";
  report(o1); // reports: {s:"baz",n:3}

Users cannot define a custom copy constructor for objects for this reason, the copy constructor always only adds a reference to the existing object. If a user wants to instantiate a new object then the ``clone()`` method (see :ref:`KLPG.types.objects.clone`)
or a custom method should be used.

.. kl-example:: Duplicating an object using a custom method

  // not permitted, custom copy constructor invalid for objects
  // function MyObjType(MyObjType o)
  // {
  //   // ...
  // }

  object MyObjType
  {
    String s;
    Integer n;
  };

  // return a new object using a custom method
  function MyObjType MyObjType.copy()
  {
    MyObjType o = MyObjType();
    o.s = this.s;
    o.n = this.n;
    return o;
  }

  operator entry()
  {
    MyObjType o1();
    o1.s = "foo";
    o1.n = 42;

    MyObjType o2 = o1.copy();

    o2.s = "bar";
    report("o1 = " + o1);
    report("o2 = " + o2);
  }

Arbitrary methods can be defined on objects just as they are on structures.  These methods are then called using the same :samp:`{object}.{methodName}({arg},{arg},...)` syntax as for structures.  Calling a method on a :code:`null` object results in a runtime exception.

.. code-block:: kl
  
  function MyObjType.reportMe() {
    report("reportMe: s="+this.s+" n="+n);
  }
  
  MyObjType obj("Fred", 49);
  obj.reportMe(); // reports: reportMe: s=Fred n=49

Members of objects are accessed in the same way as members of structures by using the :samp:`{object}.{memberName}` syntax.  Using the :code:`.` operation on a :code:`null` object will throw a runtime exception.

Additional properties of objects:

- If an value of object type is converted to a :code:`Boolean` then its value is :code:`true` if and only if the object is not :code:`null`.

- The :ref:`equality operators <equality-ops>` :samp:`{obj1} == {obj2}` and :samp:`{obj1} != {obj2}` are only valid for objects when overloaded or when comparing with :code:`null`.  The :ref:`identity operators <identity-ops>` :samp:`{obj1} === {obj2}` and :samp:`{obj1} !== {obj2}` are always valid for objects and compare based on whether the objects are references to the same object (ie. if changing one will change both).

-  Values of object type support the method :samp:`<objectValue>.uid()` that returns a unique UInt64 that can be used to identify the object.  The value is the same as it would be if `.uid()` were called on the object casted to any of the interfaces the object supports.

- Assigning :code:`null` to an object drops the reference to whatever the object was previously pointing to.

- It is possible to control access to members and methods of objects using the ``public``, ``private``, ``protected`` and ``permits`` keywords; see :ref:`KLPG.types.member-access`.

.. note:: A variable of whose type is an object cannot point to a structure.  Objects and interfaces are fundamentally different types than structures; see the section :ref:`KLPG.objects-versus-structures`

The following code provides another example of using object:

.. kl-example:: Objects
  
  object Foo {
    SInt32 intMember;
    String stringMember;
  };
  
  // A non-default constructor for Foo
  function Foo(SInt32 i, String s) {
    this.intMember = i;
    this.stringMember = s;
  }
  
  operator entry() {
    Foo foo1 = Foo(32, "foo"); // call the non-default constructor
    report(foo1);
    Foo foo2(); // call the default constructor
    report(foo2);
    Foo foo3(foo1); // make foo3 a reference to foo1
    report(foo3);
    foo3.intMember = 20;
    // since foo1 and foo3 refer to the same object, both change!
    report(foo1);
    Foo foo4 = null; // a null object
    report(foo4);
    foo4.intMember = 42; // throws an exception
  }

.. _KLPG.types.objects.clone:

The Object ``clone()`` Method
"""""""""""""""""""""""""""

.. versionadded:: 1.15.0

As with most other types in KL object types support a method ``clone()`` that does a deep copy of the object.  Every object has a default ``clone()`` implementation.  It is possible to change the behavior of ``clone()`` for an object by writing a custom method ``<ObjectType>.cloneMembersTo(io <ObjectType> that)``.  This method is automatically called during the process of cloning the object, as shown below:

.. kl-example:: Object Custom Clone

  object Obj
  {
    String s;
    Integer n;
  };

  Obj.cloneMembersTo(io Obj that)
  {
    that.s = this.s + " cloned";
    that.n = 2 * this.n;
  }

  operator entry()
  {
    Obj obj1();
    obj1.s = "string";
    obj1.n = 42;
    report("obj1 = " + obj1);

    Obj obj2 = obj1.clone();
    report("obj2 = " + obj2);
  }

.. _KPLG.object.inheritance:

Object inheritance
""""""""""""""""""

.. versionadded:: 1.13.0

Like structures, an object can inherit (or `derive`) from a single base object. The specialized object then inherits from all members and methods of the base object. The :samp:`struct {SpecializedType} : {BaseType}` syntax is used to declare the inheritance relationship.

When inheriting from a base object, the :samp:`{object}.{parent}` syntax allows to perform an explicit cast to that base type. This can be useful for accessing members or methods that have a different definition for the base and the specialized object type.

.. kl-example::

  object MyBaseObject {
    Float32 f;
    Size s;
  };

  object MyObject : MyBaseObject {
    Size s;
  };

  operator entry() {
    MyObject o();
    o.f = 0.5;
    o.s = 2;
    o.parent.s = 1;
    report(o);
  }

.. index::
  single: interfaces
  pair: interface; type

.. _KLPG.types.interfaces:

Interfaces
^^^^^^^^^^^^^^^^^^^^^

.. versionchanged:: 1.12.0
  Can no longer do "empty construction" of variables of interface type

.. versionchanged:: 1.15.0
  Added support for ``<typeExpr>.createNew()`` method

An :dfn:`interface` is a set of methods that an object agrees to implement.  Objects implement the interface by declaring the interface name in the object declaration as well as implementing each of the interface's methods.  The programmer can then use the interface as a first-class type that refers to any type of object that implements the interface.

An interface is defined using the :code:`interface` keyword.  An interface definition is similar to a structure or object definition, except that, instead of members, methods are specified.  For example:

.. code-block:: kl
  
  interface MyInt {
    UInt32 foo();
    bar?(io String s);
    Float32 baz!();
  };

This example defines the interface :code:`MyInt` as providing three methods.  The parameter and return types all work the same as for normal structure and object :ref:`methods <methods>`; however, the :code:`function` keyword and the typename are omitted.  Notice that the :code:`!` and :code:`?` modifiers for the methods also work, indicating explicitly whether the methods may modify the object they are called on.

An interface only specifies a set of methods that objects implementing the interface must support.  In order to use interfaces, you must define objects that support them:

.. code-block:: kl
  
  // An object type that implements MyInt
  object MyObj : MyInt {
    UInt32 n;
    String s;
  };
  
  function UInt32 MyObj.foo() {
    return this.n;
  }
  
  function MyObj.bar?(io String s) {
    s = this.s;
  }
  
  function Float32 MyObj.baz!() {
    return 3.14 * this.n++;
  }

Notice that, in order to implement the interface, we both list the interface after the object type name and the provide implementations for each of the methods.

.. warning::
  
  It is a compile-time error to fail to provide a definition for one or more of the methods required by the interfaces an object implements!

It is possible for an object to implement multiple interfaces:

.. code-block:: kl
  
  interface MyOtherInt {
    fred();
    Float32 baz!();
  };
  
  object MyDoubleObj : MyInt, MyOtherInt {
    Boolean b;
  };
  
  function UInt32 MyDoubleObj.foo() {
    // ....
  }
  
  function MyDoubleObj.bar?(io String s) {
    // ....
  }
  
  function Float32 MyDoubleObj.baz!() {
    this.b = !this.b;
    return this.b? -7.5: 14.5;
  }
  
  function MyDoubleObj.fred() {
    // ...
  }

Notice that it's possible for an object to support multiple interfaces that share methods.  In this case you only need to implement the method once and that implementation will be shared by all interfaces that include this method.

Once an interface has been defined, you can declare a variable that points to an object that implements the interface and call its methods using the :samp:`{int}.{methodName}({arg}, {arg}, ...)` syntax:

.. code-block:: kl
  
  MyInt myInt = null; // does not refer to an object
  myInt = MyObj();
  report(myInt); // reports: {n:0, s:""} since it is a MyObj
  report(myInt.baz()); reports: 0.0
  report(myInt.baz()); reports: 3.14
  myInt = MyDoubleObj(); // releases old object
  report(myInt); // reports: {b:false}
  report(myInt.baz()); reports: -7.5
  report(myInt.baz()); reports: 14.5

Using the :samp:`{interface}.type()` method you can determine the type of the object in interface refers to, and through an assignment or a cast you can obtain a specific object.  This allows for a simple form of weak (or runtime) typing in KL:

.. code-block:: kl
  
  if (myInt.type() == MyObj) {
    MyObj myObj = myInt;
  }
  else if (myInt.type() == MyDoubleObj) {
    MyDoubleObj myDoubleObj = myInt;
  }

In the case that an expression is of type :code:`Type` then calling the ``<typeExpr>.createNew()`` method will create a new instance of the object the interface is an instance of using its empty constructor.  The result is of the :ref:`Object interface <KLPG.interfaces.object>` type:

.. kl-example:: <typeExpr>.createNew()

  object Obj
  {
    String s;
  };

  operator entry()
  {
    Obj obj1();
    obj1.s = "hello";
    report("obj1 = " + obj1);

    Object abstractObject = obj1;

    Obj obj2 = abstractObject.type.createNew();
    report("obj2 = " + obj2);
  }

Assigning or casting an interface to the wrong object will result in a runtime exception.  You can also assign a value whose types is one interface to a variable whose type is another interface; if the underlying object supports the second interface, you will get a non-:code:`null` reference to the second interface on the object, otherwise a runtime exception will occur.

Additional properties of interfaces:

- The cast-to-:code:`Boolean` works exactly as for objects: it checks if the interface referred to is :code:`null`.

- The comparison operators :samp:`{int1} == {int2}` and :samp:`{int1} != {int2}`, as well as the identity operators :samp:`{int1} === {int2}` and :samp:`{int1} !== {int2}`, test whether two interfaces refer to the same (or different) objects. to whatever object it previously referred to.

-  Values of interface type support the method :samp:`<interfaceValue>.uid()` that returns a unique UInt64 that can be used to identify the object the interface refers to.  The value is the same as it would be if `.uid()` were called on the object the interface refers to.

- It is possible to control access to methods of interfaces using the ``public``, ``private``, ``protected`` and ``permits`` keywords; see :ref:`KLPG.types.member-access`.

.. note:: A variable of whose type is an interface cannot point to a structure.  Objects and interfaces are fundamentally different types than structures; see the section :ref:`KLPG.objects-versus-structures`

.. _KLPG.interfaces.object:

The :code:`Object` Interface
"""""""""""""""""""""""""""""""""

There is a special, predefined interface called :code:`Object` that every object in KL always supports.  This both provides backwards compatibility with older versions of the KL language as well as providing a simple way of passing a reference to an arbitrary object (much like a "void pointer" in C).  The :code:`Object` interface does not provide any methods.

.. code-block:: kl
  
  object MyObj { // implicitly implements Object
    String s;
  };
  
  operator entry() {
    Object obj = MyObj();
  }

.. _KLPG.types.member-access:

Structure, Object and Interface Access Contols
""""""""""""""""""""""""""""""""""""""""""""""

.. versionadded:: 1.15.0

Access to members and methods of structures, objects and interfaces can be controlled through the use of the ``public``, ``private`` and ``protected`` keywords.  These keywords behave in a similar way to C++:

- A member or method marked as ``public`` can be accessed by any part of the source code.  This is the behavior when no access is specified.

- A member or method marked as ``private`` can be only be accessed by methods of the structure or object.  Trying to access the member elsewhere will result in an error when the source code is compiled.

- A member or method marked as ``protected`` can be only be accessed by methods of the structure or object as well as structures or objects that inherit from it.  Trying to access the member elsewhere will result in an error when the source code is compiled.

.. kl-example:: Member and Method Access Controls
  
  struct A
  {
    private UInt32 n; // can only be access by methods of A
    protected String s; // can only be accessed by methods of A and structures that inherit from A
  };

  protected A.bar()
  {
  }

  struct B : A
  {
  };

  public B.foo()
  {
    report(this.n); // error since n is private
    report(this.s); // ok since n is protected
    this.bar(); // ok since A.bar() is procted
  }

  operator entry()
  {
    B b;
    report(b.n); // error since n is private
    report(b.s); // error since n is protected
    b.foo(); // ok since B.foo() is public
    b.bar(); // error since A.bar() is protected
  }

It is possible to allow a structure or object to bypass this mechanism from within its methods by using the ``permits`` keyword.  If a structure or object is listed in the ``permits`` section of another structure or object, it can access its private and protected members and methods:

.. kl-example:: Bypassing Acess Controls Using ``permits``
  
  object A;

  object Base permits A
  {
    private UInt32 n;
  };

  object A { Base b; };
  A() { this.b = Base(); }
  A.foo()
  {
    report(this.b.n); // OK since Base permits A
  }

  object B;
  object C;

  object Derived : Base permits B, C
  {
  };

  private Derived.bar() {}

  object B { Derived d; };
  B() { this.d = Derived(); }
  B.baz()
  {
    this.d.bar();  // OK since Derived permits B
  }

  operator entry()
  {
    A a();
    a.foo();
    B b();
    b.baz();
  }

.. _KLPG.interfaces.inheritance:

Interfaces and inheritance
""""""""""""""""""""""""""

.. versionadded:: 1.13.0

In addition to inherit from a :ref:`base object type <KPLG.object.inheritance>`, specialized objects can implement additional interfaces.

.. code-block:: kl

  object MyObj : MyBaseObj, MyInt {
    ...
  };


If a base object implements an interface, the specialized object can provide its own implementation of the interface methods, which will `override` base type's implementation. In this situation, special syntax is required to call base class's implementation of the same interface method: see :ref:`KLPG.method.interface-inheritance`.

.. _KLPG.forward-declarations:

Forward Declaration of Objects and Interfaces
"""""""""""""""""""""""""""""""""""""""""""""

.. versionadded:: 1.12.0
  Forward declaration of objects and interfaces

It is possible to declare the existence of an object or interface without actually defining its members; this is useful when you have a set of co-dependent objects or interfaces.  To forward-declare an object or interface, simply omit the members, methods and/or implemented interfaces.

.. kl-example:: Forward Declaration of Objects and Interfaces

  // Forward delcaration of interface IntTwo
  interface IntTwo;

  interface IntOne {
    add!(IntTwo int);
  };

  interface IntTwo {
    sub!(IntOne int);
  };

  // Forward delcaration of object ObjTwo
  object ObjTwo;

  object ObjOne : IntOne, IntTwo {
    UInt32 a;
    ObjTwo objTwo;
  };

  object ObjTwo {
    ObjOne objOne;
  };

  function ObjOne()
  {
    this.a = 42;
  }

  function ObjOne.add!(IntTwo intTwo) {
    ObjOne objOne = ObjOne(intTwo);
    this.a += objOne.a;
  }

  function ObjOne.sub!(IntOne intOne) {
    ObjOne objOne = ObjOne(intOne);
    this.a -= objOne.a;
  }

  operator entry() {
    ObjOne objOne();
    objOne.add( IntOne(objOne) );
    objOne.sub( IntTwo(objOne) );
    objOne.objTwo = ObjTwo();
    report(objOne);
  }

.. _unowned-object-references:

Unowned Object and Interface References
""""""""""""""""""""""""""""""""""""""""

The runtime cost of tracking all of the references to objects and interfaces can be high.  In certain situations it is desireable to avoid this reference tracking for performance reasons when it is known that there will always be at least one reference to the object in question.  Kl provides the ability to do this using the :samp:`Ref<{ObjectType}>` and :samp:`Ref<{InterfaceType}>` syntax.  This also provides the ability to create object and interface reference loops that do not leak memory.

Unowned references behave exactly the same as regular object and interface references; the only difference is that they don't track references.

.. warning:: It is very easy to create subtle bugs and crashes when using unowned references.  Use them at your own risk!  It is your responsibility to ensure that unowned references refer to objects that are owned by something else.  You can leave an unowned reference refering to an object that has been destroyed but if you try to do anything with it your program will probably crash!

Example use of unowned references:

.. kl-example:: Unowned References
  
  object Foo {
    SInt32 intMember;
    String stringMember;
  };
  
  operator entry() {
    Foo foo(); // Construct a new specific object
    foo.stringMember = "me!";
    report("foo = " + foo);
    Ref<Foo> fooRef = foo; // fooRef is an unowned reference to foo
    report("fooRef = " + fooRef);
  }

.. _KLPG.types.type:

The :code:`Type` Type
"""""""""""""""""""""""""

There is a special type in KL called :code:`Type`.  It represents the type of a
value in KL.  Every value in KL supports a method :code:`{value}.type()` that can be used
to obtain the type of the object, which is a value of type :code:`Type`.

The default value of a variable of type :code:`Type` is the special value :code:`None`.  This is also sometimes the return value of some methods described below.  :code:`None` is not equal to :code:`{value}.type()` for any :code:`{value}`.

You can only do a few things with values of type :code:`Type`; they are primarily used for runtime type inference with interfaces and objects.

- You refer to a value of type :code:`Type` just by refering to the value of the
  type; you can then use this for comparisons:
  
  .. kl-example:: Type Comparisons

    operator entry()
    {
      Type booleanType = Boolean;
      UInt32 uint32;
      report("booleanType == uint32.type" + booleanType == uint32.type);
      Boolean boolean;
      report("booleanType == boolean.type" + booleanType == boolean.type);
    }

- For :ref:`interfaces <KLPG.types.interfaces>` the :code:`{value}.type()` method returns the type of the specific object that the generic object refers to; this is how you do runtime type inference on objects.  See :ref:`KLPG.types.interfaces` for more information.

- Values of type :code:`Type` support the method :code:`{value}.parentType()`.  In the case that the type of :code:`{value}` is a structure or object type with an inherited parent, :code:`parentType()` returns the type of the parent; otherwise, :code:`parentType()` returns :code:`None`.
  
  .. kl-example:: parentType

    object Obj { /*...*/ };
    object SubObj : Obj { /*...*/ };

    operator entry() {
      Type type;
      report("type = " + type );
      report("type.parentType() = " + type.parentType());
      type = Obj;
      report("type = " + type );
      report("type.parentType() = " + type.parentType());
      type = SubObj;
      report("type = " + type );
      report("type.parentType() = " + type.parentType());
    }

- Values of type :code:`Type` support the method :code:`{value}.isA({interfaceType})`, which returns :code:`true` if and only if :code:`{value}` supports the interface :code:`{interfaceType}`.

  .. kl-example:: isA

    interface Int1 { /*...*/ };
    interface Int2 { /*...*/ };
    interface Int3 { /*...*/ };
    object Obj : Int1, Int2 { /*...*/ };
    object SubObj : Obj, Int3 { /*...*/ };

    operator entry() {
      Type nullType;
      Obj obj();
      SubObj subObj();
      report("nullType.isA(nullType) = " + nullType.isA(nullType));
      report("nullType.isA(Obj) = " + nullType.isA(Obj));
      report("nullType.isA(SubObj) = " + nullType.isA(SubObj));
      report("nullType.isA(Int1) = " + nullType.isA(Int1));
      report("nullType.isA(Int2) = " + nullType.isA(Int2));
      report("nullType.isA(Int3) = " + nullType.isA(Int3));
      report("obj.type.isA(nullType) = " + obj.type.isA(nullType));
      report("obj.type.isA(Obj) = " + obj.type.isA(Obj));
      report("obj.type.isA(SubObj) = " + obj.type.isA(SubObj));
      report("obj.type.isA(Int1) = " + obj.type.isA(Int1));
      report("obj.type.isA(Int2) = " + obj.type.isA(Int2));
      report("obj.type.isA(Int3) = " + obj.type.isA(Int3));
      report("subObj.type.isA(nullType) = " + subObj.type.isA(nullType));
      report("subObj.type.isA(Obj) = " + subObj.type.isA(Obj));
      report("subObj.type.isA(SubObj) = " + subObj.type.isA(SubObj));
      report("subObj.type.isA(Int1) = " + subObj.type.isA(Int1));
      report("subObj.type.isA(Int2) = " + subObj.type.isA(Int2));
      report("subObj.type.isA(Int3) = " + subObj.type.isA(Int3));
    }

- You can obtain a description of the type by calling the method
  :code:`{typeValue}.jsonDesc()`.  You can use this to find out things like the members of
  structures at runtime:
    
  .. kl-example:: Type Description

    struct S
    {
      String string;
      UInt32 uint32;
    };

    operator entry()
    {
      report(S.jsonDesc());
    }

.. index::
  single: unowned object references
  pair: unowned object references; type

.. _KLPG.objects-versus-structures:

Objects Versus Structures
"""""""""""""""""""""""""

The decision to use a structure versus an object for a composite type is an important design decision that affects program design as well as runtime behavior and performance.

Structures are usually the best choice for small types that are performance-critical.  If you have complex expressions that will create a lot of temporary values of the given type, you probably want to be using a structure and not an object.  One critical performance aspect is that variables whose types are structures are allocated on the program stack; this means that there is virtually no overhead to allocating and freeing the memory associated with the structure.  Examples of types that should usually be structures are mathematical types such as vectors and transforms.

Objects are usually the best choice for large types that are created and destroyed less significantly less often than they are used.  Objects are allocated on the heap, which is significantly slower than stack allocation.  Additionally, since you can have many different variables point to the same object, objects are a good choice when you want lots of references to the same data.  Hierarchies of data are usually represented with objects.

.. index::
  single: array
  pair: array; type

.. _arrays:

Arrays
^^^^^^

An :dfn:`array` is a sequence of values of the same type (referred to as the array's :dfn:`element type`) that are indexed by integers and placed sequentially in memory.  KL supports three types of arrays: variable-size arrays, fixed-length arrays, and external arrays.  The details of each array type are discussed below.

.. _array-properties:

Regardless of specific type, arrays in KL have several common behaviors:

- Arrays are indexed using the ``[..]`` operator, exactly as in JavaScript and C.  The indexing of arrays is 0-based, again just as in JavaScript and C::
  
    Size values[];    // Declare a variable-size array
    values.push(42);  // Push some elements onto the end of the array
    values.push(21);
    values.push(3);
    report(values[1]); // outputs "21"

- The size of an array is of type ``Size`` and the indexing operator takes an index of type ``Index`` (which is an alias for ``Size``).

- Array declarations can be nested, and can be co-nested with other array types::
  
    Integer b[][];  // A variable-size array of variable-size arrays of integers
    Boolean a[2][]; // An array of 2 variable-size arrays of booleans
    String c<>[];   // An external array of variable-size arrays of strings

- Arrays are :dfn:`passed by reference` into functions and operators, ie. they are not copied.  This means that it takes just a long to pass an array with one million elements to a function as it does to pass an array with one element.

- If running a Fabric client with bounds-checking enabled, indexing into arrays using the indexing operator is bounds-checked; if the index runs off the end of the array an exception is thrown.

.. index::
  single: variable-size arrays
  triple: variable-size; array; type

.. _variable-arrays:

Variable-Size Arrays
""""""""""""""""""""

A :dfn:`variable-size array` is an array whose size can be changed at runtime.  Variable-size arrays are declared by appending ``[]`` to the name of the variable, parameter or structure member where they are declared, eg. ``String strings[]``.

Variable-size arrays have all the :ref:`properties of arrays <array-properties>` as well as the following additional properties:

- The maximum size of a variable-size array is :math:`2^31-1`.

- Variable-size arrays are :dfn:`share-on-assign`, meaning that when you assign one variable-size array to another it does not copy the elements but rather copies a reference to the elements; any changes to one of the arrays changes the other as well.  This is sometimes referred to as a shallow copy (as opposed to a deep copy).  In order to obtain a deep copy of an array, use the ``clone()`` method, described below.

- Variable-size arrays support the following methods and functions:
  
  - By default, a variable array is empty.  If you specify an integer value when it is constructed, the variable array will initially have that many elements.
  
  - The ``push(element)`` method appends an element to the end of the variable-size array.  The size of the array is increased by one.
  
  - The ``pop()`` method removes the last element from the end of the array, and returns that element.  The size of the array is reduced by one.  Calling ``pop()`` on an empty array results in an error.
  
  - The ``size()`` method returns the number of elements in the variable-size array
  
  - The ``resize(newSize)`` method resizes the array.  Any new elements at the end are initialized with the default value for the underlying type.

  - The ``reserve(count)`` method ensures that space is allocated for at least ``count`` elements.  If you know the final number of elements in advance, it is much faster to call ``reserve(...)`` before calling ``push(...)`` many times.
  
  - The ``clone()`` method makes a deep copy of the variable-size array.  The resulting copy is initially not shared with any other variable-size array.
  
  - The ``swap(Size lhsIndex, Size rhsIndex)`` method swaps the values of the array at the two given indices.
  
  - The :samp:`swap({Type} lhs[], {Type} rhs[])` function swaps the contents of the two variable-size arrays.  This swap is performed in constant time and does not copy any data.

.. kl-example:: Variable-Size Arrays

  operator entry() {
    Integer a[];
    report("The array a has size " + a.size() + " and value " + a);
    a.push(42);
    a.push(84);
    report("The array NOW has size " + a.size() + " and value " + a);
    a.resize(4);
    report("The array NOW has size " + a.size() + " and value " + a);
    String b[](4);
    report("b is initially " + b);
  }

.. index::
  single: fixed-size arrays
  triple: fixed-size; array; type

.. _fixed-arrays:

Fixed-Size Arrays
"""""""""""""""""

A :dfn:`fixed-size array` is an array whose size is fixed at runtime.  Fixed-size arrays have much faster performance characteristics than variable-size arrays, therefore should be used in place of variable-sized arrays when the size of an array is known at compile time.  Fixed-size arrays are declared by appending :samp:`[{size}]` to the name of the variable, parameter or structure member where they are declared, eg. ``String strings[4]``.

Fixed-size arrays have all the :ref:`properties of arrays <array-properties>` as well as the following additional properties:

- The maximum size of a fixed-size array is :math:`2^31-1`.

  .. warning::

    Since fixed-size arrays are allocated on the stack (instead of the heap), using very large fixed-size arrays may result in a stack overflow.  It is recommended that fixed-size arrays only be used for arrays that are reasonably small.            

- Fixed-size arrays are copied when they are assigned, ie. they are :dfn:`copy-by-value`.

.. kl-example:: Fixed-Size Arrays

  function Float32 det(Float32 mat[2][2]) {
    return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0];
  }

  operator entry() {
    Float32 mat[2][2];
    mat[0][0] = 3.5;
    mat[0][1] = -9.2;
    mat[1][0] = -2.1;
    mat[1][1] = 8.6;
    report("The determinant of " + mat + " is " + det(mat));
  }

.. index::
  single: external arrays
  triple: external; array; type

.. _external-arrays:

External Arrays
""""""""""""""""

An :dfn:`external array` is an array whose size is fixed when it is created and does not own the data is operates on.  External arrays are primarily used for operator parameters bound to sliced data inside a |FABRIC_PRODUCT_NAME| dependency graph as well as arrays bound to external data within |FABRIC_PRODUCT_NAME| extensions, but they can also be used on their own within KL.  External arrays are declared by appending ``<>`` to the name of the variable, parameter or structure member where they are declared, eg. ``String strings<>``.

External arrays have all the :ref:`properties of arrays <array-properties>` as well as the following additional properties:

- An external array can be constructed from an existing variable array.  This simply points the external array to the data within the variable array at the time the variable array is constructed.  Note however that there are lots of ways that this usage can break, such as through resizing the variable array.  This usage is primarily meant for testing::
  
    String va[];
    va.push("hello");
    String ea<>(va);
    report(ea); // prints ["hello"]

- External arrays support an empty constructor (which constructs an empty external array)::
  
    Size ea<>;
    report(ea); // prints []

- External arrays support a copy constructor and an assignment operator, both of which simply make one external array refer to the same data as the other::
  
    String va[];
    va.push("hello");
    String ea1<>(va);
    String ea2<>(ea1);
    report(ea2); // prints ["hello"]
    String ea3<>;
    ea3 = ea2;
    report(ea3); // prints ["hello"]

- External arrays support a ``size()`` method that returns the number of elements in the external array.

- External arrays can be initialized given a ``data`` pointer as well as a ``size``. This allows you to map arbitrary memory as an array. This is very useful especially when passing data from C++ into KL and back out. You can also use this constructor to reinterpret any memory as an array::
    
    Float32 floats[12];
    for(Size i=0; i<floats.size(); i++)
      floats[i] = Float32(i);
    
    Vec3 vectors<>(floats.data(), floats.size() / 3);
    report(vectors);

- As opposed to variable arrays, External arrays are not ref counted objects. This makes them cheaper to pass around, but can't be used to manage the lifetime of memory. (See next point)

- External arrays do not manage the lifetime of the data they operate on. A variable array will free its memory when it is destroyed, but an external array is simply a mapping to memory owned by something else. An external array should never out-live the owner of the data, else it will map to garbage data::
    
    String ea<>;
    {
      String va[];
      for(Integer i=0; i<2023; i++)
        va.push("hello:" + i);
      String ea1<>(va);
      ea = ea1;
      // At the end of this scope, the variable array is freed, along with its data.
    }
    // The memory of the variable array is now garbage because it has been destroyed. 
    // Printing the data will return garbage data or crash KL. 
    // External arrays must be used with care to avoid mapping to garbage data in this way. 
    report(ea);

The following is an example of using external arrays:

.. kl-example:: External Arrays

  operator entry() {
    String va[];
    for (Size i=0; i<8; ++i)
      va.push("string " + (i+1));
    
    String strings<>(va);
    for (Size i=0; i<8; ++i)
      strings[i] += " appended";
    report("strings = " + strings);
    report("va = " + va);
  }

.. index::
  single: dictionaries
  pair: dictionary; type

.. _dictionaries:

Dictionaries
^^^^^^^^^^^^

KL supports key-value pair :dfn:`dictionaries`.  The type of the key of a dictionary can be any of the KL base types (e.g. :code:`Boolean`, ``String``, or any integer or floating-point type) as well as custom types for which a special :samp:`.hash` method has been defined (see :ref:`KLPG.dictionaries.custom-key-types`) and the type of the value can be any type.  Dictionaries are declared by appending :samp:`[{KeyType}]` to the variable, parameter or member name.  For example:

.. kl-example::
  :no-output:
  
  String scalarToString[Float32];     // A Float32-to-String dictionary
  Boolean integerToBoolean[Integer];  // An Integer-to-Boolean dictionary

Dictionaries in KL have the following properties:

- Dictionaries are :dfn:`share-on-assign`, meaning that when you assign one dictionary to another it does not copy the contents but rather copies a reference to the contents; any changes to one of the dictionaries changes the other as well.  This is sometimes referred to as a shallow copy (as opposed to a deep copy).  In order to obtain a deep copy of a dictionary, use the ``clone()`` method, described below.

- Dictionaries can be nested, and can be co-nested with array types.  For example:
  
  .. kl-example::
    :no-output:

    Integer b[String][2]; // An String-to-Fixed-Length-Integer-Array dictionary
    Boolean a[][Integer]; // A variable array of Integer-to-Boolean dictionaries

- Dictionaries can contain at most :math:`2^32-1` key-value pairs.

- Dictionaries support the :samp:`has({key})` method that returns a :code:`Boolean` value indicating whether there is a value in the dictionary for the given key.

- Dictionaries support the :samp:`get({key})` method that returns the value associated with the given key.  If there is no value for the given key, an exception is thrown.

- Dictionaries support the :samp:`set({key}, {value})` method that sets the value for the key, replacing the existing value if there is already a value for the key.

- Dictionaries support indexing using the :samp:`[{key}]` indexing operator.  When used as the target of an assignment or as an io parameter to a function (eg. :samp:`{dict}[{key}] = {value}`), it is equivalent to using the :samp:`set({key}, {value})` method.  When used as a read-only expression (eg. :samp:`{value} = {dict}[{key}]`), it is equivalent to using the :samp:`get({key})` method.

- Dictionaries support the :samp:`get({key}, {defaultValue})` method that returns the value associated with the given key, if it exists, or :samp:`{defaultValue}`` if there is no value for the given key.

- Dictionaries support the :samp:`delete({key})` method that deletes the value for the given key.  If there is no value for the given key, nothing happens.

- Dictionaries support the ``clone()`` method which makes a deep copy of the dictionary.  The resulting copy is initially not shared with any other dictionaries.

- Dictionaries support the ``clear()`` method which removes all keys and values.

- Dictionaries can be iterated over using JavaScript-like ``in`` iteration:
    
  .. kl-example::
    :no-output:

    String dict[String];
    for (k in dict)
      report("dict[" + k + "] = " + dict[k]);
  
  For improved performance, both the key and value can be made available through ``in`` iteration:
    
  .. kl-example::
    :no-output:

    String dict[String];
    for (k, v in dict)
      report("dict[" + k + "] = " + v);

  In a dictionary iteration, the value can be assigned to if and only if the dictionary can be assigned to.  The key, on the other hand, cannot be assigned to.

- Insertion order (not sort order!) is the iteration order for dictionaries, just as for JavaScript objects:
  
  .. kl-example::

    operator entry() {
      String numbers[Integer];
      numbers[3] = "three";
      numbers[2] = "two";
      report(numbers);
      numbers[1] = "one";
      report(numbers);
    }

The following is an example use of dictionaries:

.. kl-example:: Dictionaries

  operator entry() {
    Float32 a[String];
    a['pi'] = 3.14;
    a['e'] = 2.71;
    report("a is:");
    for ( k, v in a ) {
      report("a['" + k + "'] = " + v);
    }
    a.delete('pi');
    report("a is now:");
    for ( k, v in a ) {
      report("a['" + k + "'] = " + v);
    }
  }

.. index::
  pair: dictionary; custom key type

.. _KLPG.dictionaries.custom-key-types:

Dictionaries Using Custom Key Types
"""""""""""""""""""""""""""""""""""

You can use a custom :samp:`struct` as a key type for a dictionary by implementing a :samp:`.hash` method for the type as well as a :samp:`==` operator:

.. kl-example:: Dictionary with Custom Key Type

  struct S {
    UInt32 n;
    Float32 x;
  };


  function S(UInt32 n, Float32 x) {
    this.n = n;
    this.x = x;
  }

  function Boolean ==(S lhs, S rhs ) {
    return lhs.n == rhs.n && lhs.x == rhs.x;
  }

  function UInt32 S.hash() {
    return this.n.hash() ^ this.x.hash();
  }

  operator entry() {
    String d[S];
    d[S(56,2.4)] = "one";
    d[S(78,-1.2)] = "two";
    report(d);
  }

.. index::
  pair: type; map-reduce

Map-Reduce Types
^^^^^^^^^^^^^^^^

There are two additional derived types used exclusively for work within Fabric's map-reduce framework, namely:

- :samp:`ValueProducer<{Type}>`
- :samp:`ArrayProducer<{Type}>`

For more information, see :ref:`map-reduce`.

.. index::
  single: type aliases
  pair: type; alias

Implicit Type Casting Rules in KL
---------------------------------

When a function or method is called in KL, but the types of the arguments do not exactly match the types of the parameters for any polymorphic version of the function or method, KL will attempt to find the best match using implicit casts.  The best match is chosen as follows:

- The number of arguments must exactly match the number of parameters.  Therefore, if there is a mismatch, the polymorphic version is not considered.  For example, if the function call :code:`foo(14, 23)` is made and there is a function :code:`foo(Integer)` available, it will not be considered because it only takes one parameter but two arguments have been given.

- If the number of parameters matches the number of arguments, the "cost" of the call is computed as the maximum "cost" for each argument.  The cost for each argument is computed as follows:

  - The cost is zero if there is an exact type match
  - The cost is very low for inheritance, ie. if the parameter type is :code:`A`, the argument type is :code:`B`, and :code:`B` inherits from :code:`A`
  - Otherwise, the cost is computed on a per-type basis, and are what would generally be expected.  For instance, casts from smaller integer values to larger ones (eg. :code:`UInt16` to :code:`UInt32`) are very low cost, whereas expensive operations (conversions to strings, numerical conversions that might lose precision) have a high cost.

Type Aliases
------------

The ``alias`` statement can be used to alias a type to make code more readable.  Its syntax is the same as a variable declaration::

  alias Integer Int32;        // Int32 is now an alias for Integer
  alias Float32 float;        // float is now an alias for Float32
  alias Float32 Mat22[2][2];  // Mat22 is now an alias for Float32[2][2], ie. a size-2-array-of-size-2-arrays-of-Float32

``alias`` statements must appear within the global scope of a KL program.

.. kl-example:: Type Aliases

  alias Float32 Mat22[2][2];
  
  operator entry() {
    Mat22 mat22;
    report(mat22);
  }

.. index::
  pair: Data; type
  pair: data; method
  pair: dataSize; method

The ``Data`` Type and the ``data`` and ``dataSize`` Methods
-----------------------------------------------------------

When interfacing with external libraries such as OpenGL, it is sometimes necessary to get direct access to the data underlying a value.  An example is a library call that takes a pointer to data.  KL itself has no notion of pointers; instead, KL has the concept of the ``Data`` type whose value is a pointer to data which can be passed to an external library call.

Most values in KL have a built-in method called ``data`` that returns a value of type ``Data``, and a built-in method called ``dataSize`` that returns a value of type ``Size``.  The value returned by the ``data`` method is a pointer to the data underlying the value, and the value returned by the ``dataSize`` method is the number of bytes the value occupies in memory.  The only values which do not support the ``data`` and ``dataSize`` methods are dictionaries as well as other derived types that do not lay out their elements or members contiguously in memory:

.. kl-example:: Valid and Invalid Use of .data() and .dataSize()
  :no-output:

  Integer integers[];
  report(integers.data());  // OK: integers are contiguous in memory
  String strings[];
  report(strings.data());   // ERROR: string data is not contiguous in memory

Unlike pointers in C and C++, the values returned by ``data`` methods cannot be inspected or used in any expressions; the only thing which can be done is a cast to :code:`Boolean`, which will be :code:`true` if and only if the ``Data`` value points to a value whose size is greater than zero.  However, these ``Data`` values can be passed directly to external library functions provided by Fabric itself or Fabric extensions, where they are used as pointers to data in memory.

.. note:: For values of type ``String``, the value returned by ``dataSize`` includes a null terminator that is automatically appended to the string by Fabric; this is so that the string data can be directly used in C library calls as a regular C string.  If you want to pass the number of characters in the string, pass ``string.length`` instead.

Example of ``Data`` values and the ``data`` and ``dataSize`` methods:

.. kl-example:: .data() and .dataSize()

  operator entry() {
    String s;
    report("s = '" + s + "'");
    report("s.data() = " + s.data());
    report("Boolean(s.data()) = " + Boolean(s.data()));
    report("s.dataSize() = " + s.dataSize());
    s = "Hello";
    report("s = '" + s + "'");
    report("s.data() = " + s.data());
    report("Boolean(s.data()) = " + Boolean(s.data()));
    report("s.dataSize() = " + s.dataSize());
  }
