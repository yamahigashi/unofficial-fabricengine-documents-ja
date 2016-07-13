.. index::
  single: statement

.. _statements:

Statements
==========

The bodies of functions, operators, and so on are composed of :dfn:`statements`.  Statements are the parts of KL programs that actually do something.  Statements cause expressions to be evaluated, can conditionally execute other statements, or can iterate over another set of statements until a condition is met.

The remainder of the chapter describes the different statements that can be used inside KL function definitions.  Statements are divided into two categories: simple statements and complex statements.

.. index::
  pair: simple; statement

.. _simple-statements:

Simple Statements
-----------------

A simple statement is a statement that does not check conditions or create a nested scope.  Simple statements always end with a ``;`` (semicolon) character.

.. warning:: It is a common syntax error in KL and other C-like languages to forget to finish a simple statement with a semicolon.

.. index::
  pair: expression; statement

.. _expr-statements:

Expression Statements
^^^^^^^^^^^^^^^^^^^^^

Any expression, followed by a ``;`` (semicolon), is a statement.  The statement operates by evaluating the expression and then discarding the resulting value (if any).  The most common form of an expression statement is one that invokes a function call (eg. ``report``).

.. kl-example:: Expression Statements
  :no-output:

  operator entry() {
    // A very useless expression statement:
    // evaluates 2 + 2 then discards the
    // result
    2 + 2;

    // A more useful expression statement:
    // evaluates the report function, which
    // causes text to appear
    report("Hello!"); 
  }

.. index::
  pair: parallel execution; statement
  pair: PEX; statement

.. _KLPG.parallel-execution-statement:

Parallel Execution Statement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The :dfn:`parallel execution statement`, abbreviated as :dfn:`PEX statement`, allows a KL program to invoke an operator multiple times in parallel in a generic fashion.  Each PEX statement requires an operator (see :ref:`operators`) to invoke as well as a number of times to invoke it, but can also take an arbitrary number of additional parameters that are passed to the operator that is called.

A PEX statement takes the form:

.. parsed-literal::
  
  *operatorName*\<<<*countExpr*\>>>(*optionalArg1*\, *optionalArg2*\, ...);

:samp:`{operatorName}` must be the name of an operator whose first parameter is of type ``Index``, and :samp:`{countExpr}` must be an expression of type ``Size`` and is the number of calls to the operator to make.

The operator will be called :samp:`{countExpr}` times, potentially with overlapping parallel calls, with the first argument varying from ``0`` to :samp:`{countExpr}-1`.  Any of the optional additional arguments given are passed through verbatim, and the operator must have a parameter list that is compatible (through casting) with the arguments given.  For the purpose of readability, KL supports a special syntax for operators that adds an initial parameter of type ``Index``.  This syntax mirrors the parallel execution syntax:

.. kl-example::

  // The following operator definitions are equivalent:
  
  operator foo<<<index>>>(String string, UInt32 array[]) { /*...*/ }
  operator foo(Index index, String string, UInt32 array[]) { /*...*/ }

In a PEX statement, KL and/or |FABRIC_PRODUCT_NAME| will try to distribute the calls as evenly as possible between the available cores on the running machine, but without foreknowledge of how long any of the calls will take.  Thus, a PEX is maximally efficient in cases where each call takes the same amount of time.

It is possible and even encouraged as a programming practice to make recursive PEXes.

.. warning:: KL makes no effort to guard against changes to variables passed in the additional arguments from different cores at the same time.  It is the programmer's responsibility to ensure that two invocations of the operator used in a PEX statement cannot change the same value at the same time.  Such changes can result in difficult-to-track-down bugs or even complete failure of your program.

.. warning:: There is an inherent overhead in a PEX that may make it less efficient than serial calls in the case that the operator that is called is trivial.  Parallel executions best with large workloads.

.. kl-example:: PEX Operations
  :no-output:

  operator setArrayElementDesc<<<index>>>(io String array[]) {
    array[index] = "index=" + index;
  }
  
  operator entry() {
    String array[];
    array.resize(16);
    setArrayElementDesc<<<array.size()>>>(array);
    report(array);
  }

.. index::
  pair: empty; statement

.. _empty-statement:

The Empty Statement
^^^^^^^^^^^^^^^^^^^

A ``;`` (semicolon) alone is a statement that does nothing.  This can be used in cases where a statement is required but there is nothing to do.

.. kl-example:: The Empty Statement
  :no-output:

  function foo(io MyType myType) {
    for (; returnsFalseWhenDone(myType); )
      ; // Do nothing
  }

.. index::
  pair: variable declaration; statement

.. _var-decl-statements:

Variable Declaration Statements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A :dfn:`variable declaration statement` introduces one or more new variables into the innermost scope.  These variables remain visible for the rest of the scope and are destroyed, executing destructors when appropriate, when execution exists this scope.

Variable declarations require a type.  Multiple variables can be declared in the same statement by separating them with ``,`` (commas).

The variable names can be followed by array and dictionary specifications.  See :ref:`arrays` and :ref:`dictionaries` for more information on array and dictionary specifications.

Variables can be constructed or assigned to when declared to set their initial values; see :ref:`KLPG.constructor`.

.. kl-example:: Variable Declaration Statements
  :no-output:

  operator entry() {
    Scalar a;
    report(a);
    Integer b[], c[2][2], d;
    report(b);
    report(c);
    report(d);
  }

.. note:: It is not currently possible to initialize arrays in KL in the statement where the variable is declared.

.. index::
  pair: variable declaration; statement

.. _KLPG.const-decl-statements:

Constant Declaration Statements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A :dfn:`constant declaration statement` is similar to a :ref:`variable
declaration statement <var-decl-statements>` but is preceded with the keyword
`const`.  It follows an identical syntax to global named constants; see
:ref:`KLPG.global.named-constants`.

.. index::
  pair: return; statement

.. _return-statement:

The ``return`` Statement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``return`` statement takes two forms:

- For a function which returns a value, the ``return`` statement immediately returns the given value to the calling function.  There is an implicit cast to the type of the return value as specified in the function definition.

- For a function which does not return a value, the ``return`` statement does not take a value and simply returns immediately to the calling function.

.. kl-example:: The return Statement
  :no-output:

  // Function that returns a value
  function String markupName(String name) {
    return "My name is '" + name + "'";
  }

  // Function that does not return a value
  function suffixIndexDesc(io String strings[], Size index) {
    if (index >= strings.size())
      return;
    strings[index] += " (was at index " + index + ")";
  }

.. index::
  pair: throw; statement

.. _throw-statement:

The ``throw`` Statement
^^^^^^^^^^^^^^^^^^^^^^^

The ``throw`` statement throws an exception, which will immediately quit execution of KL code and return the exception to the calling environment (|FABRIC_PRODUCT_NAME| or the KL tool) where it will be displayed to the user.  The throw statement takes a single "parameter", which can be any value.  This value will be automatically converted to a string before it is passed back to the calling environment.

.. note:: It is not yet possible to catch exceptions from within KL; this is because LLVM lacks support for exception handling on 64-bit Windows.

.. kl-example:: The throw Statement

  operator entry() {
    report("Before throw");
    throw "Exception";
    report("After throw");
  }

.. index::
  pair: complex; statement

.. _complex-statements:

Complex Statements
------------------

A :dfn:`complex statement` is a statement that groups together and/or conditionally executes other statements.  Complex statements are built from simple statements, other complex statements, and expressions.

.. index::
  pair: compound; statement

.. _compound-statements:

Compound Statements
^^^^^^^^^^^^^^^^^^^

At any point when a single statement can be inserted in KL source code, it is possible to insert multiple statements surrounded by ``{`` (left brace) and ``}`` (right brace).  This has the following effects:

- The statements are executed, in order, as if they were together a single statement; and

- A new, nested scope is introduced; see :ref:`scope`.

.. index::
  pair: conditional; statement

.. _conditional-statements:

Conditional Statements
^^^^^^^^^^^^^^^^^^^^^^

There are two types of conditional statement in KL: the ``if`` statement and the ``switch`` statement.

.. index::
  pair: if; statement

.. _if-statement:

The ``if`` Statement
"""""""""""""""""""""""""""""

The ``if`` keyword begins a conditional statement, which can optionally include an ``else`` clause.  As in JavaScript and C, ``if`` and ``else`` statements can chain.

.. kl-example:: The if Statement
  :no-output:

  function String desc(Integer n) {
    if (n == 0)
      return "zero";
    else if (n == 1)
      return "one";
    else
      return "lots";
  }

.. index::
  pair: switch; statement

.. _switch-statement:

The ``switch`` Statement
""""""""""""""""""""""""

The ``switch...case`` construct is a more compact form for a sequence of ``if...else`` statements, just as in JavaScript and C.

.. kl-example:: The if Statement
  :no-output:

  function String descNumber(Integer i) {
    switch (i) {
      case 0:
        return "zero";
      case 1:
        return "one";
      case 2:
      case 3;
      case 4:
        return "a few";
      default:
        return "many";
    }
  }

.. index::
  pair: loop; statement

.. _loop-statements:

Loop Statements
^^^^^^^^^^^^^^^

KL supports four different types of loop statements: "C-style" loops, while loops, do-while loops, and dictionary loops.

.. index::
  pair: C-style loop; statement

.. _c-style-loop:

"C-Style" Loops
"""""""""""""""

A :dfn:`C-style loop` takes the form:

.. parsed-literal::
  
  for (:samp:`{startStmt}`\; :samp:`{checkExpr}`\; :samp:`{nextExpr}`\)
    :samp:`{bodyStmt}`

where :samp:`{startStmt}` is a statement (possibly empty), :samp:`{checkExpr}` and :samp:`{nextExpr}` are optional expressions, and :samp:`{bodyStmt}` is a statement.  The loop operates as follows:

- A new, nested scope is created.  This scope is destroyed when the loop finishes.

- The :samp:`{startStmt}` statement is executed.

- The :samp:`{checkExpr}` expression, if present, is evaluated, and the resulting value is converted to a ``Boolean``.  If the result is false, the loop finishes.

- The :samp:`{bodyStmt}` statement is executed.

- The :samp:`{nextExpr}` expression, if present, is evaluated, and the resulting value is discarded.  Execution is transferred back to the step that evaluates the :samp:`{checkExpr}` expression.

Note that since :samp:`{startStmt}` is a statement, it is possible to declare a new variable there.  This variable will go out-of-scope when the loop finishes.  It is common practice to declare loop-bound index variables in the :samp:`{startStmt}` statement.

.. kl-example:: C-Style Loops
  :no-output:

  operator entry() {
    for (Index i=0; i<10; ++i)
      report("i is now " + i);
  }

.. index::
  pair: while loop; statement

.. _while-loops:

While Loops
"""""""""""""""

A :dfn:`while loop` takes the form:

.. parsed-literal::
  
  while (:samp:`{checkExpr}`)
    :samp:`{bodyStmt}`


where :samp:`{checkExpr}` is a expression and :samp:`{bodyStmt}` is a statement.  The loop operates as follows:

- The :samp:`{checkExpr}` expression is evaluated, and the resulting value is converted to a ``Boolean``.  If the result is false, the loop finishes.

- The :samp:`{bodyStmt}` statement is executed.

- Execution is transferred back to the step that evaluates the :samp:`{checkExpr}` expression.

.. kl-example:: while Loops

  operator entry() {
    Integer i = 0;
    while (i < 10) {
      report("i is now " + i);
      ++i;
    }
  }

.. index::
  pair: do...while loop; statement

.. _do-while-loops:

Do-While Loops
""""""""""""""""""""""""


A :dfn:`do-while loop` takes the form:

.. parsed-literal::
  
  do
    :samp:`{bodyStmt}`
  while (:samp:`{checkExpr}`);

where :samp:`{checkExpr}` is a expression and :samp:`{bodyStmt}` is a statement.  The loop operates as follows:

- The :samp:`{bodyStmt}` statement is executed.

- The :samp:`{checkExpr}` expression is evaluated, and the resulting value is converted to a ``Boolean``.  If the result is false, the loop finishes.

- Execution is transferred back to the step that executes the :samp:`{bodyStmt}` statement.

.. kl-example:: do-while Loops

  operator entry() {
    Integer i=0;
    do {
      report("i is now " + i);
      ++i;
    } while (i<10);
  }

.. index::
  pair: dictionary loop; statement

.. _dictionary-loops:

Dictionary Loops
""""""""""""""""

A dictionary loop iterates over all the keys and values, or just the values, in a dictionary.  For more information on dictionary loops, see :ref:`dictionaries`.

.. index::
  pair: loop control; statement

Loop Control Statements
^^^^^^^^^^^^^^^^^^^^^^^

Within the body of a loop, the ``break`` and ``continue`` statements can be used to prematurely end the current iteration of the loop as described below.

.. index::
  pair: break; statement

.. _break-statement:

The ``break`` Statement
"""""""""""""""""""""""

The ``break`` statement immediately exits the innermost loop.  It is an error to use the ``break`` statement outside of a loop.

.. kl-example:: The break Statement

  operator entry() {
    // Only loops 5 times
    for (Integer i=0; ; ++i) {
      report("Loop " + i);
      if (i == 5)
        break; // exit the innermost loop
    }
  }

.. index::
  pair: continue; statement

.. _continue-statement:

The ``continue`` Statement
""""""""""""""""""""""""""

The ``continue`` statement immediately jumps to the next iteration of the innermost loop.  It is an error to use the ``continue`` statement outside of a loop.

.. kl-example:: The continue Statement

  operator entry() {
    // Only prints 7
    for (Integer i=0; i<10; ++i) {
      if (i != 7)
        continue; // continue to next iteration of loop
      report("Iteration " + i);
    }
  }
