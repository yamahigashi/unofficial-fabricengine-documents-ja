The Custom Commands
=====================

| Alongside the Canvas operator, a handful of custom commands are defined.
| They can be used in a script for a variety of tasks, from simply adding a Canvas operator to an object to create entire graphs from scratch.


  

FabricCanvasAddBackDrop
-----------------------------------
    
    **Description**

    Adds a backdrop to a graph.
    
    **Scripting Syntax**

    ``FabricCanvasAddBackDrop( binding, execPath, title, xPos, yPos )``
    
    **Parameters**

      - ``binding``

        The name of a CanvasOp operator (i.e. the graph).

      - ``execPath``

        The path for the new backdrop.

      - ``title``

        The title of the new backdrop, for example "recompute my normals".

      - ``xPos``

        The x position for the new backdrop.

      - ``yPos``

        The y position for the new backdrop.
    
FabricCanvasAddFunc
-----------------------------------
    
    **Description**

    Adds a function node to a graph.
    
    **Scripting Syntax**

    ``name = FabricCanvasAddFunc( binding, execPath, title, initialCode, xPos, yPos )``
    
    **Return value**

    The name of the new node.
    
    **Parameters**

      - ``binding``

        The name of a CanvasOp operator (i.e. the graph).

      - ``execPath``

        The path for the new function node.

      - ``title``

        The title of the new function node.

      - ``initialCode``

        The initial KL code of the new function node.

      - ``xPos``

        The x position for the new node.

      - ``yPos``

        The y position for the new node.
    
FabricCanvasAddGet
-----------------------------------
    
    **Description**

    Adds a 'get variable' node to a graph.
    
    **Scripting Syntax**

    ``name = FabricCanvasAddGet( binding, execPath, desiredNodeName, varPath, xPos, yPos )``
    
    **Return value**

    The name of the new node.
    
    **Parameters**

      - ``binding``

        The name of a CanvasOp operator (i.e. the graph).

      - ``execPath``

        The path for the new 'get' node.

      - ``desiredNodeName``

        The desired name for the new node. 

      - ``varPath``

        The path to the variable.

      - ``xPos``

        The x position for the new node.

      - ``yPos``

        The y position for the new node.
    
FabricCanvasAddGraph
-----------------------------------
    
    **Description**

    Adds a graph node to the graph.
    
    **Scripting Syntax**

    ``name = FabricCanvasAddGraph( binding, execPath, title, xPos, yPos )``
    
    **Return value**

    The name of the new node.
    
    **Parameters**

      - ``binding``

        The name of a CanvasOp operator (i.e. the graph).

      - ``execPath``

        The path for the new graph node.

      - ``title``

        The title for the new node.

      - ``xPos``

        The x position for the new node.

      - ``yPos``

        The y position for the new node.
    
FabricCanvasAddPort
-----------------------------------
    
    **Description**

    Adds a port to a node.
    
    **Scripting Syntax**

    ``name = FabricCanvasAddPort( binding, execPath, desiredPortName, portType, typeSpec, portToConnect, extDep, uiMetadata )``

    **Return value**

    The name of the new port. Note that the name returned by the command might be different from the name specified via ``desiredPortName`` due to the internal naming rules used by Fabric Core.
    
    **Parameters**

      - ``binding``

        The name of a CanvasOp operator (i.e. the graph).

      - ``execPath``

        The path of the node to which the port will be added to.

      - ``desiredPortName``

        The desired name for the port. If a port with the same name already exists then the name of the new port will be suffixed with a number, e.g. "2", appended to its name.

      - ``portType``

        The port type: "In", "Out" or "IO".

      - ``typeSpec``

        The data type of the port, for example "Scalar", "Vec3", "PolygonMesh".
    
      - ``portToConnect``

        An optional path to an existing port. If specified, the new port will be connected to this port.
        
      - ``extDep``

        NOT YET DOCUMENTED
        
      - ``uiMetadata``

        NOT YET DOCUMENTED
        
FabricCanvasAddSet
-----------------------------------
    
    **Description**

    Adds a 'set variable' node to a graph.
    
    **Scripting Syntax**

    ``name = FabricCanvasAddSet( binding, execPath, desiredNodeName, varPath, xPos, yPos )``
    
    **Return value**

    The name of the new node.
    
    **Parameters**

      - ``binding``

        The name of a CanvasOp operator (i.e. the graph).

      - ``execPath``

        The path for the new 'set' node.

      - ``desiredNodeName``

        The desired name for the new node. 

      - ``varPath``

        The path to the variable.

      - ``xPos``

        The x position for the new node.

      - ``yPos``

        The y position for the new node.
    
FabricCanvasAddVar
-----------------------------------
    
    **Description**

    Adds a variable node to a graph.
    
    **Scripting Syntax**

    ``name = FabricCanvasAddVar( binding, execPath, desiredNodeName, dataType, extDep, xPos, yPos )``
    
    **Return value**

    The name of the new node.
    
    **Parameters**

      - ``binding``

        The name of a CanvasOp operator (i.e. the graph).

      - ``execPath``

        The path for the new variable node.

      - ``desiredNodeName``

        The desired name for the node/variable. 

      - ``dataType``

        The data type of the variable, for example "Scalar", "Integer", "PolygonMesh".

      - ``extDep``

        The names of one or more extensions the specified dataType depends to be loaded. For example, "PolygonMesh" requires the extension "Geometry".

      - ``xPos``

        The x position for the new node.

      - ``yPos``

        The y position for the new node.
    
FabricCanvasConnect
-----------------------------------
    
    **Description**

    Connects two ports with each other.
    
    **Scripting Syntax**

    ``FabricCanvasConnect( binding, execPath, srcPortPath, dstPortPath )``
    
    **Parameters**

      - ``binding``

        The name of a CanvasOp operator (i.e. the graph).

      - ``execPath``

        The path of the node inside of which the source and destination ports are located.

      - ``srcPortPath``

        The path of the source port.

      - ``dstPortPath``

        The path of the destination port.
    
FabricCanvasDisconnect
-----------------------------------
    
    **Description**

    Removes the connection between two ports.
    
    **Scripting Syntax**

    ``FabricCanvasDisconnect( binding, execPath, srcPortPath, dstPortPath )``
    
    **Parameters**

      - ``binding``

        The name of a CanvasOp operator (i.e. the graph).

      - ``execPath``

        The path of the node inside of which the source and destination ports are located.

      - ``srcPortPath``

        The path of the source port.

      - ``dstPortPath``

        The path of the destination port.

FabricCanvasCreatePreset
-----------------------------------
    
    **Description**

    Create a new preset from an existing node.
    
    **Scripting Syntax**

    ``name = FabricCanvasCreatePreset( binding, execPath, nodeName, presetDirPath, presetName )``

    **Return value**

    The pathname where the new preset was saved on disk, or the empty
string if the preset was not saved.
    
    **Parameters**

      - ``binding``

        The name of a CanvasOp operator (i.e. the graph).

      - ``execPath``

        The path of the node to which the port belongs to.

      - ``nodeName``

        The name of the node

      - ``presetDirPath``

        The path to the directory in the preset tree where the preset should be located

      - ``presetName``

        The name of the preset to be created

FabricCanvasEditPort
-----------------------------------
    
    **Description**

    Edits an existing port. Use this to rename a port, change its data type, etc.
    
    **Scripting Syntax**

    ``name = FabricCanvasEditPort( binding, execPath, oldPortName, desiredNewPortName, typeSpec, extDep, uiMetadata )``

    **Return value**

    The new name of the new port. Note that the name returned by the command might be different from the name specified via ``desiredNewPortName`` due to the internal naming rules used by Fabric Core.
    
    **Parameters**

      - ``binding``

        The name of a CanvasOp operator (i.e. the graph).

      - ``execPath``

        The path of the node to which the port belongs to.

      - ``oldPortName``

        The current name of the port.

      - ``desiredNewPortName``

        The desired new name for the port. If a port with the same name already exists then the name of the new port will be suffixed with a number, e.g. "2", appended to its name.

      - ``typeSpec``

        The data type of the port, for example "Scalar", "Vec3", "PolygonMesh".
    
      - ``extDep``

        NOT YET DOCUMENTED
        
      - ``uiMetadata``

        NOT YET DOCUMENTED
    
FabricCanvasExplodeNode
-----------------------------------
    
    **Description**

    Explodes a node that contains a subgraph.
    All existing connections between ports are preserved.
    
    **Scripting Syntax**

    ``names = FabricCanvasExplodeNode( binding, execPath, nodeName )``
    
    **Return value**

    The names of the nodes that were inside of the node that got exploded.
    
    **Parameters**

      - ``binding``

        The name of a CanvasOp operator (i.e. the graph).

      - ``execPath``

        The path of the node containing the node to explode.

      - ``nodeName``

        The name of the node to explode.
    
FabricCanvasExportGraph
-----------------------------------
    
    **Description**

    Exports the graph of an operator as a JSON file.
    
    **Scripting Syntax**

    ``FabricCanvasExportGraph( OperatorName, JSONFilePath )``
    
    **Parameters**

      - ``OperatorName``

        The name of a CanvasOp operator. Its graph will be exported as a JSON file.

      - ``JSONFilePath``

        The path + filename + extension of the JSON file, e.g. "D:\Temp\my_graph.canvas"
    
FabricCanvasGetBindingID
-----------------------------------
    
    **Description**

    Returns the ID of the FabricCore DFGBinding used by a specified Canvas operator. This is useful if you want to create a python FabricCore client, for example, to access the same data.
    
    **Scripting Syntax**

    ``FabricCanvasGetBindingID( OperatorName )``

    **Parameters**

      - ``OperatorName``

        The name of a CanvasOp operator.

    **Example**

    The following VBScript gets the FabricCore DFGBinding ID of a null and logs it.

    .. code-block:: none

      Option Explicit

      Dim bindingID
      bindingID = FabricCanvasGetBindingID("null.kine.global.CanvasOp")
      logmessage "binding ID: " & bindingID

FabricCanvasGetContextID
-----------------------------------
    
    **Description**

    Returns the FabricCore client contextID used by Canvas operators. This is useful if you want to create a python FabricCore client, for example, to access the same data.
    
    **Scripting Syntax**

    ``FabricCanvasGetContextID( )``

    **Example**

    The following VBScript gets the FabricCore client contextID and logs it.

    .. code-block:: none

      Option Explicit

      Dim coreCtxtID
      coreCtxtID = FabricCanvasGetContextID()
      logmessage "FabricCore client contextID: " & coreCtxtID

FabricCanvasImplodeNodes
-----------------------------------
    
    **Description**

    Creates a node containing the input nodes as a subgraph.
    All existing connections between ports are preserved.
    
    **Scripting Syntax**

    ``name = FabricCanvasImplodeNodes( binding, execPath, nodeNames, desiredImplodedNodeName )``
    
    **Return value**

    The name of the new node.
    
    **Parameters**

      - ``binding``

        The name of a CanvasOp operator (i.e. the graph).

      - ``execPath``

        The path where the nodes in nodeNames (see next parameter) are located.

      - ``nodeNames``

        The name(s) of the node(s) to implode. If you have more than one name then you must separate them using ``|`` (vertical bar), e.g. "GetSphere|GetSphere_2|DrawPolygonMesh|Add".

      - ``desiredImplodedNodeName``

        The desired name for the new node that contains all the input nodes.
    
FabricCanvasImportGraph
-----------------------------------
    
    **Description**

    Sets the graph of an operator from the content of a JSON file.
    
    **Scripting Syntax**

    ``result = FabricCanvasImportGraph( OperatorName, JSONFilePath )``
    
    **Return value**

    'true' if the operator had to be recreated, else 'false'.
    
    **Parameters**

      - ``OperatorName``

        The name of a CanvasOp operator. Its graph will be set from the graph contained in a JSON file.

      - ``JSONFilePath``

        The path + fielname + extension of the JSON file, e.g. "D:\Temp\my_graph.canvas"
    
FabricCanvasInspectOp
-----------------------------------
    
    **Description**

    Opens the property page for the currently selected object's Canvas operator, if any.
    
    Note: the menu "Fabric -> Inspect Canvas Op" also calls this command.

    **Scripting Syntax**

    ``FabricCanvasInspectOp( )``

FabricCanvasInstPreset
-----------------------------------
    
    **Description**

    Adds a preset node to the graph.
    
    **Scripting Syntax**

    ``name = FabricCanvasInstPreset( binding, execPath, presetPath, xPos, yPos )``
    
    **Return value**

    The name of the new node.
    
    **Parameters**

      - ``binding``

        The name of a CanvasOp operator (i.e. the graph).

      - ``execPath``

        The path for the new preset node.

      - ``presetPath``

        The path to the preset.

      - ``xPos``

        The x position for the new node.

      - ``yPos``

        The y position for the new node.
    
FabricCanvasLogStatus
-----------------------------------
    
    **Description**

    Outputs information about Fabric for Softimage in the History Log.
    
    **Scripting Syntax**

    ``FabricCanvasLogStatus( )``
    
FabricCanvasMoveNodes
-----------------------------------
    
    **Description**

    Moves the input node(s).
    
    **Scripting Syntax**

    ``FabricCanvasMoveNodes( binding, execPath, nodeNames, xPoss, yPoss )``
    
    **Parameters**

      - ``binding``

        The name of a CanvasOp operator (i.e. the graph).

      - ``execPath``

        The path of the node containing the nodes in nodeNames (see next parameter).

      - ``nodeNames``

        The name(s) of the node(s) to move. If you have more than one name then you must separate them using ``|`` (vertical bar), e.g. "GetSphere|GetSphere_2|DrawPolygonMesh|Add".

      - ``xPoss``

        The new x position(s) for the node(s). If you have more than one position you must separate them using ``|`` (vertical bar), e.g. "302|580|492|332".

      - ``yPoss``

        The new y position(s) for the node(s). If you have more than one position you must separate them using ``|`` (vertical bar), e.g. "110|160|246|264".
    
FabricCanvasOpApply
-----------------------------------
    
    **Description**

    Adds a Canvas operator to an object.
    
    **Scripting Syntax**

    ``refOp = FabricCanvasOpApply( ObjectName, [dfgJSON], [OpenPPG], [otherOpName], [CreateSpliceOp] )``
    
    **Return value**

    A reference at the new operator.
    
    **Parameters**

      - ``ObjectName``

        The name of the object that will have the new operator attached to it.

      - ``dfgJSON``

        An optional graph description. The graph of the new operator will be set from this.

        Default is "" (empty graph).

      - ``OpenPPG``

        An optional boolean indicating whether to display the property of the new operator once it got created.

        Default is true.

      - ``otherOpName``

        An optional name of another CanvasOp operator. If specified, this command will copy parameters, exposed values, animations etc. from this operator to the new one.

        Default is "".

      - ``CreateSpliceOp``

        An optional integer indicating whether to also create a SpliceOp operator for the object:
          - **0** don't create a SpliceOp operator.
          - **1** create a SpliceOp operator.
          - **2** create a SpliceOp operator only if the object doesn't have one yet.

        Default is **2**.

        *Note: it is highly recommended to always use the default value for this parameter.*

FabricCanvasOpConnectPort
-----------------------------------
    
    **Description**

    Connects or disconnects an exposed Canvas port that has the type "XSI Port".
    
    **Scripting Syntax**

    ``success = FabricCanvasOpConnectPort( OperatorName, portName, [targetNames], [checkIfAlreadyConnected] )``
    
    **Return value**

    A boolean indicating whether the operation was successful or not.

    **Parameters**

      - ``OperatorName``

        The name of a CanvasOp operator.

      - ``portName``

        The port name.

      - ``targetNames``

        Optional target name(s), separated by semicolon. If this is set then the port specified via 'portName' is connected with the target(s). If this is not set (i.e. "") then all connections to the port specified via 'portName' are removed.

        Note: it usually is sufficient to just specify the object names, e.g. "myNull" or "myNull;null2;poi". The command will automatically expand the target to match the port's type, e.g. "myNull.kine.global" if the port has the data type "Mat44".

        Default is "".

      - ``checkIfAlreadyConnected``

        If true then check if targetNames is already connected and, if it is, don't add a further connection.

        Default is true.

FabricCanvasOpDisconnectPort
-----------------------------------
    
    **Description**

    Disconnects objects from an exposed Canvas port that has the type "XSI Port".
    
    **Scripting Syntax**

    ``success = FabricCanvasOpDisconnectPort( OperatorName, portName, [targetNames]``
    
    **Return value**

    A boolean indicating whether the operation was successful or not.

    **Parameters**

      - ``OperatorName``

        The name of a CanvasOp operator.

      - ``portName``

        The port name.

      - ``targetNames``

        Optional target name(s), separated by semicolon. If this is set then the target(s) in targetNames are disconnected from the port. If this is not set (i.e. "") then all connections to the port are removed.

        Note: it usually is sufficient to just specify the object names, e.g. "myNull" or "myNull;null2;poi". The command will automatically expand the target to match the port's type, e.g. "myNull.kine.global" if the port has the data type "Mat44".

        Default is "".

FabricCanvasOpPortMapDefine
-----------------------------------
    
    **Description**

    Defines the port mapping for one or more ports of a Canvas operator.
    
    **Scripting Syntax**

    ``refOp = FabricCanvasOpPortMapDefine( OperatorName, portmapDefinition )``
    
    **Return value**

    A reference at the new operator.

    **Parameters**

      - ``OperatorName``

        The name of a CanvasOp operator.

      - ``portmapDefinition``

        The port mapping, encoded in a single string.

    **Example**

    The following VBScript creates a null with a Canvas graph (the graph draws a red torus into the viewport using the inline drawing) and exposes the RGB channels as XSI parameters.

    .. code-block:: none

      Option Explicit

      Dim opRef
      Dim portmapDefinition

      ' create a null with a Canvas operator.
      NewScene
      GetPrim "Null"
      set opRef = FabricCanvasOpApply("null", "", False)

      ' create a small graph.
      FabricCanvasInstPreset opRef.FullName, , "Fabric.Compounds.PolygonMesh.Create.GetTorus", "100", "50"
      FabricCanvasInstPreset opRef.FullName, , "Fabric.Compounds.PolygonMesh.Display.DrawMesh", "330", "160"
      FabricCanvasInstPreset opRef.FullName, , "Fabric.Exts.Math.Color.ComposeColor", "100", "200"
      FabricCanvasConnect opRef.FullName, , "GetTorus.mesh", "DrawMesh.mesh"
      FabricCanvasConnect opRef.FullName, , "Color.result", "DrawMesh.color"

      ' create ports for "drawThis", "r", "g" and "b".
      FabricCanvasAddPort opRef.FullName, , "drawThis", "Out", "DrawingHandle", "DrawMesh.drawThis"
      FabricCanvasAddPort opRef.FullName, , "r", "In", "Scalar", "Color.r"
      FabricCanvasAddPort opRef.FullName, , "g", "In", "Scalar", "Color.g"
      FabricCanvasAddPort opRef.FullName, , "b", "In", "Scalar", "Color.b"

      ' define the port mapping so that "r", "g" and "b" are exposed as XSI parameters.
      portmapDefinition = "r|XSI Parameter" & "<<->>" & "g|XSI Parameter" & "<<->>" & "b|XSI Parameter"
      set opRef = FabricCanvasOpPortMapDefine("null.kine.global.CanvasOp", portmapDefinition)

      ' set the color to red.
      SetValue "null.kine.global.CanvasOp.r", 1
      SetValue "null.kine.global.CanvasOp.g", 0
      SetValue "null.kine.global.CanvasOp.b", 0

      ' open the property page.
      InspectObj opRef.FullName
      
FabricCanvasOpPortMapQuery
-----------------------------------
    
    **Description**

    Returns the current port mapping of a Canvas operator.
    
    **Scripting Syntax**

    ``portmap = FabricCanvasOpPortMapQuery( OperatorName, [portName] )``
    
    **Return value**

    A string containing the result or "" (i.e. empty string) if something went wrong (e.g. operator or port not found).

    The string can contain one or more port mappings and each mapping has several values. The delimiter for the ports is "<<->>" and for the values "|", here how the ports and values are encoded in the string:

    ``"<port name>|<port type>|<data type>|<map type>|<target>|<value><<->><port name>|<port type>|<data type>|<map type>|<target>|<value><<->>..."``

    See the example VBScript below on how to split the string to get the individual values.

    **Parameters**

      - ``OperatorName``

        The name of a CanvasOp operator.

      - ``portName``

        An optional port name. If specified then only the port mapping of the port named portName is returned, else the mapping of all ports is returned.

        Default is "".

    **Example**

    The following VBScript logs the entire port mapping of a Canvas operator.

    .. code-block:: none

      Option Explicit

      Dim portmap
      Dim opName
      Dim portName

      opName = "null.kine.global.CanvasOp"
      portName = ""

      portmap = FabricCanvasOpPortMapQuery(opName, portName)
      if portmap = "" then
        logmessage "invalid operator name or no ports found"
      else
        Dim i, p, pa
        pa = Split(portmap, "<<->>")
        for i = 0 to UBound(pa)
          p = Split(pa(i), "|")
          logmessage "port " & Chr(34) & p(0) & Chr(34) & ":"
          logmessage "    port type: " & p(1)
          logmessage "    data type: " & p(2)
          logmessage "     map type: " & p(3)
          if p(4) <> "" then logmessage "       target: " & p(4)
          if p(5) <> "" then logmessage "        value: " & p(5)
        next
      end if

FabricCanvasPaste
-----------------------------------
    
    **Description**

    Pastes a text (i.e. a JSON string) into the graph.
    
    **Scripting Syntax**

    ``names = FabricCanvasPaste( binding, execPath, text, xPos, yPos )``
    
    **Return value**

    The names of the nodes that got pasted.
    
    **Parameters**

      - ``binding``

        The name of a CanvasOp operator (i.e. the graph).

      - ``execPath``

        The path where the new nodes will get pasted into.

      - ``text``

        The "text" to paste. Note: the "text" must be a JSON representation of a graph or subgraph.

      - ``xPos``

        The x position for the pasted node(s).

      - ``yPos``

        The y position for the pasted node(s).
    
FabricCanvasRemoveNodes
-----------------------------------
    
    **Description**

    Removes one or more nodes from the graph.
    
    **Scripting Syntax**

    ``FabricCanvasRemoveNodes( binding, execPath, nodeNames )``
    
    **Parameters**

      - ``binding``

        The name of a CanvasOp operator (i.e. the graph).

      - ``execPath``

        The path of the node containing the nodes in nodeNames (see next parameter).

      - ``nodeNames``

        The name(s) of the node(s) to remove. If you have more than one name then you must separate them using ``|`` (vertical bar), e.g. "GetSphere|GetSphere_2|DrawPolygonMesh|Add".
    
FabricCanvasRemovePort
-----------------------------------
    
    **Description**

    Removes a port from a graph or a node.
    
    **Scripting Syntax**

    ``FabricCanvasRemovePort( binding, execPath, portName )``
    
    **Parameters**

      - ``binding``

        The name of a CanvasOp operator (i.e. the graph).

      - ``execPath``

        The path of the node with the port that is to be removed.

      - ``portName``

        The name of the port to remove.
    
FabricCanvasRenamePort
-----------------------------------
    
    **Description**

    Renames a port.
    
    **Scripting Syntax**

    ``name = FabricCanvasRenamePort( binding, execPath, oldPortName, desiredNewPortName )``
    
    **Return value**

    The new name of the port.
    
    **Parameters**

      - ``binding``

        The name of a CanvasOp operator (i.e. the graph).

      - ``execPath``

        The path of the node with the port that is to be renamed.

      - ``oldPortName``

        The current name of the port.

      - ``desiredNewPortName``

        The desired new name for the port. If a port with the same name already exists then the new name of the port will have a number, e.g. "2", appended to its name.
    
FabricCanvasReorderPorts
-----------------------------------
    
    **Description**

    Reorders ports.
    
    **Scripting Syntax**

    ``FabricCanvasReorderPorts( binding, execPath, indices )``
    
    **Parameters**

      - ``binding``

        The name of a CanvasOp operator (i.e. the graph).

      - ``execPath``

        The path of the node with the ports that are to be reordered.

      - ``indices``

        An array of indices that defines the new order for the ports.

        Example: say you have three ports. Then their indices are "0", "1" and "2" and the current order of the ports is "[0, 1, 2]". If you now wish to reorder the ports so that port 1 comes before port 0 you would call this command with the following indices: "[1, 0, 2]".
    
FabricCanvasResizeBackDrop
-----------------------------------
    
    **Description**

    Resizes and repositions a backdrop.
    
    **Scripting Syntax**

    ``FabricCanvasResizeBackDrop( binding, execPath, backDropName, xPos, yPos, width, height )``
    
    **Parameters**

      - ``binding``

        The name of a CanvasOp operator (i.e. the graph).

      - ``execPath``

        The path of the node containing the backdrop.

      - ``backDropName``

        The name of the backdrop.

      - ``xPos``

        The new x position of the backdrop.

      - ``yPos``

        The new y position of the backdrop.

      - ``width``

        The new width of the backdrop.

      - ``height``

        The new height of the backdrop.
    
FabricCanvasSelectConnected
-----------------------------------
    
    **Description**

    Selects all object that are connected to an operator.
    
    **Scripting Syntax**

    ``FabricCanvasSelectConnected( OperatorName, [selWhat], [preClearSel], [skipReservedPorts] )``
    
    **Parameters**

      - ``OperatorName``

        The name of a CanvasOp operator.

      - ``selWhat``

        An optional integer specifying what to select:
          - **-1** select only objects connected to "In" ports.
          - **0** select all connected objects.
          - **+1** select only objects connected to "Out" ports.

        Default is 0.

      - ``preClearSel``

        An optional boolean indicating whether to clear the current selection before selecting the connected objects.

        Default is true.

      - ``skipReservedPorts``

        An optional boolean indicating whether to also select objects that are connected to the operator's reserved ports. 

        Default is true.
    
FabricCanvasSetArgType
-----------------------------------
    
    **Description**

    Sets the data type of one of the graph's ports (a.k.a. *arguments*). Note: these are the ports that can be exposed to Softimage and that are displayed in the tab "Ports and Tools" of the operator's property page.
    
    **Scripting Syntax**

    ``FabricCanvasSetArgType( binding, argName, typeName )``
    
    **Parameters**

      - ``binding``

        The name of a CanvasOp operator (i.e. the graph).

      - ``argName``

        The name of the port / argument.

      - ``typeName``

        The new data type of the port, e.g. "Scalar", "Mat44", "PolygonMesh".
    
FabricCanvasSetArgValue
-----------------------------------
    
    **Description**

    Sets the value of one of the graph's ports (a.k.a. *arguments*). Note: these are the ports that can be exposed to Softimage and that are displayed in the tab "Ports and Tools" of the operator's property page.
    
    **Scripting Syntax**

    ``FabricCanvasSetArgValue( binding, argName, typeName, valueJSON )``
    
    **Parameters**

      - ``binding``

        The name of a CanvasOp operator (i.e. the graph).

      - ``argName``

        The name of the port / argument.

      - ``typeName``

        The type of the parameter ``valueJSON``.

      - ``valueJSON``

        The actual value, as a JSON string.
    
FabricCanvasSetCode
-----------------------------------
    
    **Description**

    Sets the code of a (function) node.
    
    **Scripting Syntax**

    ``FabricCanvasSetCode( binding, execPath, code )``
    
    **Parameters**

      - ``binding``

        The name of a CanvasOp operator (i.e. the graph).

      - ``execPath``

        The path of the function node.

      - ``code``

        The KL code.

FabricCanvasSetExtDeps
-----------------------------------
    
    **Description**

    Sets the extension dependencies of a node.
    
    **Scripting Syntax**

    ``FabricCanvasSetExtDeps( binding, execPath, extDeps )``
    
    **Parameters**

      - ``binding``

        The name of a CanvasOp operator (i.e. the graph).

      - ``execPath``

        The path of the node.

      - ``extDeps``

        The name(s) of the extensions for the node. If you want to specifiy more than one extension then you must separate them using ``|`` (vertical bar), e.g. "Alembic|Geometry|Math".

FabricCanvasSetNodeComment
-----------------------------------
    
    **Description**

    Sets the comment of a node.
    
    **Scripting Syntax**

    ``FabricCanvasSetNodeComment( binding, execPath, nodeName, comment )``
    
    **Parameters**

      - ``binding``

        The name of a CanvasOp operator (i.e. the graph).

      - ``execPath``

        The path of the node.

      - ``nodeName``

        The name of the node to add a comment to.

      - ``comment``

        The comment.
    
FabricCanvasSetTitle
-----------------------------------
    
    **Description**

    Sets the title of an executable.
    
    **Scripting Syntax**

    ``FabricCanvasSetTitle( binding, execPath, title )``
    
    **Parameters**

      - ``binding``

        The name of a CanvasOp operator (i.e. the graph).

      - ``execPath``

        The path of the executable in the Canvas operator.

      - ``title``

        The new title for the node.
    
FabricCanvasEditNode
-----------------------------------
    
    **Description**

    Renames a node in a Canvas graph
    
    **Scripting Syntax**

    ``FabricCanvasEditNode( binding, execPath, currentNodeName, desiredNodeName, uiMetadata )``
    
    **Parameters**

      - ``binding``

        The name of a CanvasOp operator (i.e. the graph).

      - ``execPath``

        The path of the node.

      - ``oldNodeName``

        The current name of the node.

      - ``desiredNewNodeName``

        The desired new name of the node.
        
      - ``nodeMetadata``

        NOT YET DOCUMENTED
        
      - ``execMetadata``

        NOT YET DOCUMENTED

    **Returns**

    The actual new name of the node
    
FabricCanvasSetPortDefaultValue
-----------------------------------
    
    **Description**

    Sets the default value of a port.
    
    **Scripting Syntax**

    ``FabricCanvasSetPortDefaultValue( binding, execPath, portPath, typeName, valueJSON )``
    
    **Parameters**

      - ``binding``

        The name of a CanvasOp operator (i.e. the graph).

      - ``execPath``

        The path of the node with the port.

      - ``portPath``

        The port path.

      - ``typeName``

        The type of the parameter ``valueJSON``.

      - ``valueJSON``

        The new default value, as a JSON string.
    
FabricCanvasSetRefVarPath
-----------------------------------
    
    **Description**

    NOT YET DOCUMENTED
    
    **Scripting Syntax**

    ``FabricCanvasSetRefVarPath( binding, execPath, refName, varPath )``
    
    **Parameters**

      NOT YET DOCUMENTED

FabricCanvasSplitFromPreset
-----------------------------------
    
    **Description**

    Splits an executable (graph or function) from the preset it references
    
    **Scripting Syntax**

    ``FabricCanvasSplitFromPreset( binding, execPath )``
    
    **Parameters**

      - ``binding``

        The name of a CanvasOp operator (i.e. the graph).

      - ``execPath``

        The path of the node.
    
FabricCanvasDismissLoadDiags
-----------------------------------
    
    **Description**

    Dismisses load diagnostics.
    
    **Scripting Syntax**

    ``FabricCanvasDismissLoadDiags( binding, diagIndices )``
    
    **Parameters**

      - ``binding``

        The name of a CanvasOp operator (i.e. the graph).

      - ``diagIndices``

        An array of load diagnostics indices.
