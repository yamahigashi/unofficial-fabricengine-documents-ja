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

.. _GETTINGSTARTED_STANDALONE:

Launching the Fabric Standalone (canvas.py)
-----------------------------------------------------

.. versionadded:: 2.2.0

As of 2.2.0 the Fabric Standalone has been converted to Python. ``canvas.py`` is a python app that requires a 64 bit Python 2.7 installed in your system (as defined by the VFX Reference Platform). OS X and most common Linux distributions already ship with it (if your Linux distribution doesn’t have a Python 2.7.x installation or has an older one, you will need to install it, either with your typical package manager or manually). Be aware, though, that Python 2.7 needs to be the default version in the system in order for the environment.sh shell script to work properly. If Python 2.7 is not your default version you will need to modify the environment.sh or prompt.bat scripts to pick up the correct ``PYTHONPATH``. In the case of Windows, just install Python 2.7 and make sure your PATH enviroment variable includes the directory of your Python distribution.

.. note::

  On OSX it is currently necessary to use the default system Python. If you've installed a newer version via homebrew or another package manager you will need to ensure that you're using the system version found in ``/usr/bin/python`` when you run the Fabric Standalone.

|FABRIC_PRODUCT_NAME| relies on several environment variables. For convenience, a :dfn:`canvas.bat` (Windows) and :dfn:`canvas.sh` (Linux / OSX) files are provided to run canvas.py automatically. Double clicking these files will internally call the :dfn:`environment.bat` (Windows) or :dfn:`environment.sh` (Linux / OSX) to set up the environment variables and then launch ``python bin/canvas.py``. A shortcut to the :dfn:`canvas.bat` or :dfn:`canvas.sh` file can also be made to make launching the application more accessible for users.

Alternatively, you can define these environment variables manually following the procedures described below.

On Windows:

  Open the :dfn:`prompt.bat` file to set up all the environment variables for you. If you are using `mingw <http://www.mingw.org>`_ / `Git Bash <https://msysgit.github.io/>`_ you can also source the :dfn:`environment.sh` file instead.

  .. code-block:: bash

      source environment.sh

On Windows all further steps in the documentation that involve setting and exporting environment variables assume you are using *mingw* or *Git Bash*.

On Linux / OSX:

  To setup all required environment variables simply source the :dfn:`environment.sh` file within a terminal session.

  .. code-block:: bash

      source environment.sh

``canvas.py`` can be launched from the terminal/command prompt after sourcing the ``environment.sh`` or running the ``prompt.bat`` by just typing ``canvas.py`` in the command-line:

  .. code-block:: bash

      canvas.py

Or by invoking it with python: ``python bin/canvas.py``:

  .. code-block:: bash

      python $FABRIC_DIR/bin/canvas.py

.. note:: The first time any |FABRIC_PRODUCT_NAME| utilities / plugins are launched, the KL compiler will compile and optimize all provided KL extensions for the target platform on multiple CPUs. This may take a few minutes. You will also get a Fabric Licensing dialog. Check the next section for instructions on license installation.
