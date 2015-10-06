.. _syntax:

KL Syntax
=========

When KL was developed it was designed to have a syntax as close as possible to JavaScript, which itself is what is referred to as a *C-like language* (as far as syntax is concerned).  This chapter goes into the details of KL syntax, and can act as a reference for you if you are not familiar with C-like languages.  On the other hand, if you are already familiar with the syntax of JavaScript and/or C, we recommend that you skip this chapter and move on to the next.

Some of the key characteristics of C-like languages are:

- Programs are plain, human-readable text files.

- A program is a sequence of :index:`tokens <single: token>`.  There are four major types of tokens: keywords, identifiers, symbols and constants.

- Tokens may be separated by arbitrary whitespace and **must** be separated by whitespace in the case that it would make two adjacent tokens appear to be a single, different token.  By whitespace, we mean spaces (ASCII 32), newlines (ASCII 10), tabs (ASCII 9), carriage returns (ASCII 13) and vertical tabs (ASCII 11).

- Programs can contain comments anywhere and comments are treated like whitespace when the program is processed by the computer.  There are two types of comments: block comments, which begin with ``/*`` and end with ``*/``, and line comments, which begin with ``//`` and continue to the next newline (ASCII 10).

- Blocks are delimited by ``{`` and ``}``

- Statements are terminated with ``;``

We delve into some more details of the KL syntax below.

.. index::
  single: encoding
  pair: utf-8; encoding
  pair: ucs-2; encoding
  pair: unicode; encoding
  pair: ascii; encoding

Encoding
--------

Although KL programs are plain, human-readable text files, KL does specify an encoding for the text files: UTF-8.  The KL compiler assumes that all KL source code is encoded as UTF-8 without any encoding marks.  KL programs which contain invalid UTF-8 sequences cannot be compiled and will result in syntax errors.

If you don't understand exactly what this means, don't worry: plain 7-bit ASCII text files, such as used for C source code (and often for JavaScript source code) are by default UTF-8 encoded.  The only thing to keep in mind is that text files saved on Windows in "Unicode format" (which technically means they are encoded as UCS-2) cannot be read by the KL compiler.  If you want to insert foreign language characters into a KL source file you must use an editor that can write UTF-8 files.

The benefit of specifying an encoding is that high-bit characters, such as foreign language characters, can be inserted directly into string constants in KL source files.

.. index::
  single: line continuation

Line Continuations
------------------

Like C, any line of a KL program that ends with a ``\`` (backslash) character causes the line to be joined with the next line.  This is useful for breaking long lines into multiple lines when a single token needs to be split; usually this token would be a long string.

This example shows the use of line continuations in a KL source file:

.. kl-example:: Line Continuations

  operator entry() {
    report("\
  This is a really, really long string \
  that spans multiple lines.\n\
  Note that \
       <-- the SPACES at the beginning \
  of the next line are preserved!");
  }

.. index::
  single: comment

Comments
--------

KL supports the same two types of comments as C and JavaScript: block comments and line comments.

.. index::
  pair: block; comment

Block Comments
^^^^^^^^^^^^^^

A block comment in KL is an arbitrary sequence of characters that begins with the characters ``/*`` and ends with the characters ``*/``.  Like C, KL ends a block comment as soon as it encounters the first sequence ``*/``.  Also like C, KL does not recognize nested comments.

The following example illustrates acceptable block comments in KL:

.. code-block:: kl

  /* A simple, one-line block comment */

  /* This is
     a multi-line
     block comment
     */
     
  /*
  ** And so is this
  */

  operator entry() {
    /* comments can appear in source code */
    report("Hello!"); /* pretty much anywhere */
    foo( 32 /*, 53*/ ); /* block comments are a simple way to temporarily remove code */
  }

The following example unacceptable (erroneous) block comments in KL:

.. code-block:: kl

  /* KL ends the comment
   * as soon as the first */
   * is seen, so this is
   * a bad block comment that 
   * results in a syntax error
   */

  /* Like C, block comments
   * cannot nest in KL,
     /* so this is also
      * a bad comment that
      * will result in a
      * syntax error
      */
   */

Be careful with block comments; if either of the errors of the type given above occur in your program it can be very difficult to figure out what has gone wrong; the syntax errors you are given will seem to have nothing to do with your program.  For this reason, we recommend that you use line comments, which are described next.

.. index::
  pair: line; comment

Line Comments
^^^^^^^^^^^^^

A line comment in KL begins with the character sequence ``//`` and continues until the end of the line (ASCII character 10).  Unlike block comments, there are no "gotchas" with line comments: they work exactly as expected.  However, they can't be used to comment out sections of code in the middle of a line.

The following example illustrates the use of line comments in KL:

.. code-block:: kl

  // A simple, one-line line comment

  // This is
  // a multi-line
  // line comment

  operator entry() {
    // comment can appear in source code
    report("Hello!"); // pretty much anywhere
    foo( 32 //, 53 ); // can't comment out code in the middle of the line
            ); // but you can continue it on the next line.
  }

.. index::
  single: token

Tokens
------

A KL program is *parsed* as a sequence of tokens.  A token is a sequence of characters that begins with something other than whitespace and is not a comment.  There are four categories of tokens in KL: keywords, identifiers, symbols, and constants.

.. index::
  pair: keyword; token

Keywords
^^^^^^^^

The following is the list of all the keywords in KL:

.. hlist::
  :columns: 3
  
  * ``alias``
  * ``break``
  * ``case``
  * ``const``
  * ``continue``
  * ``default``
  * ``do``
  * ``else``
  * ``false``
  * ``FILE``
  * ``for``
  * ``FUNC``
  * ``function``
  * ``if``
  * ``in``
  * ``inline``
  * ``io``
  * ``LINE``
  * ``object``
  * ``operator``
  * ``require``
  * ``return``
  * ``struct``
  * ``switch``
  * ``true``
  * ``var``
  * ``while``

Keywords cannot be used as identifiers, ie. cannot be used for variable, parameter, function, constant or type names.

.. index::
  pair: symbol; identifier

Identifiers
^^^^^^^^^^^

:dfn:`Identifiers` are a sequence of one or more characters that:

- begin with any of the characters ``a...z``, ``A...Z`` or ``_``; and
- are followed by zero or more of the characters ``a...z``, ``A...Z``, ``0...9`` or ``_``

Identifiers are used in KL for variable names, parameter names, function names, constant names, method names and type names.

.. note:: The built-in base types in KL (eg. ``Boolean``, ``String``, ``Float32``) are not keywords but rather identifiers.  This is a technical detail that is important in the design of the language grammar but doesn't make much difference in practice; it simply changes certain syntax errors into semantic errors.

Some examples of valid identifiers in KL:

- ``foo``
- ``someVariable``
- ``MyType``
- ``MyTypeVersion2``
- ``variable_with_underscores``
- ``piBy2``
- ``_``

Some examples of invalid identifiers:

- ``2by4``
- ``my%Share``

.. index::
  pair: symbol; token

Symbols
^^^^^^^

A small set of non-alphanumeric, non-underscore characters or short sequences of such characters are the :dfn:`symbols` in KL.  They are specifically:

.. hlist::
  :columns: 6
  
  * ``=``
  * ``==``
  * ``===``
  * ``+``
  * ``+=``
  * ``++``
  * ``-``
  * ``-=``
  * ``--``
  * ``*``
  * ``*=``
  * ``/``
  * ``/=``
  * ``%``
  * ``%=``
  * ``^``
  * ``^=``
  * ``^^``
  * ``&``
  * ``&=``
  * ``&&``
  * ``|``
  * ``|=``
  * ``||``
  * ``[``
  * ``[]``
  * ``]``
  * ``(``
  * ``)``
  * ``{``
  * ``}``
  * ``;``
  * ``.``
  * ``<``
  * ``<=``
  * ``<<``
  * ``<<=``
  * ``<<<``
  * ``<>``
  * ``>``
  * ``>=``
  * ``>>``
  * ``>>=``
  * ``>>>``
  * ``~``
  * ``!``
  * ``!=``
  * ``!==``
  * ``,``
  * ``?``
  * ``;``
  * ``#``

The KL compiler is "greedy" when looking for symbols: it looks for the longest sequence of characters that are a valid symbol.  This is why ``==(`` is treated as the two symbols ``==`` and ``(``: there is no symbol starting with ``==(`` but ``==`` is a symbol.

.. index::
  single: constant

.. _literal-constants:

Constants
^^^^^^^^^

A constant is a token that is interpreted as a fixed value of a specific type. KL supports five types of constants: boolean constants, integer constants, floating-point constants, and string constants.  Each of these are explained below.

.. index::
  pair: boolean; constant

Boolean Constants
"""""""""""""""""

The two keywords ``true`` and ``false`` are the two :dfn:`boolean constants`.  They are each a value of type ``Boolean``.

.. kl-example:: Boolean Constants

  operator entry() {
    Float32 value = 1.1;
    Index steps = 0;
    Boolean done = false;
    while (!done) {
      value *= value;
      if (value > 2)
        done = true;
      ++steps;
    }
    report("took " + steps + " steps");
  }

.. index::
  pair: integer; constant

.. _integer-constants:

Integer Constants
"""""""""""""""""

An :dfn:`integer constant` can take one of three forms:

- The single digit ``0``
- A decimal constant that starts with a single digit in the range ``1...9`` followed by zero or more digits in the range ``0...9``
- The two characters ``0x`` or ``0X`` followed by one or more characters in one of the ranges ``0...9``, ``a...f`` and ``A...F``

In all cases, an integer constant may be optionally followed by an integer type specification.  An integer type specification specified the signededness and bit width of the integer and takes the form

- The character ``s`` (signed) or the character ``u``, followed by:
- (optionally) ``8``, ``16``, ``32`` or ``64`` (the bit width)

If no bit width is provided in the type specification the integer is 32-bit.  So, for example, ``145u`` is an unsigned 32-bit integer constant and ``78s`` is a signed 32-bit integer constant.

If no type specification is provided at all the integer is signed 32-bit.  For example, ``5421`` is a signed 32-bit integer constant.

.. kl-example:: Integer Constants

  operator entry() {
    report(0);            // SInt32
    report(1);            // SInt32
    report(123456789u);   // UInt64
    report(0xA9);         // SInt32
    report(0xdeadBEEFu);  // UInt32
    report(123456789012345678u64); // UInt64
  }

.. index::
  pair: floating-point; constant

.. _floating-point-constants:

Floating-Point Constants
""""""""""""""""""""""""

A :dfn:`floating-point constant` in KL is either of type ``Float32`` or type ``Float64``.  The syntax follows closely that of C/C++, with ``Float32`` corresponding to the C type ``float`` and ``Float64`` corresponding to the C type ``double``:

- ``1.2`` is of type ``Float64``
- ``1.2f`` is of type ``Float32``
- ``.7`` is of type ``Float64``
- ``3.4e7`` and ``3.4e+7`` are of type ``Float64``
- ``3.4e7f`` and ``3.4e+7f`` are of type ``Float32``
- ``.5e-4f`` is of type ``Float32``

KL extends the C/C++ syntax by allowing more explicit specification of the type using the ``f32`` and ``f64`` suffixes.  For example:

- ``4.5e-6f32`` is the same as ``4.5e-6f``
- ``2.874f64`` is the same as ``2.873``

If none of the ``f``, ``f32`` or ``f64`` suffixes are present then the floating-point constant is an :dfn:`untyped floating-point constant`.  An untyped floating-point constant automatically inherits the type of its surrounding expression.  For instance, if the floating-point constant ``.5`` is added to a variable of type ``Float32`` then the constant is treated as having type ``Float32``.

.. kl-example:: Floating-Point Constants

  operator entry() {
    // Float32
    report(0.f);
    report(0.0f);
    report(.0f);
    report(0.5f);
    report(.5f);
    report(-5.6e7f);
    report(.75e-10f);
    report(3.4e14f32);
    report(7.89f32);
    report(.67f32);
    report(.12e20f32);

    // Float64
    report(0.);
    report(0.0);
    report(.0);
    report(0.5);
    report(.5);
    report(-5.6e7);
    report(.75e-45);
    report(5.4f64);
    report(.78f64);
    report(7.532453e-120f64);
    report(.754e45f64);
  }

.. note::
  
  It is not possible to represent many decimal fractional expressions in IEEE floating point format.  As such, do not be surprised if the output values of such expressions appear to be slightly off, as seen in the example above with the constant ``.12e20f32``.

.. index::
  pair: string; constant

.. _string-constants:

String Constants
""""""""""""""""

A :dfn:`string constant` is a constant value of type ``String``.  It takes one of the following forms:

- A sequence of characters, possibly including string constant escape sequences (described below), enclosed in a pair of ``"`` (double-quote) characters; or

- A sequence of characters, possibly including string constant escape sequences (described below), enclosed in a pair of ``'`` (single-quote) characters; or

A :dfn:`string constant escape sequence` is one of the following sequences of characters, describing what the sequence is replaced by in the string: 

``\n``
  a single newline (ASCII 10) character
``\f``
  a single form feed (ASCII 12) character
``\r``
  a single carriage return (ASCII 13) character
``\t``
  a single carriage tab (ASCII 9) character
``\v``
  a single vertical tab (ASCII 11) character
``\a``
  a single bell (ASCII 7) character
``\b``
  a single backspace (ASCII 8) character
``\0``
  a single null (ASCII 0) character
``\"``
  a single double-quote (ASCII 34) character
``\'``
  a single single-quote (ASCII 39) character
``\\``
  a single backslash (ASCII 92) character
:samp:`\\x{HH}`
  A single character whose ASCII code is given in hexadecimal.  The two characters :samp:`{HH}` must each be a hexadecimal character, ie. in one of the ranges ``0...9``, ``a...f`` and ``A...F``.  For example, the escape sequence ``0x0A`` (decimal 10) is equivalent to the escape sequence ``\n`` (ASCII 10).

.. kl-example:: String Constants

  operator entry() {
    report("double-quoted!");
    report('single-quoted\nwith a newline');
    report("double-quoted containing \"double quotes\"");
  }

The ``FILE`` and ``LINE`` Constants
""""""""""""""""""""""""""""""""""""""

The two keywords ``FILE`` and ``LINE`` are special constants in a KL program.  The keyword ``FILE`` is replaced by a string constant whose value is the filename of the current file being compiled.  The keyword ``LINE`` is similarly replaced with an integer constant whose value is the line number of the current file being compiled.  So, for example, if the following KL source code is passed on standard input:

.. kl-example:: FILE and LINE

  operator entry() {
    report(FILE + ":" + LINE);
  }

.. index::
  single: program structure

Program Structure
-----------------

A KL program consists of zero or more :index:`global declarations <single: global declaration>` in sequence.  A global declaration is one of:

- A declaration of a function, a function prototype, an operator, a constructor, a destructor, a method or an operator overload; see :ref:`functions`.

- A declaration of a structure or an object; see :ref:`KLPG.types.structures` and :ref:`KLPG.types.objects`.

- A declaration of global named constant; see :ref:`KLPG.global.named-constants`.

- A ``require`` statement; see see :ref:`KLPG.require`

In turn, functions, operators, and other similar constructs consist of zero or more :index:`statements <single: statement>`.  Each statement is terminated with a ``;`` (semicolon) character.  For more detailed information on all the statements available in KL, see :ref:`statements`.

A sequence of statements, surrounded by braces (a ``{`` and a ``}``), can take the place of a single statement.  This also introduces a nested scope; for more information, see :ref:`scope-compound-statement`.
