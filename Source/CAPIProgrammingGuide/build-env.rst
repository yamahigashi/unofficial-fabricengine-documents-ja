


.. _build-env:

The CAPI Build Environment
==========================

CAPI Prerequisites
------------------------------------------------

In order to use CAPI in your applications, you need a basic build environment.  This build environment is operating system-dependent as follows:

Windows
  You must have Visual Studio 2010 or later installed.  The "Express" version will work for building 32-bit CAPI applications and plugins, but the "Professional" version is required to build for 64-bit.  It may be possible to make CAPI work with non-Visual Studio compilers for Windows but it is not supported.

Linux
  You must have a C and/or C++ compiler installed.  CAPI is built and tested with a gcc version 4.x compiler but should work with any reasonably-modern version of gcc, and may also work with other C and C++ compilers as well, but this is not supported.

Mac OS X
  You must have installed Xcode 4.2 or later.

In addition, you must have any libraries that CAPI is dependent on installed on your system; however, these libraries are automatically satisfied as part of the Fabric Core installer process.

Finally, to build the CAPI samples without modification, you will need to have installed version 2.x.x of the :dfn:`SCons` build tool.  Scons distributions can be found at http://www.scons.org/; it can also be installed using your usual package management system for Linux or through MacPorts under Mac OS X (see http://www.macports.org/).

CAPI Files and the :envvar:`FABRIC_DIR` Environment Variable
-----------------------------------------------------------------

CAPI is installed on your system as part of the Fabric Engine install.  Your scripts should set the environment variable :envvar:`FABRIC_DIR` to the directory in which Fabric Engine is installed on your system.  During the install process, the CAPI files are copied under subdirectories of :file:`$FABRIC_DIR` (the value of the :envvar:`FABRIC_DIR` environment variable) as follows:

The CAPI header files are installed under the :file:`$FABRIC_DIR/include` subdirectory

The CAPI shared library is stored under the :file:`$FABRIC_DIR/lib` subdirectory

The CAPI sample source code is installed under the :file:`$FABRIC_DIR/CAPI/Samples` subdirectory

CAPI Library Linking
------------------------------------------------

When compiling against the CAPI you must define one of `FEC_STATIC` or `FEC_SHARED` depending on the type of CAPI library you will be using. If you will be linking statically with the CAPI library (using a .a file on Linux/OSX or a static .lib file on Windows) you must set `FEC_STATIC`. If you will be linking against a dynamic library (a .so file on Linux, .dylib on OSX or .lib + .dll on Windows) then you will defined FEC_SHARED.

Use of these defines allows for optimizing the API calls on Windows using dllimport and is maintained across Linux and OSX for consistency and future compatibility.

Building the Samples
------------------------------------------------

CAPI is provided with sample code that you can build and run on your system.  They can be found under the :file:`$FABRIC_DIR/CAPI/Samples` directory and currently consist of the following:


:file:`C/HelloWorld/...`
  The C interface version of the "HelloWorld" application

:file:`CPP/HelloWorld/...`
  The C++ interface version of the "HelloWorld" application

It is recommended to make a copy of the desired source code directory into another location before building a sample rather than building it in place.

To build a sample, you can simply run the :command:`scons` command from the command line for you platform within the copy of the sample directory.  It will produce an executable that can be run from the sample build directory.

Using CAPI With Other Build Systems and Projects
------------------------------------------------

In order to integrate the use of CAPI with another build system or project, you need to set a few options for the C/C++ compiler and linker.  Rather than give operating system- and compiler-specific instructions, we provide high level steps that are will need to be done for every C/C++ project or build system in which you wish to use CAPI.  They are:

Add the directory :file:`$FABRIC_DIR/include` to the include (header) search path.

Add the CAPI library (.lib/.so), located in :file:`$FABRIC_DIR/lib`.  The name of the shared library is operating system- and CAPI version-specific, but will generally contain the text :samp:`FabricCore-{X}.{Y}` where :samp:`{X}` and :samp:`{Y}` are the major and minor versions of the Fabric Core that are installed (eg. ``1.5``).

Be sure to include the CAPI header at the top of any C/C++ source files that use CAPI as follows:

.. code-block:: c

  #include <FabricEngine/FabricCore.h>



