.. _scopes-namespaces:

Scopes and Namespaces
=========================

This chapter covers the topics of scoping rules and namespaces in KL.  These topics are related since they concern how types, functions and variables are visible within KL programs.

.. index:
  single: scope

.. _scope:

Scoping Rules
-------------

The term :dfn:`scope` in programming languages refers to the parts of a program in which variables, constants and functions are visible; the rules that govern how scopes work are referred to as :dfn:`scoping rules`.  Scopes are also responsible for managing the "lifecycle" of variables; in the case of KL, this refers to when destructors are called for structure values.

.. index:
  pair: types; scope

Types of Scopes
^^^^^^^^^^^^^^^

In KL, there are four kinds scopes: the global scope, function scopes, compound statement scopes and temporary scopes.  Scopes :dfn:`nest` inside each other; when a KL program refers to a variable by name, the compiler determines which variable is being referred to by searching from the current innermost scope outwards through the nested scopes to the outermost scope (which is always the global scope).  Like C, KL is a statically-scoped language, meaning that the exact variable that is being referred to is resolved at compile time (and not at run time).

.. index::
  pair: global; scope

The Global Scope
""""""""""""""""

The global scope is the top-level scope of a KL program.  The symbols that are visible in the global scope are global constants as well as functions and operators.  The global scope is always the outermost scope at any point in a KL program.

.. index::
  pair: function; scope

Function Scope
""""""""""""""

Whenever a function or other function-list entity is defined, a function scope is created that is nested inside the global scope.  The arguments to the function are provided within the function scope.  Within the function scope, a function definition also creates a compound statement scope corresponding to the compound statement that constitutes the body of the function.

.. index::
  pair: compound statement; scope

.. _scope-compound-statement:

Compound Statement Scope
""""""""""""""""""""""""

Any time that a ``{`` followed by zero or more statements followed by ``}`` is used to introduce a compound statement, a new :dfn:`compound statement scope` is introduced.  Compound statement scopes are nested inside function scopes (when they correspond to the compound statement that constitutes the body of a function) or inside other compound statement scopes.

When control reaches the end of a compound statement (by executing the last statement or via the ``return``, ``break`` or ``continue`` statements), any structure values that have corresponding destructors will have those destructors executed.

Note that declaring a loop index variable inside a loop statement is a special case of a compound statement scope.  In the case that the loop body is a compound statement, the corresponding compound statement scope is nested inside the loop's compound statement scope.

.. index::
  pair: temporary; scope

Temporary Scope
"""""""""""""""

Any time that a constructor is directly invoked to create a temporary value (see :ref:`KLPG.constructor.invocation.temporary`), a scope is created to contain the temporary value.  The scope encloses the surrounding expression of the temporary value; this means that when the surrounding expression is finished execution, the temporary value's destructor, if it exists, is executed.

Nested Scopes Example
^^^^^^^^^^^^^^^^^^^^^

For a precise understanding of the nesting of KL scopes, study the following example carefully.

.. kl-example: Nested Scopes

  struct T {
    String s;
  };
  
  function T(String s) {
    this.s = s;
    report("created T; s = " + this.s);
  }
  
  function ~T() {
    report("destroying T; s = " + this.s);
  }
  
  function foo(T t) {
    report("start of foo; t is now " + t);
    T t("fooT");
    report("declared t in foo; t is now " + t);
    for (Index i=0; i<3; ++i) {
      report("top of loop body; t is now " + t);
      T t("loopT:" + i);
      report("declared t in loop; t is now " + t);
    }
    report("after loop; t is now " + t);
  }
  
  const Float32 t = 2.75;
  
  operator entry() {
    report("top of entry; t is now " + t);
    T t("entryT");
    report("declared t in entry; t is now " + t);
    foo(t);
    report("came back from foo; t is now " + t);
  }

.. index:
  single: namespace

.. _namespaces:

Namespaces
-------------

.. versionadded:: 2.4.0

A common problem in large software systems is ensuring the uniqueness of the names of types and global functions.   For example, there could be two different places that define a type ``Logger`` because two different parts of the system have a need for a logging object; however, defining two different types with the same name will create an error in KL because it wouldn't be possible to figure out which type was being referred to when ``Logger`` was used.  In KL, a common manifestation of this problem is when two different KL extensions define types or functions with the same name.

As an example, consider the following code:

.. kl-example:: Type and Function Name Collisions
  :no-output:

  //////////////////////////////////////////////
  // In some part of the code, we have a type named Logger and a CreateLogger
  // function.

  struct Logger {
    Integer fd;
  };

  Logger CreateLogger(String filename) {
    // ...
  }
  //////////////////////////////////////////////

  //////////////////////////////////////////////
  // In some other part of the code, we have a different type Logger and
  // a different function CreateLogger

  struct Logger {
    FileHandle fh;
    Integer level;
  };

  Logger CreateLogger(String filename) {
    // ...
  }
  //////////////////////////////////////////////

  operator entry() {
    Logger l = CreateLogger("output.log");  // will result in a compilation error
  }

Note that it's not necessary for all the code to be in a single file for there to be an issue; the two different definitions for ``Logger`` and ``CreateLogger`` could be in different files and could be located in different extensions.

In order to avoid problems with global names types and functions colliding, KL provides support for namespaces.  A :dfn:`namespace` is a named collection of types and functions that are referred to using a prefix to ensure that names of the types and functions do not collide with other types and functions of the same name.  To declare that types and/or functions belong in a namespace named ``Name``, simply encode them in a :dfn:`namespace block` as follows:

.. kl-example:: namespace
  :no-output:

  namespace NamespaceName {
  // functions and types in the namespace
  }

Then, to refer to functions and types in this namespace, use the syntax ``NamespaceName::TypeName`` or ``NamespaceName::FunctionName``.  The following example shows namespaces used to resolve the name collisions in the example above:

.. kl-example:: namespace
  :no-output:

  //////////////////////////////////////////////
  namespace Transaction {

  struct Logger {
    Integer fd;
  };

  Logger CreateLogger(String filename) {
    // ...
  }

  }
  //////////////////////////////////////////////

  //////////////////////////////////////////////
  namespace Util {

  struct Logger {
    FileHandle fh;
    Integer level;
  };

  Logger CreateLogger(String filename) {
    // ...
  }

  }
  //////////////////////////////////////////////

  operator entry() {
    Transaction::Logger l = Transaction::CreateLogger("output.log");
  }

If you know you will only need to be using the types and/or functions from one of the namespaces, you can use the ``using namespace NamespaceName;`` global declaration to ensure that the ``NamespaceName::`` prefix is not needed (although it can still be used).  The following example modifies the last example to use `using`:

.. kl-example:: using namespace
  :no-output:

  //////////////////////////////////////////////
  namespace Transaction {

  struct Logger {
    Integer fd;
  };

  Logger CreateLogger(String filename) {
    // ...
  }

  }
  //////////////////////////////////////////////

  //////////////////////////////////////////////
  namespace Util {

  struct Logger {
    FileHandle fh;
    Integer level;
  };

  Logger CreateLogger(String filename) {
    // ...
  }

  }
  //////////////////////////////////////////////

  using namespace Transaction;

  operator entry() {
    // because of the 'using namespace Transaction' global declaration,
    // we don't need to prefix these with Transaction::
    Logger l = CreateLogger("output.log");
  }

For code within a namespace, it is not necessary to use the namespace prefix to access other types and/or functions in that namespace.  So, for example, the following code is correct:

.. kl-example:: namespace
  :no-output:

  namespace Foo {
  
  struct MyType { /*...*/ };

  // Note that we don't need to specify Foo::MyType here in either case:
  MyType SomeFunc() {
    return MyType();
  }

  SomeOtherFunc() {
    MyType mt = SomeFunc(); // nor do we here
  }

  }

Several important details on the use of namespaces:

- It is possible to have two or more namespace blocks with the same namespace name.  In this case, all of the types and functions among all the blocks are included in the namespace.

- It is possible to nest namespaces.  For example, if we have the nested namespace blocks:

.. kl-example:: namespace
  :no-output:

  namespace Foo {
  namespace Bar {
  struct MyType { /*...*/ };
  }
  }

Then you can refer to ``MyType`` through ``Foo::Bar::MyType``.

- It is possible to have multiple ``using namespace ...;`` global declarations; however, it is also possible that doing so will reintroduce name collisions, eg. if we had instead declared ``using namespace Transaction, Util;`` in the example above.

- The "scope" of a ``using namespace ...;`` global declaration is the file in which it is used.  Therefore, you will need to repeat the declaration in each file that needs it.

Autonamespacing of Extensions
---------------------------------

In order to ease the use of namespaces with KL extensions, Fabric supports a feature to automatically place the types and functions of an extension into a namespace whose name is the name of the extension.

When an extension is declared to be "autonamespaced", all of its functions and types are automatically placed into a namespace whose name is the name of the extension.  Furthermore, whenever ``require ExtName;`` is used in KL code, there is an implicit ``using namespace ExtName;`` that happens at the point of the require statement.

For backwards compatibility with previous versions of Fabric this feature is disabled by default.  To enable autonamespacing of an extension, add an ``autoNamespace`` member with value ``true`` to the ``ExtName.fpm.json`` file, eg::

  {
    "code": "ExtName.kl",
    "autoNamespace": true
  }
