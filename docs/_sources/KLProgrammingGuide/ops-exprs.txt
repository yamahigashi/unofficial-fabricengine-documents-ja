.. _ops-exprs:

Operators and Expressions
=========================

This chapter explains the possible operators and resulting expressions in KL.  Generally, KL has the same operator and expression syntax as JavaScript and C, and in particular follows exactly the same precedence and associativity rules.

.. _ops:

Operators
---------

KL supports the same basic set of operators as JavaScript and C.  These operations are broadly categorized as :ref:`arithmetic operators <arithmetic-ops>`, :ref:`logical operators <logical-ops>`, :ref:`bitwise operators <bitwise-ops>` and :ref:`assignment operators <ass-ops>`.

.. _arithmetic-ops:

Arithmetic Operators
^^^^^^^^^^^^^^^^^^^^

Add and Subtract
""""""""""""""""

When ``+`` or ``-`` appear between two expressions they are referred to as the :dfn:`add` and :dfn:`subtract` binary operators.  These operators are pre-defined for all integer and floating point types, where they perform the usual arithmetic operations, but they can also be overloaded to apply to user-defined structures or different combinations of types.  For example, it is possible to define an operator that takes a user-defined ``Rect`` on the left and a user-defined ``Point`` on the right.

In addition to being pre-defined for integer and floating-point types, the ``+`` (add) operator (but not the ``-`` (subtract) operator) is defined for the ``String`` type; the result of adding two strings is the two strings concatenated together.

Multiply, Divide and Remainder
""""""""""""""""""""""""""""""

When ``*``, ``/`` or ``%`` appear between two expressions they are referred to as the :dfn:`multiply`, :dfn:`divide` and :dfn:`remainder` binary operators.  These operators are pre-defined for all integer and floating point types, where they perform the usual arithmetic operations, but they can also be overloaded to apply to user-defined structures or different combinations of types.  For example, it is possible to define a multiply operator that takes a ``Float32`` on the left and a user-defined ``Vec3`` on the right.

Unary Plus and Minus
""""""""""""""""""""

When ``+`` or ``-`` appears in front of an integer or floating-point expression without an expression to the left they are referred to as the :dfn:`unary plus` and :dfn:`unary minus` operators.  The unary plus operator doesn't do anything to the value it operates on, but the unary minus operator returns the value that, when added to the original, produces zero (for unsigned integer expressions); for signed integer and floating-point expressions, this is value of the expression with its sign reversed.

Increment and Decrement Operators
"""""""""""""""""""""""""""""""""

The ``++`` (increment) and ``--`` (decrement) operators can be used to add one to or subtract one from a variable.  These operators have the following properties:

- The operators only work on variables or input-output parameters; then cannot operate on constants or input parameters.  This is because they change the value of the expression.

- They only operate on integer values.

- Each operator can appear either *precede* or *follow* the variable it operates on.  When it precedes the variable, the value of the expression is the value of the variable *after* incrementing; this is referred to as a *prefix* increment (or decrement).  When it follows the variable, the result is the value of the variable *before* incrementing; this is referred to as a *postfix* increment (or decrement).

- They cannot be overloaded.

.. _logical-ops:

Logical Operators
^^^^^^^^^^^^^^^^^

.. _equality-ops:

Equality Operators
""""""""""""""""""

When ``==`` or ``!=`` appear between two expressions they are referred to as the :dfn:`equal-to` or :dfn:`not-equal-to` binary operators, respectively; collectively, they are referred to as the :dfn:`equality operators`.

The equality operators are pre-defined for all integer and floating-point types as well as the ``Boolean`` and ``String`` types.  They can also be overloaded to apply to user-defined structure and specific object types or combinations of different types.

.. _identity-ops:

Identity Operators
""""""""""""""""""

When ``===`` or ``!==`` appear between two expressions they are referred to as the :dfn:`identical-to` or :dfn:`not-identical-to` binary operators, respectively; collectively, they are referred to as the :dfn:`identity operators`.

The identity operators are pre-defined only for :ref:`object types <KLPG.types.objects>` and :ref:`interface types <KLPG.types.interfaces>`.  They test whether two objects or interfaces refer to the same object, ie. whether changing one will change the other.

.. _relational-ops:

Relational Operators
""""""""""""""""""""

When ``<``, ``<=``, ``>`` or ``>=`` appear between two expressions they are referred to as the :dfn:`less-than`, :dfn:`less-than-or-equal-to`, :dfn:`greater-than` or :dfn:`greater-than-or-equal-to` binary operators, respectively; collectively, they are referred to as the :dfn:`relational operators`.

The relational operators are pre-defined for all integer and floating-point types as well as the ``String`` type.  They can also be overloaded to apply to user-defined structure types or combinations of different types.

Logical AND
"""""""""""

When ``&&`` appears between two expressions it is referred to as the :dfn:`logical AND` binary operator.  Logical AND operates as follows: the left operand is cast to a ``Boolean`` (ie. a ``Boolean`` value is constructed from the left hand operand).  If the result is ``true``, the result is the right operand, otherwise the result is the left operand.

.. warning:: The behavior of logical AND is the same as in JavaScript but different than C.  In C, the result value of a logical AND is always an integer (bool in C++).

It is not possible to overload the logical AND operator.  However, you can "enable" it for custom types (structures) by creating a ``Boolean`` constructor with a single parameter whose type is the type of the left operand.

Logical OR
""""""""""

When ``||`` appears between two expressions it is referred to as the :dfn:`logical OR` binary operator.  Logical OR operates as follows: the left operand is cast to a ``Boolean`` (ie. a ``Boolean`` value is constructed from the left hand operand).  If the result is ``true``, the result is the left operand, otherwise the result is the right operand.

.. warning:: The behavior of logical OR is the same as in JavaScript but different than C.  In C, the result value of a logical AND is always an integer (bool in C++).

It is not possible to overload the logical OR operator.  However, you can "enable" it for custom types (structures) by creating a ``Boolean`` constructor with a single parameter whose type is the type of the left operand.

Logical NOT
"""""""""""

When ``!`` (exclamation mark) appears in front of an expression it is referred to as the :dfn:`logical NOT` unary operator.  Logical NOT inverts the logical value of expression; more specifically, it constructs a new ``Boolean`` value from the expression and then inverts its logical value.  Therefore, logical not can be applied to any expression that has a ``Boolean`` constructor that takes a single parameter whose types is the type of the expression.

It is not possible to overload the logical NOT operator.  However, you can "enable" it for custom types (structures) by creating a ``Boolean`` constructor with a single parameter whose type is the structure.

The Conditional Operator
""""""""""""""""""""""""

When three expressions are separated by ``?`` (question mark) and ``:`` (colon) it is referred to as the :dfn:`conditional operator` (or :dfn:`ternary operator`).  The conditional operator constructs a ``Boolean`` from the first operand; if it has value ``true``, the result is the second operand, otherwise it is the third.

It is not possible to overload the conditional operator.

The Comma Operator
"""""""""""""""""""""""

When two expressions are separated by ``,`` (comma) it is referred to as the :dfn:`comma operator`).  The comma operator first evaluates the left-hand expression, throwing away the result, and then evaluates the right-hand expression.  The value of the right-hand expression is the value of the comma operator expression.

It is not possible to overload the comma operator.

.. _bitwise-ops:

Bitwise Operators
^^^^^^^^^^^^^^^^^

Bitwise AND, OR and XOR
"""""""""""""""""""""""

When ``&``, ``|`` or ``^`` appear between two expressions they are referred to as :dfn:`bitwise AND`, :dfn:`bitwise OR` or :dfn:`bitwise XOR` binary operators, respectively.

Bitwise AND, OR and XOR are predefined for all integer types; they perform the usual bitwise operation on the two values.  They are also predefined for the ``Boolean`` type, which is treated as if it was a single bit with value 1 (if true) or 0 (if false).

Bitwise AND, OR and XOR can be overloaded for user-defined structures or combinations of different types.

Bitwise NOT
"""""""""""

When ``~`` (tilde) appears in front of an expression it is referred to as the :dfn:`bitwise NOT` unary operator.

Bitwise NOT is predefined for all integer types; it inverts the state of the bits of the value.  It is also predefined for the ``Boolean`` type, which is treated as if it was a single bit with value 1 (if true) or 0 (if false).

Left and Right Shift
""""""""""""""""""""

When ``<<`` or ``>>`` appear between two expressions they are referred to as the :dfn:`left shift` or :dfn:`right shift` binary operators, respectively.  These operators are pre-defined for all integer types, where they perform a left or right bit shift of the left operand by the number of bits given in the right operand.

A right-shift of a signed integer value will fill the left most bits with the sign bit, not with zeros.  Right shifts of unsigned integer values and left shifts of any integer values always fill with zeros.

It is possible to overload the shift operators for user-defined types, and even provide non-integer types as right-hand operands.

.. _ass-ops:

Assignment Operators
^^^^^^^^^^^^^^^^^^^^

Direct Assignment Operator
""""""""""""""""""""""""""

When ``=`` appears between two expressions it is referred to as the :dfn:`direct assignment operator`.  The direct assignment operator is predefined for all types; see :ref:`KLPG.types` for details on how direct assignment operates for a given type.  It is also possible to overload the direct assignment operator for any type. See :ref:`overloading-direct-ass-op`

Compound Assignment Operators
"""""""""""""""""""""""""""""

Any of the arithmetic or bitwise (but not logical) binary operators can be combined with ``=`` to form a :dfn:`compound assignment operator`; these are specifically ``+=``, ``-=``, ``*=``, ``/=``, ``%=``, ``<<=``, ``>>=``, ``&=``, ``^=`` and ``|=``.

A compound assignment operator is predefined for a given type if and only if the corresponding binary operator is predefined for the type.  It is also possible to overload the compound assignment operator for any type, and it is even possible to have different types for the left and right operands. See :ref:`overloading-compound-ass-ops`.

Operators and Polymorphism
^^^^^^^^^^^^^^^^^^^^^^^^^^

Operator invocations are subject to the same rules as function calls with respect to polymorphism.  If an exact match for an operator with the parameter types equal to the operand types is not found, KL will find the best-match among the existing implementations of the operator.  This makes it possible, for instance, to add an integer and a string; the result is that the integer is cast to a string and then the strings are concatenated.

For more information on polymorphism and best-match rules, see :ref:`polymorphism`.

Expressions
-----------

There are two types of expressions in KL: simple expressions and compound expressions.

.. _simple-exprs:

Simple Expressions
^^^^^^^^^^^^^^^^^^

:dfn:`Simple expressions` are the expressions from which more complex expressions are derived.  The simple expressions are:

- Symbols that refer to variables, function arguments or constants.  The type of the expression is the type of the entity referred to.  Examples: ``foo``, ``myParam``, ``mathPI``.  See :ref:`scope` for how symbol names are resolved.

- Boolean, integer, floating-point and string constants.  The type of the expression is the type of the constant.  Examples: ``true``, ``42``, ``3.14159``, ``FILE``, ``LINE``.  See :ref:`literal-constants`.

Compound Expressions
^^^^^^^^^^^^^^^^^^^^

:dfn:`Compound expressions` are built from :ref:`simple expressions <simple-exprs>` and/or other compound expressions using :ref:`operators <ops>`.

The following table lists all the different compound expressions in KL.  Compound expressions are grouped by :dfn:`type`; all expressions of the same type are of the same precedence and share the same associativity.  Compound expression types are listed from highest to lowest precedence.

+----------------------+---------------+-------------------------------------------------+
| Type                 | Associativity | Expression(s)                                   |
+======================+===============+=================================================+
| Postfix              | left-to-right | :samp:`{functionName}({args})`                  |
|                      |               +-------------------------------------------------+
|                      |               | :samp:`{expr}[{expr}]`                          |
|                      |               +-------------------------------------------------+
|                      |               | :samp:`{expr}.{member}`                         |
|                      |               +-------------------------------------------------+
|                      |               | :samp:`{expr}.{method}({args})`                 |
|                      |               +-------------------------------------------------+
|                      |               | :samp:`{expr}++`                                |
|                      |               +-------------------------------------------------+
|                      |               | :samp:`{expr}--`                                |
+----------------------+---------------+-------------------------------------------------+
| Prefix               | right-to-left | :samp:`+{expr}`                                 |
|                      |               +-------------------------------------------------+
|                      |               | :samp:`-{expr}`                                 |
|                      |               +-------------------------------------------------+
|                      |               | :samp:`++{expr}`                                |
|                      |               +-------------------------------------------------+
|                      |               | :samp:`--{expr}`                                |
|                      |               +-------------------------------------------------+
|                      |               | :samp:`!{expr}`                                 |
|                      |               +-------------------------------------------------+
|                      |               | :samp:`~{expr}`                                 |
+----------------------+---------------+-------------------------------------------------+
| Multiplicative       | left-to-right | :samp:`{expr} * {expr}`                         |
|                      |               +-------------------------------------------------+
|                      |               | :samp:`{expr} / {expr}`                         |
|                      |               +-------------------------------------------------+
|                      |               | :samp:`{expr} % {expr}`                         |
+----------------------+---------------+-------------------------------------------------+
| Additive             | left-to-right | :samp:`{expr} + {expr}`                         |
|                      |               +-------------------------------------------------+
|                      |               | :samp:`{expr} - {expr}`                         |
+----------------------+---------------+-------------------------------------------------+
| Shift                | left-to-right | :samp:`{expr} << {expr}`                        |
|                      |               +-------------------------------------------------+
|                      |               | :samp:`{expr} >> {expr}`                        |
+----------------------+---------------+-------------------------------------------------+
| Relational           | left-to-right | :samp:`{expr} < {expr}`                         |
|                      |               +-------------------------------------------------+
|                      |               | :samp:`{expr} <= {expr}`                        |
|                      |               +-------------------------------------------------+
|                      |               | :samp:`{expr} > {expr}`                         |
|                      |               +-------------------------------------------------+
|                      |               | :samp:`{expr} >= {expr}`                        |
+----------------------+---------------+-------------------------------------------------+
| Equality             | left-to-right | :samp:`{expr} == {expr}`                        |
| Identity             |               +-------------------------------------------------+
|                      |               | :samp:`{expr} != {expr}`                        |
|                      |               +-------------------------------------------------+
|                      |               | :samp:`{expr} === {expr}`                       |
|                      |               +-------------------------------------------------+
|                      |               | :samp:`{expr} !== {expr}`                       |
+----------------------+---------------+-------------------------------------------------+
| Bitwise AND          | left-to-right | :samp:`{expr} & {expr}`                         |
+----------------------+---------------+-------------------------------------------------+
| Bitwise XOR          | left-to-right | :samp:`{expr} ^ {expr}`                         |
+----------------------+---------------+-------------------------------------------------+
| Bitwise OR           | left-to-right | :samp:`{expr} | {expr}`                         |
+----------------------+---------------+-------------------------------------------------+
| Logical AND          | left-to-right | :samp:`{expr} && {expr}`                        |
+----------------------+---------------+-------------------------------------------------+
| Logical OR           | left-to-right | :samp:`{expr} || {expr}`                        |
+----------------------+---------------+-------------------------------------------------+
| Conditional          | right-to-left | :samp:`{expr}? {expr}: {expr}`                  |
+----------------------+---------------+-------------------------------------------------+
| Assignment           | right-to-left | :samp:`{expr} = {expr}`                         |
|                      |               +-------------------------------------------------+
|                      |               | :samp:`{expr} += {expr}`                        |
|                      |               +-------------------------------------------------+
|                      |               | :samp:`{expr} -= {expr}`                        |
|                      |               +-------------------------------------------------+
|                      |               | :samp:`{expr} *= {expr}`                        |
|                      |               +-------------------------------------------------+
|                      |               | :samp:`{expr} /= {expr}`                        |
|                      |               +-------------------------------------------------+
|                      |               | :samp:`{expr} %= {expr}`                        |
|                      |               +-------------------------------------------------+
|                      |               | :samp:`{expr} <<= {expr}`                       |
|                      |               +-------------------------------------------------+
|                      |               | :samp:`{expr} >>= {expr}`                       |
|                      |               +-------------------------------------------------+
|                      |               | :samp:`{expr} &= {expr}`                        |
|                      |               +-------------------------------------------------+
|                      |               | :samp:`{expr} ^= {expr}`                        |
|                      |               +-------------------------------------------------+
|                      |               | :samp:`{expr} |= {expr}`                        |
+----------------------+---------------+-------------------------------------------------+
| Comma                | left-to-right | :samp:`{expr} , {expr}`                         |
+----------------------+---------------+-------------------------------------------------+

Controlling Order of Operations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The order of operations can be explicitly controlled by putting ``(`` and ``)`` (parentheses) around expressions.

.. kl-example:: Order of Operations

  operator entry() {
    report( (2 * 3) + 5 );
    report( 2 * (3 + 5) );
  }

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
