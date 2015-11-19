.. _DG.envvars:

Environment Variables
=====================

There are certain environment variables that can affect how Fabric behaves. These are not **all** officially supported.

Fabric Core
-----------

FABRIC_CUDA_LOG
+++++++++++++++

If set, the Core will output verbose logging info whenever a KL operator is passed into the CUDA codegen. In addition it will output cuda.ll and cuda.ptx files containing the IR and PTX of the last KL operator into the current directory. In order to ensure that the CUDA operator is actually compiled this flag also causes the Core to bypass the cache for GPU operators only.

FABRIC_DEBUG
++++++++++++

This controls whether or not debug info will be output into compiled KL code and can take the following values:

  - 1 (the default): The Core will output Dwarf debug info into all compiled KL code, allowing code debugging with gdb, lldb or tools based on either. This debug info is also consumed by other KL features such as KL stack traces for KL exceptions and in the crash handler.

  - 2: The same will occur but the Core will also open a control port that will accept connections from our zBug debugger front-end to provide additional debug data such as KL source code. Note that the zBug debugger is currently only supported on Linux.

  - 0: There is no debug info output into compiled KL code. There should be no reason to use this value unless errors are found in the KL debug info generation that require disabling it temporarily.

FABRIC_ENABLE_CRASH_HANDLER
+++++++++++++++++++++++++++

When greater than zero, the Core will attempt to catch anything that would normally cause the process to crash and exit (such as a SIGSEGV on Linux or an Access Violation on Windows) in order to provide a stack trace including KL symbols before exiting. If the crash occurs within KL, the crash handler will attempt to use information from LLVM to determine any KL symbol names in the stack trace where possible. If combined with FABRIC_DEBUG above, the crash handler will use the debug info to resolve all KL symbols in the stack trace. The crash handler is currently unsupported on OSX.

FABRIC_EXTS_PATH
++++++++++++++++

Specifies a list of folders separated by ":" (on POSIX) or ";" (on Windows) where the Core should search for extensions.

FABRIC_FEATURE_CUDA_COMPUTE
+++++++++++++++++++++++++++

If non-zero this will cause the Fabric Core to attempt to load the CUDA and NVVM dynamic libraries on systems with supported Nvidia hardware in order to enable GPU compute. The libraries must be available in default system library paths or provided via the PATH environment variable on Windows or LD_LIBRARY_PATH on Linux. Error information will be printed to the console if the Core is unable to bind to the CUDA libraries when this variable is set.

FABRIC_GUARDED_GPU
++++++++++++++++++

.. versionadded:: 1.15.0
  FABRIC_GUARDED_GPU

If non-zero this will enable compiling GPU KL code in guarded mode. By default this is disabled even if normally compiling code in guarded mode as it slows down GPU compilation considerably, however it can be enabled explicitly in cases where extra debuggability of GPU code is required.

FABRIC_CACHE_DIR
++++++++++++++++

.. versionadded:: 1.13.0
  FABRIC_CACHE_DIR

This specifies the folder where cached KL code should be stored (LLVM IR, object code and potentially CUDA PTX). The defaults for these are:

Linux/OSX:

- ~/.fabric-engine/.private

Windows:

- %APPDATA%\\Fabric Engine\\.private

FABRIC_CACHE_MAX_AGE_DAYS
+++++++++++++++++++++++++

.. versionadded:: 2.0.0
  FABRIC_CACHE_MAX_AGE_DAYS

This specifies the maximum age, in days, of cached KL code that should be stored (LLVM IR, object code and potentially CUDA PTX).  The age is computed based on the last time the cache file was accessed.  The default is 30 days.

.. warn::

  Setting FABRIC_CACHE_MAX_AGE_DAYS too small may cause extensions to be recompiled on each startup!

FABRIC_CACHE_MAX_SIZE_MB
++++++++++++++++++++++++

.. versionadded:: 2.0.0
  FABRIC_CACHE_MAX_SIZE_MB

This specifies the maximum amount, in megabytes, of cached KL code that should be stored (LLVM IR, object code and potentially CUDA PTX). The default is 250 megabytes.

.. warn::

  Setting FABRIC_CACHE_MAX_SIZE_MB too small may cause extensions to be recompiled on each startup!

FABRIC_KL_ERROR_TRACE
+++++++++++++++++++++

Setting this to zero tells the Core to not output a KL stack trace whenever a KL exception is encountered (either a KL throw(), setError(), or dumpstack()). The only reason to disable this would be to work around any errors found in the stack generation code.

FABRIC_KL_HEAP_DEBUG and FABRIC_MEMORY_DEBUG
++++++++++++++++++++++++++++++++++++++++++++

Setting these to different non-zero values prints different types of detailed internal memory allocation information to the console. This information isn't intended for users and is probably not useful to them.

FABRIC_LOAD_ALL_EXTS
++++++++++++++++++++

When set to a non-zero value the Fabric Core will bypass the normal extensions mechanism of registering an extension's location on startup but only loading each extension when requested and will instead immediately load all extensions that it encounters at startup.

FABRIC_LOG_FILE
+++++++++++++++

If set, the Core will synchronously log all output to the specified log file. This includes everything that the Core normally outputs to the console such as errors and report() statements.


FABRIC_LOG_LEVEL
++++++++++++++++

If set the Core will output log messages only at the specified level or below. The default log level is 3, at log level 4 some additional debug information will also be displayed.

FABRIC_NO_INLINE
++++++++++++++++

Specifies that the Core should not inline KL functions explicitly marked as 'inline'. This is useful only for testing purposes.

FABRIC_OPT_TYPE
+++++++++++++++

When specified, KL code optimization will depend on the value of this variable. The values used here are the same as those specified in FabricCore.h:

- 0: KL code will first be compiled unoptimized so that it's usable immediately. Optimization will occur on background threads and optimized code will be swapped in to replace the unoptimized code as it becomes ready.

- 1: KL code will be optimized synchronously on the main thread before being compiled. Startup will take longer in this case and unoptimized code will never be run.

- 2: KL code will not be optimized. This can be useful when combined with FABRIC_DEBUG in order to ensure that all KL function calls exist in the resulting machine code.

This value does not apply for the KL tool, which has its own command-line options to control this.

FABRIC_TRACE_OPERATORS
++++++++++++++++++++++

When greater than zero all operators in KL print an ENTER/LEAVE pair to the console when entering and when leaving the function. This was primarily used in debugging as a coarse means of pinpointing which operator is responsible for a given crash but is becoming less important now that proper debug info exists.

FABRIC_VERBOSE_IR_CACHE
+++++++++++++++++++++++

If non-zero, the Core will output additional information into the IR cache. It will output the source KL, the unoptimized IR for the given KL, and finally the optimized IR once optimization is complete. The files are named by cache key as with the existing cache files.

Fabric Canvas
--------------------

FABRIC_DFG_PATH
++++++++++++++++++++++++

A colon-separated (semicolon on Windows) path of additional directories to search for Canvas presets.

FABRIC_CANVAS_JSON_STRICT
+++++++++++++++++++++++++++++++

Setting this variable to 1 will cause Canvas to export its JSON representations for graphs and functions using a strict JSON format; by default, Fabric will export using a loose format where newlines and other control characters will not be escaped.  This loose format is better for version control but not compatible with strict JSON parsers.

FABRIC_NO_EXPIRY_DIALOG
+++++++++++++++++++++++++++++++

Normally when canvas loads it will pop a warning window if the user's license expires in less than a month. Setting this variable to 1 will cause Canvas to skip this window and instead print the warning to the command line.

SPLICE API
---------------

FABRIC_NODES_PATH
+++++++++++++++++

This is used by the SpliceAPI to resolve file paths. If a file path is provided as a relative path to any of the splice commands, it will try to resolve the filePath based on the list of directories in the FABRIC_NODES_PATH. You can separate directories using a semicolon or a colon.

FABRIC_SPLICE_DISABLE_LOG
++++++++++++++++++++++++++

If non-zero this will disable printing of ordinary ("info") log messages from the Fabric DCC plugins.  This does not apply to warning and error messages, and does not apply to Fabric Canvas messages of any sort (which use the usual Fabric Core logging mechanism).

FABRIC_SPLICE_UNGUARDED
+++++++++++++++++++++++

If non-zero then KL code will be compiled and run in "unguarded" mode, meaning that array out-of-bounds accesses and object NULL pointer references will not be checked. This allows for faster code at the expense of potential crashes on programmer error in the KL code.

Fabric Licensing
----------------

FABRIC_LICENSE_DIR
++++++++++++++++++

Specifies the folder that Fabric will use to search for node-locked .lic license files.
