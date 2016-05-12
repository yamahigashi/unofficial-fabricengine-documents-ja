.. _FabricForMODO.CanvasScripting:

Canvas scripting interface
=============================

Fabric for MODO comes with a scripting interface which allows you to author graphs from, for example, Python scripts. Script commands are logged automatically when working with the UI, so most of the time you won't need the reference below. You can just perform the work interactively and investigate the logged script steps in MODO's "Command History".

.. note::
  Commands in MODO either perform a task *or* return a value. This means that you cannot execute a command and get its return value at the same time. Instead there is a special command called ``FabricCanvasGetResult`` which returns the result of the last executed Fabric command.

  The following example uses the command ``FabricCanvasAddFunc`` to add an empty function node to a CanvasPI item and then the command ``FabricCanvasGetResult`` to get the return value of ``FabricCanvasAddFunc``:

  .. code-block:: python

    lx.eval("FabricCanvasAddFunc CanvasPI {} myLittleFunction {} 110 120")
    print "added a new function node called " + lx.eval("FabricCanvasGetResult ?")


FabricCanvasAddBackDrop
-----------------------------------
    
    **Description**

    Adds a backdrop to a graph.
    
    **Scripting Syntax**

    ``FabricCanvasAddBackDrop( binding, execPath, title, xPos, yPos )``
    
    **Parameters**

      - ``binding``

        The name of a Canvas item.

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

        The name of a Canvas item.

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

        The name of a Canvas item.

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

    Adds a graph node to a graph.
    
    **Scripting Syntax**

    ``name = FabricCanvasAddGraph( binding, execPath, title, xPos, yPos )``
    
    **Return value**

    The name of the new node.
    
    **Parameters**

      - ``binding``

        The name of a Canvas item.

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

        The name of a Canvas item.

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

        The name of a Canvas item.

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

        The name of a Canvas item.

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

        The name of a Canvas item.

      - ``execPath``

        The path of the node inside of which the source and destination ports are located.

      - ``srcPortPath``

        The path of the source port.

      - ``dstPortPath``

        The path of the destination port.
    
FabricCanvasDisconnect
-----------------------------------
    
    **Description**

    Removes connections between two ports.
    
    **Scripting Syntax**

    ``FabricCanvasDisconnect( binding, execPath, srcPortPath, dstPortPath )``
    
    **Parameters**

      - ``binding``

        The name of a Canvas item.

      - ``execPath``

        The path of the node inside of which the source and destination ports are located.

      - ``srcPortPath``

        The path(s) of the source port(s). If you have more than one path then you must separate them using ``|`` (vertical bar).

      - ``dstPortPath``

        The path(s) of the destination port(s). If you have more than one path then you must separate them using ``|`` (vertical bar).

    **Note**

    The amount of source and destination paths should be the same!

FabricCanvasDismissLoadDiags
-----------------------------------
    
    **Description**

    Dismisses load diagnostics.
    
    **Scripting Syntax**

    ``FabricCanvasDismissLoadDiags( binding, diagIndices )``
    
    **Parameters**

      - ``binding``

        The name of a Canvas item.

      - ``diagIndices``

        An array of load diagnostics indices.

FabricCanvasCreatePreset
-----------------------------------
    
    **Description**

    Create a new preset from an existing node.
    
    **Scripting Syntax**

    ``name = FabricCanvasCreatePreset( binding, execPath, nodeName, presetDirPath, presetName )``

    **Return value**

    The pathname where the new preset was saved on disk, or an empty string if the preset was not saved.
    
    **Parameters**

      - ``binding``

        The name of a Canvas item.

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

        The name of a Canvas item.

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

        The name of a Canvas item.

      - ``execPath``

        The path of the node containing the node to explode.

      - ``nodeName``

        The name of the node to explode.
    
FabricCanvasExportGraph
-----------------------------------
    
    **Description**

    Exports the graph of an operator as a JSON file.
    
    **Scripting Syntax**

    ``FabricCanvasExportGraph( OperatorName )``
    
    **Parameters**

      - ``OperatorName``

        The name of a CanvasOp operator. Its graph will be exported as a JSON file.
    
FabricCanvasGetResult
-----------------------------------
    
    **Description**

    Returns the result of the last Canvas command.
    
    **Scripting Syntax**

    ``FabricCanvasGetResult( )``

    **Example**

    The following script adds an empty function node to a CanvasPI item and then outputs the name of the newly created node.

    .. code-block:: python

      lx.eval("FabricCanvasAddFunc CanvasPI {} myLittleFunction {} 110 120")
      print "added a new function node called " + lx.eval("FabricCanvasGetResult ?")

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

        The name of a Canvas item.

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

    ``result = FabricCanvasImportGraph( OperatorName )``
    
    **Return value**

    'true' if the operator had to be recreated, else 'false'.
    
    **Parameters**

      - ``OperatorName``

        The name of a CanvasOp operator. Its graph will be set from the graph contained in a JSON file.

      - ``JSONFilePath``

        The path + fielname + extension of the JSON file, e.g. "D:\Temp\my_graph.canvas"
    
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

        The name of a Canvas item.

      - ``execPath``

        The path for the new preset node.

      - ``presetPath``

        The path to the preset.

      - ``xPos``

        The x position for the new node.

      - ``yPos``

        The y position for the new node.
        
FabricCanvasMoveNodes
-----------------------------------
    
    **Description**

    Moves the input node(s).
    
    **Scripting Syntax**

    ``FabricCanvasMoveNodes( binding, execPath, nodeNames, xPoss, yPoss )``
    
    **Parameters**

      - ``binding``

        The name of a Canvas item.

      - ``execPath``

        The path of the node containing the nodes in nodeNames (see next parameter).

      - ``nodeNames``

        The name(s) of the node(s) to move. If you have more than one name then you must separate them using ``|`` (vertical bar), e.g. "GetSphere|GetSphere_2|DrawPolygonMesh|Add".

      - ``xPoss``

        The new x position(s) for the node(s). If you have more than one position you must separate them using ``|`` (vertical bar), e.g. "302|580|492|332".

      - ``yPoss``

        The new y position(s) for the node(s). If you have more than one position you must separate them using ``|`` (vertical bar), e.g. "110|160|246|264".
      
FabricCanvasOpenCanvas
-----------------------------------
    
    **Description**

    Opens the Canvas graph editor for a given Canvas item.
    
    **Scripting Syntax**

    ``FabricCanvasOpenCanvas( binding )``
    
    **Parameters**

      - ``binding``

        The name of a Canvas item.
      
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

        The name of a Canvas item.

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

        The name of a Canvas item.

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

        The name of a Canvas item.

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

        The name of a Canvas item.

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

        The name of a Canvas item.

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

        The name of a Canvas item.

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
    
FabricCanvasSetArgValue
-----------------------------------
    
    **Description**

    Sets the value of one of the graph's ports (a.k.a. *arguments*). Note: these are the ports that are exposed to MODO.
    
    **Scripting Syntax**

    ``FabricCanvasSetArgValue( binding, argName, typeName, valueJSON )``
    
    **Parameters**

      - ``binding``

        The name of a Canvas item.

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

        The name of a Canvas item.

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

        The name of a Canvas item.

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

        The name of a Canvas item.

      - ``execPath``

        The path of the node.

      - ``nodeName``

        The name of the node to add a comment to.

      - ``comment``

        The comment.
    
FabricCanvasEditNode
-----------------------------------
    
    **Description**

    Renames a node in a Canvas graph
    
    **Scripting Syntax**

    ``FabricCanvasEditNode( binding, execPath, currentNodeName, desiredNodeName, uiMetadata )``
    
    **Parameters**

      - ``binding``

        The name of a Canvas item.

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

        The name of a Canvas item.

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

        The name of a Canvas item.

      - ``execPath``

        The path of the node.
    