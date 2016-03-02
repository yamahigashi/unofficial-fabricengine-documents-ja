Building the Sample Extension
=======================================

To make it easy to build your first extension, the |FABRIC_PRODUCT_NAME| installer automatically installs a sample extension that you should start with.

Install Developer Tools
----------------------------------

The first step is to install the appropriate developer tools for your platform.  At a very minimum, you must install the C++ compiler for your platform as well as the :command:`scons` build tool.

The instructions for installing developer tools vary by platform:

- On Windows, install Visual Studio.  Visual Studio 2013 is the officially supported version, but other versions may work as well.

- On Linux, installed the Clang++ or the GNU C++ compiler.  Usually this means installing a package such as ``clang`` or ``g++`` (on Ubuntu).

- On OS X, install Xcode 5 (we use 5.0.1), available from the OS X app store.

Installing the :command:`scons` tool also varies by platform.

- On Windows, download and unpack the Zip file for Scons from from http://scons.org.  Then open a command prompt, go to the directory containing scons, and run :command:`python setup.py install`.  In the directory :file:`c:\Python27\Scripts`, rename the file :file:`scons.py` to :file:`scons`.  Finally, ensure that :file:`c:\Python27\Scripts` is in your :envvar:`PATH` environment variable.

- On Linux, install :command:`scons` from your package manager, eg. :command:`apt-get install scons`

- On OS X, download and unpack the Zip file for Scons from from `http://scons.org/ <http://scons.org/>`_.  Then open a Terminal, go to the directory containing scons, and run :command:`python setup.py install`.

You can verify that :command:`scons` is installed by opening a command prompt, going to an empty directory and running :command:`scons`.  You should see output similar to the following:

.. code-block:: console

  scons: *** No SConstruct file found.
  File "/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/scons-2.2.0/SCons/Script/Main.py", line 905, in _main

Copy the Sample
-------------------------

The next step is to make a copy of the directory containing the sample extension.  The sample extension is located in the directory :file:`$FABRIC_DIR/EDK/Samples/HelloWorld`, where :code:`$FABRIC_DIR` is the value of the :envvar:`FABRIC_DIR` environment variable that is set by the installer.  Make a copy of the directory and all of its contents using, for instance, the :command:`cp -r` command.

Build the Sample
----------------------------

From a command prompt in the directory containing your copy of the sample, simply run :command:`scons`.  You should see output similar to the following:

.. code-block:: console

  scons: Reading SConscript files ...
  Running SCons with -j8
  scons: done reading SConscript files.
  scons: Building targets ...
  /Users/pzion/Fabric/SceneGraph/stage/Darwin/x86_64/Release/Tools/kl2edk -o HelloWorld.h HelloWorld.kl
  Compiling       HelloWorld.cpp
  SharedLibrary   libHelloWorld-Darwin-x86_64.dylib
  scons: done building targets.

Test the Sample
--------------------------

In the same directory, run :command:`python test.py`.  You should see output similar to the following:

.. code-block:: console
  
  [FABRIC:MT] |FABRIC_PRODUCT_NAME| version |FABRIC_VERSION|
  [FABRIC:MT] Registered extension {HelloWorld} in directory: .
  [FABRIC:MT] Registered extensions {BadVersion,UnitTest,FabricALEMBIC,FabricBULLET,FabricCIMG,FabricEXR,FabricFBX,FabricFILESTREAM,Geometry,FabricHDR,Images,FabricLIDAR,Math,FabricOBJ,FabricOPENCV,FabricOGL,FabricPNG,RTR,RTRAdaptors,FabricStringTools,FabricTEEM,FabricTGA,FabricVIDEO} in directory: /Users/pzion/Fabric/SceneGraph/stage/Darwin/x86_64/Release/Exts
  [FABRIC:MT] Compiled extension HelloWorld in 0.572ms
  [FABRIC:ID] Optimized extension HelloWorld in 7.398ms
  [FABRIC:MT:node:op] KL: Enter entry
  [FABRIC:MT:node:op] HelloWorld: Extension: Enter GetHelloWorldString
  [FABRIC:MT:node:op] HelloWorld: Extension: Leave GetHelloWorldString
  [FABRIC:MT:node:op] KL: GetHelloWorldString returned: Hello, world!
  [FABRIC:MT:node:op] KL: Leave entry
  Python got: Hello, world!

The output shows output from KL code that calls the function in the extension as well as from the extension code itself.  We will go through in detail how the sample extension works in the next section.
