
.. _functions:

Global functions 
=========================

The SPLICECAPI provides several global functions. These can be used to initialize the use of the library as well as control the licensing aspects of Fabric:Splice.

.. code-block:: c++

    namespace FabricSplice 
    {
      // Initialize needs to be called before calling into 
      // any other functionality of the SPLICECAPI.
      void Initialize();

      // Finalize needs to be called whenever the host application
      // is finished with accessing the SPLICECAPI.
      void Finalize();

      // Returns the major component of the Fabric version
      uint8_t GetFabricVersionMaj();

      // Returns the minor component of the Fabric version
      uint8_t GetFabricVersionMin();

      // Returns the revision component of the Fabric version
      uint8_t GetFabricVersionRev();

      // Returns the Core Version number as a string
      char const * GetFabricVersionVersionStr();

      // Returns the Splice Version number as a string
      char const * GetSpliceVersion();

      // Constructs a FabricCore client
      FabricCore::Client ConstructClient(int guarded = 1, FabricCore::ClientOptimizationType optType = FabricCore::ClientOptimizationType_Background);

      // Destroys a FabricCore client
      bool DestroyClient(bool force = false);

      // returns the ID for the client-context used by splice
      char const * GetClientContextID();

      // addExtFolder can be used to add paths to KL extension
      // resolval mechanism. First the folders listed in the
      // FABRIC_EXTS_PATH variable will be checked, followed
      // by the list of folders defined through this function.
      bool addExtFolder(const char * folder)

      // a DCC callback function to gather KL operator code from the UI
      typedef const char *(*GetOperatorSourceCodeFunc)(const char * graphName, const char * opName);

      // set a callback to allow the splice persistence framework to gather
      // the last unsaved code for a given KL operator. this code might still
      // sit in the UI somewhere but hasn't been pushed to the DGGraph.
      void setDCCOperatorSourceCodeCallback(GetOperatorSourceCodeFunc func);

      // creates a RTVal just given a KL type name
      FabricCore::RTVal constructRTVal(const char * rt);

      // creates a RTVal given a KL type name and construction args
      FabricCore::RTVal constructRTVal(const char * rt, uint32_t nbArgs, const FabricCore::RTVal * args);

      // creates a RTVal just given a KL object name
      FabricCore::RTVal constructObjectRTVal(const char * rt);

      // creates a RTVal given a KL object name and construction args
      FabricCore::RTVal constructObjectRTVal(const char * rt, uint32_t nbArgs, const FabricCore::RTVal * args);

      // creates a KL interface RTVal given a KL object to cast
      FabricCore::RTVal constructInterfaceRTVal(const char * rt, const FabricCore::RTVal & object);

      // creates a Boolean RTVal given its value
      FabricCore::RTVal constructBooleanRTVal(bool value);

      // creates a SInt8 RTVal given its value
      FabricCore::RTVal constructSInt8RTVal(int8_t value);

      // creates a SInt16 RTVal given its value
      FabricCore::RTVal constructSInt16RTVal(int16_t value);

      // creates a SInt32 RTVal given its value
      FabricCore::RTVal constructSInt32RTVal(int32_t value);

      // creates a SInt64 RTVal given its value
      FabricCore::RTVal constructSInt64RTVal(int64_t value);

      // creates a UInt8 RTVal given its value
      FabricCore::RTVal constructUInt8RTVal(uint8_t value);

      // creates a UInt16 RTVal given its value
      FabricCore::RTVal constructUInt16RTVal(uint16_t value);

      // creates a UInt32 RTVal given its value
      FabricCore::RTVal constructUInt32RTVal(uint32_t value);

      // creates a UInt64 RTVal given its value
      FabricCore::RTVal constructUInt64RTVal(uint64_t value);

      // creates a Float32 RTVal given its value
      FabricCore::RTVal constructFloat32RTVal(float value);

      // creates a Float64 RTVal given its value
      FabricCore::RTVal constructFloat64RTVal(double value);

      // creates a Data RTVal given its value
      FabricCore::RTVal constructDataRTVal(void *value);

      // creates a String RTVal given its value
      FabricCore::RTVal constructStringRTVal(const char * value);

      // creates a variable array RTVal given its type
      FabricCore::RTVal constructVariableArrayRTVal(const char * rt);

      // creates an external array RTVal given its type, nbElements and the void pointer
      FabricCore::RTVal constructExternalArrayRTVal(const char * rt, uint32_t nbElements, void * data);
    };
