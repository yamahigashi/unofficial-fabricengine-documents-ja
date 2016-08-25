.. _FabricForMaya.Canvas:

Canvas inside of Maya
=============================

.. image:: /images/Canvas/userguide_29.png

Canvas Node Types
--------------------

Fabric for Maya comes with two node types:

The CanvasNode is a generic MPxNode where you can attach almost every kind of maya attribute type, it is suited for any generic computation such as rigging or simulation solvers.

The CanvasDeformer is a deformer node that seamlessly works with Maya's deformation tools and commands and works with a PolygonMesh Array, allowing to modify the positions of a mesh without changing its topology. It is faster than CanvasNode for deformations since it avoids creating a new full mesh.

CanvasNode
--------------------

This is the main Canvas node and the one you will typically be using in your scenes.

You can instantiate the canvasNode in the node editor hitting :dfn:`TAB` and typing :dfn:`canvas` or through the Fabric top level menu and choosing :dfn:`Create graph (Node)`. You can then open up the Canvas graph through the :dfn:`Open Canvas` button on the Maya Attribute editor.

.. image:: /images/Canvas/userguide_30.jpg

CanvasDeformer
--------------------

This node is a variant of the Canvas node and it is specialized / optimized for deformations, taking advantage of Maya's deformation features. The benefit of using this node for deformations rather than the 'regular' Canvas node is a gain in speed of around 3x - 5x.

.. note:: The gain in speed comes at a price: the node is not as flexible as the 'regular' Canvas node and, more importantly, one must respect a certain way of building the Canvas graph. See following section for more detailed information.

You can instantiate the canvasDeformer in the node editor hitting :dfn:`TAB` and typing :dfn:`canvasDeformer` or through the Fabric top level menu and choosing :dfn:`Create graph (Deformer)` with an object selection. You can then open up the Canvas graph through the :dfn:`Open Canvas` button on the Maya Attribute editor.

When opening the Canvas graph you will notice there is a default an IO port called **meshes**.

.. note:: This port must not be removed nor renamed or else the deformer node will not work properly!.

The correct and safe way to apply a deformation consists of getting the array of vertex positions of a PolygonMesh element from the meshes PolygonMesh array (using Array.Get and GetAllPointPositions), modify the values of the array and finally setting the vertex positions on the output PolygonMesh to the meshes array with Array.Set.

The following image shows the correct way to do it.

.. image:: /images/Canvas/userguide_31.png

**A (get)** get the mesh from the array meshes and its point positions as an array of Vec3.

**B (do the magic)** perform the actual deformation by modifying the values of the Vec3 array. You can do whatever you want with the array just as long as you do *not modify its size, ie. the amount of elements in the array should not be changed*.

**C (set)** set the new vertex positions on the mesh and put the changes back into the array meshes.

 
Adding ports / attributes
----------------------------

The CanvasNode inside of Maya doesn't come with any attributes by default. It's so to say a generic node for any purpose. After opening up the Canvas user interface you can expose ports the normal way. Doing that will also add matching attributes to the Maya node, which allow you to connect data between the two worlds. The supported data types are;

  - Boolean
  - Integer / SInt32 / UInt32
  - Scalar / Float32 / Float64
  - String
  - Vec3
  - Euler
  - Color
  - Mat44
  - Lines
  - PolygonMesh

When using the dialog to create a port there are a couple of extra features within Maya.

.. image:: /images/Canvas/userguide_31.jpg

Native vs. multi arrays
-------------------------

Maya supports two types of arrays

  - Native: Maya has a way of representing a IntArray, DoubleArray or VectorArray as a single attribute. This is very efficient for large arrays and is much faster than using multi arrays.
  - Multi: Each element of the array has its own single plug, you can connect them to different things in the hyper graph and you can build up arrays interactively. This is very flexible, but much slower than native arrays.

Within Canvas you can choose which type of array you want - depending on your needs.

.. note:: Native arrays are only support for these types: :code:`Scalar[]`, :code:`Float32[]`, :code:`Integer[]`, :code:`SInt32[]`, :code:`Vec3[]`.

Opaque data
--------------------

By checking the :dfn:`opaque in DCC` checkbox causes Maya to use a special data type for the Maya attribute instead of reflecting it as a native type. These attributes can be connected between each other (from one Maya node to the next) without Maya interpreting the data. This is very useful when passing heavy data around which you don't need access to outside of Canvas, but you still want to pass it between Maya nodes. This is also very useful for passing data between Canvas Maya nodes which Maya is not able to reflect at all (for example a custom KL datastructure).

Port metadata
--------------------------

To drive some of the user interface features you can set metadata on the port. This will be picked up by Maya when creating attribute. Open the meta data section of the dialog when creating a port. Right now Maya supports only the :dfn:`range` settings.

.. image:: /images/Canvas/userguide_32.jpg

Maya evaluation of Canvas graphs
----------------------------------------

One important aspect to mention is that a Canvas Node is a Maya dependency graph node that is not connected to the Maya DAG. This means that the Canvas graph is going to be evaluated **only** when there is an output in the Canvas Node that is connected to the Maya DAG (i.e: a Vec3 output port connected to the Translate of a locator).

Loading / saving of Canvas graphs
----------------------------------------

You can save out Canvas graphs from Maya to disk and also load them back. To do this select the Canvas Maya node of choice and pick :dfn:`Load graph` or :dfn:`Save graph`.

.. note:: You can only load graphs into a Canvas Maya node which is empty.

Realtime Rendering
---------------------

You can draw into Maya's viewport directly from Canvas. For this you can use the :dfn:`EmptyDrawingHandle` node and consecutive nodes such as :dfn:`DrawingHandle.DrawPolygonMesh`. Please see the :code:`InlineDrawing` Canvas sample scenes for examples of this.

.. image:: /images/Canvas/userguide_33.jpg

.. note:: You need to provide a proper name (for the name port) for each of the drawing nodes when using multiple nodes consecutively.

Keyboard shortcuts
-------------------------

Canvas for Maya implements all standard :ref:`canvas-user-guide-shortcuts`.

