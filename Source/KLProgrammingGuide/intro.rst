Introduction
============

KL (pronounced "kale") is the programming language used for |FABRIC_PRODUCT_NAME| operators.  KL stands for "kernel language"; in this context, *kernel* refers to the concept of a computational kernel as used in multithreaded programming.

KL was designed with the following goals:

- KL is designed to run performance-critical sections of dynamic-language programs.  As such, KL is designed so that KL programs run as quickly as possible on modern hardware.

- KL should be easy to learn for someone who is already familiar with programming in Python, JavaScript and other scripting languages.

- It must be possible to compile most KL programs to run on different architectures and kinds of hardware, specifically CPUs and GPUs.

KL is a language with a syntax very similar to JavaScript but that is *procedural*, *strongly-typed* and with *low-level data layouts*.  Being **procedural** means that, unlike JavaScript, functions (or, rather, closures) are not first-class objects that can be passed around in the language; instead, functions are always globally declared.  Being **strongly-typed** means that, in a KL program, the types of all variables and function parameters are known at compile type, unlike JavaScript where types are only known at runtime.  Having **low-level data layouts** means that the size of data and the way that it is laid out in memory is guaranteed and controllable by the programmer.

.. _KLPG.kl-tool:

Running the Examples
--------------------

This guide is full of KL example code.  We encourage you to not only read the examples and their output, but to try making changes to them based on what you're learning and see how it affects the results.

In order to run KL code in isolation (ie. outside of |FABRIC_PRODUCT_NAME|) we have created the *KL tool*.  The KL tool has been used to generate all of the output you will find in this guide.  It is installed as part of the |FABRIC_PRODUCT_NAME| installer, available at http://dist.fabric-engine.com/|FABRIC_PRODUCT_NAME_CAMEL_CASE|/latest/.  As part of the install process, the :envvar:`FABRIC_DIR` environment variable will be set, and the KL tool will be installed in the directory :file:`$FABRIC_DIR/bin`.  Once the KL tool is installed, you can copy the source code for an example into a text file and run :command:`kl filename.kl` from a command line to reproduce the results.

.. hint:: The KL tool supports a wide variety of options that can aid in developing |FABRIC_PRODUCT_NAME| applications.  Run :command:`kl --help` for information on the available options.  In particular, :command:`kl --loadexts` is very useful for debugging custom |FABRIC_PRODUCT_NAME| extensions.

Hello World in KL
-----------------

Before diving in to the details of the language, we will present some simple examples.  We don't expect you to understand all the details of the examples, but hopefully they will give you a basic idea of what KL programs look like as well as some of what is possible with KL.

Traditionally, the first program you see in a language is one that says hello.  In KL, the "Hello, world!" program is simple:

.. kl-example:: Hello World

  operator entry() {
    report("Hello, world!");
  }

Running this program through the KL tool, the output is "Hello, world!".

There's not much to learn from this program, but it does introduce a few concepts:

- The ``entry`` operator is what is run by the KL tool.  KL distinguishes places in the program that can be called from the outside world; in this case, the outside world is the KL tool itself.  We discuss more about operators in the section :ref:`operators`

- The ``report`` function sends some text to wherever messages go.  In the case of the KL tool, messages go to standard output; for console applications (in Node.js or Python for example), messages go to standard error.

- The text ``"Hello, world!"`` is a string constant.  String constants in KL follow almost exactly the same syntax as JavaScript.

Fibonacci Sequence in KL
------------------------

Next, we present a somewhat more sophisticated example that computes the first few terms of the Fibonacci sequence.  The Fibonacci sequence is the number sequence whose first two terms are 1 and 1, and whose further terms are the sum of the previous two in the sequence, ie. 2, 3, 5, 8, and so on.  There are several ways of computing the Fibonacci sequence in a programming language but we choose the naive, recursive way in order to illustrate some more language features of KL.

The source code for the Fibonacci sequence generator in KL is:

.. kl-example:: Fibonacci Sequence

  /* Recursively compute the Fibonacci sequence.
  ** The first term is returned with n = 0
  */

  function Integer fibonacci(Integer n) {
    if (n <= 1)
      return 1; // The first two terms (n=0 or n=1) are 1
    else 
      return fibonacci(n - 2) + fibonacci(n - 1);
  }

  operator entry() {
    for (Integer i = 0; i < 10; ++i)
      report(fibonacci(i));
  }

The Fibonacci example highlights a few simple features of KL, including:

- Function and parameter declaration
- Recursion
- Conditional statements
- Loops
- Comments

Mandelbrot Set in KL
--------------------

Finally, we present an example of a KL program that generates the Mandelbrot set and outputs it visually as ASCII art.  The Mandelbrot set is a mathematical set defined by complex recursive functions, but that it best known because the patterns it contains are visually stunning.  Refer to the Wikipedia entry on the Mandelbrot set at http://en.wikipedia.org/wiki/Mandelbrot_set for more information.

KL includes very powerful features for extending the language for computational problems such as that of computing the values of the Mandelbrot set, as seen in the source code below:

.. kl-example:: Mandelbrot Set
  
  struct Complex32 {
    Float32 re;
    Float32 im;
  };

  function Complex32(Float32 re, Float32 im) {
    this.re = re;
    this.im = im;
  }

  function Complex32 +(Complex32 lhs, Complex32 rhs) {
    return Complex32(lhs.re + rhs.re, lhs.im + rhs.im);
  }

  function Complex32 *(Complex32 lhs, Complex32 rhs) {
    return Complex32(lhs.re*rhs.re-lhs.im*rhs.im, lhs.re*rhs.im + lhs.im*rhs.re);
  }

  function Float32 Complex32.normSq() {
    return this.re*this.re + this.im*this.im;
  }

  function UInt8 computeDwell(Complex32 c) {
    Complex32 z = c;
    UInt8 count;
    for (count = 0; count < 255; ++count) {
      if (z.normSq() > 4)
        break;
      z = z*z + c;
    }
    return count;
  }

  operator entry()
  {
    Complex32 z;
    for (Size row=9; row<=31; ++row) {
      z.im = Float32(4.0 * row / 40.0 - 2.0);
      String rowString;
      for (Size col=0; col<=78; ++col) {
        z.re = Float32(4.0 * col / 78.0 - 2.0);
        UInt8 dwell = computeDwell(z);
        
        if (dwell & 192)
          rowString += "#";
        else if (dwell & 48)
          rowString += "*";
        else if (dwell & 12)
          rowString += ".";
        else
          rowString += " ";
      }
      report(rowString);
    }
  }

The Mandelbrot set example highlights a few of the more sophisticated features of KL, including:

- User-defined types
- Constructors
- Operator overloads
- Methods
- Bitwise operators
- Variable-length arrays

How This Guide is Organized
---------------------------

Unlike other languages, KL is a language designed to add performance-critical sections to programs written in dynamic languages.  As such, this guide assumes that you are already familiar with the basic concepts of modern programming languages, including types, expressions, statements (eg. conditional statements, loop statements, return statements) and functions.

Since it's difficult to provide meaningful examples in a computer language without using many concepts of the language, we will often use or even refer to concepts that aren't discussed until later in the guide.  We leave it up to you to decide whether to jump ahead or to just keep reading and see where things go.

The remainder of the guide is laid out as follows:

- :ref:`syntax` describes the syntax of KL.  KL has a syntax very similar to JavaScript (like JavaScript, it is a C-like language) so this syntax will be familiar to many programmers.  If you are already familiar with the syntax of JavaScript or C, we recommend that you skip this chapter and move on to the next; you can always come back to it later for reference.

- :ref:`KLPG.types` introduces the type system of KL.  KL comes with a rich set of base types that includes integers, floating-point numbers, strings and booleans, as well as derived types including structures, arrays and dictionaries.

- :ref:`globals` describes how functions and other global declarations are made in KL.  KL includes support for basic functions (also referred to as procedures in other languages), but also support more complex function concepts such as prototypes, methods and overloaded operators.  It also supports global constants, as well as a facility to import functionality from external modules.

- :ref:`ops-exprs` describes the set of operators supported by KL and the different kinds of expressions that can be formed using these operators.  It also discusses the rules that govern scoping for variables and other symbols.

- :ref:`statements` describes the different statements that are available for function bodies in KL.
