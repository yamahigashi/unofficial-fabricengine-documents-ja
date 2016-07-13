.. _GETTINGSTARTED_MAYATUTORIALS:

Fabric for Maya Tutorials
=====================================================

Driving a locator - Linear interpolation
--------------------------------------------

In this tutorial you will learn how to drive the position of a locator using Canvas. This is the first step towards using Canvas for rigging. Since |FABRIC_PRODUCT_NAME| provides a portable solution for any custom node within Maya, you'll be able to build flexible kinematic solutions which are portable between applications.

* Open a fresh Maya scene.

* Create three locators, place the first two somewhere to create a fictional line.

* Create a canvasNode by using the Fabric top menu: "Fabric -> Create Graph".

* With the canvasNode selected, click the Open Canvas button in the Maya Attribute Editor to get into the Canvas UI.

* Insert a "Func.LinearInterpolate" node ("Exts.Math.Func.LinearInterpolate").

* Expose the port "this" as input.

* Right-click on the exposed port and choose "Edit".

* Set the data type to "Vec3" and click on Ok. Note how all the previously black ports turn yellow, indicating that they are of type "Vec3".

* Expose the ports "other" and "t" as inputs and "result" as an output, so that your graph looks like this:

.. image:: /images/GettingStarted/12_maya_tut_00.png

* In the Maya Node Editor, connect the two driving locator's translate attributes to the two Vec3 inputs on the canvasNode.

* Connect the result attribute of the canvasNode to the third locator's translate attribute, so that things look about like this:

.. image:: /images/GettingStarted/12_maya_tut_01.png

* Play with the t attribute on the canvasNode to place the third locator between the other two.

* Now select "locator1" and move it around in the viewport.

Procedural mesh
--------------------------------------------

In this tutorial you will learn how to create a procedurally driven mesh within Maya. This is a very powerful concept and will allow you to create portable procedural assets driven by an Alembic reader or a Bullet Softbody simulation, for example. We'll focus on the basics in this tutorial to get you started.

* Open a fresh Maya scene.

* In the Maya Node Editor create a new mesh node and a canvasNode.

* With the canvasNode selected, click the Open Canvas button in the Maya Attribute Editor to get into the Canvas UI.

* Create an output port named "outMesh" of type PolygonMesh by right-clicking on the right Side Panel.

* In the Maya Node Editor, connect the "outMesh" attribute on the canvasNode to the "inMesh" attribute on the Maya mesh node, as shown here:

.. image:: /images/GettingStarted/13_maya_tut_01.png

* In the Canvas UI, add a "GetSphere" and connect it to the mesh mesh out port.

* Expose the other parameters of the GetSphere as needed and play with the settings in the Maya Attribute Editor:

.. image:: /images/GettingStarted/13_maya_tut_02.png

Debug Realtime Rendering
---------------------------------

In this tutorial you will learn how to harness the power of the |FABRIC_PRODUCT_NAME| InlineDrawing rendering system directly within the Maya viewport. This can be very useful if you want to draw auxiliary debug information such as axes, lines or points.

* Open a fresh Maya scene.

* In the Maya Node Editor create a locator and a canvasNode.

* With the canvasNode selected, click the Open Canvas button in the Maya Attribute Editor to get into the Canvas UI.

* Create an output port named "evaluateMe" of type Vec3 by right-clicking on the right Side Panel.

* In the Maya Node Editor, connect the "evaluateMe" attribute on the canvasNode to the "translate" attribute on the locator. This is required to force Maya to pull on the canvas graph for each draw of the locator.

* In the Canvas UI, create an EmptyDrawingHandle node.

* Add a GetEmptyDebugShape node and connect it to the DrawingHandle.

* Add a DrawSegmentedLine node and connect it to the DebugShape.

* Expose the "result" port as an output of the graph.

* Expose the "from" and "to" inputs of the DrawSegmentedLine node as inputs of the graph.

* Double click the DrawSegmentedLine node and set the segments to 12. Your graph should now look like this:

.. image:: /images/GettingStarted/14_maya_tut_02.png

* Change the values of "from" and "to" in the Maya Attribute Editor: a red segmented line is drawn between the two positions:

.. image:: /images/GettingStarted/14_maya_tut_03.png
