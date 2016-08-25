
.. _dggraph:

FabricSplice::DGGraph
=========================

The DGGraph is the dependency graph container in the SPLICECAPI. It hosts KL operators, FabricCore elements such as dependency graph nodes, and provides access to :ref:`dgport` objects. The DGGraph class wraps the functionality of the lower level FabricCore CAPI and provides persistence functionality to store/restore the computation setup to/from files or strings. The class outline can be found further down on this page.

Example
---------------------------------

The sample below shows how to use graphs. All of the other examples also use graphs, of course. This example focuses on the persistence capability of the DGGraph class.

.. code-block:: c++

    #include <FabricSplice.h>

    using namespace FabricSplice;

    int main( int argc, const char* argv[] )
    {
      Initialize();

      // create a graph to store the nodes
      DGGraph graph = DGGraph("myGraph");

      // create two DG nodes
      // the first DG node is established
      // as the 'default' DGNode
      graph.constructDGNode("compute");
      graph.constructDGNode("data");

      // create a dependency
      graph.setDGNodeDependency("compute", "data");

      // create the members to connect
      graph.addDGNodeMember("someValues", "Scalar[]", FabricCore::Variant(), "data");
      graph.addDGNodeMember("sum", "Scalar"); // default DGNode
      graph.addDGNodeMember("product", "Scalar"); // default DGNode

      // create ports
      DGPort someValues = graph.addDGPort("someValues", "someValues", Port_Mode_IN, "data");
      DGPort sum = graph.addDGPort("sum", "sum", Port_Mode_OUT); // default DGNode
      DGPort product = graph.addDGPort("product", "product", Port_Mode_OUT); // default DGNode

      // create an operator
      std::string klCode = "";
      klCode += "operator addOp(Scalar someValues[], io Scalar sum) {";
      klCode += "  sum = 0.0;";
      klCode += "  for(Size i=0;i<someValues.size();i++)";
      klCode += "    sum += someValues[i];";
      klCode += "}";
      graph.constructKLOperator("addOp", klCode.c_str()); // default DGNode

      // create another operator
      klCode = "";
      klCode += "operator mulOp(Scalar someValues[], io Scalar product) {";
      klCode += "  product = 1.0;";
      klCode += "  for(Size i=0;i<someValues.size();i++)";
      klCode += "    product *= someValues[i];";
      klCode += "}";
      graph.constructKLOperator("mulOp", klCode.c_str()); // default DGNode

      // persist the data to json
      // (alternatively, you can also call the saveToFile method to persist to a file)
      std::string jsonData = graph.getPersistenceDataJSON();

      // destroy the ports, the node and close the FabricCore::Client
      graph = DGGraph();

      // print the persisted data
      printf("%s\n", jsonData.c_str());

      // create a new graph
      graph = DGGraph("anotherGraph");

      // reconstruct the members, ports and operators!
      // (alternatively, you can also call the loadFromFile method to persist from a file)
      graph.setFromPersistenceDataJSON(jsonData.c_str());

      // print all of the port names
      for(unsigned int i=0;i<graph.getDGPortCount();i++)
        printf("port reconstructed: %s\n", graph.getDGPortName(i).getStringData());

      // print all of the operator names
      for(unsigned int i=0;i<graph.getKLOperatorCount();i++)
        printf("operator reconstructed: %s\n", graph.getKLOperatorName(i).getStringData());

      Finalize();
      return 0;
    }


Class Outline
---------------------------------

.. code-block:: c++

    namespace FabricSplice
    {
      struct PersistenceInfo
      {
        FabricCore::Variant hostAppName;
        FabricCore::Variant hostAppVersion;
      };

      class DGGraph
      {
      public:

        // obsolete, empty constructor
        DGGraph();

        // constructor which creates a FabricCore::Client and initiates an internal FabricCore::DGNode
        DGGraph(const char * name, int guarded = 1, FabricCore::ClientOptimizationType optType = FabricCore::ClientOptimizationType_Background);

        // copy constructor
        DGGraph(DGGraph const & other);

        // copy operator
        DGGraph & operator =( DGGraph const & other );

        // returns true if the object is valid
        bool isValid() const;

        // bool conversion operator
        operator bool() const;

        // empties the content of the node
        void clear();

        // returns the FabricCore client
        static const FabricCore::Client * getClient();

        // loads the given extension
        static void loadExtension(const char *extensionName);

        // retrieve the user pointer
        void * getUserPointer();

        // store a user pointer
        void setUserPointer(void * data);

        // returns the name of this graph
        const char * getName();

        // sets the name and ensures name uniqueness
        bool setName(const char * name);

        // retrieves the metadata from the DGGraph
        const char * getMetaData();

        // sets metadata on the DGGraph
        void setMetaData(const char * json);

        // returns the number of DGNodes on this graph
        unsigned int getDGNodeCount();

        // returns the name of a specific DGNode in this graph
        char const * getDGNodeName(unsigned int index = 0);

        // adds a member based on a member name and type (rt)
        bool addDGNodeMember(const char * name, const char * rt, FabricCore::Variant defaultValue = FabricCore::Variant(), const char * dgNodeName = "", const char * extension = "");

        // returns true if a specific member exists
        bool hasDGNodeMember(const char * name, const char * dgNodeName = "");

        // removes a member
        bool removeDGNodeMember(const char * name, const char * dgNodeName = "");

        // returns KL source code for the parameter list for all available ports
        FabricCore::Variant generateKLOperatorParameterList();

        // returns dummy KL source code for a new operator
        FabricCore::Variant generateKLOperatorSourceCode(const char * name, const char * additionalBody = "", const char * additionalFunctions = "", const char * executeParallelMember = "");

        // constructs a FabricCore::DGOperator based on a name and a kl source string.
        // the portMap is a variant dict providing operator parameter name to port name mappings.
        bool constructKLOperator(const char * name, const char * sourceCode = "", const char * entry = "", const char * dgNodeName = "", const FabricCore::Variant & portMap = FabricCore::Variant::CreateDict());

        // removes a KL operator from this Node
        bool removeKLOperator(const char * name, const char * dgNodeName = "");

        // returns true if this graph contains a given KL operator
        bool hasKLOperator(const char * name, const char * dgNodeName = "");

        // gets the entry point of a specific FabricCore::DGOperator
        char const * getKLOperatorEntry(const char * name);

        // sets the entry point of a specific FabricCore::DGOperator
        bool setKLOperatorEntry(const char * name, const char * entry);

        // moves the FabricCore::DGOperator on the stack to a given index
        bool setKLOperatorIndex(const char * name, unsigned int index);

        // gets the source code of a specific FabricCore::DGOperator
        char const * getKLOperatorSourceCode(const char * name);

        // sets the source code of a specific FabricCore::DGOperator
        bool setKLOperatorSourceCode(const char * name, const char * sourceCode, const char * entry = "");

        // loads the source code of a specific FabricCore::DGOperator from file
        void loadKLOperatorSourceCode(const char * name, const char * filePath);

        // saves the source code of a specific FabricCore::DGOperator to file
        void saveKLOperatorSourceCode(const char * name, const char * filePath);

        // returns true if the KL operator is using a file
        bool isKLOperatorFileBased(const char * name);

        // gets the filepath of a specific FabricCore::DGOperator
        char const * getKLOperatorFilePath(const char * name);

        // loads the content of the file and sets the code
        void setKLOperatorFilePath(const char * name, const char * filePath, const char * entry = "");

        // returns the number of operators in this graph
        unsigned int getKLOperatorCount(const char * dgNodeName = "");

        // returns the name of a specific operator in this graph
        char const * getKLOperatorName(unsigned int index = 0, const char * dgNodeName = "");

        // returns the number of operators in total
        static unsigned int getGlobalKLOperatorCount();

        // returns the name of a specific operator
        static char const * getGlobalKLOperatorName(unsigned int index = 0);

        // checks all FabricCore::DGNodes and FabricCore::Operators for errors, return false if any errors found
        static bool checkErrors();

        // evaluates the contained DGNode
        bool evaluate();

        // clears the evaluate state
        bool clearEvaluate();

        // requires the evaluate to take place
        bool requireEvaluate();

        // returns if this graph is using the eval context
        bool usesEvalContext();

        // returns the graph's evaluation context
        FabricCore::RTVal getEvalContext();

        // adds a new Port provided a name, the member and a mode
        DGPort addDGPort(const char * name, const char * member, FabricSplice::Port_Mode mode, const char * dgNodeName = "", bool autoInitObjects = true);

        // removes an existing Port by name
        bool removeDGPort(const char * name);

        // returns a specific Port by name
        DGPort getDGPort(const char * name);

        // returns a specific Port by index
        DGPort getDGPort(unsigned int index);

        // returns the number of ports in this graph
        unsigned int getDGPortCount();

        // returns the name of a specific port in this graph
        char const * getDGPortName(unsigned int index);

        // returns JSON string encoding the port layout of the node
        std::string getDGPortInfo();

        // returns true if a DGNode of the given name exists
        bool hasDGNode(const char * dgNodeName);

        // returns the internal FabricCore::DGNode based on an index
        FabricCore::DGNode getDGNode(unsigned int index = 0);

        // returns the internal FabricCore::DGNode based on a name
        FabricCore::DGNode getDGNode(const char * dgNodeName = "");

        // creates a new DG node
        void constructDGNode(const char * dgNodeName = "");

        // removes an existing DG node
        void removeDGNode(const char * dgNodeName);

        // returns true if a given DG node is dependent on another one
        bool hasDGNodeDependency(const char * dgNode, const char * dependency);

        // depends one DGNode on another one
        bool setDGNodeDependency(const char * dgNode, const char * dependency);

        // removes the dependency of one DGNode on another one
        bool removeDGNodeDependency(const char * dgNode, const char * dependency);

        // returns variant dict of the persistence data of a node
        FabricCore::Variant getPersistenceDataDict(const PersistenceInfo * info = NULL);

        // returns JSON string encoding of the persistence data of a node
        std::string getPersistenceDataJSON(const PersistenceInfo * info = NULL);

        // constructs the node based on a variant dict
        bool setFromPersistenceDataDict(const FabricCore::Variant & dict, PersistenceInfo * info = NULL, const char * baseFilePath = NULL);

        // constructs the node based on a JSON string
        bool setFromPersistenceDataJSON(const char * json, PersistenceInfo * info = NULL, const char * baseFilePath = NULL);

        // persists the node description into a JSON file
        bool saveToFile(const char * filePath, const PersistenceInfo * info = NULL);

        // constructs the node based on a persisted JSON file
        bool loadFromFile(const char * filePath, PersistenceInfo * info = NULL, bool asReferenced = false);

        // reloads an already referenced graph from file
        bool reloadFromFile(PersistenceInfo * info = NULL);

        // returns true if this graph is referenced from a file
        bool isReferenced();

        // returns the splice file path referenced by this graph
        const char * getReferencedFilePath();

        // marks a member to be persisted
        void setMemberPersistence(const char * name, bool persistence);
      };
    };
