.. _KLTOOLGUIDE:

Using the KL Tool to Develop and Debug Extensions
=================================================

.. image:: /images/FE_logo_345_60.*
   :width: 345px
   :height: 60px

| |FABRIC_PRODUCT_NAME| version |FABRIC_VERSION|
| |FABRIC_COPYRIGHT|


The KL Tool
-----------

Distributed with Fabric Engine is a command-line executable :file:`kl`
(:file:`kl.exe` on Windows) under the :file:`bin/` folder in the Fabric
Engine distribution.  It is referred to as the :dfn:`KL tool`.

The KL tool enables running KL programs from the command line and reporting
results. The KL tool is used throughout the internal unit test suite at
Fabric Software. In addition, the KL tool can be very useful in the
development of your own custom KL extensions.

When a Fabric Engine environment is set up by sourcing :file:`environment.sh`
at the root level of the Fabric Engine distribution, or by double-clicking
:file:`prompt.bat` on Windows, the KL tool should be available on your
:envvar:`PATH` and can be run on the command line as the command :file:`kl`.
You can verify that it is working by running :command:`kl --help`, which
should show you all the options available.

Compiling and Evaluating KL Source Files with the KL Tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The KL tool should be run providing the name of a KL source file to compile
and run. The provided KL source file is normally a small text file containing
an entry operator (see below) and some code to generate output. For example,
if the file :file:`MyTest.kl` contained KL source code, you would run it in
the KL tool with the command::

  kl MyTest.kl


The ``entry()`` Operator
~~~~~~~~~~~~~~~~~~~~~~~~

The KL tool will look for an operator called ``entry`` taking zero arguments
within the code. This operator will be called by the KL tool after it
has compiled the source code.

.. kl-example::

  operator entry() {
    report("Hello World");
  }

Testing Extensions
------------------

Often, a simple KL source file can be written that loads and performs various
tests on your extension. Simply by including the ``require MyExtension;``
statement at the beginning of the file will cause the functionality of your
entire extension to included. The ``require`` statement will also validate
that your extension does not include any syntactic errors. If the compilation
of the extension as well as the code in the KL source file that requires it is
successful, then the entry operator will be invoked.

In order to test your extension, the KL source file will will typically
construct objects and structs defined in your extension, and test the
functions by invoking them and reporting the results.

.. note::

  It is better to avoid reporting entire data structures, as these can change
  without breaking the behavior of the code. Instead, consider invoking
  methods on your types and check the results. Avoid testing internal methods
  that are not intended to be exposed to users.Your extension should define
  methods that are expected to be used in other extensions, or in operators in
  Splice. These methods define the interface to your extension, and should be
  tested thoroughly.It is good practice to use access modifiers such as
  :code:`public` and :code:`private` to control the external API to your
  objects and structs; see :ref:`KLPG.types.member-access` for more details.

.. kl-example:: A Simple Test in KL

  require Math;

  operator entry() {
    Mat33 mat33 = Quat(Euler(0.0, HALF_PI, 0.0, RotationOrder('zyx'))).toMat33();
    report(mat33);
  }

Output to a Text File
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The output of the KL tool can be sent to a text file by using the :code:`>`
shell operator::

  kl MyTest.kl > MyTest.out

This can be useful when the test generates a lot of output, or when you want
to search through the output in a text editor.  It is also useful for 
generating the file with correct output for unit test cases.

Setting up Unit Tests that Use the KL Tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Unit testing systems are easy to setup using the KL tool. Unit tests typically
compare a reference output against the current output to determine if the
behavior of your code has changed.

If you are using Linux or OS X, or a mingw shell on Windows, you can use the
:command:`cmp` and :command:`diff` utilities to create simple scripts to
perform tests.  A sample such script might be:

.. code:: bash

  #!/bin/bash

  USAGE="Usage: $0 file1.kl file2.kl ... fileN.kl"

  if [ "$#" == "0" ]; then
    echo "$USAGE"
    exit 1
  fi

  while (( "$#" )); do

    KL=$1
    OUT=${KL%.kl}.out
    RES=${KL%.kl}.res

    kl "$KL" >"$RES"
    if ! cmp "$OUT" "$RES"; then
      echo "FAIL $KL"
      echo "diff:"
      diff -u "$OUT" "$RES"
      # rm "$RES"
      exit 1
    else
      echo "PASS $KL"
      rm "$RES"
    fi

    shift

  done

This script expects, for a given KL source file :file:`test.kl`, for there
to be a corresponding file :file:`test.out` with the correct output.  If
this script is placed in a file such as :file:`verify.sh`, you can then run::

  ./verify.sh test.kl

to see whether the output of :file:`test.kl` matches the contents of
:file:`test.out`.

More complex scripts can be written for testing.  The following example Python
code runs the KL tool and compares the output against a reference file. The
reference file will be generated if it does not exist, or the :code:`--update
True` option is set.

.. code:: python

  # Import system modules
  import sys, string, os
  import argparse
  import subprocess

  # Parse the commandline args.
  parser = argparse.ArgumentParser()
  parser.add_argument('klFile', help = "The kl File to use in the test")
  parser.add_argument('--update', required=False, help = "Force the update of the reference file")
  args = parser.parse_args()

  klFile = args.klFile
  cmdstring = "kl.exe " + klFile

  # Call the KL tool piping output to the output buffer. 
  proc = subprocess.Popen(cmdstring,stdout=subprocess.PIPE)
  output = ""
  while True:
    line = proc.stdout.readline()
    if line != '':
      output += line.rstrip()
    else:
      break
  referencefile = os.path.splitext(klFile)[0]+'.txt'
  if not os.path.exists(referencefile) or args.update == 'True':
      with open(referencefile, 'w') as f:
        f.write(output)
      print "Reference Created"
  else:
    referenceTxt = str(open( referencefile ).read())
    if referenceTxt == output:
      print "Test:" + klFile + " Passed"
    else:
      print "Test:" + klFile + " Failed"


Place the python code above in a python file called (for example)
:file:`pythonTester.py`. You would then run it passing a unit test KL source
file to test against.

.. code::

  python pythonTester.py test.kl

To update test results, run the tester with the --update argument.

.. code::

​  python pythonTester.py test.kl --update

Setting up a unit testing framework for your custom extensions and running
them regularly will help catch changes that might break your APIs.

Indices and Tables
---------------------

* :ref:`genindex`
* :ref:`search`
