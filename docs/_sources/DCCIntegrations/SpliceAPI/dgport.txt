
.. _dgport:

FabricSplice::DGPort
=========================

The DGPort class allows to get or set :ref:`dggraph` data. DGPorts can communicate with the FabricCore layer in various ways.

.. note::

  When accessing data on instances of FabricSplice::DGPort, eg. through
  :code:`DGPort::getRTVal()`, it is the responsibility of the client to ensure
  that accesses to data on the same port are synchronized, ie. that two threads
  don't try to change the value at the same time.  However, it is safe to access
  data on different instances of FabricSplice::DFGPort without locking.

Example
---------------------------------

The sample below shows how to use ports. The class outline can be found at the end of this page.

.. code-block:: c++

    #include <FabricSplice.h>
    #include <vector>

    using namespace FabricSplice;

    int main( int argc, const char* argv[] )
    {
      Initialize();

      // create a graph
      DGGraph graph = DGGraph("myGraph");

      // create a DG node
      graph.constructDGNode();

      // create a member
      graph.addDGNodeMember("myScalar", "Scalar");

      // create a port
      // the mode defines if a port can be read from, 
      // written to or both (like in this case)
      DGPort port = graph.addDGPort("myPortName", "myScalar", Port_Mode_IO);

      // set some data on the port using JSON
      port.setJSON("1.3");

      // print the data
      printf("%s\n", port.getJSON().getStringData());

      // set some data on the port using a variant
      port.setVariant(FabricCore::Variant::CreateFloat64(2.6));

      // print the data
      printf("%s\n", port.getJSON().getStringData());

      // nodes can store any number of values. the count of the values
      // is referred to as 'slice count'
      port.setSliceCount(3);
      port.setVariant(FabricCore::Variant::CreateFloat64(1.6), 0);
      port.setVariant(FabricCore::Variant::CreateFloat64(2.6), 1);
      port.setVariant(FabricCore::Variant::CreateFloat64(3.6), 2);

      // print the data
      for(uint32_t i=0;i<port.getSliceCount();i++)
        printf("%x: %s\n", i, port.getJSON(i).getStringData());

      // aside from json and variants you can also use the 
      // high performance IO on a port.
      std::vector<float> values(5);
      values[0] = 3.4;
      values[1] = 4.5;
      values[2] = 5.6;
      values[3] = 6.7;
      values[4] = 7.8;
      port.setSliceCount(values.size());
      port.setAllSlicesData(&values[0], sizeof(float) * values.size());

      // clear the values
      values.clear();
      values.resize(port.getSliceCount());

      // get the data again using the high performance IO
      port.getAllSlicesData(&values[0], sizeof(float) * values.size());

      // print the retured data
      for(uint32_t i=0;i<values.size();i++)
        printf("%x: %f\n", i, values[i]);

      Finalize();
      return 0;
    }

Class Outline
---------------------------------

.. code-block:: c++

    namespace FabricSplice
    {
      enum Port_Mode
      {
        Port_Mode_IN = 0,
        Port_Mode_OUT = 1,
        Port_Mode_IO = 2
      };

      class DGPort
      {
      public:

        // default constructor
        DGPort();

        // copy constructor
        DGPort(DGPort const & other);

        // copy operator
        DGPort & operator =( DGPort const & other );

        // returns true if the object is valid
        bool isValid() const;

        // bool conversion operator
        operator bool() const;

        // resets the port and detaches it
        void clear();

        // returns the name of this DGPort
        char const * getName();

        // returns the name of the member this DGPort is connected to
        char const * getMember();

        // returns the name of the DGNode this DGPort is connected to
        char const * getDGNodeName();

        // returns a unique key descripting the DGPort
        char const * getKey();

        // returns the mode of this DGPort
        DGPort_Mode getMode();

        // sets the mode of this DGPort
        void setMode(DGPort_Mode mode);

        // returns the data type of the member this DGPort is connected to
        char const * getDataType();

        // returns the data size of a single element of the member this DGPort is connected to.
        // So for example, both for a 'Vec3' and 'Vec3[]' this will return sizeof(Vec3) == 12
        unsigned int getDataSize();

        // returns true if the data type of this DGPort is shallow.
        // only shallow data types can be used with the high performance IO
        bool isShallow();

        // returns true if the data type of this DGPort is an array (Vec3[] for example)
        bool isArray();

        // returns true if the data type of this DGPort is a struct
        bool isStruct();

        // returns true if the data type of this DGPort is an object
        bool isObject();

        // returns true if the data type of this DGPort is an interface
        bool isInterface();

        // returns true if this port auto initializes KL objects
        bool doesAutoInitObjects() const { return mAutoInitObjects; }

        // returns the slice count of the FabricCore::DGNode this DGPort is connected to
        unsigned int getSliceCount();

        // sets the slice count of the FabricCore::DGNode this DGPort is connected to
        bool setSliceCount(unsigned int count);

        // returns the value of a specific slice of this DGPort as a FabricCore::Variant
        FabricCore::Variant getVariant(unsigned int slice = 0);

        // sets the value of a specific slice of this DGPort from a FabricCore::Variant
        bool setVariant(FabricCore::Variant value, unsigned int slice = 0);

        // returns the value of a specific slice of this DGPort as a JSON string
        std::string getJSON(unsigned int slice = 0);

        // sets the value of a specific slice of this DGPort from a JSON string
        bool setJSON(const char * json, unsigned int slice = 0);

        // returns the default value of this DGPort as a FabricCore::Variant
        FabricCore::Variant getDefault();

        // returns the value of a specific slice of this DGPort as a FabricCore::RTVal
        FabricCore::RTVal getRTVal(bool evaluate = false, uint32_t slice = 0);

        // sets the value of a specific slice of this DGPort from a FabricCore::RTVal
        bool setRTVal(FabricCore::RTVal value, uint32_t slice = 0);

        // returns the size of an array member this DGPort is connected to
        unsigned int getArrayCount(unsigned int slice = 0);

        // returns the void* array data of this DGPort.
        // this only works for array DGPorts (isArray() == true)
        // the bufferSize has to match getArrayCount() * getDataSize()
        bool getArrayData(void * buffer, unsigned int bufferSize, unsigned int slice = 0);

        // sets the void* array data of this DGPort.
        // this only works for array DGPorts (isArray() == true)
        // this also sets the array count determined by bufferSize / getDataSize()
        bool setArrayData(void * buffer, unsigned int bufferSize, unsigned int slice = 0);

        // gets the void* slice array data of this DGPort.
        // this only works for non-array DGPorts (isArray() == false)
        // the bufferSize has to match getSliceCount() * getDataSize()
        bool getAllSlicesData(void * buffer, unsigned int bufferSize);

        // sets the void* slice array data of this DGPort.
        // this only works for non-array DGPorts (isArray() == false)
        // the bufferSize has to match getSliceCount() * getDataSize()
        bool setAllSlicesData(void * buffer, unsigned int bufferSize);

        // set the array data based on another port
        // this performs data replication, and only works on shallow array data ports.
        // the data type has to match as well (so only Vec3 to Vec3 for example).
        bool copyArrayDataFromDGPort(DGPort other, unsigned int slice = 0, unsigned int otherSlice = UINT_MAX);

        // set the slices data based on another port
        // this performs data replication, and only works on shallow non array data ports.
        // the data type has to match as well (so only Vec3 to Vec3 for example).
        bool copyAllSlicesDataFromDGPort(DGPort other, bool resizeTarget = false);

        // sets an auxiliary option
        void setOption(const char * name, const FabricCore::Variant & value);

        // gets an auxiliary option (empty variant if not defined)
        FabricCore::Variant getOption(const char * name);

        // returns true if an auxiliary option exists
        bool hasOption(const char * name);

        // gets an auxiliary option as boolean
        bool getBooleanOption(const char * name, bool defaultValue = false);

        // gets an auxiliary option as int
        int getIntegerOption(const char * name, int defaultValue = -1);

        // gets an auxiliary option as float
        float getScalarOption(const char * name, float defaultValue = 0.0);

        // gets an auxiliary option as string
        std::string getStringOption(const char * name, const char * defaultValue = "");

        // returns true if this port can be manipulated
        bool isManipulatable();

        // returns all animation channels of this port
        FabricCore::RTVal getAnimationChannels();

        // sets the values of all animation channels
        void setAnimationChannelValues(unsigned int nbChannels, float * values);

        // perform a manipulation and returns the event
        // int codes from ManipulationContext.kl
        int manipulate(FabricCore::RTVal & manipulationContext);
      };
    };
