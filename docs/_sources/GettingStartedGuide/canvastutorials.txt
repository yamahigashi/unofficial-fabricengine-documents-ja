.. _GETTINGSTARTED_CANVASTUTORIALS:

Fabric Standalone Tutorials
=====================================================

Simple Hello World
--------------------------------------------

In this tutorial you will learn how to create nodes, how to connect up ports and how to assign values to untyped (black) ports.

Nodes and ports are key concepts within Canvas. As you learn, you will find yourself building more complex graphs, but the real power is in joining multiple nodes together to create a tool that simplifies your workflow and improves performance.

* Launch :dfn:`Fabric Standalone` (see :ref:`GETTINGSTARTED_FIRSTSTEPS`)

* Create a report node (Func.Report) - try hitting tab and type *rep* for example

* Expose the value port both as an input as well as an output (drag `report` node's left connection to left panel's Expose port, do the same on the right)

* Right click the input port (since it has no type), choose `Edit` and assign a *Float32* as the `data type`

* Show the Log Messages Window  (*Window* -> *Log Messages*)

* Double click the left panel to inspect the exposed ports in the value editor and pull the value_2 slider to see the log reporting the change.

.. image:: /images/GettingStarted/08_canvas_tut_01.png

First Math Formula
------------------------------

In this tutorial we will do a linear interpolation between two vectors and add the result to the original vector, then we will encapsulate this functionality into a graph. Math nodes are the back bone of most rigging tasks or simulation tasks, so it's good to start simple and build up from here.

* Create a generic Func.LinearInterpolate node. It will show in red since the type has not been defined yet and can't be evaluated.

.. image:: /images/GettingStarted/09_canvas_tut_02_1.png

* Expose the *this*, *other* and *t* ports as inputs

.. image:: /images/GettingStarted/09_canvas_tut_02_2.png

* Edit the this port type to Vec3. this and other will change to yellow.

.. image:: /images/GettingStarted/09_canvas_tut_02_3.png

* Create an Add node (Math.Add)

* Connect the result of the LinearInterpolate to the *lhs* port from the Add node

* Connect the *this* port of the LinearInterpolate to the *rhs* port of the Add node

* Expose the Add node's result to the sidebar

.. image:: /images/GettingStarted/09_canvas_tut_02_4.png

* Select both nodes

* Right click one of them and choose *Implode Nodes*, using *MyFormula* as the name

* Double click the left panel to inspect the exposed ports in the value editor and fill in some values and with the *t* slider

.. image:: /images/GettingStarted/09_canvas_tut_02.png

Animated Geometry
--------------------------

In this tutorial we'll create some procedural geometry and draw it on the screen. Canvas can be used to massage geometry, which is a very powerful concept. Even though this example is simple the concept also applies to scenarios such as loading data from Alembic or other formats and complex procedural content. Given that Canvas graphs are portable this allows to build geometry pipelines between DCCs.

* Create a GetTorus node (Create.GetTorus)

* Create a DrawMesh node (Display.DrawMesh)

* Connect the mesh output port from GetTorus to the mesh input port in DrawMesh

* Connect the drawThis output port from DrawMesh to the right Expose ports panel

.. image:: /images/GettingStarted/10_canvas_tut_03.png

* Create a new Float32 input port called *timeline*, which will automatically access the time in the graph

* Connect the timeline port to the inner and outer radius of the Add Torus node

* Pull on the time slider and see how the torus grows.

.. image:: /images/GettingStarted/10_canvas_tut_03_1.png

Custom KL Function
-----------------------

Writing KL function nodes is a very powerful feature in Canvas, since some problems are better suitable for code than graphs. In this tutorial we'll create a custom KL function node.

* Right click in Canvas, and choose *New empty function*, using *MyMultiply* as the name

.. image:: /images/GettingStarted/11_canvas_tut_04.png

* Shift double click on the node to enter the function definition dialog

* Fill in the name of the first port with the mode set to *in*, name to *a* and the type to *Float32*

* Add another port by hitting Ctrl+Enter or right click and choose *Add new port*

* Fill in the name of the second port with the mode set to *in*, name to *b* and the type to *Float32*

* Add the last port with the mode set to *out*, name to *result* and the type to *Float32*

* For the source code use: *result = a + a + b;*

.. image:: /images/GettingStarted/11_canvas_tut_04_1.png

* Hit *Save* and *Go Up* afterwards

* Expose the a and b ports in the left panel

* Expose the result in the right panel

* Double click the left panel to inspect the exposed ports in the value editor and see how the result changes accordingly

.. image:: /images/GettingStarted/11_canvas_tut_04_2.png

