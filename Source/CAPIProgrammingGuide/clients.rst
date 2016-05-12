


.. highlight:: c

.. _clients:

Clients and the Application Lifecycle
=====================================

Before an application can do anything meaningful with CAPI it must first create a :dfn:`client`.  Similarly, before an application exits it must release the client.  This chapter explains these steps in detail.

Creating a Client
--------------------

In order to work with CAPI a client object must be created.  Client objects represent a space of objects, types and programs, and a given application can create multiple client objects to represent multiple Fabric applications.  However, most fabric applications will only need a single client.

A client object is created through a call to one of the following functions::

  // Creating a client object - C
  FEC_ClientRef FEC_ClientCreate(
    FEC_ClientReportCallback reportCallback,
    void *reportUserdata,
    ...
   );

  // Creating a client object - C++
  FabricCore::Client::Client(
    ReportCallback reportCallback,
    void *reportUserdata,
    ...
    );

The required parameter ``guarded`` is a boolean indicating whether array accesses should be guarded (ie. bounds-checked).  Setting this flag to a true value will slightly decrease runtime performance but will also provide errors when any array accesses are out-of-bounds.

The optional parameters ``reportCallback`` and ``reportUserdata``, if present, are a C function (or a "static" C++ function) to be called with any report statements the Fabric Core wishes to have displayed.  Such report statements are usually the result of ``report`` calls within KL code or runtime errors (such as out-of-bounds errors).  The function must have the prototype::

  // Report callback function prototype - C and C++
  void ReportCallbackFunction(
    void *reportUserdata,
    char const *stringData,
    uint32_t stringLength
    );

The provided value of ``reportUserdata`` will be passed as the first parameter to the provided function.  The ``stringData`` and ``stringLength`` parameters will be a pointer to a C string representing the message to report (without newline) and the length of the string, respectively.

If a ``reportCallback`` is not provided (or is ``NULL``) then the Fabric Core will output the report statements to standard output.

Releasing Clients
--------------------

Once you are done using a client, it must be released.  Clients are reference-counted objects, so in C++ they will be automatically released then they go out of scope.  In C, you must make a manual call to :c:func:`FEC_RefRelease` to release the client.

Manipulating Clients
--------------------

Once a client is created, it can be manipulated using the :ref:`client API functions <CAPI.clients.api-reference>`.

.. _CAPI.clients.api-reference:

.. _CAPI.clients.api-reference-c:

API Reference - C
-----------------

There is also an :ref:`CAPI.clients.api-reference-cpp`.

.. c:type:: FEC_ClientRef

  A reference to a CAPI client.  These references are returned when creating a client with :c:func:`FEC_ClientCreate` and must be eventually released using :c:func:`FEC_RefRelease`.




.. c:type:: FEC_ReportSource

  The source type of a report line coming from the Fabric Core.  Can be one of:

  - ``FEC_ReportSource_System``
  - ``FEC_ReportSource_System``

  These values can also be used as as bits to mask or unmask these values using the :c:func:`FEC_ClientSetReportSourceMask` function.  As such, the following masks are also provided:

  - ``FEC_ReportSource_NONE``
  - ``FEC_ReportSource_ALL``




.. c:type:: FEC_ReportLevel

  The severity level of a report line coming from the Fabric Core.  Can be one of:

  - ``FEC_ReportLevel_Error``
  - ``FEC_ReportLevel_Warning``
  - ``FEC_ReportLevel_Info ``
  - ``FEC_ReportLevel_Debug``




.. c:type:: FEC_ClientReportCallback

  The type of a report callback function associated with a client.  Such a function must have the prototype::

    void ClientReportCallback(
      void *reportUserdata,
      FEC_ReportSource source,
      FEC_ReportLevel level,
      char const *lineCStr,
      uint32_t lineSize
      );




.. c:type: FEC_ClientOptimizationType

  A type used to indicate which KL background optimization mode to use when creating the client using :c:func:`FEC_ClientCreate`.  It can have one of three values:

  FEC_ClientOptimizationType_Background

    Optimize in the background (the default)

  FEC_ClientOptimizationType_Synchronous

    Optimize KL code synchronously.  Slows program startup but optimized code is used immediately.

  FEC_ClientOptimizationType_None

    Do not optimize KL code




.. c:type: FEC_ClientLicenseType

  A type used to indicate which type of license to request when calling :c:func:`FEC_ClientCreate`. It can have one of two values:

  FEC_ClientLicenseType_Compute

    A command-line compute-only license suitable for render farms or other computation (the default).

  FEC_ClientLicenseType_Interactive

    A full interactive license for use in Splice and other interfaces.

  FEC_ClientLicenseType_Developer

    A developer license grants all the rights of an interactive license in additional to the ability to export obfuscated KL source code.




.. c:function:: FEC_ClientRef FEC_ClientCreate(FEC_ClientReportCallback reportCallback, void *reportUserdata, int guarded, int traceOperators, FEC_ClientOptimizationType optimizationType)

  Create a new Fabric Platform core client.

  :param reportCallback: The callback function for report statements coming from the |FABRIC_PRODUCT_NAME| core
  :param reportUserdata: The userdata for report statements; passed to reportCallback
  :param guarded: Whether to throw out-of-bounds exceptions for array accesses in KL
  :param trapOnThrow: Whether to trap when an exception is thrown from KL
  :param traceOperators: Whether to add automatic tracing report statements to operators
  :param optimizationType: The KL optimization type for the client
  :returns: The reference to the new client, or FEC_NULL_REF on error.




.. c:function:: FEC_ClientRef FEC_ClientBind(FEC_ClientReportCallback reportCallback, void *reportUserdata, char const *contextID)

  Bind to an existing client with a given client ID.  This allows multiple CAPI programs to work with the same client state inside the core of |FABRIC_PRODUCT_NAME|.

  :param contextID: (C string) The context ID to bind to.  The context ID of a client can be obtained with the :c:func:`FEC_ClientGetContextID` function.
  :returns: A new reference to the existing client with the given context ID, or FEC_NULL_REF on error.




.. c:function:: void FEC_ClientSetReportCallback(FEC_ClientRef clientRef, FEC_ClientReportCallback reportCallback, void *reportUserdata)

  Set the report callback for the client.  This will replace whatever report callback was already there.  Passing NULL for reportCallback will cause no report callbacks to be fired back to the client.

  :param clientRef: The client
  :param reportCallback: The new report callback
  :param reportUserdata: The userdata to pass to the report callback when fired




.. c:function:: void FEC_ClientEnableRuntimeLogging(FEC_ClientRef clientRef)

  Enable runtime logging for the client.  Runtime logging is what causes the report statements from KL programs to be fired as report callbacks to the client.  By default, runtime logging is enabled.

  :param clientRef: The client




.. c:function:: void FEC_ClientDisableRuntimeLogging(FEC_ClientRef clientRef)

  Disable runtime logging for the client.  Runtime logging is what causes the report statements from KL programs to be fired as report callbacks to the client.  By default, runtime logging is enabled.

  :param clientRef: The client




.. c:function:: void FEC_ClientSetReportSourceMask(
  FEC_ClientRef clientRef,
  FEC_ReportSource sourceMask
  )

  Set the source mask for report lines coming from the Core.  This allows you, for instance, to only receive user report statements.

  .. note::

    Report line filtering could also happen at the client end, but it is generally more performant to allow the Core to perform the filtering.




.. c:function:: void FEC_ClientSetReportLevelMax(
  FEC_ClientRef clientRef,
  FEC_ReportLevel levelMax
  )

  Set the maximum severity level for report lines coming from the Core.  This allows you, for instance, to only receive report lines that are warnings or errors, and to filter out the info and debug lines.

  .. note::

    Report line filtering could also happen at the client end, but it is generally more performant to allow the Core to perform the filtering.




.. c:function:: char const *FEC_ClientGetContextID(FEC_ClientRef clientRef)

  Get the context ID (a C string) associated with the client.  This string can be used in a call to :c:func:`FEC_ClientBind` to get a new reference to the client.

  :param clientRef: The client
  :returns: The client ID as a C string




.. c:function:: void FEC_ClientStartInstrumentation(FEC_ClientRef clientRef)

  Start instrumentation of the client.  If instrumentation has already started, this function restarts it.

  :param clientRef: The client




.. c:function:: FEC_Variant FEC_ClientStopInstrumentation_Variant(FEC_ClientRef clientRef, char const *resultType)

  Stop instrumentation of the client and return the instrumentation results.  The format of the results depends on the value of the string *resultType*, and can be one of `"timing"`, `"simpleTiming"`, `"simpleTimingNoExternal"` and `"raw"`.

  :param clientRef: The client
  :param resultType: The result format to use
  :returns: The instrumentation data as a variant




.. c:function:: void FEC_ClientLoadExtension(FEC_ClientRef clientRef, char const *extName, int reload)

  Load an extension if it hasn't already been loaded.

  :param clientRef: The client
  :param extName: The name of the extension to load (a C string)
  :param reload: If set to true to extension's KL code will be reloaded from disk.




.. c:function:: void FEC_ClientRegisterExtensions(FEC_ClientRef clientRef, char const *pathname)

  Register extensions below the specified directory

  :param clientRef: The client
  :param pathname: The pathname in which to search for extensions




.. c:function:: void FEC_ClientExportExtension(FEC_ClientRef clientRef, char const *extNameCString, char const *outputFile)

  Export an extension in obfuscated format to the specified file.

  :param clientRef: The client
  :param extNameCString: The name of the extension to export.
  :param outputFile: The name of file to create.
  :param compress: Compress the output file or leave it in plain text




.. c:function:: void FEC_ClientSetLogWarnings(FEC_ClientRef clientRef, int logWarnings)

  Tell the core whether to log warnings produced by the client.  Warnings are for deprecated behaviors on which the client is depending.  By default, warnings are *not* logged.

  :param clientRef: The client
  :param logWarnings: Whether to log warnings




.. c:type:: FEC_ClientStatusCallback

  The type of a status callback function associated with a client; see :c:func:`FEC_ClientSetStatusCallback`.  Such a function must have the prototype::

    void ClientStatusCallback(
    void *userdata,
    char const *destData, uint32_t destLength,
    char const *payloadData, uint32_t payloadLength
      );




.. c:function:: void FEC_ClientSetStatusCallback(FEC_ClientRef clientRef, FEC_ClientStatusCallback callback, void *userdata)

  Set the status callback associated with the client.  Status callbacks are used for KL code to communicate status messages back to the client.

  :param clientRef: The client
  :param callback: The status callback to set
  :param userdata: The userdata to pass to the status callback when called




.. c:function:: void *FEC_ClientGetStatusUserdata(FEC_ClientRef clientRef)

  Returns the status userdata associated with the client, specifically the last value set by :c:func:`FEC_ClientSetStatusCallback`.

  :param clientRef: The client
  :returns: The status userdata associated with the client




.. c:function:: void FEC_ClientQueueStatusMessage(FEC_ClientRef clientRef, char const *destCString, char const *payloadCString)

  Queue a status message to be sent to all the clients with the current client ID (including the given client).  This allows a simple asynchronous communication mechanism between different parts of the same process that have references to the same client.

  :param clientRef: The client
  :param destCString: The destination string passed to the status callbacks; a C string
  :param payloadCString: the payload string passed to the status callbacks; a C string




.. c:function:: void FEC_ClientValidateLicense()

  Force license evaluation to happen immediately.  This can be used to re-evaluate the license after it has been saved to disk. Results of license validation will be sent to the clients logger and licensing data will be also sent as a status callback.

  :param clientRef: The client




.. c:function:: void FEC_ClientHasCommercialLicense()

  Returns true if the license currently in use is a paid commercial license. Always returns false if the license is not valid.

  :param clientRef: The client




.. c:function:: void FEC_SetStandaloneLicense(char const *licenseCString)

  Set the local license.

  :param licenseCString: The license in RLM format




.. c:function:: void FEC_FlagUserInteraction()

  Notify the Core of user activity.




.. c:function:: void FEC_ClientEnableBackgroundTasks(FEC_ClientRef clientRef)

  Enable background task execution for the client.  This should be called once the application has finished loading.  If this function is never called then background tasks (such as background optimization of KL code) will never execute.  You can call this function immediately when the client is created but startup performance may suffer.

  :param clientRef: The client




.. c:function:: int FEC_ClientIsBackgroundOptimizationInProgress(FEC_ClientRef clientRef)

  Check whether background optimization of KL code is currently in progress.

  :param clientRef: The client
  :returns: Non-zero if background optimization is in progress, zero otherwise




.. c:function:: void FEC_ClientAdoptCurrentGLContext( FEC_ClientRef clientRef )

  ***FIXME***.

  :param FEC_ClientRef clientRef: The client




.. c:function:: void FEC_ClientIdle( FEC_ClientRef clientRef )

  Tell the |FABRIC_PRODUCT_NAME| core that the main thread of the client is idle. Calling this function periodically gives the Core a chance to service callbacks that would otherwise not be serviced until the next time the Core is called.

  :param FEC_ClientRef clientRef: The client




.. c:function:: void FEC_ClientSupportsGPUCompute( FEC_ClientRef clientRef )

  Returns true if the |FABRIC_PRODUCT_NAME| core has found hardware support for GPU compute.

  :param FEC_ClientRef clientRef: The client




.. cpp:namespace:: FabricCore

.. _CAPI.clients.api-reference-cpp:

API Reference - C++
-------------------

There is also an :ref:`CAPI.clients.api-reference-c`.

.. cpp:type:: FabricCore::ClientOptimizationType

  A type used to indicate which KL background optimization mode to use when creating the client using the Client constructor.  It can have one of three values:

  FabricCore::ClientOptimizationType_Background

    Optimize in the background (the default)

  FabricCore::ClientOptimizationType_Synchronous

    Optimize KL code synchronously.  Slows program startup but optimized code is used immediately.

  FabricCore::ClientOptimizationType_None

    Do not optimize KL code




    .. cpp:function:: void registerExtensions(char const *pathnameCStr)

      Register extensions below the specified directory

      :param pathname: The pathname in which to search for extensions


