.. _DG.zbug:

Using zBug
==========

Setting up the Environment
--------------------------

By default KL code is compiled with full optimization and with no debug info in order to reduce memory use as much as possible and to make the KL code run as fast as possible. However in order to debug you will need at the very least to include debug info with your KL code, and in order to take full advantage of all debugging features you will likely want to disable optimization. Fortunately both of these are automatically done for you when launching a Fabric application from zBug.

When a Fabric application is launched from zBug the following environment variables are automatically set:

.. code-block:: none

  export FABRIC_DEBUG=2
  export FABRIC_OPT_TYPE=2

This will enable debug info and disable optimizations. For more detailed information on what these environment variables do you can see this section: :ref:`DG.envvars`.

Launching an Application
------------------------

The current version of zBug requires launching the Fabric application within zBug in order to provide debugging capabilities. For most applications this is as simple as pre-pending zBug to the command being run:

.. code-block:: none

  zBug <application> [<arg1> <arg2> ...]

For example debugging a Fabric Engine Python application could be launched like this:

.. code-block:: none

  zBug python MyFabricApp.py

Debugging Maya
++++++++++++++

Maya under Linux can't be launched as above however Maya provides a -d command-line option that allows it to be started within a debugger. Running Maya inside zBug is as simple as providing this option and pointing it to zBug:

.. code-block:: none

  maya -d zBug

Attaching to a Running Application
++++++++++++++++++++++++++++++++++

If zBug is launched without any command-line parameters it will look for a Fabric application running in debug mode (FABRIC_DEBUG=2) and automatically connect to this process if it exists. The process is located via a PID file found in the user's Fabric application data folder.

.. note:: Since in this case Fabric will start before zBug, you will need to manually set `export FABRIC_DEBUG=2` and `export FABRIC_OPT_TYPE=2` before starting the application, otherwise zBug will not see the KL debugging symbols.

If there is more than one Fabric application running on the system at a given time then the user can supply a -p parameter to zBug to specify the process ID of the Fabric process to connect to. In the case of Fabric running within a DCC, this process ID will normally be that of the DCC itself.

.. code-block:: none

  zBug -p <pid>

Once connected with zBug debugging can occur as it would for a process launched from within zBug. Simply closing zBug will disconnect from the running process and allow execution to continue normally.

Depending on the version of Linux you're using you may need to run zBug as root if you're attaching to a process. You will see an error message like this if you try to run as a normal user:

.. code-block:: none

  error: attach failed: Operation not permitted

This is a security measure of certain distros and not a limitation of zBug.

User Interface
--------------

The zBug user interfaces tries to keep its defaults as simple as possible while leaving access to more advanced debugging features open to those who need them. The interface is written in Python and uses PySide for its UI elements. As such it is very configurable, both from a source code level as well as from within the UI itself.

Inside each subwindow in the UI (except for the source code window, which is fixed) there is a button at the top right corner of the subwindow that will cause it to pop out so that it can be moved around the screen. With this a user is able to configure zBug to have exactly the windows that are most important in the places that make the most sense.

Interrupts and Breakpoints
++++++++++++++++++++++++++

When debugging an application in zBug the application may either be running or else in an interrupted or breakpoint state (we'll refer to this as being stopped). Controls within a stopped state are the same, however most of the functionality in zBug is disabled while the application is running.

In order to interact with a running application a user will first have to click the Interrupt button in order to stop execution. When zBug enters an interrupted or breakpoint state the UI will update all relevant sections to indicate where the program has stopped. If there is source code available for the current position the :ref:`DG.zbug.source` section will be updated to display this source code and the current line will be highlighted in yellow. The interface will update in the same way if a breakpoint is hit, and the line currently breakpointing will also be highlighted in yellow.

Source code will not exist for all possible execution points within a running Fabric application, since the C++ code for the closed Fabric application itself is not available to end users, and neither are code sections and function calls that live within the DCCs. The :ref:`DG.zbug.source` subwindow will indicate if the source code for the given frame is available or not. However all KL code used in your application should always be available.

Any breakpoints in the source code currently loaded will show up as a red line in the source file. A complete list of current breakpoints across all source files is available in the :ref:`DG.zbug.breakpoints` subwindow.

UI Sections
+++++++++++

.. _DG.zbug.breakpoints:

Breakpoints
^^^^^^^^^^^

The breakpoints window lists all breakpoints currently set in the program. Clicking on any breakpoint found here will open up the source file and line where the breakpoint is set in the :ref:`DG.zbug.source` window.

In the current release there is an extra internal breakpoint that always shows up in this list and can simply be ignored. It will be hidden in a future version.

Control Toolbar
^^^^^^^^^^^^^^^

The topmost area of zBug holds the process control toolbar and contains buttons to control execution and process flow of the application being debugged.

- Start: When a zBug session is opened this is the only button accessible and clicking it will launch the process being debugged.

- Interrupt: Once the debugged application is running, clicking Interrupt at any time will stop its execution and return control to zBug. At that point you can browse any code that's been loaded to that point, you can view where the execution has stopped by looking at the :ref:`DG.zbug.stack` or :ref:`DG.zbug.threads` and you can set breakpoints.

- Continue: When in a stopped state you may click Continue to tell the application to continue running.

- Step In: When in a stopped state you may use Step In to bring execution inside the function currently being highlighted in the :ref:`DG.zbug.source` subwindow. If it's not possible for execution to go inside the function on the currently highlighted line (for example if the line is a simple variable assignment) then behavior is the same as for Step Over.

- Step Over: When in a stopped state you may Step Over the current instruction to allow execution to continue down the current file. Step Over does not necessarily take you to the next line as there may be several instructions that need to execute on the line that's currently selected, for example the line :code:`for (Integer i=0; i<5; i++) {` contains an assignment, a comparison, and a variable increment, and each of these will be processed individually before moving on to the next line in the KL file.

- Step Out: When in a stopped state you may Step Out of the current function into its calling function. This will bring execution to the current function's caller as seen in the :ref:`DG.zbug.stack`.

Disassembly
^^^^^^^^^^^

This window will probably not be used by most users but provides access to the assembly code for the source code visible in the currently selected frame.

LLDB
^^^^

This window gives a standard LLDB console, opening up access to any LLDB functionality that is not provided through the zBug UI. It's not expected that users will need to enter manual LLDB commands but more advanced users may want access and it's provided for that reason. A tutorial on basic LLDB commands is available here: `LLDB Tutorial <http://lldb.llvm.org/tutorial.html>`_.

Locals
^^^^^^

In this section all local variables found in the scope of the current stop position will be listed, whether in C++ code or KL. Variables with some structure (for example KL :code:`struct` and :code:`object`) can be unfolded using the '+' symbol next to the variable name to inspect values at each level of the type's hierarchy.

Currently for certain KL types such as :code:`object` or variable arrays you will see type members that don't form part of the type that you defined in KL code. These refer to internal KL data that isn't normally seen by users but is useful for Fabric Core team developers when working on the KL compiler. These may be hidden in a future version but for now show up in the UI and can simply be ignored.

Support is also missing for some KL types, specifically dictionaries, interfaces, and Map-Reduce producers. These will be added in an upcoming release.

Output
^^^^^^

The output window displays any output that would normally be printed to the command-line in a console application.

Registers
^^^^^^^^^

Most users will not make use of this subwindow but it provides access to the CPU register values in the currently highlighted frame.

.. _DG.zbug.source:

Source Code
^^^^^^^^^^^

The source window is the main window of the zBug application and displays the source code (if available) for the currently selected frame in the :ref:`DG.zbug.stack` window.

.. _DG.zbug.stack:

Sources List
^^^^^^^^^^^^

The sources list in zBug defaults to only displaying KL code that's been received from the debugged application. Clicking on any KL source file in this list will open up its source code into the :code:`DG.zbug.source` window, allowing the user to set or unset breakpoints there.

Stack
^^^^^

This window provides a stack trace for the currently selected thread. Clicking on any function name in the stack trace will take you to the source code for that function (if available).

.. _DG.zbug.threads:

Threads
^^^^^^^

All threads found in the current application will be listed here and clicking on any one will open up its current stack trace into the :ref:`DG.zbug.stack` window.


