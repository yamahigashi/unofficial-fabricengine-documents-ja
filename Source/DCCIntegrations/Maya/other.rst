.. _FabricForMaya.Other:

Other Goodies in Fabric for Maya
================================

Aside the Canvas node there are a few other things that are shipped with Fabric for Maya.

The "FabricConstraint" node
---------------------------

.. image:: /images/Canvas/userguide_34.jpg

The node :dfn:`FabricConstraint` is a standard pose constraint, implemented as a Maya C++ node. It was implemented primarily to increase the performance of Kraken rigs, but it can be used in any Maya DG. The node's output transformation is split into a :dfn:`Translate`, a :dfn:`Rotate` and a :dfn:`Scale` port, so it can also be used as a translation constraint, a rotation constraint, a scale constraint or any combination of the three.

To add a :dfn:`FabricConstraint` node to your Maya scene you can use the Tab search inside Maya's node editor or run the following MEL script:

.. code-block:: MEL

    createNode "fabricConstraint";

The node comes with the following input and output ports.

Inputs:
  - :dfn:`Input` - the matrix of the constraining object.
  - :dfn:`Offset` - the matrix for the constrain offset.
  - :dfn:`Parent` - the matrix of the constrained object's parent.

Outputs:
  - :dfn:`Translate` - the output translation.
  - :dfn:`Rotate` - the output rotation.
  - :dfn:`Scale` - the output scale.

Finally the node has an input parameter called :dfn:`rotateOrder` to define the order of rotation.
You can set the value of :dfn:`rotateOrder` either in Maya's attribute editor or via scripting.

The "CanvasFuncNode" node
-------------------------

This node is the 'techy' brother of the regular :dfn:`CanvasNode` node. With the :dfn:`CanvasFuncNode` you can only define ports and KL code, but no graph.

To add a :dfn:`CanvasFuncNode` node to your Maya scene you can use the Tab search inside Maya's node editor or run the following MEL script:

.. code-block:: MEL

    createNode "canvasFuncNode";

A new :dfn:`CanvasFuncNode` node is initially empty: it has no ports and no code other than the standard :dfn:`dfgEntry` block.

The "CanvasFuncDeformer" node
-----------------------------

This node is the 'techy' brother of the regular :dfn:`CanvasDeformer` node. With the :dfn:`CanvasFuncDeformer` you can only define ports and KL code, but no graph.

To add a :dfn:`CanvasFuncDeformer` node to your Maya scene you can use the Tab search inside Maya's node editor or run the following MEL script:

.. code-block:: MEL

    createNode "canvasFuncDeformer";

A new :dfn:`CanvasFuncDeformer` comes with a predefined `meshes` port of type `PolygonMesh[]` and no code other than the standard :dfn:`dfgEntry` block.

Maya deformer nodes are somewhat special and they need to be connected with the source/target Maya mesh in a certain way. The easiest way to create a complete and working setup is to select the polygon mesh in your Maya scene and then to run the following MEL script:

.. code-block:: MEL

    string $sel[];
    $sel = `ls -selection -exactType transform`;
    $d=`deformer -type "canvasFuncDeformer"`;
    select -r $d;
    FabricCanvasSetCode -m $d -e "" -c "dfgEntry \n{\n  if (meshes.size() > 0)\n  {\n    Vec3 p[] = meshes[0].getAllPointPositions();\n\n    // add your KL code here to\n    // modify the positions in p[];\n\n    meshes[0].setAllPointPositions(p);\n  }\n}";

The "enableEvalContext" hidden attribute
-----------------------------

Nodes have an attribute "enableEvalContext" which you can set to false. This will disable the evalContext functionality and should benefit the resulting performance. 

