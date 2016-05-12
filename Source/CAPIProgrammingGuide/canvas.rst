

.. _CAPIPG.canvas:

Canvas Core API
====================

The Canvas Core API is the lowest-level interface at which Canvas can be
used.  The API is designed for use by a visual programming interface,
but can be driven directly by scripting.

The objects that are used by the Canvas Core API generally start with the
the letters :code:`DFG` for historical reasons.  Occasionally Canvas may
be referred to as "the DFG" in documentation.

The main classes that the Canvas Core API exposes are:

- :code:`FabricCore::DFGHost`: this object manages everything shared between
  different Canvas executables and bindings, such as the undo/redo stack and
  the preset tree, and is also the interface to use to create new bindings.

- :code:`FabricCore::DFGBinding`: this object is a binding of an executable
  to a set of arguments, and is the interface for actually computing things
  in Canvas.  The executable that it binds may be a very complex graph with
  subgraphs, but fundamentally all computation happens at the level of
  bindings.

- :code:`FabricCore::DFGExec`: this object is a Canvas executable, which
  can be either a graph of nodes or a KL function.

Each of these objects has its API details laid out below.

Canvas Core API in Python
-----------------------------

Note that the entire Canvas Core API is also available in Python through the
FabricEngine.Core module.  The calls are 1-1 with the CAPI calls.  For examples
of using the Python API to access the Canvas Core, please refer to the
Canvas Core unit tests located under :file:`$FABRIC_DIR/Test/Core/Canvas`.




Canvas Core API Enums
-----------------------------





:code:`enum FabricCore::DFGPortType`
  
  The type of a port in Canvas.  One of:

  - :code:`DFGPortType_In`
  - :code:`DFGPortType_IO`
  - :code:`DFGPortType_Out`




:code:`FabricCore::DFGExecType`
  
  The type of an executable in Canvas.  One of:

  - :code:`DFGExecType_Graph`
  - :code:`DFGExecType_Func`




:code:`FabricCore::DFGNodeType`
  
  The type of a node in a Canvas graph.  One of:

  - :code:`DFGNodeType_Inst` - an instance of an executable
  - :code:`DFGNodeType_Get` - a variable get node
  - :code:`DFGNodeType_Set` - a variable set node
  - :code:`DFGNodeType_Var` - a variable definition node
  - :code:`DFGNodeType_User` - a user node




Canvas Core API Classes
-----------------------------




.. cpp:class:: FabricCore::DFGExec : public FabricCore::Ref




    .. cpp:function:: DFGExec()




    .. cpp:function:: DFGExec( DFGExec const &that )




    .. cpp:function::
      DFGExec &operator=( DFGExec const &that )




    .. cpp:function:: ~DFGExec()




    .. cpp:function::
      DFGExecType getType() const

      Returns the type of the executable, either :code:`FabricCore::DFGExecType_Graph`
      or :code:`FabricCore::DFGExecType_Func`.

      :returns: The type of the executable




    .. cpp:function:: DFGNodeType getNodeType(char const *nodePath ) const

      Returns the type of a node in a graph.  See :cpp:enum:`DFGNodeType` for
      various node types.
      
      :param nodeName: The name of the node in the graph
      :returns: The type of the node




    .. cpp:function:: DFGHost getHost() const

      Returns the host to which the executable belongs.
      
      :returns: :code:`FabricCore::DFGHost`




    .. cpp:function:: DFGExec getSubExec(char const *execPath ) const

      Returns the sub-executable of an executable path. A sub-executable is
      referenced through a path of the form "node.subnode.subnode", where
      each element of the path is a node in its containing graph.
      
      :param execPath: The path to the sub-executable
      :returns: The sub-executable




    .. cpp:function:: String getErrors() const

      Returns the errors on the executable as a JSON array of strings.




    .. cpp:function:: String getErrors() const

      Returns the errors on the executable as a JSON array of strings.




    .. cpp:function:: String getLoadDiags() const

      Returns the load diagnostics on the binding as a JSON array of objects.




    .. cpp:function:: String getExtDeps() const

      Get the extension dependencies description for the executabe in JSON-encoded form.

      :returns: The extension dependencies description for the executabe in JSON-encoded form




    .. cpp:function:: unsigned getExtDepCount() const

      Get the numbed of extension dependencies for the executable.  Extension
      dependency information can be accessed on an index-basis; see also
      :cpp:func:`FabricCore::DFGExec::getExtDepName` and
      :cpp:func:`FabricCore::DFGExec::getExtDepVersion`.

      :returns: The number of extension dependencies




    .. cpp:function:: char const *getExtDepName( unsigned index ) const

      Get the name of the extension dependency at the given index.  Extension
      dependency information can be accessed on an index-basis; see also
      :cpp:func:`FabricCore::DFGExec::getExtDepCount` and
      :cpp:func:`FabricCore::DFGExec::getExtDepVersion`.
      
      :param index: The index of the extension dependency
      :returns: The name of the extension




    .. cpp:function:: String getExtDepVersion( unsigned index ) const

      Get the version specification of the extension dependency at the given index.  Extension
      dependency information can be accessed on an index-basis; see also
      :cpp:func:`FabricCore::DFGExec::getExtDepCount` and
      :cpp:func:`FabricCore::DFGExec::getExtDepName`.
      
      :param index: The index of the extension dependency
      :returns: The version specification name of the extension




    .. cpp:function:: bool haveExecPort(char const *portName ) const

      Query whether the executable has a port with the given name.
      
      :param portName: The name to query
      :returns: true if there is a port with the given name, false if not




    .. cpp:function:: unsigned getExecPortCount() const

      Get the number of ports on the executable.
      
      :returns: The number of ports on the executable




    .. cpp:function:: char const *getExecPortName(unsigned index ) const

      Get the name of the executable port at the given index.
      
      :param index: The index of the port
      :returns: The name of the port




    .. cpp:function:: unsigned getNodeCount() const

      Get the number of nodes in a graph.  Will throw an exception if the
      executable is not a graph.
      
      :returns: The number of nodes in the graph




    .. cpp:function:: char const *getNodeName(unsigned index ) const

      Get the name of the node at the given index.    Will throw an exception if the
      executable is not a graph.
      
      :param index: The index of the node
      :returns: The number of nodes in the graph




    .. cpp:function:: DFGNodeType getNodeType(unsigned index ) const

      Get the type of the node at the given index.    Will throw an exception if the
      executable is not a graph.  See :cpp:enum:`DFGNodeType` for the various
      node types.
      
      :param index: The index of the node
      :returns: The type of the node




    .. cpp:function:: DFGExec getInstExec(unsigned index ) const

      Gets a handle to the executable that the instance node at the given index is an
      instance of.  Will throw an exception if the executable is not a graph
      or the node is not an instance.
      
      :param index: The index of the instance node
      :returns: The executable that the instance node is an instance of




    .. cpp:function:: String getDesc()

      Gets a description of the executable.  The description is in JSON
      form, and can be useful for debugging.  Note, however, that it should
      not be used for persistence; instance, use :cpp:func:`FabricCore::DFGExec::exportJSON`.
      
      :returns: A description of the executable in JSON form




    .. cpp:function:: String getExecPortDesc(char const *execPortName )

      Gets a description of a port of the executable.  The description is in JSON
      form, and can be useful for debugging.
      
      :param execPortName: The name of the port of the executable
      :returns: A description of the port in JSON form




    .. cpp:function:: String getNodeDesc(char const *nodeName )

      Gets a description of a node of the executable.  The description is in JSON
      form, and can be useful for debugging.
      
      :param nodeName: The name of the node of the graph
      :returns: A description of the node in JSON form




    .. cpp:function:: String getNodePortDesc(char const *nodePortPath )

      Gets a description of a port of a node of the executable.  The path should be
      of the form "nodeName.portName".  The description is in JSON
      form, and can be useful for debugging.
      
      :param nodeName: The path to a port of a node in the graph
      :returns: A description of the port in JSON form




    .. cpp:function:: bool isExecPortResolvedType(unsigned index, char const *typeName )

      Determine whether the resolved type of a port of the executable is
      the given type (or an alias of that type).
      
      :param index: The index of the port of the executable
      :param typeName: The name of the type
      :returns: Whether the resolved type of the port is the given type




    .. cpp:function:: char const *getExecPortResolvedType(unsigned index )

      Get the resolved type of a port of the executable at a given index.

      .. note::

        This will return the type alias for the resolved type, so it
        shouldn't generally be used for type checking; for example, this function
        could return :code:`Integer` or :code:`SInt32`, depending on how the
        graph was created.
      
      :param index: The index of the port of the executable
      :returns: The resolved type of the port




    .. cpp:function:: char const *getExecPortResolvedType(char const *execPortName )

      Get the resolved type of a port of the executable with a given name.

      .. note::

        This will return the type alias for the resolved type, so it
        shouldn't generally be used for type checking; for example, this function
        could return :code:`Integer` or :code:`SInt32`, depending on how the
        graph was created.
      
      :param execPortName: The name of the port of the executable
      :returns: The resolved type of the port




    .. cpp:function:: char const *getNodePortResolvedType(char const *nodePortPath )

      Get the resolved type of a port of a node of the graph with a given path.
      The path should be of the form "nodeName.portName".

      .. note::

        This will return the type alias for the resolved type, so it
        shouldn't generally be used for type checking; for example, this function
        could return :code:`Integer` or :code:`SInt32`, depending on how the
        graph was created.
      
      :param nodePortPath: The path to a port of a node in the graph
      :returns: The resolved type of the port




    .. cpp:function:: String exportJSON()

      Create a JSON representation of the executable that can later be used
      by :cpp:func:`FabricCore::DFGExec::addInstFromJSON` to create a new
      executable that is the same.
      
      :returns: The JSON representation of the graph




    .. cpp:function:: char const *addInstFromPreset(char const *presetFilePath, char const *desiredName = 0)

      Create a new instance node in the graph that is an instance of the
      preset with the given preset path.  Will throw an exception if the
      preset is not found or if the executable is not a graph.  The name of 
      the new node will be derived from the name of the preset, but made unique
      within the graph.
      
      :param presetFilePath: The path to the preset in the preset tree
      :returns: The name of that node that was created




    .. cpp:function:: char const *addInstWithNewGraph(char const *title = 0)

      Create a new instance node in the graph that is an instance of a new
      (empty) graph.  Optionally, specify the title of the new graph; if present,
      the name of the new node is derived from the title of the graph.
      
      :param title: (optional) The title of the graph that will be created
      :returns: The name of that node that was created




    .. cpp:function:: char const *addInstWithNewFunc(char const *title = 0)

      Create a new instance node in the graph that is an instance of a new
      (empty) function.  Optionally, specify the title of the new function; if present,
      the name of the new node is derived from the title of the function.
      
      :param title: (optional) The title of the function that will be created
      :returns: The name of that node that was created




    .. cpp:function:: char const *addInstFromJSON(char const *json )

      Create a new instance node in the graph that is an instance of a new executable
      described by JSON obtained from :cpp:func:`FabricCore::DFGExec::exportJSON`.  The
      name of the node will be derived from the title of the executable.
      
      :param json: The JSON description of the executable
      :returns: The name of that node that was created




    .. cpp:function:: char const *addVar(char const *desiredName, char const *dataType, char const *extDep = 0 )

      Create a new variable declaration node in the graph with a given type and,
      optionally, an extension dependency for the type.  The actual name of
      the node will be derived from the :code:`desiredName` parameter.
      
      :param desiredName: The desired name of the new variable within the graph
      :param dataType: The KL data type of the variable
      :param extDep: (optional) An extension dependency for the type of the form :code:`{ExtensionName}:{VersionSpec}`.
      :returns: The actual name of the variable declaration node that was created




    .. cpp:function:: char const *addGet(char const *desiredName, char const *varPath )

      Create a new get variable node in the graph.
      
      :param desiredName: The desired name of the get variable node within the graph
      :param varPath: The path to the variable.  Variable paths follow "namespacing" rules whereby the are looked up starting from the current graph and continue searching in parent graphs until a match is found.
      :returns: The actual name of the get variable node that was created




    .. cpp:function:: char const *addSet(char const *desiredName, char const *varPath )

      Create a new set variable node in the graph.
      
      :param desiredName: The desired name of the get variable node within the graph
      :param varPath: The path to the variable.  Variable paths follow "namespacing" rules whereby the are looked up starting from the current graph and continue searching in parent graphs until a match is found.
      :returns: The actual name of the set variable node that was created




    .. cpp:function:: RTVal getVarValue(char const *name )

      Get the current value of a variable within the graph.
      
      :param name: The name of the get variable within the graph
      :returns: The current value of the variable as an RTVal, or a null RTVal if there is no current value




    .. cpp:function:: void setVarValue(char const *name, RTVal value )

      Set the current value of a variable within the graph.
      
      :param name: The name of the get variable within the graph
      :param value: The new value of the variable




    .. cpp:function:: char const *getRefVarPath(char const *name )

      Get the variable path associated with the given variable reference
      (get or set) node.
      
      :param name: The name of the variable reference node
      :returns: The current variable path of the node




    .. cpp:function:: void setRefVarPath(char const *name, char const *varPath )

      Set the variable path associated with the given variable reference
      (get or set) node.
      
      :param name: The name of the variable reference node
      :param varPath: The new variable path to set




    .. cpp:function:: char const *addUser(char const *desiredName )

      Create a new user node in the graph.
      
      :param desiredName: The desired name of the user node within the graph
      :returns: The actual name of the user node that was created




    .. cpp:function:: void addExtDep(char const *extName, char const *versionRange = "")

      Add an extension dependency to the executable.
      
      :param extName: The name of the extension
      :param versionRange: (optional) The version range of the extension




    .. cpp:function:: void setExtDeps(uint32_t nameAndVerCount, char const **nameAndVers )

      Replace the current extension dependencies of the executable with a
      new set.
      
      :param nameAndVerCount: The number of new extension dependencies
      :param nameAndVers: The new extension dependencies.  Each is a string of the form :code:`{ExtensionName}:{VersionRange}`




    .. cpp:function:: void removeExtDep(char const *extName )

      Remove the extension dependency for the extension with the given name
      
      :param extName: The name of the extension




    .. cpp:function:: char const *addExecPort(char const *desiredName, FEC_DFGPortType portType, char const *typeSpec = 0 )

      Add a new port to the executable.
      
      :param desiredName: The desired name for the new port
      :param portType: The type of the port, one of :cpp:enum:`DFGPortType`
      :param typeSpec: The type specification of the port (eg. :code:`Float32` or :code:`$TYPE$`).  Note that type specifications only work with functions, and not with graphs.
      :returns: The actual name of the new port




    .. cpp:function:: void reorderExecPorts(unsigned newIndCount, unsigned const *newInds )

      Reorder the ports of the executable.  Takes an array of integers for which the element
      at index oldIndex is the newIndex for the existing port.
      
      :param newIndCount: The number of elements in the index map.  Must be equal to the number of ports.
      :param newInds: The elements of the index map.




    .. cpp:function:: bool isConnectedTo(char const *srcPortPath, char const *dstPortPath ) const

      Query whether the source port is connected to the destination port.  The ports can be either node ports,
      in which case the path is of the form "nodeName.portName", or executable ports,
      in which case the path is of the form "portName".
      
      :param srcPortPath: The source port to check for connection
      :param dstPortPath: The destination port to check for connection




    .. cpp:function:: bool hasSrcPorts(char const *portPath ) const

      Query whether a given port has a connection from another port.
      
      :param portPath: The port to check




    .. cpp:function:: bool hasDstPorts(char const *portPath ) const

      Query whether a given port has one or more connections to other ports.
      
      :param portPath: The port to check




    .. cpp:function:: String canConnectTo(char const *srcPortPath, char const *dstPortPath, char const *separator ) const

      Query whether a given port can connect to another port.  If connection 
      is possible, it will return the empty string; otherwise, it will return
      a list of errors that would occur if the connection were made, with the
      errors separated by the specified separator string.
      
      :param srcPortPath: The source port for which to check connection
      :param dstPortPath: The destination port for which to check connection
      :param separator: The separator string for the errors




    .. cpp:function:: void connectTo(char const *srcPortPath, char const *dstPortPath )

      Connect two ports in a graph.
      
      :param srcPortPath: The source port to connect
      :param dstPortPath: The destination port to connect




    .. cpp:function:: void disconnectFrom(char const *srcPortPath, char const *dstPortPath )

      Disconnect two ports in a graph.
      
      :param srcPortPath: The source port to disconnect
      :param dstPortPath: The destination port to disconnect




    .. cpp:function:: void disconnectFromAll(char const *portPath )

      Disconnect any existing connections to the given port.
      
      :param portPath: The port to disconnect




    .. cpp:function:: char const *attachPresetFile(char const *parentPresetDirPath, char const *desiredName, bool replaceExisting )

      Attach the executable to a location in the preset tree, making it
      an available preset.
      
      :param parentPresetDirPath: The path of the directory in the preset tree in which to attach the preset
      :param desiredName: The desired name of the preset within the preset directory
      :param replaceExisting: If true and the desired name is used by an existing preset, replace the existing preset with this one; otherwise, a unique new name will be generated.
      :returns: The actual name of the preset within the preset directory




    .. cpp:function:: char const *renameExecPort(char const *oldName, char const *desiredNewName )

      Rename a port of the executable.
      
      :param oldName: The old name of the port
      :param desiredNewName: The desired new name of the port
      :returns: The actual new name of the port




    .. cpp:function:: char const *renameNode(char const *oldName, char const *desiredNewName )

      Rename a node of the executable.
      
      :param oldName: The old name of the node
      :param desiredNewName: The desired new name of the node
      :returns: The actual new name of the node




    .. cpp:function:: char const *getTitle()

      Get the title of the executable.
      
      :returns: The title of the executable




    .. cpp:function:: void setTitle(char const *title )

      Set the title of the executable.
      
      :param title: The new title of the executable




    .. cpp:function:: void setVersion(char const *version )

      Set the version of the executable; used when referencing presets with
      version requirements
      
      :param version: The new version of the executable in the form "X.Y.Z"




    .. cpp:function:: char const *getInstTitle(unsigned index )

      Get the title of the instance node at the given node index.
      
      :param index: The index of the instance node
      :returns: The title of the instance node




    .. cpp:function:: char const *getInstTitle(char const *nodeName )

      Get the title of the instance node with the given name.
      
      :param nodeName: The name of the instance node
      :returns: The title of the instance node




    .. cpp:function:: void setInstTitle(unsigned index, char const *title )

      Set the title of the instance node at the given index.  If the title that
      is passed is empty, the instance will adopt the title of the executable it
      is an instance of.
      
      :param index: The index of the instance node
      :param title: The new title of the instance node




    .. cpp:function:: void setInstTitle(unsigned index, char const *title )

      Set the title of the instance node with the given name.  If the title that
      is passed is empty, the instance will adopt the title of the executable it
      is an instance of.
      
      :param nodeName: The name of the instance node
      :param title: The new title of the instance node




    .. cpp:function:: DFGPortType getNodePortType(char const *portPath )

      Get the node port type of a port in the graph.  The portPath should be
      of the form "nodeName.portName" for node ports and "portName" for
      executable ports.

      The node port type is the type of the port for connection within the
      graph.  This is the inverse of the executable port type for an 
      executable port; for example, if you have an 'In' executable port on a
      graph, this has a node port type of 'Out' because it acts like an 'Out'
      port within the graph, ie. it connects to other 'In' and 'IO' ports.

      :param portPath: The port path
      :returns: The node port type of the port




    .. cpp:function:: DFGPortType getExecPortType(unsigned index )

      Get the executable port type of the port of the executable at the given
      index.

      :param index: The index of the executable port
      :returns: The executable port type of the port




    .. cpp:function:: DFGPortType getExecPortType(char const *portName )

      Get the executable port type of the port of the executable with the given
      name.

      :param portName: The name of the executable port
      :returns: The executable port type of the port




    .. cpp:function:: void setExecPortType(char const *portName, DFGPortType portType )

      Set the executable port type of the port of the executable with the given
      name.

      :param portName: The name of the executable port
      :param portType: The new executable port type for the port




    .. cpp:function:: char const *getCode()

      Get the KL code of the function executable.  If the executable
      is not a function executable an exception will be thrown.

      :returns: The KL code of the function executable




    .. cpp:function:: void setCode(char const *code )

      Set the KL code of the function executable.  If the executable
      is not a function executable an exception will be thrown.

      :param code: The new KL code of the function executable




    .. cpp:function:: char const *getMetadata(char const *key ) const

      Gets the metadata for the executable for the given key.

      :param key: The key for the metadata
      :returns: The metadata for that key, or the empty string if there is no metadata for that key




    .. cpp:function:: char const *getExecPortMetadata(char const *execPortPath, char const *key )

      Gets the metadata for a port for the given key.

      :param portName: The name of the port
      :param key: The key for the metadata
      :returns: The metadata for that key, or the empty string if there is no metadata for that key




    .. cpp:function:: char const *getNodeMetadata(char const *nodeName, char const *key )

      Gets the metadata for a node for the given key.

      :param nodeName: The name of the node
      :param key: The key for the metadata
      :returns: The metadata for that key, or the empty string if there is no metadata for that key




    .. cpp:function:: char const *getNodePortMetadata(char const *nodePortPath, char const *key )

      Gets the metadata for a node port for the given key.

      :param nodePortPath: The node port path of the form "nodeName.portName"
      :param key: The key for the metadata
      :returns: The metadata for that key, or the empty string if there is no metadata for that key




    .. cpp:function:: void setMetadata(char const *key, char const *value, bool canUndo = true, bool shouldSplitFromPreset = true )

      Sets the metadata on the executable for the given key.

      :param key: The key for the metadata
      :param value: The value for the metadata
      :param canUndo: Whether the action should be undoable
      :param shouldSplitFromPreset: Whether the metadata change should split from the preset, if the executable is an instance of a preset




    .. cpp:function:: void setExecPortMetadata(char const *name, char const *key, char const *value, bool canUndo = true, bool shouldSplitFromPreset = true )

      Sets the metadata for an executable port for the given key.
      
      :param name: The name of the executable port
      :param key: The key for the metadata
      :param value: The value for the metadata
      :param canUndo: Whether the action should be undoable
      :param shouldSplitFromPreset: Whether the metadata change should split from the preset, if the executable is an instance of a preset




    .. cpp:function:: void setExecPortMetadata(unsigned index, char const *key, char const *value, bool canUndo = true, bool shouldSplitFromPreset = true )

      Sets the metadata for an executable port for the given key.
      
      :param index: The index of the executable port
      :param key: The key for the metadata
      :param value: The value for the metadata
      :param canUndo: Whether the action should be undoable
      :param shouldSplitFromPreset: Whether the metadata change should split from the preset, if the executable is an instance of a preset




    .. cpp:function:: void setNodeMetadata(char const *nodeName, char const *key, char const *value, bool canUndo = true, bool shouldSplitFromPreset = true )

      Sets the metadata for a node for the given key.
      
      :param nodeName: The name of the node
      :param key: The key for the metadata
      :param value: The value for the metadata
      :param canUndo: Whether the action should be undoable
      :param shouldSplitFromPreset: Whether the metadata change should split from the preset, if the executable is an instance of a preset




    .. cpp:function:: void setNodePortMetadata(char const *nodePortPath, char const *key, char const *value, bool canUndo = true, bool shouldSplitFromPreset = true )

      Sets the metadata for a node port for the given key.
      
      :param nodeName: The path to the node port, of the form "nodeName.portName"
      :param key: The key for the metadata
      :param value: The value for the metadata
      :param canUndo: Whether the action should be undoable
      :param shouldSplitFromPreset: Whether the metadata change should split from the preset, if the executable is an instance of a preset




    .. cpp:function:: RTVal getPortDefaultValue(char const *portPath, char const *typeName )

      Gets the current default value for a port for a given type.  The default
      value is the value the port has when it is disconnected but resolved to
      that type.  The path can be either to a node port (of the form "nodeName.portName")
      or just the name of an executable port.
      
      :param portPath: The path the node port or executable port
      :param typeName: The name of type for which to return the current default value
      :returns: The current default value for the port for the given type




    .. cpp:function:: void setPortDefaultValue(char const *portPath, RTVal defaultValue, bool canUndo = true )

      Sets the current default value for a port.  The default
      value for a given type is the value the port has when it is disconnected but resolved to
      that type.  In this case, the type is the type of the RTVal. The path can be either to a node port (of the form "nodeName.portName")
      or just the name of an executable port.
      
      :param portPath: The path the node port or executable port
      :param defaultValue: The new default value for the port for the type of the default value
      :param canUndo: Whether the action should be undoable




    .. cpp:function:: char const *getImportPathname()

      Gets the current import pathname for an executable.  The import pathname
      is automatically set for executables when they are loaded as presets; it
      is the path on disk from which the preset was loaded.

      :returns: The import pathname for the executable




    .. cpp:function:: void setImportPathname(char const *importPathname )

      Sets a new import pathname for an executable.

      :param importPathame: The new import pathname for the executable




    .. cpp:function:: DFGBinding bind(uint32_t rtValCount = 0, RTVal const *rtVals = 0 )

      Create a new binding that is bound to this executable as its root
      executable, optionally providing RTVals to use as the binding's
      arguments.

      :param rtValCount: (optional) The number of RTVal arguments for the binding
      :param rtValCount: (optional) The RTVal arguments for the binding




    .. cpp:function:: void removeExecPort(char const *portName )

      Remove the executable port with the given name

      :param portName: The name of the port




    .. cpp:function:: void removeExecPort(unsigned index )

      Remove the executable port at the given index

      :param index: The index of the port




    .. cpp:function:: void removeNode(char const *nodeName )

      Remove the node with the given name

      :param nodeName: The name of the node




    .. cpp:function:: DFGView createView(DFGNotificationCallback callback, void *userdata )

      Create a view object that receives notifications of things that
      happen within the executable.

      .. note::

        Views are not recursive; you will received notifications about
        the executable itself, its ports, its nodes and its node ports,
        but not about subexecutables or their components.

      :param callback: The callback function to be invoked when a notification is sent
      :param userdata: The userdata to pass to the callback function




    .. cpp:function:: char const *getExecPortTypeSpec(unsigned execPortIndex )

      Get the current typeSpec for the executable port with the given index.

      :param execPortIndex: The index of the executable port
      :returns: The current typeSpec for the port




    .. cpp:function:: char const *getExecPortTypeSpec(char const *execPortName )

      Get the current typeSpec for the executable port with the given name.

      :param execPortName: The name of the executable port
      :returns: The current typeSpec for the port




    .. cpp:function:: void setExecPortTypeSpec(unsigned execPortIndex, char const *typeSpec )

      Set the current typeSpec for the executable port with the given index.

      :param execPortIndex: The index of the executable port
      :param typeSpec: The new typeSpec to set




    .. cpp:function:: void setExecPortTypeSpec(char const *execPortName, char const *typeSpec )

      Set the current typeSpec for the executable port with the given name.

      :param execPortName: The name of the executable port
      :param typeSpec: The new typeSpec to set




    .. cpp:function:: char const *getExecPortName(unsigned execPortIndex )

      Get the name of the executable port at the given index.

      :param execPortIndex: The index of the executable port




    .. cpp:function:: unsigned getNodePortCount(char const *nodeName )

      Get the number of node ports on the given node.

      :param nodeName: The name of the node




    .. cpp:function:: char const *getNodePortName(unsigned nodeIndex, unsigned nodePortIndex )

      Get the name of the node port for the given node and node port indices

      :param nodeIndex: The index of the node
      :param nodePortIndex: The index of the node port




    .. cpp:function:: char const *getNodePortName(char const *nodeName, unsigned nodePortIndex )

      Get the name of a node port.

      :param nodeName: The name of the node
      :param nodePortIndex: The index of the node port




    .. cpp:function:: String exportNodesJSON(uint32_t nodeCount, char const * const *nodeNames )

      Export a collection of nodes as JSON that can later be used by
      :cpp:func:`FabricCore::DFGExec::importNodesJSON` to recreate the nodes
      elsewhere.

      :param nodeCount: The number of nodes to export
      :param nodeNames: The names of the nodes to export
      :returns: The nodes encoded as JSON




    .. cpp:function:: String importNodesJSON(char const *nodesJSON )

      Import a collection of nodes from JSON that were exported using
      :cpp:func:`FabricCore::DFGExec::exportNodesJSON`.

      :param nodesJSON: The nodes, encoded as JSON
      :returns: The names of the newly created nodes as a JSON array of strings




    .. cpp:function:: char const *implodeNodes(char const *desiredName, uint32_t nodeCount, char const * const *nodeNames )

      Implode a collection of nodes down to a single node.

      .. note::

        Imploding a collection of nodes will also include any nodes that
        are "between" nodes in the collection with respect to connections.

      :param desiredName: The desired name of the resulting node
      :param nodeCount: The number of nodes to implode
      :param nodeNames: The names of the nodes to implode
      :returns: The actual name of the resulting node.




    .. cpp:function:: String explodeNode(char const *nodeName )

      Explode a single node that is an instance of a graph into individual
      nodes within the executable.

      :param nodeName: The name of the node to explode
      :returns: The names of the resulting nodes, encoded as a JSON array of strings




    .. cpp:function:: char const *getPresetName() const

      Get the name component of the preset path of the executable if it is
      an instance of a preset; otherwise, returns the empty string.




    .. cpp:function:: String getPresetGUID() const

      Get the preset GUID of the executable if it is an instance of a preset,
      otherwise returns the empty string.




    .. cpp:function:: void setPresetGUID( char const *presetGUID ) const

      Set the preset GUID of the executable.  The preset GUID must be a
      exactly 32 hex digits.

      .. warning::

        This function does not split the executable from the preset; it will
        change the preset GUID for all instance of the preset.




    .. cpp:function:: String getPresetGUID() const

      Get the original preset GUID of the executable if it was an instance of a preset,
      but is no longer a preset; otherwise, returns the empty string.




    .. cpp:function:: bool isPreset() const

      Queries whether the executable is a preset




    .. cpp:function:: bool instExecIsPreset( char const *instName ) const

      Queries whether the executable is a preset




    .. cpp:function:: bool editWouldSplitFromPreset() const

      Queries whether editing the executable would cause it or one of its
      containing graphs would cause a preset split.




    .. cpp:function:: unsigned getExecPortIndex() const

      Get the exec port index for the named exec port.




    .. cpp:function:: void maybeSplitFromPreset()

      Split the executable from the preset it is an instance of if it is
      an instance of a preset; otherwise, has no effect.




    .. cpp:function:: void addPriorPortName()

      Split the executable from the preset it is an instance of if it is
      an instance of a preset; otherwise, has no effect.




  The DFGBinding Class
  -----------------------------

  .. cpp:class:: FabricCore::DFGBinding : public FabricCore::Ref




    .. cpp:function:: DFGBinding()




    .. cpp:function:: DFGBinding( DFGBinding const &that )




    .. cpp:function:: DFGBinding &operator=( DFGBinding const &that )




    .. cpp:function:: ~DFGBinding()




    .. cpp:function:: DFGBinding getBindingForID(uint32_t bindingID )

      Get the binding ID for the binding.  This can be used by :cpp:func:`FabricCore::DFGHost::getBindingForID` to obtain a handle to a given binding in situations where it is not possible to pass the binding as a DFGBinding object.
      
      :returns: The binding ID for the DFGBinding




    .. cpp:function:: DFGHost getHost() const

      Get the DFGHost that owns the DFGBinding.
      
      :returns: The DFGHost that owns the DFGBinding.




    .. cpp:function:: DFGExec getExec() const

      Get the root DFGExec for the DFGBinding.
      
      :returns: The root DFGExec for the DFGBinding




    .. cpp:function:: RTVal getArgValue(unsigned index )

      Get the RTVal value for the binding argument at the given index.  Throws an exception if the index is not less than the result of :code:`FabricCore::DFGExec::getExecPortCount` on the root executable of the binding.
      
      :param index: The index of the port for which to get the argument.
      :returns: The value of the argument as an RTVal.




    .. cpp:function:: RTVal getArgValue(char const *name )

      Get the RTVal value for the binding argument with the given name.  Throws an exception if there is no port with the given name.
      
      :param name: The name of the port for which to get the argument.
      :returns: The value of the argument as an RTVal.




    .. cpp:function:: void setArgValue(LockType lockType, unsigned index, RTVal value, bool canUndo = true )

      Set the RTVal value for the binding argument at the given index.  Throws an exception if there is no port with the given name.

      The KL type of the RTVal can be the same as or different from the current value for the argument.
      
      :param lockType: What type of locking do to.  Note that this also affects the messages you will see.
      :param index: The index of the port for which to set the argument
      :param value: The new value of the argument
      :param canUndo: Whether the change to the argument should be an undoable action.




    .. cpp:function:: void setArgValue(unsigned index, RTVal value, bool canUndo = true )

      Alias for :code:`FabricCore::DFGBindign::setArgValue(FabricCore::LockType_Exclusive, index, value, canUndo)`




    .. cpp:function:: void setArgValue(LockType lockType, char const *name, RTVal value, bool canUndo = true )

      Set the RTVal value for the binding argument with the given name.  Throws an exception if there is no port with the given name.

      The KL type of the RTVal can be the same as or different from the current value for the argument.
      
      :param lockType: What type of locking do to.  Note that this also affects the messags you will see.
      :param name: The name of the port for which to set the argument.
      :param value: The new value of the argument
      :param canUndo: Whether the change to the argument should be an undoable action.




    .. cpp:function:: void setArgValue(char const *name, RTVal value, bool canUndo = true )

      Alias for :code:`FabricCore::DFGBindign::setArgValue(FabricCore::LockType_Exclusive, name, value, canUndo)`




    .. cpp:function:: bool hasRecursiveConnectedErrors() const




    .. cpp:function:: String getErrors(bool recursive) const

      Returns the errors on the binding as a JSON array of objects.




    .. cpp:function:: String getLoadDiags() const

      Returns the load diagnostics on the binding as a JSON array of objects.




    .. cpp:function:: void dismissLoadDiag(unsigned diagIndex) const

      Dismisses the given load diagnostic.




    .. cpp:function:: void suspendDirtyNotifs()

      Suspends dirty notifications until resumeDirtyNotifs() is called




    .. cpp:function:: void resumeDirtyNotifs()

      Suspends dirty notifications after suspectDirtyNotifs() has been called




    .. cpp:function:: void execute_lockType(LockType lockType )

      Execute the binding, ie. execute the KL function that is generated from the root executable (graph or function), passing the argument values as the port values.
      
      Throws an exception if the graph cannot be executed for some reason, for instance there is a node in error that is (transitively) connected to one of the output ports.

      :param lockType: The type of lock to hold during execution




    .. cpp:function:: void execute()

      Alias for :code:`FabricCore::DFGBinding::execute_lockType(FabricCore::LockType_Exclusive)`




    .. cpp:function:: void registerNotificationCallback( DFGNotificationCallback callback, void *userdata )

      Register a notification callback function and userdata to pass it.  The
      function must have the function signature::

        void BindingNotificationCallback(
          void *userdata,
          char const *jsonCString,
          uint32_t jsonLength
          );
      
      It will receive the value of :code:`userdata` that was passed to :code:`registerNotificationCallback`,
      and :code:`jsonCString` and :code:`jsonLength` will be a JSON-encoded string with
      the contents of the notification.

      The callback must be removed with :cpp:func:`FabricCore::DFGBinding::unregisterNotificationCallback`
      if it is no longer intersted in notifications.

      :param callback: The callback function to call for notifications
      :param userdata: The userdata value to pass to the callback function




    .. cpp:function:: void setNotificationCallback( DFGNotificationCallback callback, void *userdata )

      Set a notification callback function and userdata to pass it.  The
      function must have the function signature::

        void BindingNotificationCallback(
          void *userdata,
          char const *jsonCString,
          uint32_t jsonLength
          );
      
      It will receive the value of :code:`userdata` that was passed to :code:`registerNotificationCallback`,
      and :code:`jsonCString` and :code:`jsonLength` will be a JSON-encoded string with
      the contents of the notification.

      This function will throw an error if a callback has already been registered,
      unless callback is :code:`NULL` in which case it will
      remove the existing callback.

      :param callback: The callback function to call for notifications, or NULL to clear the current callback
      :param userdata: The userdata value to pass to the callback function




    .. cpp:function:: void unregisterNotificationCallback( DFGNotificationCallback callback, void *userdata )

      Unregister a notification callback function and userdata that was previously
      added with :cpp:func:`FabricCore::DFGBinding::registerNotificationCallback`.
      Both the callback and userdata must match what was passed to this function.

      :param callback: The callback function to call for notifications
      :param userdata: The userdata value to pass to the callback function




    .. cpp:function:: String exportJSON()

      Export the binding as a JSON-encoded string.  This string can be used by 
      :cpp:func:`FabricCore::DFGHost::createBindingFromJSON` to create a binding
      with the same contents.

      The contents of the binding are recusrsively encoded.  Presets are reference
      through their preset path and/or GUID, while locally-defined graphs and
      functions are encoded inline.  The values of the binding argument and the default values
      of ports are also encoded, provided that the RTVal codecs provided to the
      Core are able to encode them; see the Core client constructors for details.

      :returns: The binding encoded as a JSON string




    .. cpp:function:: void deallocValues()

      Flush any temporary storage used by the binding.  This can be called
      on a binding that will never again be used in order to free memory used
      by the binding.




    .. cpp:function:: char const *getMetadata(char const *keyCStr ) const

      Gets a named metadata value associated with the binding.  The key is case-sensitive,
      and if there is no metadata present for the given key this function
      returns the empty string.  See :cpp:func:`FabricCore::DFGBinding::setMetdata`.

      :param key: The key for the metadata to obtain
      :returns: The value for the metadata, or the empty string if there is none.




    .. cpp:function:: void setMetadata(char const *keyCStr, char const *valueCStr, bool canUndo = true )

      Sets a named metadata value associated with the binding.  The key is 
      case-sensitive.  The current value for the key, if any, will be replaced.
      The canUndo parameter can optionally be provided to specify whether the
      action should be undoable; if it is not undoable then no undo action will
      be stored and then the previous value of the metadata for the key will
      not be restored when an undo occurs.

      :param key: The key for the metadata to obtain
      :param value: The new value for the metadata
      :param canUndo: Optional; whether to make the change undoable




    .. cpp:function:: String getVars()

      Returns a JSON-encoded description of Canvas variables available within the
      binding.

      :result: The JSON-encoded descripton of Canvas variables




    .. cpp:function:: uint32_t getVersion()

      Returns the version of the binding.  The version of the binding is zero 
      when the binding is first created, and is incremented every time the binding
      changes.  The binding version changes are undone when actions on the binding
      are undone.  The purpose of the version is to allow applications to know
      when the binding has changed and may need to be saved.  Note that the binding
      version is not persisted when the binding is persisted.

      :result: The version of the binding




  The DFGHost Class
  -----------------------------

  .. cpp:class:: FabricCore::DFGHost : public FabricCore::Ref




    .. cpp:function:: DFGHost()




    .. cpp:function:: DFGHost( DFGHost const &that )




    .. cpp:function:: DFGHost &operator=( DFGHost const &that )




    .. cpp:function:: DFGHost &~DFGHost()




    .. cpp:function:: Context &getContext() const

      Get the Fabric Core context to which the DFGHost belongs




    .. cpp:function:: bool maybeUndo()

      Attempt to undo one Canvas Core command.

      :returns: Whether a command was undone




    .. cpp:function:: bool maybeUndo()

      Attempt to redo one Canvas Core command.

      :returns: Whether a command was redone




    .. cpp:function:: void flushUndoRedo()

      Flush the undo and redo stacks.  This will purge memory used by the
      commands on the stack but the commands will destroyed.




    .. cpp:function:: char const *getPresetImportPathname( char const *nameSpacePath )

      Get the filename from which a preset was imported.
      
      :param presetPath: The path to the preset in the preset tree
      :returns: The filename from which the preset was imported, or the empty string if the preset was not imported from a file




    .. cpp:function:: FabricCore::String getPresetDesc( char const *presetPath )

      Generate a JSON description of a preset
      
      :param presetPath: The path to the preset in the preset tree
      :returns: The JSON description




    .. cpp:function:: char const *addPresetDir(char const *parentPresetDirPath, char const *desiredName, char const *pathname = 0 )

      Add a new preset directory (child) to an existing preset directory (parent) within the preset tree.
      
      :param parentPresetDirPath: The path of the parent preset directory to contain the new child preset directory
      :param desiredName: The desired name of the new child preset directory
      :param importPathname: If given, the import pathname to associate with the new child preset directory
      :returns: The actual name of the new child preset directory




    .. cpp:function:: char const *importPresetFileJSON(char const *parentPresetDirPath, char const *desiredName, char const *json, char const *importPathname = 0 )

      Import a new preset (child), encoded as JSON, into an existing preset directory (parent).  The JSON-encoded representation is usually obtained through :cpp:func:`String exportPresetJSON`.
      
      :param parentPresetDirPath: The path of the parent preset directory to contain the new child preset
      :param desiredName: The desired name of the new child preset
      :param json: The new preset encoded as JSON
      :returns: The actual name of the new child preset




    .. cpp:function:: String exportPresetJSON(char const *presetPathCStr )

      Export an existing preset as JSON.
      
      :param presetPath: The path to the preset
      :returns: The preset encoded as JSON




    .. cpp:function:: void removePreset(char const *presetPath )

      Remove an existing preset from the preset tree.
      
      :param presetPath: The path to the preset




    .. cpp:function:: DFGExec createNewUnboundGraph()

      Create a new DFGExec object that references an empty graph.  The graph is unbound, ie. it is not attached to a DFGBinding, and so can be edited but not executed.
      
      :returns: The new DFGExec object




    .. cpp:function:: DFGExec createNewUnboundExecFromJSON(char const *json )

      Create a new DFGExec object described by JSON.  The JSON is usually obtained through :cpp:func:`FabricCore::DFGExec::exportJSON`.  The executable is unbound, ie. it is not attached to a DFGBinding, and so can be edited but not executed.
      
      :param json: The JSON-encoded description of the executable
      :returns: The new DFGExec object




    .. cpp:function:: DFGExec createNewUnboundFunc()

      Create a new DFGExec object that references an empty function.  The function is unbound, ie. it is not attached to a DFGBinding, and so can be edited but not executed.
      
      :returns: The new DFGExec object




    .. cpp:function:: DFGBinding createBindingToNewGraph()

      Create a new DFGBinding object with an empty graph as its root executable.
      
      :returns: The new DFGBinding




    .. cpp:function:: DFGBinding createBindingToNewFunc()

      Create a new DFGBinding object with an empty function as its root executable.
      
      :returns: The new DFGBinding




    .. cpp:function:: DFGBinding createBindingFromJSON(char const *json, uint32_t rtValCount = 0, RTVal const *rtVals = 0 )

      Create a new DFGBinding object with its root executable described by JSON.  The JSON is usually obtained through :cpp:func:`FabricCore::DFGExec::exportJSON`.
      
      :param json: The JSON-encoded description of the root executable
      :param rtValCount: If given, the number of RTVals to bind to the arguments of the new DFGBinding
      :param rtVals: If given, the RTVals to bind to the arguments of the new DFGBinding
      :returns: The new DFGBinding




    .. cpp:function:: DFGBinding createBindingToPreset(char const *presetFile, uint32_t rtValCount = 0, RTVal const *rtVals = 0 )

      Create a new DFGBinding object with its root executable being an instance of a specified preset.  The JSON is usually obtained through :cpp:func:`FabricCore::DFGExec::exportJSON`.
      
      :param presetFilePath: The path to the preset, within the preset tree, to use as the root executable
      :param rtValCount: If given, the number of RTVals to bind to the arguments of the new DFGBinding
      :param rtVals: If given, the RTVals to bind to the arguments of the new DFGBinding
      :returns: The new DFGBinding




    .. cpp:function:: DFGBinding getBindingForID(uint32_t bindingID )

      Obtain a reference to the DFGBinding with the given binding ID, obtained through :cpp:func:`FabricCore::DFGBinding::getBindingID`.
      
      :param bindingID: The binding ID
      :returns: The DFGBinding with the given binding ID




    .. cpp:function:: void blockComps()

      Block recompilations of DFGBindings.  This can be used to increase performance during long scripted building of graphs.  Calling :cpp:func:`FabricCore::DFGBinding::execute` while recompilations are blocked will throw an exception.




    .. cpp:function:: void blockComps()

      Unblock recompilations of DFGBindings.




  The DFGNotifBracket Class
  -----------------------------

  .. cpp:class:: FabricCore::DFGNotifBracket

    The DFGNotifBracket class is used to suspend notifications until
    a set of DFG commands has executed.




    .. cpp:function:: DFGNotifBracket( DFGHost host )

      By creating a DFGNotifBracket in the current scope, all DFG
      notifications will be suspended until the scope closes.




    .. cpp:function:: ~DFGNotifBracket()




.. cpp:class:: FabricCore::Client : public FabricCore::Ref


