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

FabricCanvasAddBackDrop
-------------------------------------

Adds a new backdrop node to the Canvas graph.

  - -m, -mayaNode: The name of the Canvas maya node
  - -e, -execPath: The path of the node inside of Canvas to operate on
  - -x, -xPos: The x coordinate for placing the new node
  - -y, -yPos: The y coordinate for placing the new node
  - -t, -title: The name of the new node

.. code-block:: KL

    FabricCanvasAddBackDrop -m "canvasNode1" -e "" -t "MathNodes" -x "265" -y "132";

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

FabricCanvasAddPort
-------------------------------------

Adds a new port to a given node.

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
  - -s, -srcPortPath: The path to the source (left) port / pin
  - -d, -dstPortPath: The path to the destination (left) port / pin

.. code-block:: KL

  FabricCanvasConnect -m "canvasNode1" -e "" -s "Scalar.value" -d "Vec3.z";

FabricCanvasDisconnect
-------------------------------------

Disconnects two pins / ports inside a Canvas graph.

  - -m, -mayaNode: The name of the Canvas maya node
  - -e, -execPath: The path of the node inside of Canvas to operate on
  - -s, -srcPortPath: The path to the source (left) port / pin
  - -d, -dstPortPath: The path to the destination (left) port / pin

.. code-block:: KL

  FabricCanvasDisconnect -m "canvasNode1" -e "" -s "Scalar.value" -d "Vec3.z";

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

Disconnects two pins / ports inside a Canvas graph.

  - -n, -oldPortName: The old name of the port
  - -d, -desiredNewPortName: The desired new name of the port
  - -t, -typeSpec: The wanted datatype of the port
  - -xd, -extDep: An additional extension dependency of the port
  - -ui, -uiMetadata: Additional metadata, such as UI ranges and combos.

.. code-block:: KL

    FabricCanvasEditPort -m "canvasNode1" -e "" -n "x" -d "factor" -t "Scalar" -ui "";

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
  - -d, -desiredNodeName: The desired name of the new subgraph node

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
  - -n, -nodeName: The name(s) of the node(s) to move

.. code-block:: KL

  FabricCanvasRemoveNodes -m "canvasNode1" -e "" -n "Vec3";
  FabricCanvasRemoveNodes -m "canvasNode1" -e "" -n "Scalar|Vec3_2";

FabricCanvasRemovePort
-------------------------------------

Removes a port from the Canvas graph.

  - -m, -mayaNode: The name of the Canvas maya node
  - -e, -execPath: The path of the node inside of Canvas to operate on
  - -n, -name: The name of the port to remove

.. code-block:: KL

  FabricCanvasRemovePort -m "canvasNode1" -e "" -n "factor";

FabricCanvasRenamePort
-------------------------------------

Renames a port in the Canvas graph.

  - -m, -mayaNode: The name of the Canvas maya node
  - -e, -execPath: The path of the node inside of Canvas to operate on
  - -n, -name: The name of the port to rename
  - -d, -desiredName: The desired new name for the port

.. code-block:: KL

  FabricCanvasRenamePort -m "canvasNode1" -e "" -n "factor" -d "strength";

FabricCanvasReorderPorts
-------------------------------------

Reorders the ports of a Canvas graph or sub graph

  - -m, -mayaNode: The name of the Canvas maya node
  - -e, -execPath: The path of the node inside of Canvas to operate on
  - -i, -indices: The new index order for the ports

.. code-block:: KL

  FabricCanvasReorderPorts -m "canvasNode1" -e "" -i "[1, 0, 2]";

FabricCanvasResizeBackDrop
-------------------------------------

Resizes a backdrop inside of a Canvas graph

  - -m, -mayaNode: The name of the Canvas maya node
  - -e, -execPath: The path of the node inside of Canvas to operate on
  - -x, -xPos: The x coordinate for the backdrop
  - -y, -yPos: The y coordinate for the backdrop
  - -w, -width: The new width for the backdrop
  - -h, -height: The new height for the backdrop

.. code-block:: KL

  FabricCanvasResizeBackDrop -m "canvasNode1" -e "" -n "backdrop" -x "248" -y "280" -w "401" -h "131";

FabricCanvasSetArgType
-------------------------------------

Changes the data type for an argument of the Canvas graph.

  - -m, -mayaNode: The name of the Canvas maya node
  - -n, -name: The name of the argument
  - -t, -type: The new data type for the argument

.. code-block:: KL

  FabricCanvasSetArgType -m "canvasNode1" -n "factor" -t "Float32";

FabricCanvasSetArgValue
-------------------------------------

Sets the value of an argument in a Canvas graph.

  - -m, -mayaNode: The name of the Canvas maya node
  - -n, -name: The name of the argument
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

FabricCanvasSetTitle
-------------------------------------

Sets the title of an executable in a Canvas graph

  - -m, -mayaNode: The name of the Canvas maya node
  - -e, -execPath: The path of the executable inside of Canvas to operate on
  - -t, -title: The new title for the executable

.. code-block:: KL

  FabricCanvasSetTitle -m "canvasNode1" -e "" -t "MyTitle";

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
