.. _GETTINGSTARTED_SOFTIMAGETUTORIALS:

Fabric for Softimage Tutorials
=====================================================

Procedural mesh
--------------------------------------------

In this tutorial you will learn how to create a procedurally driven mesh within Softimage. This is a very powerful concept and will allow you to create portable procedural assets driven by any KL extension, for example an Alembic reader or a Bullet Softbody simulation. We'll focus on the basics in this tutorial to get you started.

* Start with a new Softimage scene.

* Go into the Fabric menu and choose "Create Polymesh with Graph" to create a ready-to-use polygon mesh with a Canvas operator. After a short moment the property page of the operator will show up.

* Open the Canvas UI by clicking on the button "Open Canvas" in the property page.

* Click into the main area (where you can see a little "Press TAB to insert nodes") and then press the TAB key. This will start the tab search. Enter "gettor" and press return. A "GetTorus" node is added to your graph.

* Now we are going to expose the output of the "GetTorus" node so that we can use it to set the geometry of an object in our scene: left-click on the "mesh" port and then drag it to the black "Expose" port on the right and release the mouse button. Your graph should now look like this:

.. image:: /images/GettingStarted/21_softimage_tut_01.png

* Close the Canvas window and, in the property page, switch to the "Ports and Tools" tab. There you should see the port that you just exposed: "mesh | PolygonMesh | Out | Internal".

* The type of the port is still "internal" and in order to be able to connect it with an object we need to change its type. Click on the button "Define Type/Target", set the port's type to "XSI Port" and press "Okay". The property page gets updated.

* The last thing left to do is to connect the port with a polygon mesh. In the property page select the port by clicking on its name (the cell containing the word "mesh") and then click on the button "Connect with Self". 

.. image:: /images/GettingStarted/21_softimage_tut_02.png

* You should now see a torus in the viewport.

Mesh deformer
--------------------------------------------

An step-by-step tutorial of how to create a mesh deformer.

* Start with a new Softimage scene.

* Get a polygon mesh, for example "Get -> Primitive -> Polygon Mesh -> Torus". Set the U and V subdivision to 128 and 64, so that we will have more detail later on.

* Select the polygon mesh and add a Canvas operator to it by going into the Fabric menu and choosing "Create Graph". After a short moment the property page of the operator will show up.

* Open the Canvas UI by clicking on the button "Open Canvas" in the property page.

* Right-click on the left panel and choose "Create port". Set the title to "inMesh" and the data type to "PolygonMesh" and press OK.

* Now do the same on the right panel: right-click on the right panel and choose "Create port". Set the title to "outMesh" and the data type to "PolygonMesh" and press OK.

* Add a "Turbulize" node: press the TAB key, enter "turbulize" and choose "...Deform.Turbulize".

* Connect the "inMesh" port with the "Turbulize" node: left-click on "inMesh" and then drag it to the port "mesh" and release the mouse button. 

* Connect the "outMesh" port with the "Turbulize" node: left-click on "outMesh" and then drag it to the port "result" and release the mouse button. 

* Expose the "time" port of the "Turbulize" node: left-click on the "time" port and then drag it to the black "Expose" port on the left and release the mouse button. Your graph should now look like this:

.. image:: /images/GettingStarted/22_softimage_tut_01.png

* Close the Canvas window and, in the property page, switch to the "Ports and Tools" tab. There you see all the ports you just created: "inMesh", "outMesh" and "time".

* The type of the ports is still "internal" and in order to be able to connect them with an object we need to change their type. Click on the button "Define Type/Target", set the type of "inMesh" and "outMesh" to "XSI Port", the type of "time" to "XSI Parameter" and press "Okay". The property page gets updated.

* The last thing left to do is to connect the port with our polygon mesh. In the property page select the port "inMesh" by clicking on its name (the cell containing the word "inMesh") and then click on the button "Connect with Self". Do the same thing for the port "outMesh". Your torus should look like this:

.. image:: /images/GettingStarted/22_softimage_tut_02.png

* That's it, the deformer is finished! You should now see a turbulized torus and can start playing with the parameters, for example you can go into the tab "Main" and modify/animate the value of the "time" parameter. You can also go back to the torus settings and tweak the radius and subdivisions.

Driving a Null - Linear Interpolation
--------------------------------------------

Here you will learn how to drive the kinematic of a null. This is the first step towards using Canvas for rigging.

* Start with a new Softimage scene.

* Get two nulls and place them somewhere in your scene.

* Go into the Fabric menu and choose "Create Null with Graph" to create a third null with a Canvas operator. After a short moment the property page of the operator will show up.

* Open the Canvas UI by clicking on the button "Open Canvas" in the property page.

* Insert one "Func.LinearInterpolate" node.

* Insert two "Xfo.SetFromMat44" nodes.

* Insert one "Xfo.ToMat44" node.

* Connect everything and expose the "m", the "t" and the "result" ports so that your graph looks like this:

.. image:: /images/GettingStarted/23_softimage_tut_01.png

* Close the Canvas window and, in the property page, switch to the "Ports and Tools" tab.

* Click on "Define Type/Target" and set the type of the ports "m", "m_2" and "result" to "XSI Port" and the type of "t" to "XSI Parameter" and press "Okay". The property page updates itself and the graph ports should look like this:

.. image:: /images/GettingStarted/23_softimage_tut_02.png

* To complete the setup you need to connect the two nulls you created at the beginning of this tutorial with the "m" and "m_2" ports and the "result" port with the current null:
    - click on "m", then on "Connect (Pick)" and pick the first null.
    - click on "m_2", then on "Connect (Pick)" and pick the second null.
    - click on "result" and then on "Connect with Self".
  The graph ports should now look like this:

.. image:: /images/GettingStarted/23_softimage_tut_03.png

* Go to the tab "Main" and adjust the parameter "t" so that the third null is in between the two others. Now move, rotate and scale the first two nulls and see how the third one behaves.
