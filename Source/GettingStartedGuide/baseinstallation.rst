.. _GETTINGSTARTED_BASEINSTALLATION:

Installing the |FABRIC_PRODUCT_NAME| archive
============================================================

|FABRIC_PRODUCT_NAME| runs on Windows 7 SP1 (or later) 64-bit, CentOS 6.x 64-bit, and Mac OS X 10.7 "Lion" (or later).

.. note:: Windows requires installing Visual Studio 2013 `redistributable <https://www.microsoft.com/en-us/download/details.aspx?id=40784>`_ if it is not already in the system.
 

|FABRIC_PRODUCT_NAME| is provided as a single archive for each platform. The archive contains:

* :strong:`bin` The binaries, including tools such as kl, kl2dfg and kl2edk
* :strong:`Documentation` The HTML and RST documentation
* :strong:`Exts` All officially supported KL extensions
* :strong:`include` The C/C++ headers for all available APIs
* :strong:`lib` The C/C++ libraries for all available APIs
* :strong:`Presets` The Fabric Canvas presets
* :strong:`Python` The python modules for each supported python version, including the Fabric Core python client
* :strong:`Resources` Auxiliary resources, for example content used by the Fabric Standalone samples
* :strong:`Samples` Example files for the supported DCCs and the Fabric Standalone
* :strong:`Sources` Source code for the KL extensions and Fabric Standalone
* :strong:`DCCIntegrations` The DCC Integrations for Fabric Engine
* :strong:`Tests` The source code of the core unit tests as well as the KL extension unit tests

To install |FABRIC_PRODUCT_NAME| on your machine simply extract the provided archive. You may use multiple installations next to each other, each directory name is unique and based on the specific version of |FABRIC_PRODUCT_NAME|.

Launching the Fabric Standalone
-----------------------------------------------------

|FABRIC_PRODUCT_NAME| relies on several environment variables. To make this easy for you a shell script / batch file for each supported operating system are provided.

On Windows:

  Opening the :dfn:`prompt.bat` file will set up all the environment variables for you. Alternatively, if you are using `mingw <http://www.mingw.org>`_ / `Git Bash <https://msysgit.github.io/>`_ you can source the :dfn:`environment.sh` file instead.

  .. code-block:: bash

      source environment.sh

On Windows all further steps in the documentation that involve setting and exporting environment variables assume you are using *mingw* or *Git Bash*.

On Linux / OSX:

  To setup all required environment variables simply source the :dfn:`environment.sh` file.

  .. code-block:: bash

      source environment.sh

To launch the Fabric Standalone, type canvas and hit enter in the shell of choice:

  .. code-block:: bash

      canvas

.. note:: The first time any |FABRIC_PRODUCT_NAME| utilities / plugins are launched, the KL compiler will compile and optimize all provided KL extensions for the target platform on multiple CPUs. This may take a few minutes. You will also get a Fabric Licensing dialog. Check the next section for instructions on license installation.
