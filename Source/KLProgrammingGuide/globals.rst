.. _globals:

Functions and Other Global Declarations
=======================================

In this chapter we detail the different entities that can appear in the global scope of a KL program, including functions and function-like entities, name constants, and instances of the ``require`` statement.  Structure and object definitions can also appear in the global scope and are covered in the section :ref:`KLPG.types`.

.. index::
  single: function

.. _functions:

Functions
---------

A function is a collection of program statements that can be called from another part of a program.  A function takes a list of zero or more :dfn:`parameters` and optionally returns a :dfn:`return value`.

.. index::
  pair: function; definition

Function Definitions
^^^^^^^^^^^^^^^^^^^^

Function definitions in KL are much the same as the "traditional" function definition syntax in JavaScript, with the following key differences:

- The return type and the type of each function parameter must be explicitly declared.  If a function does not return a value, the return type must be omitted.

- The parameter declarations may additionally declare the parameter as input (read-only; the default) by preceding the type by ``in`` or input-output (read-write) by preceding the value by ``io``.

- Functions can optionally be defined using the ``inline`` keyword in place of ``function``; see :ref:`inline`.

- The ``function`` keyword is optional.  If neither ``function`` nor ``inline`` is present then ``function`` is assumed.

.. kl-example:: Function Definitions

  // Function returning a value and using only
  // input parameters
  
  function Float32 add(Float32 lhs, Float32 rhs) {
    return lhs + rhs;
  }
  
  // Function not returning a value and using both
  // input and input-output parameters
  
  function add(in Float32 lhs, in Float32 rhs, io Float32 result) {
    result = lhs + rhs;
  }

  // The 'function' keyword is totally optional
  Float32 double(Float32 x) {
    return 2 * x;
  }

  operator entry() {
    report(add(2, 2));

    Float32 addResult;
    add(2, 2, addResult);
    report(addResult);

    report(double(2));
  }

.. index::
  pair: function; invocation

Function Invocations
^^^^^^^^^^^^^^^^^^^^

Function invocations ("calls") are made using the same syntax as JavaScript, namely by appending a comma-delimited list of arguments, surrounded by parentheses, to the function name.

.. kl-example:: Function Invocation

  function Integer add(Integer lhs, Integer rhs) {
    return lhs + rhs;
  }

  operator entry() {
    report("2 plus 2 is " + add(2, 2));
  }

.. index::
  pair: function; prototype

Function Prototypes
^^^^^^^^^^^^^^^^^^^

A :dfn:`function prototype` in KL is a function declaration that is missing a body.  Providing a function prototype allows the function to be called before it is defined.  This is useful under two circumstances:

- When two or more functions call each other.  Such functions are sometimes referred to as :dfn:`co-recursive`:
  
  .. kl-example:: Co-recursive Functions
  
    // Function prototype for 'two', so that 'one' can call it before it is defined
    function two(Integer n);
    
    // The function 'one' calls 'two' even though it is not yet defined
    function one(Integer n) {
      report("one");
      if (n > 0)
        two(n - 1);
    }
    
    // The definition of the function 'two' comes after its prototype
    function two(Integer n) {
      report("two");
      if (n > 0)
        one(n - 1);
    }
    
    operator entry() {
      one(4);
    }

- When a function definition is provided by a Fabric extension.  The name of the symbol of the function in the Fabric extension is provided by appending :samp:`= "{symbol name}"` or :samp:`= '{symbol name}'` to the function prototype.  These is usually referred to as :defn:`external functions`:
  
  .. kl-example:: External Functions
    :no-output:
    
    // The prototype 'libc_perror' is linked to an external function 'perror'
    function libc_perror(Data cString) = 'perror';
    
    // The KL function 'perror' is what KL functions actually call
    function perror(String string) {
      libc_perror(string.data());
    }
    
    operator entry() {
      perror("something that caused an error");
    }

.. _polymorphism:

Polymorphism
---------------------

KL supports :dfn:`compile-time function polymorphism`.  This means that you can have multiple functions with the same name so long as they have a different number of parameters or those parameters differ by type and/or their input versus input-output qualification.

.. note:: It is an error to have two functions with the same name that take exactly the same parameter types but return different types

When a function call is made in KL source, if there are multiple functions with the same name then the KL compiler uses a best-match system to determine which function to call.  Exact parameter type matches are always prioritized over type casts.  If the compiler is unable to choose a unique best match then an error will be reported showing the ambiguity.

The following example demonstrates a simple use of function polymorphism:

.. kl-example:: Function Polymorphism

  function display(Integer a) {
    report("integer value is " + a);
  }
  
  function display(String s) {
    report("string value is '" + s + "'");
  }
  
  operator entry() {
    Integer integer = 42;
    display(integer);
    
    String string = "hello";
    display(string);
    
    Byte byte = 64;
    display(byte);
  }

.. index::
  single: operator

.. _operators:

Operators
---------

The ``operator`` keyword in KL is used to mark functions that are to be used as entry points into KL from the Fabric dependency graph.  Operators are declared in the same way as functions except that they must not return a value.  Fabric does special type-checking to ensure that operators are bound properly to nodes in a Fabric dependency graph.

.. code-block:: kl

  operator addElements(io Float32 lhs, io Float32 rhs, io Float32 result) {
    result = lhs + rhs;
  }

.. index::
  single: constructor

.. _KLPG.constructor:

Constructors
------------

A :dfn:`constructor` for a user-defined type is a function that initializes a value with the given the type from other values.

.. index::
  pair: constructor; declaration

Constructor Declarations
^^^^^^^^^^^^^^^^^^^^^^^^

A constructor is declared as a function whose name is the name of the user-defined type.  The function can take any number of parameters, all of which must be input parameters; constructors cannot take input-output parameters.  Constructors cannot return values.

Within the body of a constructor definition, the value being initialized is referred to with the ``this`` keyword; its members are accessed using the ``.`` (dot) operator.  In this context, ``this`` is always read-write, ie. its members can be modified.

.. kl-example:: Constructor Declarations

  struct Complex32 {
    Float32 re;
    Float32 im;
  };

  // The empty constructor; 
  function Complex32() {
    this.re = this.im = 0.0;
  }

  // Construct a Complex from a Float32
  function Complex32(Float32 x) {
    this.re = x;
    this.im = 0.0;
  }

  // Construct a Complex from two Float32s
  function Complex32(Float32 x, Float32 y) {
    this.re = x;
    this.im = y;
  }

  operator entry() {
    report(Complex32());
    report(Complex32(3.141));
    report(Complex32(3.141, 2.718));
  }

Like functions, constructors can optionally be defined using the ``inline`` keyword in place of ``function``; see :ref:`inline`.

.. index::
  pair: constructor; invocation

Constructor Invocation
^^^^^^^^^^^^^^^^^^^^^^

Constructors are invoked in one of several ways.

Naked Initialization
""""""""""""""""""""

If a variable is declared without any initialization, the :dfn:`empty constructor` (ie. the constructor that takes no parameters) is invoked to initialize the variable.  This is referred to as :dfn:`naked initialization`.

.. kl-example:: Naked Initialization
  
  struct MyType {
    Integer n;
    Float32 x;
  };
  
  // The empty constructor
  function MyType() {
    this.n = 42;
    this.x = 3.141;
  }
  
  operator entry() {
    MyType myType; // invokes the empty constructor
    report(myType);
  }

Assignment Initialization
"""""""""""""""""""""""""

If a variable is assigned to as part of its declaration, a single-parameter constructor is invoked.  This is referred to as :dfn:`assignment initialization`.  If there isn't an exact match for the type of the value assigned, best-match polymorphism rules are used to choose the constructor to invoke.

Example:

.. code-block:: kl

  struct MyType {
    String string;
  };
  
  // Construct from a string
  function MyType(String string) {
    this.string = "The string was '" + string + "'";
  }
  
  // Construct from a scalar
  function MyType(Float64 float64) {
    this.string = "The float64 was " + float64;
  }
  
  operator entry() {
    // Construct MyType from String value
    MyType myTypeFromString = "foo";
    report(myTypeFromString);
  
    // Construct MyType from Float64 value
    MyType myTypeFromFloat64 = 2.718;
    report(myTypeFromFloat64);
  
    // There is no constructor that takes a Boolean but
    // there is a cast from Boolean to String
    MyType myTypeFromBoolean = true;
    report(myTypeFromBoolean);
  }

Output:

.. code-block:: none

  {string:"The string was 'foo'"}
  {string:"The float64 was 2.718"}
  {string:"The string was 'true'"}

Invocation Initialization
"""""""""""""""""""""""""

If a variable is "called" (ie. using function call syntax) as part of its declaration, the constructor taking the given arguments is invoked.  This is referred to as :dfn:`invocation initialization`.  If there isn't an exact match for the arguments passed to the call, best-match polymorphism rules are used to choose the constructor to invoke.

Example::

  struct Vec2 {
    Float64 x;
    Float64 y;
  };
  
  // Construct from two scalars
  function Vec2(Float64 x, Float64 y) {
    this.x = x;
    this.y = y;
  }
  
  operator entry() {
    Vec2 vec2FromFloat64s(3.141, 2.718);
    report(vec2FromFloat64s);
    Vec2 vec2FromIntegers(42, -7);  // Uses best-match polymorphism to convert Integer to Float64
    report(vec2FromIntegers);
  }

Output::

  {x:3.141,y:2.718}
  {x:42,y:-7}

.. _KLPG.constructor.invocation.temporary:

Temporary Initialization
""""""""""""""""""""""""

If a function call is performed where the name of the function is the name of the type, the constructor taking the given arguments is invoked to create a temporary value of the named type.  If there isn't an exact match for the arguments passed to the call, best-match polymorphism rules are used to choose the constructor to invoke.  This is refered to as :dfn:`temporary initialization`.

.. note:: KL does not distinguish between construction and casting.  Casting a value to a different type is the same as constructing a temporary value of the given type and initializing it, using the appropriate constructor, from the given value.

Example:

.. code-block:: kl

  struct Vec2 {
    Float64 x;
    Float64 y;
  };
  
  // Construct from two scalars
  function Vec2(Float64 x, Float64 y) {
    this.x = x;
    this.y = y;
  }
  
  operator entry() {
    report(Vec2(3.141, 2.718));
    report(Vec2(42, -7));  // Uses best-match polymorphism to convert Integer to Float64
  }

Output::

  {x:3.141,y:2.718}
  {x:42,y:-7}

Base type constructors (inheritance)
""""""""""""""""""""""""""""""""""""

.. versionadded:: 1.13.0

When a specialized structure or object type :ref:`inherits <KPLG.object.inheritance>` from a base type, the base type's default constructor is implicitly called before the specialized type's one.

.. note::

  It is a current limitation that base type constructors with arguments cannot be called by specialized type constructors. The following example uses an `initialize` method to workaround this issue:

  .. kl-example::

    object Shape {
      Float32 centerX, centerY;
    };

    inline Shape( Float32 centerX, Float32 centerY ) {
      this.initialize( centerX, centerY );
    }

    /// \internal
    inline Shape.initialize!( Float32 centerX, Float32 centerY ) {
      this.centerX = centerX;
      this.centerY = centerY;
    }

    object Circle : Shape {
      Float32 radius;
    };

    inline Circle( Float32 centerX, Float32 centerY, Float32 radius ) {
      this.parent.initialize( centerX, centerY );
      this.radius = radius;
    }

    operator entry() {
      Circle c( 1, 2, 3);
      report( c );
    }


.. index::
  single: destructor

.. _KLPG.destructor:

Destructors
-----------

A destructor is a function that is called when a variable goes out of scope and its resources are freed.  Destructors are declared by prepending ``~`` (tilde) in front of the name of the type and using it as a function.  Destructors cannot take any parameters or return values.  The destructor is called before the value is freed so that its members are still accessible.  In the body of the destructor the value is referred to using the ``this`` keyword; the value is input-output, ie. it can be modified in the destructor.

Example use of destructor:

.. code-block:: kl

  struct MyType {
    String s;
  };
  
  // Empty constructor
  function MyType() {
    this.s = "foo";
    report("Creating MyType: this.s = " + this.s);
  }
  
  // Destructor
  function ~MyType() {
    report("Destroying MyType: this.s = " + this.s);
  }
  
  operator entry() {
    MyType myType;
  }

Output::

   Creating MyType: this.s = foo
   Destroying MyType: this.s = foo

Like functions, destructors can optionally be defined using the ``inline``
keyword in place   of ``function``; see :ref:`inline`.

When a specialized structure or object type :ref:`inherits <KPLG.object.inheritance>` from a base type, base type's destructor is called after the specialized one.

.. index::
  single: method

.. _methods:

Methods
-------

A :dfn:`method` is a function that operates on a user-defined structure.  It uses a slightly different (and more suggestive) syntax than plain function calls for the case that the method call is strongly tied to a value whose type is a user-defined structure.

.. index::
  pair: method; definition

Method Definitions
^^^^^^^^^^^^^^^^^^

If :samp:`{Type}` is a structure or alias, then a method named :samp:`{methodName}` can be added to the type using the following syntax:

.. code-block:: kl

  // A method that returns a value
  function <ReturnType> <Type>.<methodName>(<parameter list>) {
    <method body>
  }
  
  // A method that does not return a value
  function <Type>.<methodName>(<parameter list>) {
    <method body>
  }

Within the method body, ``this`` refers to the value on which the method is called.  ``this`` is read-only if the method returns a value and is read-write if the method does not return a value.

Like functions, methods can optionally be defined using the ``inline``
keyword in place   of ``function``; see :ref:`inline`.

.. index::
  pair: method; invocation

Method Invocation
^^^^^^^^^^^^^^^^^

If :samp:`{value}` is a value of type :samp:`{Type}` then the method :samp:`{methodName}` can be invoked on :samp:`{value}` using the expression :samp:`{value}.{methodName}({argument list})`.

Just as there can be multiple functions with the same name, a given type can have multiple methods with the same name.  When deciding which method to invoke, the usual best-match rules apply.

Example of method definition and invocation:

.. kl-example:: Method Definition and Invocation

  struct MyType {
    Integer a;
    Float32 b;
  };
  
  // Add method desc to MyType
  function String MyType.desc() {
    return "a:" + this.a + "; b:" + this.b;
  }
  
  operator entry() {
    MyType t;
    t.a = 1;
    t.b = 3.14;
    // Reports 'a:1; b:3.14'
    report(t.desc());
  }

.. _KLPG.method.this-type:

Methods Taking Read-Only or Read-Write Values for ``this``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. versionchanged:: 1.12.0
  :code:`this` now always defaults to read-only in method definitions unless an explicit :code:`!` is specified after method name; the default no longer depends on whether the method returns a value.

Whether :code:`this` is read-only or read-write (in compiler terms, an r-value or an l-value) can be controlled on a per-method basis.  By default, :code:`this` is read-only; :code:`this` can be made read-write by suffixing the method name with ``!`` (exclamation mark).  The method name can be suffixed with :code:`?` (question mark) to explicitly mark read-only methods.

Example of explicit read-only or read-write :code:`this` in methods:

.. kl-example:: Explcit read-only or read-write "this" in methods

  struct Vec2 {
    Float64 x;
    Float64 y;
  };
  
  function Vec2(in Float64 x, in Float64 y) {
    this.x = x;
    this.y = y;
  }
  
  // Explicitly make 'this' read-only
  function Vec2.getComponents?(io Float64 x, io Float64 y) {
    x = this.x;
    y = this.y;
  }
  
  function Float64 Vec2.normSq() {
    return this.x*this.x + this.y*this.y;
  }
  
  function Float64 Vec2.norm() {
    return sqrt(this.normSq());
  }
  
  function Vec2./=(in Float64 value) {
    this.x /= value;
    this.y /= value;
  }
  
  // Explicitly make 'this' read-write
  function Float64 Vec2.normalizeAndReturnOldNorm!() {
    Float64 oldNorm = this.norm();
    this /= oldNorm;
    return oldNorm;
  }
  
  operator entry() {
    Vec2 vec2(3.14, 2.71);
    
    Float64 x, y;
    vec2.getComponents(x, y);
    report("vec2.getComponents: x=" + x + ", y=" + y);
    
    report("vec2.normalizeAndReturnOldNorm returned " + vec2.normalizeAndReturnOldNorm());
    report("vec2 is now " + vec2);
  }

.. _KLPG.method.interface-inheritance:

Interface methods and inheritance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. versionadded:: 1.13.0

Although it is usually transparent to the KL coder, interface method's calling mechanism differs from usual methods, and this requires special care in some situations.

A specialized object can inherit from a :ref:`base object type <KPLG.object.inheritance>`. If that base type implements an interface, the specialized object can provide its own implementation of the same interface methods. In that case, invoking the interface method will always call the specialized version of the method (the specialized object method `overrides` the base object method). This is always true, and it doesn't matter if the method is called in the context of functions, specialized object's methods, or base object's method.

However, it is frequent that the specialized implementation of a method needs to invoke its base implementation. The :samp:`{Type}.parent.{methodName}` syntax allows a specialized class to invoke the base implementation of an interface method, as seen below:

.. kl-example::

  interface Described {
    String describe();
  };

  object Shape : Described {
    Float32 centerX, centerY;
  };

  function String Shape.describe() {
    return "Center: (" + this.centerX + ", " + this.centerY + ")";
  }

  object Circle : Shape {
    Float32 radius;
  };

  inline Circle.setRadius!( Float32 r ) {
    this.radius = r;
  }

  function String Circle.describe() {
    // Call Shape.describe and append to it
    return this.parent.describe() + " Radius: " + this.radius;
  }

  operator entry() {
    Circle c();
    c.centerX = 1;
    c.centerY = 2;
    c.radius = 3;

    Described d = c;
    report( d.describe() );
  }

.. _KLPG.methods.access:

Access to Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. versionadded:: 1.15.0

Access to methods can be controlled in the same was as :ref:`access to members <KLPG.types.structs.member-access>` using the ``public``, ``private`` and ``protected`` keywords:

.. kl-example:: Access to Methods

  interface Int
  {
    private int_priv();
    protected int_prot();
  };

  object A : Int
  {
  };

  public A.a_pub()
  {
    this.int_priv(); // ok since A implements Int
    this.int_prot(); // ok since A implements Int
  }

  protected A.a_prot() {}
  private A.a_priv() {}

  A.int_priv() {}
  A.int_prot() {}

  object B : A
  {
  };

  public A.b_pub()
  {
    this.int_priv(); // error since int_priv is private
    this.int_prot(); // ok since B inherits A
  }

  protected B.b_prot()
  {
    this.a_prot(); // ok since B inherits A 
  }

  private B.b_priv()
  {
    this.a_priv(); // error since a_priv is private
  }

  operator entry()
  {
    A a();
    a.a_pub(); // ok since a_pub is public
    a.a_prot(); // error since a_prot is protected
    a.a_priv(); // error since a_prot is private

    B b();
    b.b_pub(); // ok since a_pub is public
    b.b_prot(); // error since a_prot is protected
    b.b_priv(); // error since a_prot is private
  }

.. index::
  single: overload

Overloaded Operators
--------------------

KL allows overloading of binary operators and compound assignment operators for custom types (ie. specified through ``struct``).

Like functions, operator overloads can optionally be defined using the
``inline`` keyword in place   of ``function``; see :ref:`inline`.

.. index::
  pair: binary; overload

Binary Operator Overloads
^^^^^^^^^^^^^^^^^^^^^^^^^

Binary operators can be overloaded using the following syntax:

.. kl-example:: Binary Operator Overloads

  struct MyType {
    Integer a;
    Float32 b;
  };
  
  function MyType +(MyType lhs, MyType rhs) {
    MyType result;
    result.a = lhs.a + rhs.a;
    result.b = lhs.b + rhs.b;
    return result;
  }
  
  operator entry() {
    MyType t1; t1.a = 42; t1.b = 3.14; report(t1);
    MyType t2; t2.a = 7; t2.b = 2.72; report(t2);
    MyType t3 = t1 + t2; report(t3);
  }

Any of the binary arithmetic (``+``, ``-``, ``*``, ``/`` and ``%``), bitwise (``|``, ``&``, ``^``, ``<<`` and ``>>``) and comparison (``==``, ``!=``, ``<``, ``<=``, ``>`` and ``>=``) operators can be overloaded.

Binary operator overloads are subject to the following restrictions:

- They must take exactly two parameters.  The two parameters may be of any type and the two types may be different but they must both be input-only parameters.

- They must return a value.  However, the return type can be any type.

.. index::
  pair: unary; overload

.. _KLPG.unary-op-overloads:

Unary Operator Overloads
^^^^^^^^^^^^^^^^^^^^^^^^^

.. versionadded:: 1.12.0
  Unary Operator Overloads

Unary operators can be overloaded using the following syntax:

.. kl-example:: Binary Operator Overloads

  struct MyType {
    Integer a;
    Float32 b;
  };
  
  function MyType -MyType() {
    MyType result;
    result.a = -this.a;
    result.b = -this.b;
    return result;
  }
  
  operator entry() {
    MyType t1; t1.a = 42; t1.b = 3.14; report(-t1);
    MyType t2; t2.a = 7; t2.b = 2.72; report(-t2);
  }

Only the unary operators ``+``, ``-`` and ``~`` can be overloaded.

Unary operator overloads are subject to the following restrictions:

- They must return a value.  However, the return type can be any type.

.. index::
  pair: compound assignment; overload

.. _overloading-direct-ass-op:

Direct Assignment Overloads
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

KL provides a default direct assignment for custom types which simply assigns each of the members.  However, it is also possible to provide an overload for the direct assignment operator as shown in the example below::

.. kl-example:: Direct Assignment Overload

  struct A {
    UInt32 a;
  };

  A(UInt32 x) {
    this.a = x;
  }

  A.=(A a) {
    report("Performing assignment");
    this.a = 2 * a.a;
  }

  operator entry() {
    A a1(42), a2(56);
    report("Before: a1 = " + a1 + ", a2 = " + a2);
    a1 = a2;
    report("After: a1 = " + a1 + ", a2 = " + a2);
  }

Compound assignment overloads are subject to the following restrictions:

- They must take exactly one parameter.  The parameter may be of any type but it must be an input-only parameter.

- They must not return a value.

.. _overloading-compound-ass-ops:

Compound Assignment Overloads
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

KL provides a default direct assignment for custom types which simply assigns each of the members.  It also provides a default :dfn:`compound assignment` operator (ie. ``+=``, ``-=``, ``*=``, ``/=``, ``%=``, ``|=``, ``&=``, ``^=``, ``<<=`` and ``>>=``) by composing the associated binary operator, if available, with an assignment.

However, it is also possible to provide an overload for any of the compound assignment operators using the following syntax::

  struct Type {
    Integer a;
    Float32 b;
  };
  
  function Type.+=(Type that) {
    this.a += that.a;
    this.b += that.b;
  }
  
  operator entry() {
    Type t1; t1.a = 42; t1.b = 3.14; report("t1 is " + t1);
    Type t2; t2.a = 7; t2.b = 2.72; report("t2 is " + t2);
    t1 += t2; report("t1 is now " + t1);
  }

This produces the following output::

  t1 is {a:42,b:3.14}
  t2 is {a:7,b:2.72}
  t1 is now {a:49,b:5.86}

Compound assignment overloads are subject to the following restrictions:

- They must take exactly one parameter.  The parameter may be of any type but it must be an input-only parameter.

- They must not return a value.

.. index::
  pair: function; inline
  pair: method; inline

.. _inline:

Inline Functions and Methods
------------------------------

Functions, methods, and so on--but not operators--can optionally be declared
with the ``inline`` keyword in place of the ``function`` keyword, which tells
KL to try to inline the function  definition wherever it is used. ``inline``
should generally only be used on small functions, which this may result in
improved runtime performance::

  inline Integer add(Integer lhs, Integer rhs) {
    return lhs + rhs;
  }

.. index::
  pair: function; built-in

Built-In Functions and Methods
------------------------------

KL has several built-in functions and methods that are available to all KL programs.

Debugging Functions
^^^^^^^^^^^^^^^^^^^^^^

.. kl:function::
  function report(String message)
  
  Outputs a message to wherever messages are sent from KL; when |FABRIC_PRODUCT_NAME| is used from the command line or when the KL tool is used the output is sent to standard error and standard output respectively.  A newline is appended to the message when it is sent.
  
  Within |FABRIC_PRODUCT_NAME| the report function is primarily used for debugging, whereas it is used for general output from the KL tool.

.. kl:function::
  function dumpstack()
  
  .. versionadded:: 1.13.0

Outputs the KL function call stack that leads to the calling location, including KL file names and line numbers. For example the following KL code::

  function func2()
  {
    dumpstack();
  }

  function func1()
  {
    func2();
  }

  operator entry()
  {
    func1();
  }

Will output::

  1 function.func2() call.kl:4
  2 function.func1() call.kl:9
  3 operator.entry() call.kl:14
  4 kl.internal.entry.stub.cpu()

Error Status Functions
^^^^^^^^^^^^^^^^^^^^^^

KL maintains a contextual error status which can be set, queried and reset using some built-in functions. This status is restricted to the contextual KL evaluation and thread. Some KL operations such as integer divide-by-zero and array out-of-bounds access (when running KL with bounds checking enabled) will internally call :kl:func:`setError`. |FABRIC_PRODUCT_NAME| extensions typically set the error status as a way to report operation failures.

.. kl:function::
  function String getLastError()
  
  Get the last error status that was set.

.. kl:function::
  function clearLastError()
  
  Resets the last error status.

.. kl:function::
  function setError(String status)
  
  Sets a new error status and reports it using the :kl:func:`report` mechanism.

.. _integer_numerical_functions:

Integer Numerical Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

KL has support for several integer numerical functions that are helpful when dealing with integer expressions.  Each of these functions has a version for each of the numerical types (``UInt8``, ``SInt8``; ``UInt16``, ``SInt16``; ``UInt32``, ``SInt32``; ``UInt64``, ``SInt64``). The one that is called is chosen using polymorphism best-match rules; see :ref:`polymorphism`.

.. kl:function::
  function <SignedIntegerType> abs(<IntegerType> n)
  
  Returns the integer absolute value of the argument.
  
  Regardless of the type of the argument ``n``, the type of the return value is signed, and is the absolute value of the argument ``n`` interpreted as a signed integer.  This allows the ``abs`` function to be used on expressions involving differences of unsigned integers, eg. ``abs(Size(offset)-Size(index))``

.. _floatingpoint_numerical_functions:

Floating-Point Numerical Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

KL has support for many of the "standard library" floating-point numerical functions from C.  Each of these functions has a version that takes a parameter or parameters of type ``Float32``, and another that takes a parameter or parameters of type ``Float64``.  The one that is called is chosen using polymorphism best-match rules; see :ref:`polymorphism`.

.. _trigonometric_functions:

Trigonometric Functions
"""""""""""""""""""""""

Like the C standard library, all trigonometric function use radians for their arguments and return values, where appropriate.

.. kl:function::
  function Float32 sin(Float32 x)
  function Float64 sin(Float64 x)
  
  Returns the sine of the angle :samp:`{x}`.  :samp:`{x}` is measured in radians.

.. kl:function::
  function Float32 cos(Float32 x)
  function Float64 cos(Float64 x)
  
  Returns the cosine of the angle :samp:`{x}`.  :samp:`{x}` is measured in radians.

.. kl:function::
  function Float32 tan(Float32 x)
  function Float64 tan(Float64 x)
  
  Returns the tangent of the angle :samp:`{x}`.  :samp:`{x}` is measured in radians.

.. kl:function::
  function Float32 asin(Float32 x)
  function Float64 asin(Float64 x)
  
  Returns the arcsine of the argument :samp:`{x}`.  The return value is measured in radians.

.. kl:function::
  function Float32 acos(Float32 x)
  function Float64 acos(Float64 x)
  
  Returns the arccosine of the argument :samp:`{x}`.  The return value is measured in radians.

.. kl:function::
  function Float32 atan(Float32 x)
  function Float64 atan(Float64 x)
  
  Returns the arctangent of the argument :samp:`{x}`.  The return value is measured in radians.
  
  .. warning:: This function doesn't work for large :samp:`{x}` and can only return values in the range :math:`(-\pi/2,\pi/2]`; use the :kl:func:`atan2` function instead when possible.

.. kl:function::
  function Float32 atan2(Float32 y, Float32 x)
  function Float64 atan2(Float64 y, Float64 x)

  Returns the arctangent of the ratio :samp:`{y}/{x}`; the result is measured in radians and is in the range :math:`(-\pi,\pi]`.

.. _exponential_and_logarithmic_functions:

Exponential and Logarithmic Functions
""""""""""""""""""""""""""""""""""""""""""""

.. kl:function::
  function Float32 pow(Float32 x, Float32 y)
  function Float64 pow(Float64 x, Float64 y)
  
  Returns the value of :samp:`{x}` raised to the power of :samp:`{y}`.

.. kl:function::
  function Float32 pow(Float32 x, <IntegerType> y)
  function Float64 pow(Float64 x, <IntegerType> y)
  
  Returns the value of :samp:`{x}` raised to the power of :samp:`{y}` where :samp:`{y}` is an integer.  Uses exponentiation by squaring for very high performance, and will expand into a fixed operation in the case that :samp:`{y}` is a constant integer.

.. kl:function::
  function Float32 exp(Float32 x)
  function Float64 exp(Float64 x)
  
  Returns the value of :math:`e` raised to the power of :samp:`{x}` where :math:`e` is the base of the natural logarithm (approximately 2.7182818...).

.. kl:function::
  function Float32 log(Float32 x)
  function Float64 log(Float64 x)
  
  Returns the natural (base :math:`e`) logarithm of :samp:`{x}`.

.. kl:function::
  function Float32 log10(Float32 x)
  function Float64 log10(Float64 x)
  
  Returns the common (base 10) logarithm of :samp:`{x}`.

.. _non_transcendental_functions_functions:

Non-Transcendental Functions
""""""""""""""""""""""""""""""""""""""""""""

.. kl:function::
  function Float32 abs(Float32 x)
  function Float64 abs(Float64 x)
  
  Returns the absolute value of :samp:`{x}`.
  
.. kl:function::
  function Float32 round(Float32 x)
  function Float64 round(Float64 x)
  
  Returns the value of :samp:`{x}` rounded to the nearest whole (fractional part of zero) floating-point number.

.. kl:function::
  function Float32 floor(Float32 x)
  function Float64 floor(Float64 x)
  
  Returns the greatest whole floating-point number less than or equal to :samp:`{x}`.

.. kl:function::
  function Float32 ceil(Float32 x)
  function Float64 ceil(Float64 x)
  
  Returns the smallest whole floating-point number greater than or equal to :samp:`{x}`.

Category Functions
""""""""""""""""""""""""""""""""""""""""""""

.. kl:function::
  function Boolean Float32.isReg()
  function Boolean Float64.isReg()

  Returns true if and only if the floating-point number is a regular floating-point number; that is, if it is not infinite and not a NaN (not-a-number) value.

.. kl:function::
  function Boolean Float32.isInf()
  function Boolean Float64.isInf()
  
  Returns true if and only if the floating-point number is infinite.  Note that this does not check for NaN values; use the :kl:method:`Float32.isNaN()` method for that.

.. kl:function::
  function Boolean Float32.isNaN()
  function Boolean Float64.isNaN()
  
  Returns true if and only if the floating-point number is a not-a-number (NaN) value.  Note that this does not check for infinite values; use the :kl:method:`Float32.isInf()` method for that.

.. note::
  
  For a floating-point value ``x``, the condition ``!x.isReg()`` is equivalent to ``x.isInf() || x.isNaN()``

.. _vector_functions:

Vector Functions
^^^^^^^^^^^^^^^^

KL support a large set of :dfn:`vector functions` that are automatically made available for structures whose members are all of the same integer or floating-point type (as is usually the case for structures that represent vectors).  The KL compiler automatically reduces the function call to vector intrinsic operation that is optimal for the running architecture; for example, on a modern Intel x86 machine they will be reduced to instructions using the SSE or AVX vector extensions, resulting in improved performance over non-vector code.

When :samp:`{<V>}` is a structure whose members :samp:`{<m1>}, {<m2>}, ... {<mN>}` are all of exactly the same integer or floating-point type :samp:`{<T>}`, the following functions are made available:

.. kl:function::
  function <V> vecAdd(<V> lhs, <V> rhs)
  
  Returns :samp:`lhs.{m1} + rhs.{m1}`, :samp:`lhs.{m2} + rhs.{m2}`, ... :samp:`lhs.{mN} + rhs.{mN}`

.. kl:function::
  function <V> vecAdd(<T> k, <V> rhs)
  
  Returns :samp:`k + rhs.{m1}`, :samp:`k + rhs.{m2}`, ... :samp:`k + rhs.{mN}`

.. kl:function::
  function <V> vecAdd(<V> lhs, <T> k)
  
  Returns :samp:`lhs.{m1} + k`, :samp:`lhs.{m2} + k`, ... :samp:`lhs.{mN} + k`

.. kl:function::
  function <V> vecSub(<V> lhs, <V> rhs)
  
  Returns :samp:`lhs.{m1} - rhs.{m1}`, :samp:`lhs.{m2} - rhs.{m2}`, ... :samp:`lhs.{mN} - rhs.{mN}`

.. kl:function::
  function <V> vecSub(<T> k, <V> rhs)
  
  Returns :samp:`k - rhs.{m1}`, :samp:`k - rhs.{m2}`, ... :samp:`k - rhs.{mN}`

.. kl:function::
  function <V> vecSub(<V> lhs, <T> k)
  
  Returns :samp:`lhs.{m1} - k`, :samp:`lhs.{m2} - k`, ... :samp:`lhs.{mN} - k`

.. kl:function::
  function <V> vecMul(<V> lhs, <V> rhs)
  
  Returns :samp:`lhs.{m1} * rhs.{m1}`, :samp:`lhs.{m2} * rhs.{m2}`, ... :samp:`lhs.{mN} * rhs.{mN}`

.. kl:function::
  function <V> vecMul(<T> k, <V> rhs)
  
  Returns :samp:`k * rhs.{m1}`, :samp:`k * rhs.{m2}`, ... :samp:`k * rhs.{mN}`

.. kl:function::
  function <V> vecMul(<V> lhs, <T> k)
  
  Returns :samp:`lhs.{m1} * k`, :samp:`lhs.{m2} * k`, ... :samp:`lhs.{mN} * k`

.. kl:function::
  function <V> vecDiv(<V> lhs, <V> rhs)
  
  Returns :samp:`lhs.{m1} / rhs.{m1}`, :samp:`lhs.{m2} / rhs.{m2}`, ... :samp:`lhs.{mN} / rhs.{mN}`

.. kl:function::
  function <V> vecDiv(<T> k, <V> rhs)
  
  Returns :samp:`k / rhs.{m1}`, :samp:`k / rhs.{m2}`, ... :samp:`k / rhs.{mN}`

.. kl:function::
  function <V> vecDiv(<V> lhs, <T> k)
  
  Returns :samp:`lhs.{m1} / k`, :samp:`lhs.{m2} / k`, ... :samp:`lhs.{mN} / k`

.. kl:function::
  function <V> vecRem(<V> lhs, <V> rhs)
  
  Returns :samp:`lhs.{m1} % rhs.{m1}`, :samp:`lhs.{m2} % rhs.{m2}`, ... :samp:`lhs.{mN} % rhs.{mN}`

.. kl:function::
  function <V> vecRem(<T> k, <V> rhs)
  
  Returns :samp:`k % rhs.{m1}`, :samp:`k % rhs.{m2}`, ... :samp:`k % rhs.{mN}`

.. kl:function::
  function <V> vecRem(<V> lhs, <T> k)
  
  Returns :samp:`lhs.{m1} % k`, :samp:`lhs.{m2} % k`, ... :samp:`lhs.{mN} % k`

When ``<T>`` is an integer type, the following additional function are available:

.. kl:function::
  function <V> vecBitOr(<V> lhs, <V> rhs)
  
  Returns :samp:`lhs.{m1} | rhs.{m1}`, :samp:`lhs.{m2} | rhs.{m2}`, ... :samp:`lhs.{mN} | rhs.{mN}`

.. kl:function::
  function <V> vecBitOr(<T> k, <V> rhs)
  
  Returns :samp:`k | rhs.{m1}`, :samp:`k | rhs.{m2}`, ... :samp:`k | rhs.{mN}`

.. kl:function::
  function <V> vecBitOr(<V> lhs, <T> k)
  
  Returns :samp:`lhs.{m1} | k`, :samp:`lhs.{m2} | k`, ... :samp:`lhs.{mN} | k`

.. kl:function::
  function <V> vecBitAnd(<V> lhs, <V> rhs)
  
  Returns :samp:`lhs.{m1} & rhs.{m1}`, :samp:`lhs.{m2} & rhs.{m2}`, ... :samp:`lhs.{mN} & rhs.{mN}`

.. kl:function::
  function <V> vecBitAnd(<T> k, <V> rhs)
  
  Returns :samp:`k & rhs.{m1}`, :samp:`k & rhs.{m2}`, ... :samp:`k & rhs.{mN}`

.. kl:function::
  function <V> vecBitAnd(<V> lhs, <T> k)
  
  Returns :samp:`lhs.{m1} & k`, :samp:`lhs.{m2} & k`, ... :samp:`lhs.{mN} & k`

.. kl:function::
  function <V> vecBitXor(<V> lhs, <V> rhs)
  
  Returns :samp:`lhs.{m1} ^ rhs.{m1}`, :samp:`lhs.{m2} ^ rhs.{m2}`, ... :samp:`lhs.{mN} ^ rhs.{mN}`

.. kl:function::
  function <V> vecBitXor(<T> k, <V> rhs)
  
  Returns :samp:`k ^ rhs.{m1}`, :samp:`k ^ rhs.{m2}`, ... :samp:`k ^ rhs.{mN}`

.. kl:function::
  function <V> vecBitXor(<V> lhs, <T> k)
  
  Returns :samp:`lhs.{m1} ^ k`, :samp:`lhs.{m2} ^ k`, ... :samp:`lhs.{mN} ^ k`

.. kl:function::
  function <V> vecShl(<V> lhs, <V> rhs)
  
  Returns :samp:`lhs.{m1} << rhs.{m1}`, :samp:`lhs.{m2} << rhs.{m2}`, ... :samp:`lhs.{mN} << rhs.{mN}`

.. kl:function::
  function <V> vecShl(<T> k, <V> rhs)
  
  Returns :samp:`k << rhs.{m1}`, :samp:`k << rhs.{m2}`, ... :samp:`k << rhs.{mN}`

.. kl:function::
  function <V> vecShl(<V> lhs, <T> k)
  
  Returns :samp:`lhs.{m1} << k`, :samp:`lhs.{m2} << k`, ... :samp:`lhs.{mN} << k`

.. kl:function::
  function <V> vecShr(<V> lhs, <V> rhs)
  
  Returns :samp:`lhs.{m1} >> rhs.{m1}`, :samp:`lhs.{m2} >> rhs.{m2}`, ... :samp:`lhs.{mN} >> rhs.{mN}`

.. kl:function::
  function <V> vecShr(<T> k, <V> rhs)
  
  Returns :samp:`k >> rhs.{m1}`, :samp:`k >> rhs.{m2}`, ... :samp:`k >> rhs.{mN}`

.. kl:function::
  function <V> vecShr(<V> lhs, <T> k)
  
  Returns :samp:`lhs.{m1} >> k`, :samp:`lhs.{m2} >> k`, ... :samp:`lhs.{mN} >> k`

.. _conversion-funcs:

Conversion Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. kl:function::
  function <Type>.appendDesc(io String string)

  .. versionadded:: 1.12.0

  The :code:`appendDesc` method is called to convert the given type to a :code:`String`.  You can write a custom :code:`appendDesc` method to 
  customize this conversion, as shown in the following example:

  .. kl-example:: Custom appendDesc Method

    struct Vec3 { Float32 x, y, z; };

    function Vec3(Float32 x, Float32 y, Float32 z) {
      this.x = x; this.y = y; this.z = z;
    }

    function Vec3.appendDesc(io String string) {
      string += "vec3:[";
      string += this.x;
      string += ":";
      string += this.y;
      string += ":";
      string += this.z;
      string += "]";
    }

    operator entry() {
      Vec3 vec3(6.7, -9.4, 2.3);
      report(vec3);
    }

.. kl:function::
  function String hex(UInt8 n)
  function String hex(UInt16 n)
  function String hex(UInt32 n)
  function String hex(UInt64 n)

  Converts an unsigned integer value into a hexadecimal string representation of the value.

.. kl:function::
  function String hex(SInt8 n)
  function String hex(SInt16 n)
  function String hex(SInt32 n)
  function String hex(SInt64 n)

  Converts an integer value into a hexadecimal string representation of the value.  The output is as if ``n`` was of the corresponding unsigned integer type; there is no consideration for negative values.

.. kl:function::
  function Float32 bitcastUIntToFloat(UInt32 n)
  function Float64 bitcastUIntToFloat(UInt64 n)
  
  Bitcasts an unsigned integer of the same width to a floating-point number.  This is a non-numerical conversion that is mostly useful for unit testing KL itself.

.. kl:function::
  function UInt32 bitcastFloatToUInt(Float32 x)
  function UInt64 bitcastFloatToUInt(Float64 x)
  
  Bitcasts a floating-point number to an unsigned integer of the same width.  This is a non-numerical conversion that is mostly useful for unit testing KL itself.

Thread/Core-related Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. kl:function::
  function UInt16 getThreadIndex()
  
  Returns the index of the currently-executing thread.  This number is guaranteed to be in the range 0 to kl:func:`getThreadCount()`-1.

  For a give PEX workload, two concurrently executing threads are guaranteed to return different values for this function.

.. kl:function::
  function UInt16 getThreadCount()
  
  Returns the upper bound of the :kl:func:`getThreadIndex()` return value.
  
.. kl:function::
  function UInt16 getCoreCount()
  
  Returns the number of CPU cores in the machine.
  
.. kl:function::
  function atomicMemoryBarrier()
  
  Produces an atomic memory barrier at this point in the code.  The barrier
  is a "full" (sequentially consistent) barrier.
  
.. kl:function::
  function atomicMemoryBarrier_Acquire()
  
  Produces an atomic memory barrier at this point in the code.  The barrier
  is a "acquire" barrier.
  
.. kl:function::
  function atomicMemoryBarrier_Release()
  
  Produces an atomic memory barrier at this point in the code.  The barrier
  is a "release" barrier.
  
.. kl:function::
  function atomicMemoryBarrier_AcquireRelease()
  
  Produces an atomic memory barrier at this point in the code.  The barrier
  is a "acquire-release" barrier.

Performance Counter Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

KL provides access to high-performance system timer information that can be used to time operations from within KL code.

.. kl:function::
  function UInt64 getCurrentTicks()
  
  Returns the current value of the performance counter.  This number has no meaning on its own (ie. its units are undefined) but can be used in calls to ``getSecondsBetweenTicks()`` to measure absolute elapsed time.  Note that the value returned by ``getCurrentTicks()`` is not affected by system ("wall") clock time changes.

.. kl:function::
  function Float64 getSecondsBetweenTicks(UInt64 start, UInt64 end)
  
  Returns the number of seconds between two performance counter values.  The measurable resolution is guaranteed to be at least one million parts per second.

Example usage of the performance counter functions::

  operator entry() {
    UInt64 start = getCurrentTicks();
    // Do nothing...
    UInt64 end = getCurrentTicks();
    report("Elapsed time: " + getSecondsBetweenTicks(start, end) + " seconds");
  }

Output::

  Elapsed time: 4.1e-08 seconds

.. index::
  single: polymorphism
  single: function polymorphism
  pair: function; polymorphism

.. index::
  pair: named; constant

Fabric Context Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These functions are used to interact with the Fabric Core context.

.. kl:function::
  function String fabricCoreContextID()
  
  Returns the Fabric Core context ID as a String.  This context ID can be
  used to bind a new Fabric Core client to an existing context.

.. _KLPG.global.named-constants:

Named Constants
---------------

A :dfn:`named constant` in KL is a value that can be referred to by name in
expressions but that cannot be changed at runtime.  Named constants are
essentially read-only variables; however, since the KL compiler knows that
their value can never change, it can often produce faster code when named
constants are used in place of variables.  Both scalar and array named
constants can be declared.

Named constants can be declared within any scope (see :ref:`scope`), including
the global scope.  Named constants are only visible within the scope in which
they are declared.

Scalar named constants take the form:

.. parsed-literal::

  const :samp:`{Type}` :samp:`{name}` = :samp:`{expr}`;

and array named constants take the form:

.. parsed-literal::

  const :samp:`{Type}` :samp:`{name}`\[] = [
    :samp:`{expr1}`, :samp:`{expr2}`, ..., :samp:`{exprN}`
  ];

In either case, :samp:`{Type}` must be a boolean, integer, floating-point or string type; :samp:`{name}` must be an identifier; and :samp:`{expr}` must be an expression involving constant(s) that evaluates to a constant of type `{Type}`.  In the case of a scalar named constant, the type of the named constant is :samp:`{Type}`.  In the case of an array named constant, the type of the named constant is a fixed array of elements of type :samp:`{Type}`; the size of the fixed array is the number of initializing values given within the brackets.

It is a compile-time error to do any of the following:

- assign to a named constant

- pass a named constant to a function as an ``io`` parameter

- declare a global named constant with the same name as a function, operator or another global named constant

- declare a non-global named constant with the same name as a variable or another named constant declared in the same scope

Example usage of named constants:

.. code-block:: kl
  
  const String MODULE_NAME = "KL";
  const String PREFIX = MODULE_NAME + ": ";
  const UInt32 twoToTheSixteen = 1 << 16;
  const Float32 familiarValues[] = [3.141, 2.718, (3 * 7.4) / 3.4];

  operator entry() {
    report(PREFIX + "twoToTheSixteen = " + twoToTheSixteen);
    report(PREFIX + "familiarValues = " + familiarValues);
    for (UInt32 i=0; i<4; ++i) {
      const UInt32 a = 3;
      const UInt32 b = 4;
      report(PREFIX + "a*"+i+"+b = "+(a*i+b));
    }
  }

Output:

.. code-block:: none
  
  KL: twoToTheSixteen = 65536
  KL: familiarValues = [+3.141000,+2.717999,+6.529411]
  KL: a*0+b = 4
  KL: a*1+b = 7
  KL: a*2+b = 10
  KL: a*3+b = 13

.. _KLPG.named-constants.predefined:

.. index::
  pair: predefined; constant

Predefined Constants
^^^^^^^^^^^^^^^^^^^^

There are a variety of predefined constants available to every KL program.

Fabric Version Pre-Defined Constants
""""""""""""""""""""""""""""""""""""

The three constants ``FabricVersionMaj``, ``FabricVersionMin`` and ``FabricVersionRev`` are three predefined constants of type ``UInt8`` that are the major, minor and revision components of the running Fabric version.  For example, this documentation was built for Fabric version {{FABRIC_VERSION}}, and so KL code executed in this version will have ``FabricVersionMaj = {{FABRIC_VERSION_MAJ}}``, ``FabricVersionMin = {{FABRIC_VERSION_MIN}}`` and ``FabricVersionRev = {{FABRIC_VERSION_REV}}``.

.. code-block:: kl

  operator entry() {
    report("FabricVersionMaj = " + FabricVersionMaj);
    report("FabricVersionMin = " + FabricVersionMin);
    report("FabricVersionRev = " + FabricVersionRev);
  }

Integer Limit Pre-Defined Constants
"""""""""""""""""""""""""""""""""""

For every integer type ``<IntTy>`` there is a pre-defined integer constant ``<IntTy>Max`` that is the maximum value the integer can attain.  Additionally, for signed integer types there is a pre-defined integer constant ``<IntTy>Min`` that is the minimum value the integer can attain.  In both cases, the type of the integer constant is the type of the integer itself.  For example:

.. code-block:: kl

  operator entry() {
    report("UInt8Max=" + UInt8Max);
    report("UInt16Max=" + UInt16Max);
    report("UInt32Max=" + UInt32Max);
    report("UInt64Max=" + UInt64Max);
    report("SInt8Min=" + SInt8Min);
    report("SInt8Max=" + SInt8Max);
    report("SInt16Min=" + SInt16Min);
    report("SInt16Max=" + SInt16Max);
    report("SInt32Min=" + SInt32Min);
    report("SInt32Max=" + SInt32Max);
    report("SInt64Min=" + SInt64Min);
    report("SInt64Max=" + SInt64Max);
  }

produces:

.. code-block:: none

  UInt8Max=255
  UInt16Max=65535
  UInt32Max=4294967295
  UInt64Max=18446744073709551615
  SInt8Min=-128
  SInt8Max=127
  SInt16Min=-32768
  SInt16Max=32767
  SInt32Min=-2147483648
  SInt32Max=2147483647
  SInt64Min=-9223372036854775808
  SInt64Max=9223372036854775807

The ``FUNC`` Pre-Defined Constants
""""""""""""""""""""""""""""""""""

The KL compiler automatically predefines the constant ``FUNC`` at the start of every function as a string constant describing the function.  The following code:

.. code-block:: kl
  
  function foo(Float32 x) {
    report("This function is: " + FUNC);
  }
  
  operator entry() {
    foo(3.14);
  }

produces the output:

.. code-block:: none
  
  This function is: function foo(Float32)  

.. index::
  single: require

.. _KLPG.require:

Importing Functionality With ``require``
----------------------------------------

Through integration with Fabric, it is possible for derived KL types and/or
Fabric extensions to provide KL code that is defined externally to the current
source file.  To use these types and code within the current source file, the
``require`` statement is provided; it is similar to the ``import`` statement
in Python.

The ``require`` statement should be followed by the name of the registered
type or extension.  For example, to include the functionality provided by the
extension named "Math" and the registered type named "RegType", the program
should start with::

  require Math, RegType;

Any ``require`` statements must appear at the top of the KL program that uses
the associated functionality.  You can have as many ``require`` statements as
you would like.

.. _KLPG.require.versioning:

Using ``require`` with version information
---------------------------------------------

By default the ``require`` statement will load the latest version of the extension
available. So for example given two versions of the :code:`ExtensionName` extension
with the versions :code:`"1.0.0"` and :code:`"1.2.1"`, doing

.. code-block:: kl

  require ExtensionName;

will result in the version :code:`"1.2.1"` being loaded. If you want to load a 
specific version, you can use the following syntax

.. code-block:: kl

  require ExtensionName:"=1.0.0";

which will result in loading the specific :code:`"1.0.0"` version of the extension. 
If the specific version cannot be found, an error will be thrown.
Alternatively, if you just want to make sure an extension version is higher than a
specific version number, you can use the lesser / greater sign like so:

.. code-block:: kl

  require ExtensionName:">1.0.0";

If the version lesser / greater than what is specified cannot be found, an error will be thrown.
In this example the :code:`"1.2.1"` version of the extension will be loaded.

Furthermore you can use preprocessor statements to add optional KL code or to switch 
behaviors based on extension versions. For that you can use the :code:`EXT_VER_IF: and
:code:`EXT_VER_ENDIF` statements. For this you can use the equal, lesser or greater sign.

.. code-block:: kl

  require ExtensionName;

  EXT_VER_IF ExtensionName:">1.0.0"

  function dummyFunction() {
    report('Found an extension version for "ExtensionName" higher than "1.0.0"');
  }

  EXT_VER_ENDIF

  operator entry() {

  EXT_VER_IF ExtensionName:">1.0.0"

    dummyFunction();

  EXT_VER_ENDIF

  }

The :code:`dummy` function's definition and invocation will only happen if the extension version
of the :code:`ExtensionName` is higher to :code:`"1.0.0"` in the example above.

For more information on how to embed versioning information in extensions please refer to :ref:`EXTS_VERSIONING`.

.. _KLPG.require.versioning.envvars:

Extension versioning environment variables
---------------------------------------------

Additional to the facilities mentioned above in :ref:`KLPG.require.versioning` you can drive the :code:`require` statement 
with a set of environment variables. There are several ways to use environment variables.

The first approach, which uses a single environment variable for each extension, defines an environment variable like so:

.. code-block:: bash

  export FABRIC_EXT_VER_EXTENSIONNAME="=1.0.0"

For the second approach, which suits environments better when you have to switch between a large amount of environment variables for a given build set, first you may optionally specify the :envvar:`FABRIC_EXT_VER_PREFIX` and :envvar:`FABRIC_EXT_VER_SUFFIX` environment variables, which contain a prefix and a suffix to be used when looking up additional environment variables, or you can use their default values. 

Then for each extension you may specify an environment variable using the prefix and suffix and the extension's name, which will then contain the versioning information. For example, using the default prefix and suffix:

.. code-block:: bash

  export FABRIC_EXT_VER_EXTENSIONNAME="=1.0.0"

Or changing the prefix and suffix:

.. code-block:: bash

  export FABRIC_EXT_VER_PREFIX="COMPANY_"
  export FABRIC_EXT_VER_SUFFIX="_VER_INFO"
  export COMPANY_EXTENSIONNAME_VER_INFO="=1.0.0"

This would resolve in the extension loading mechanism to first resolve the :envvar:`FABRIC_EXT_VER_PREFIX` and :envvar:`FABRIC_EXT_VER_SUFFIX`
environment variables, then will resolve the :envvar:`COMPANY_EXTENSIONNAME_VER_INFO` based on these and will figure out that version 1.0.0 of the two available versions should be used.

The third approach uses an auxiliary json file which needs to provide a mapping between the name of the extension and a version to use. The file path of the json file needs to be specified in the :envvar:`FABRIC_EXT_VERFILE` environment variable. The content of the file needs to look for example like this:

.. code-block:: js

  {
    "Alembic": ">=1.0", 
    "FBX": ">=1.1"
  }

In the final approach users may set the :envvar:`FABRIC_EXT_OVERRIDE` environment variable which can be used to specify sets of extensions that should be loaded together. Each extension may define an override key (see :ref:`EXTS_VERSIONING`) and if that key matches the value of :envvar:`FABRIC_EXT_OVERRIDE` then that extension will be loaded before others with a different or missing override key. This may cause lower version numbers of extensions to load. For example:

.. code-block:: bash

  export FABRIC_EXT_OVERRIDE="MyOverride"

This will cause all extensions with an override key of "MyOverride" to be preferred over other versions of the same extension with a different override key.

.. note:: All environment variables need to use capital letters throughout.

For more information on how to embed versioning information in extensions please refer to :ref:`EXTS_VERSIONING`.
