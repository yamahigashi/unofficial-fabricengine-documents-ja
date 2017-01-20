.. _FabricForMaya.CanvasScripting:

Canvas scripting interface
=============================

Fabric for Maya comes with a rich scripting interface which allows you to author graphs from MEL. Script commands are logged automatically when working with the UI, so most of the time you won't need the reference below. You can just perform the work interactively and investigate the logged script steps.

For example this was copied out of the Maya script editor for creating a small graph:

.. code-block:: kl

    FabricCanvasInstPreset -m "canvasNode1" -e "" -p "Fabric.Exts.Math.Vec3.Vec3" -x "345" -y "85";
    FabricCanvasAddPort -m "canvasNode1" -e "" -d "x" -p "In" -t "Scalar" -c "Vec3.x";
    FabricCanvasAddPort -m "canvasNode1" -e "" -d "y" -p "In" -t "Scalar" -c "Vec3.y";
    FabricCanvasAddPort -m "canvasNode1" -e "" -d "z" -p "In" -t "Scalar" -c "Vec3.z";
    FabricCanvasAddPort -m "canvasNode1" -e "" -d "result" -p "Out" -t "Vec3" -c "Vec3.result";

FabricCanvasGetFabricVersion
-------------------------------------

Returns the Fabric version.

.. code-block:: kl

  FabricCanvasGetFabricVersion;
  // Result: 2.3.0 // 

FabricCanvasAddBackDrop
-------------------------------------

Adds a new backdrop node to the Canvas graph.

  - -m, -mayaNode: The name of the Canvas maya node
  - -e, -execPath: The path of the node inside of Canvas to operate on
  - -x, -xPos: The x coordinate for placing the new backdrop
  - -y, -yPos: The y coordinate for placing the new backdrop
  - -t, -title: The name of the new backdrop

.. code-block:: KL

    FabricCanvasAddBackDrop -m "canvasNode1" -e "" -t "MathNodes" -x "265" -y "132";

FabricCanvasAddBlock
-------------------------------------

Adds a new block node to the Canvas graph.

  - -m, -mayaNode: The name of the Canvas maya node
  - -e, -execPath: The path of the node inside of Canvas to operate on
  - -x, -xPos: The x coordinate for placing the new node
  - -y, -yPos: The y coordinate for placing the new node
  - -d, -desiredName: The name of the new node

FabricCanvasAddBlockPort
-------------------------------------

Adds a new port to a given block node.

  - -m, -mayaNode: The name of the Canvas maya node
  - -e, -execPath: The path of the node inside of Canvas to operate on
  - -b, -blockName: The name of the block
  - -d, -desiredPortName: The desired name of the new port
  - -p, -portType: The type, can be "In", "Out" or "IO"
  - -t, -typeSpec: The data type for the new port
  - -c, -pathToConnect: An optional argument to describe it's initial connection
  - -ct, -connectType: The type, can be "In", "Out" or "IO"
  - -xd, -extDep: An optional extension dependency for the port
  - -md, -metaData: Additional metadata, for example UI ranges or combo lists

FabricCanvasAddFunc
-------------------------------------

Adds a new KL function node to the Canvas graph.

  - -m, -mayaNode: The name of the Canvas maya node
  - -e, -execPath: The path of the node inside of Canvas to operate on
  - -x, -xPos: The x coordinate for placing the new node
  - -y, -yPos: The y coordinate for placing the new node
  - -t, -title: The name of the new node
  - -c, -code: The KL code for the new node

.. code-block:: KL

    FabricCanvasAddFunc -m "canvasNode1" -e "" -t "func" -c "dfgEntry {\n  // result = a + b;\n}\n" -x "549" -y "63";

FabricCanvasAddGet
-------------------------------------

Adds a new variable getter node to the Canvas graph.

  - -m, -mayaNode: The name of the Canvas maya node
  - -e, -execPath: The path of the node inside of Canvas to operate on
  - -x, -xPos: The x coordinate for placing the new node
  - -y, -yPos: The y coordinate for placing the new node
  - -d, -desiredNodeName: The desired name for the new node
  - -p, -varPath: The path to the variable

.. code-block:: KL

    FabricCanvasAddGet -m "canvasNode1" -e "" -d "get" -p "factor" -x "293" -y "370";

FabricCanvasAddGraph
-------------------------------------

Adds a new sub graph node to the Canvas graph.

  - -m, -mayaNode: The name of the Canvas maya node
  - -e, -execPath: The path of the node inside of Canvas to operate on
  - -x, -xPos: The x coordinate for placing the new node
  - -y, -yPos: The y coordinate for placing the new node
  - -t, -title: The name of the new graph

.. code-block:: KL

    FabricCanvasAddGraph -m "canvasNode1" -e "" -t "MySubGraph" -x "265" -y "132";

FabricCanvasAddInstBlockPort
-------------------------------------

Adds a new port to a block instance.

  - -m, -mayaNode: The name of the Canvas maya node
  - -e, -execPath: The path of the node inside of Canvas to operate on
  - -n, -instName: The name of the instance
  - -b, -blockName: The name of the block
  - -d, -desiredPortName: The desired name of the new port
  - -t, -typeSpec: The data type for the new port
  - -c, -pathToConnect: An optional argument to describe it's initial connection
  - -xd, -extDep: An optional extension dependency for the port
  - -md, -metaData: Additional metadata, for example UI ranges or combo lists

FabricCanvasAddInstPort
-------------------------------------

Adds a new port to an instance node.

  - -m, -mayaNode: The name of the Canvas maya node
  - -e, -execPath: The path of the node inside of Canvas to operate on
  - -n, -instName: The name of the instance
  - -d, -desiredPortName: The desired name of the new port
  - -p, -portType: The type, can be "In", "Out" or "IO"
  - -t, -typeSpec: The data type for the new port
  - -c, -pathToConnect: An optional argument to describe it's initial connection
  - -ct, -connectType: The type, can be "In", "Out" or "IO"
  - -xd, -extDep: An optional extension dependency for the port
  - -md, -metaData: Additional metadata, for example UI ranges or combo lists

FabricCanvasAddPort
-------------------------------------

Adds a new port to a given node.

  - -m, -mayaNode: The name of the Canvas maya node
  - -e, -execPath: The path of the node inside of Canvas to operate on
  - -d, -desiredPortName: The desired name of the new port
  - -p, -portType: The type, can be "In", "Out" or "IO"
  - -t, -typeSpec: The data type for the new port
  - -c, -connectToPortPath: An optional argument to describe it's initial connection
  - -xd, -extDep: An optional extension dependency for the port
  - -ui, -uiMetadata: Additional metadata, for example UI ranges or combo lists

.. code-block:: KL

  FabricCanvasAddPort -m "canvasNode1" -e "" -d "factor" -p "In" -t "Float32";

FabricCanvasAddSet
-------------------------------------

Adds a new variable setter node to the Canvas graph.

  - -m, -mayaNode: The name of the Canvas maya node
  - -e, -execPath: The path of the node inside of Canvas to operate on
  - -x, -xPos: The x coordinate for placing the new node
  - -y, -yPos: The y coordinate for placing the new node
  - -d, -desiredNodeName: The desired name for the new node
  - -p, -varPath: The path to the variable

.. code-block:: KL

    FabricCanvasAddSet -m "canvasNode1" -e "" -d "get" -p "factor" -x "293" -y "370";

FabricCanvasAddVar
-------------------------------------

Adds a new variable node to the Canvas graph.

  - -m, -mayaNode: The name of the Canvas maya node
  - -e, -execPath: The path of the node inside of Canvas to operate on
  - -x, -xPos: The x coordinate for placing the new node
  - -y, -yPos: The y coordinate for placing the new node
  - -d, -desiredNodeName: The desired name for the new variable
  - -t, -type: The data type for the variable
  - -xd, -extDep: An [optional] extension dependency

.. code-block:: KL

    FabricCanvasAddVar -m "canvasNode1" -e "" -d "factor" -t "Float32" -xd "" -x "51" -y "64";

FabricCanvasConnect
-------------------------------------

Connects two pins / ports inside a Canvas graph.

  - -m, -mayaNode: The name of the Canvas maya node
  - -e, -execPath: The path of the node inside of Canvas to operate on
  - -s, -srcPortPath: The path(s) to the source (left) port(s) / pin(s)
  - -d, -dstPortPath: The path(s) to the destination (left) port(s) / pin(s)

.. code-block:: KL

  FabricCanvasConnect -m "canvasNode1" -e "" -s "Scalar.value" -d "Vec3.z";

.. code-block:: KL

  FabricCanvasConnect -m "canvasNode1" -e "" -s "Scalar.value|Scalar.value|Scalar.value" -d "Vec3.x|Vec3.y|Vec3.z";

FabricCanvasDisconnect
-------------------------------------

Disconnects two pins / ports inside a Canvas graph.

  - -m, -mayaNode: The name of the Canvas maya node
  - -e, -execPath: The path of the node inside of Canvas to operate on
  - -s, -srcPortPath: The path(s) to the source (left) port(s) / pin(s)
  - -d, -dstPortPath: The path(s) to the destination (left) port(s) / pin(s)

.. code-block:: KL

  FabricCanvasDisconnect -m "canvasNode1" -e "" -s "Scalar.value" -d "Vec3.z";

.. code-block:: KL

  FabricCanvasDisconnect -m "canvasNode1" -e "" -s "Scalar.value|Scalar.value|Scalar.value" -d "Vec3.x|Vec3.y|Vec3.z";  

FabricCanvasCreatePreset
-------------------------------------

Create a new preset from an existing node.

  - -n, -nodeName: The name of the node
  - -pd, -presetDirPath: The path to the directory in the preset tree where the preset should be located
  - -pn, -presetName: The name of the preset to be created

Returns the pathname where the new preset was saved on disk, or the empty
string if the preset was not saved.

.. code-block:: KL

    FabricCanvasCreatePreset -m "canvasNode1" -e "" -n "x" -pd "User" -pn "MyPreset"

FabricCanvasEditPort
-------------------------------------

Edits an existing port. Use this to rename a port, change its data type, etc.

  - -n, -oldPortName: The old name of the port
  - -d, -desiredNewPortName: The desired new name of the port
  - -p, -portType: The type, can be "In", "Out" or "IO"
  - -t, -typeSpec: The wanted datatype of the port
  - -xd, -extDep: An additional extension dependency of the port
  - -ui, -uiMetadata: Additional metadata, such as UI ranges and combos.

.. code-block:: KL

    FabricCanvasEditPort -m "canvasNode1" -e "" -n "x" -d "factor" -p "In" -t "Scalar" -ui "";

FabricCanvasExplodeNode
-------------------------------------

Explodes a sub graph node and moves all of the contains nodes into the parent graph.

  - -m, -mayaNode: The name of the Canvas maya node
  - -e, -execPath: The path of the node inside of Canvas to operate on
  - -n, -nodeName: The name of the subgraph node to explode

.. code-block:: KL

  FabricCanvasExplodeNode -m "canvasNode1" -e "" -n "graph_2";

FabricCanvasGetContextID
-------------------------------------

Returns the FabricCore client contextID used by Canvas Maya nodes. This is useful if you want to create a python FabricCore client, for example, to access the same data.

.. code-block:: kl

  FabricCanvasGetContextID;
  // Result: QmwISgSKKfQmqJYLnQuG9vtwrM/zvquvibDemkR8/TahGgHW9Z1yl9IlDFBRfl0nreQyb6yKtgfYrOHPyUdGDE1vBDD84M3D4ndWStI0ijIORlTepDtNOjEbmN8kArnX 

FabricCanvasGetBindingID
-------------------------------------

Returns the ID of the FabricCore DFGBinding used by a specified Canvas Maya node. This is useful if you want to create a python FabricCore client, for example, to access the same data.

  - -n, -node: The name of the Canvas maya node

.. code-block:: kl

  FabricCanvasGetBindingID -n "canvasNode1";
  // Result: 6119 // 

FabricCanvasImplodeNodes
-------------------------------------

Implodes a selection of nodes and create a new subgraph node containing them.

  - -m, -mayaNode: The name of the Canvas maya node
  - -e, -execPath: The path of the node inside of Canvas to operate on
  - -n, -nodeName: The names of all of the nodes to implode. Separated by the pipe character.
  - -d, -desiredImplodedNodeName: The desired name of the new subgraph node

.. code-block:: KL

  FabricCanvasImplodeNodes -m "canvasNode1" -e "" -n "Vec3|Scalar|Report" -d "implodedGraph";

FabricCanvasInstPreset
-------------------------------------

Creates a new node by instantiating an existing Canvas preset.

  - -m, -mayaNode: The name of the Canvas maya node
  - -e, -execPath: The path of the node inside of Canvas to operate on
  - -x, -xPos: The x coordinate for placing the new node
  - -y, -yPos: The y coordinate for placing the new node
  - -p, -presetPath: The path for the preset to instantiate

.. code-block:: KL

  FabricCanvasInstPreset -m "canvasNode1" -e "" -p "Fabric.Exts.Math.Vec3.Vec3" -x "162" -y "62";

FabricCanvasMoveNodes
-------------------------------------

Moves a single or multiple nodes in the Canvas graph.

  - -m, -mayaNode: The name of the Canvas maya node
  - -e, -execPath: The path of the node inside of Canvas to operate on
  - -n, -nodeName: The name(s) of the node(s) to move
  - -x, -xPos: The x coordinate(s) for moving the node(s)
  - -y, -yPos: The y coordinate(s) for moving the node(s)

.. code-block:: KL

  FabricCanvasMoveNodes -m "canvasNode1" -e "" -n "Vec3_2" -x "215" -y "23";
  FabricCanvasMoveNodes -m "canvasNode1" -e "" -n "Scalar|Vec3_2" -x "97|248" -y "295|41";

FabricCanvasPaste
-------------------------------------

Creates nodes in the Canvas graph based on a JSON text

  - -m, -mayaNode: The name of the Canvas maya node
  - -e, -execPath: The path of the node inside of Canvas to operate on
  - -t, -text: The JSON content for the nodes to paste
  - -x, -xPos: The x coordinate of the center of the freshly pasted nodes
  - -y, -yPos: The y coordinate of the center of the freshly pasted nodes

.. code-block:: KL

  FabricCanvasPaste -m "canvasNode1" -e "" -t "{\n  \"nodes\" : [\n    {\n      \"objectType\" : \"Inst\",\n      \"name\" : \"func\",\n      \"ports\" : [],\n      \"definition\" : {\n        \"objectType\" : \"Func\",\n        \"title\" : \"func\",\n        \"ports\" : [],\n        \"extDeps\" : {},\n        \"code\" : \"\"\n        }\n      }\n    ],\n  \"connections\" : []\n  }" -x "680" -y "80";

FabricCanvasRemoveNodes
-------------------------------------

Removes a single or multiple nodes from the Canvas graph.

  - -m, -mayaNode: The name of the Canvas maya node
  - -e, -execPath: The path of the node inside of Canvas to operate on
  - -n, -nodeName: The name(s) of the node(s) to remove

.. code-block:: KL

  FabricCanvasRemoveNodes -m "canvasNode1" -e "" -n "Vec3";
  FabricCanvasRemoveNodes -m "canvasNode1" -e "" -n "Scalar|Vec3_2";

FabricCanvasRemovePort
-------------------------------------

Removes port(s) from the Canvas graph.

  - -m, -mayaNode: The name of the Canvas maya node
  - -e, -execPath: The path of the node inside of Canvas to operate on
  - -n, -portName: The name of the port(s) to remove

.. code-block:: KL

  FabricCanvasRemovePort -m "canvasNode1" -e "" -n "factor";

.. code-block:: KL

  FabricCanvasRemovePort -m "canvasNode1" -e "" -n "factorX|factorY|factorZ|resultXYZ";

FabricCanvasRenamePort
-------------------------------------

Renames a port in the Canvas graph.

  - -m, -mayaNode: The name of the Canvas maya node
  - -e, -execPath: The path of the node inside of Canvas to operate on
  - -n, -oldPortName: The name of the port to rename
  - -d, -desiredNewPortName: The desired new name for the port

.. code-block:: KL

  FabricCanvasRenamePort -m "canvasNode1" -e "" -n "factor" -d "strength";

FabricCanvasReorderPorts
-------------------------------------

Reorders the ports of a Canvas graph or sub graph

  - -m, -mayaNode: The name of the Canvas maya node
  - -e, -execPath: The path of the node inside of Canvas to operate on
  - -p, -itemPath: The path to the item
  - -i, -indices: The new index order for the ports

.. code-block:: KL

  FabricCanvasReorderPorts -m "canvasNode1" -e "" -p "" -i "[1, 0, 2]";

FabricCanvasResizeBackDrop
-------------------------------------

Resizes a backdrop inside of a Canvas graph

  - -m, -mayaNode: The name of the Canvas maya node
  - -e, -execPath: The path of the node inside of Canvas to operate on
  - -n, -nodeName: The name of the backdrop node  
  - -x, -xPos: The x coordinate for the backdrop
  - -y, -yPos: The y coordinate for the backdrop
  - -w, -width: The new width for the backdrop
  - -h, -height: The new height for the backdrop

.. code-block:: KL

  FabricCanvasResizeBackDrop -m "canvasNode1" -e "" -n "backdrop" -x "248" -y "280" -w "401" -h "131";

FabricCanvasSetArgValue
-------------------------------------

Sets the value of an argument in a Canvas graph.

  - -m, -mayaNode: The name of the Canvas maya node
  - -n, -argName: The name of the argument
  - -t, -type: The new data type for the argument
  - -v, -value: The JSON encoding the value

.. code-block:: KL

  FabricCanvasSetArgValue -m "canvasNode1" -n "Vec3.x" -t "Float32" -v "1";

FabricCanvasSetCode
-------------------------------------

Sets the KL code for a KL function node inside a Canvas graph.

  - -m, -mayaNode: The name of the Canvas maya node
  - -e, -execPath: The path of the node inside of Canvas to operate on
  - -c, -code: The new KL code for the KL function node

.. code-block:: KL

  FabricCanvasSetCode -m "canvasNode1" -e "func" -c "dfgEntry {\n  //result = lhs + rhs;\n \n}\n";

FabricCanvasSetExtDeps
-------------------------------------

Sets the extension dependencies of a KL function node in a Canvas graph

  - -m, -mayaNode: The name of the Canvas maya node
  - -e, -execPath: The path of the node inside of Canvas to operate on
  - -xd, -extDep: The list of extension dependencies

.. code-block:: KL
  
  FabricCanvasSetExtDeps -m "canvasNode1" -e "func" -xd "Math:*";

FabricCanvasSetNodeComment
-------------------------------------

Sets the content of a node comment in a Canvas graph

  - -m, -mayaNode: The name of the Canvas maya node
  - -e, -execPath: The path of the node inside of Canvas to operate on
  - -n, -nodeName: The name of the node
  - -c, -comment: The text for the comment

.. code-block:: KL

  FabricCanvasSetNodeComment -m "canvasNode1" -e "" -n "Vec3" -c "My useful information";

FabricCanvasEditNode
-------------------------------------

Renames a node in a Canvas graph.

  - -m, -mayaNode: The name of the Canvas maya node
  - -e, -execPath: The path of the graph inside of Canvas to operate on
  - -n, -oldNodeName: The current name of the node
  - -d, -desiredNewNodeName: The desired new name for the node
  - -nm, -nodeMetadata: (Optional) Additional metadata for the node
  - -xm, -execMetadata: (Optional) Additional metadata for the executable (for instances)

.. code-block:: KL

  FabricCanvasEditNode -m "canvasNode1" -e "" -n "Vec3" -d "MyTitle";

FabricCanvasSetPortDefaultValue
-------------------------------------

Sets the default value of a port on a node in a Canvas graph

  - -m, -mayaNode: The name of the Canvas maya node
  - -e, -execPath: The path of the node inside of Canvas to operate on
  - -p, -portPath: The path to the port below the execPath
  - -t, -type: The type of the new default value
  - -v, -value: The JSON encoding the default value for the port

.. code-block:: KL

  FabricCanvasSetPortDefaultValue -m "canvasNode1" -e "" -p "Vec3.x" -t "Float32" -v "1";

FabricCanvasSetRefVarPath
-------------------------------------

Sets the reference variable path on a Canvas get or set node

  - -m, -mayaNode: The name of the Canvas maya node
  - -e, -execPath: The path of the node inside of Canvas to operate on
  - -n, -refName: The name of the get or set node to operate on
  - -p, -varPath: The new path of a variable to reference

.. code-block:: KL

  FabricCanvasSetRefVarPath -m "canvasNode1" -e "" -n "get" -p "factor";

FabricCanvasSplitFromPreset
-------------------------------------

Splits an executable (graph or function) from the preset it references

  - -m, -mayaNode: The name of the Canvas maya node
  - -e, -execPath: The path of the node inside of Canvas to operate on

.. code-block:: KL

  FabricCanvasSplitFromPreset -m "canvasNode1" -e "DrawMesh";

FabricCanvasDismissLoadDiags
-------------------------------------

Dismisses one or more load diagnostics

  - -m, -mayaNode: The name of the Canvas maya node
  - -di, -diagIndices: The indices of the load diagnostics to dismiss

.. code-block:: KL

  FabricCanvasDismissLoadDiags -m "canvasNode1" -di "[3, 14]";

FabricCanvasGetExecuteShared
----------------------------

Returns the current shared execution state.

  - -m, -mayaNode: The name of the Canvas maya node

.. code-block:: KL

  FabricCanvasGetExecuteShared -m "canvasNode1";

FabricCanvasSetExecuteShared
----------------------------

Enables/disables canvas nodes to be executed in parallel with the Maya parallel evaluation capabilities.

  - -m, -mayaNode: The name of the Canvas maya node
  - -e, -enable: 'true' to enable parallel evaluation, else 'false'

.. code-block:: KL

  FabricCanvasSetExecuteShared -m "canvasNode1" -e true;

dfgImportJSON
-------------

Sets the graph of a canvas node either from a canvas file or from a JSON string.

Note that one can only import graphs into empty Canvas nodes.

  - -m, -mayaNode: The name of the Canvas maya node
  - -p, -path: unused.
  - -f, -filePath: The path and filename of a .canvas file.
  - -j, -json: An optional JSON representation of a Canvas graph.
  - -r, -referenced: 'true' set as reference.

.. code-block:: KL

  dfgImportJSON -m "canvasNode1" -f "C:/test.canvas";

dfgExportJSON
-------------

Exports the graph of a canvas node as a .canvas file.

  - -m, -mayaNode: The name of the Canvas maya node
  - -p, -path: unused.
  - -f, -filePath: The path and filename of the output .canvas file.

.. code-block:: KL

  dfgExportJSON -m "canvasNode1" -f "C:/test.canvas";

dfgReloadJSON
-------------

Reloads the graph of a canvas node that references a .canvas file (see command "dfgImportJSON").

  - -m, -mayaNode: The name of the Canvas maya node
  - -p, -path: unused.
  - -f, -filePath: unused.
  - -j, -json: unused.
  - -r, -referenced: unused.

.. code-block:: KL

  dfgReloadJSON -m "canvasNode1";

