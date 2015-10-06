.. _GETTINGSTARTED_FIRSTSTEPS:

First steps with Fabric Canvas
================================================

|FABRIC_PRODUCT_NAME| provides a standalone application, called :dfn:`Fabric Standalone`, as well as integrations 
into various DCCs. Once you have installed |FABRIC_PRODUCT_NAME| successfully, 
we recommend to make yourself familiar with :dfn:`Fabric Standalone` first before diving into the DCC integrations.

Test-Driving Fabric Standalone
----------------------------------------

To launch :dfn:`Fabric Standalone` double click on prompt.bat on Windows, or open up a shell, source the environment script and run `canvas`.

.. code-block:: bash

    source environment.sh
    canvas

Using `Git Bash <https://msysgit.github.io/>`_ on Windows it looks like this:

.. image:: /images/GettingStarted/03_bash_launch_canvas.png

.. note:: The look of the application may vary depending on the operating system. On Windows it looks like this:

.. image:: /images/GettingStarted/04_canvas_standalone.png

|FABRIC_PRODUCT_NAME| ships with a series of examples for the :dfn:`Fabric Standalone`. You can find them in the :dfn:`Samples/Canvas` folder below the root folder of the |FABRIC_PRODUCT_NAME| archive extraction location.

The :dfn:`Fabric Standalone` is divided into five areas in its default layout:

* The :dfn:`Preset Tree Explorer` (top left)
   
  In this view you access all of the available presets in the current session. The presets reflect most of the KL extensions available, including the Math extension and things like Alembic. Feel free to explore and look through the library.

* The :dfn:`Value Editor` (top right)
   
  This view is used to edit values through the user interface. To show widgets within the :dfn:`Value Editor` double click on any node.

* The :dfn:`Real-time 3D Viewport` (top center)

  This view is used to display realtime rendering content within the :dfn:`Fabric Standalone`. You can manipulate the camera by holding down :dfn:`ALT` and using the left mouse button for orbiting, middle mouse button for panning and right mouse button for dollying. You may also use the mouse wheel for dollying.

  .. note:: The camera interaction in :dfn:`Fabric Standalone` is modeled after Autodesk Maya.

  You can use the top level menu "View" in the :dfn:`Fabric Standalone` to toggle a standard 2D grid.

* The :dfn:`Canvas Graph` (center)

  This view is the heart of the visual programming system. It follows the Autodesk Maya interaction model as well. A few highlights and things to try:

  * Right click the side panels to add or remove ports
  * Hit tab in the view to start a quick search, hit enter to insert nodes
  * Copy and paste nodes and connected graph sections
  * Right click the canvas to create new subgraphs or KL functions  
  * Double click to inspect a selected node
  * Shift double click to edit a selected node
  * Press 1,2 and 3 to cycle from the different collapse states of nodes.
  * Press A to frame all the nodes in the graph
  * Right click on nodes for further actions  

* The :dfn:`Timeline` (bottom)

  This view is used to control the time of the application. You can set specific frame rates, drive time through the slider or through playback modes.
 
  .. note:: You can access the time in the graph by adding an input port called :dfn:`timeline` with either a Float32 or SInt32 type.

Further detailed information on the user interface can be found in the :ref:`CANVASUSERGUIDE`.

.. note:: The |FABRIC_PRODUCT_NAME| log is available as output in the shell the application was launched from, but you can also access it as a view in the application itself. Try :dfn:`Window` -> :dfn:`Log Messages`.

Test-Driving the |FABRIC_PRODUCT_NAME| Maya plugin
------------------------------------------------------------

After setting up the right environment variables (please refer to :ref:`GETTINGSTARTED_DCCINSTALLATION` for more info) you can just go ahead and launch Maya. Go to Window > Settings/Preferences > Plug-in Manager window to load the FabricMaya plugin, you will see a top menu like this:

.. image:: /images/GettingStarted/05_maya_plugin_manager.png

.. note:: Once it is loaded successfully we recommend restarting maya to persist the plugin manager's settings in the Maya preferences file.

To start using :dfn:`Fabric for Maya` you will have to create a Fabric Canvas node. You can do this through the Maya Node Editor, if you hit tab and type :dfn:`canvasNode` you will see it listed. Or hit the Fabric top menu, and choose :dfn:`Create Graph`. Once the node is created you should see this button in the Attribute Editor:

.. image:: /images/GettingStarted/06_maya_ui_a.png

Clicking the Open Canvas button will give you access the :dfn:`Fabric Standalone` user interface directly within Maya. You can dock the Canvas Editor like any other Maya widget.

.. image:: /images/GettingStarted/07_maya_ui_b.png

The capabilities of the :dfn:`Canvas Graph` user interface are exactly the same as in :dfn:`Fabric Standalone`. Notice that you can pull out the edges on the left to reveal the :dfn:`Preset Tree`, the edge on the right to reveal the :dfn:`Value Editor` and also the edge at the bottom to reveal the :dfn:`Log Messages`.

|FABRIC_PRODUCT_NAME| ships with a series of examples for use in :dfn:`Fabric for Maya`. You can find them in the :dfn:`Samples/FabricMaya/Canvas` folder below the root folder of the |FABRIC_PRODUCT_NAME| archive extraction location.

A few things to try when working with |FABRIC_PRODUCT_NAME| and a :dfn:`canvasNode` inside Maya:

* Exposing ports creates Maya attributes. Some of the data types currently supported are:

  * SInt32
  * Float32
  * String
  * Vec3
  * Color
  * Mat44
  * PolygonMesh

* You can load and save :dfn:`canvasNode` graphs through the top |FABRIC_PRODUCT_NAME| menu.

Test-Driving the |FABRIC_PRODUCT_NAME| Softimage plugin
------------------------------------------------------------

After setting up the right environment variables (please refer to :ref:`GETTINGSTARTED_DCCINSTALLATION` for more info) you can just go ahead and launch Softimage. To verify if the plugin is correctly installed you can open the Plugin Manager, it should look like this:

.. image:: /images/GettingStarted/20_softimage_plugin_manager.png

To start using :dfn:`Fabric for Softimage` you will have to create a CanvasOp operator for an object. The easiest way to do this is by using the Fabric top menu. Go into the Fabric menu and choose "Create Null with Graph": a null will be added to the scene with a CanvasOp operator attached under its global kinematics and the operator's property page will show up. Now click on the button "Open Canvas" and you should have something looking like this:

.. image:: /images/GettingStarted/20_softimage_null_with_canvas.png


The capabilities of the :dfn:`Canvas Graph` user interface are exactly the same as in the :dfn:`Fabric Standalone`. Notice that you can pull out the edges on the left to reveal the :dfn:`Preset Tree`, the edge on the right to reveal the :dfn:`Value Editor` and also the edge at the bottom to reveal the :dfn:`LogWidget`.

|FABRIC_PRODUCT_NAME| ships with a series of examples for use in :dfn:`Fabric for Softimage`. You can find them in the Softimage project :dfn:`Samples/FabricSoftimage/Canvas` folder below the root folder of the |FABRIC_PRODUCT_NAME| archive extraction location.

The recommended thing to do now is to load and play around with some of the samples scenes and then to do the Fabric for Softimage tutorials, see links below in the "What's next?" section.

.. note::

  When graph's top-level ports are added or removed, an explicit "Synch Op" operation might be required to reflect the changes as Softimage properties and ports, indicated by a red exclamation mark (illustrated below). More details on the mapping from Softimage to Canvas ports can be accessed in the "Ports and Tools" tab of the operator properties.
  
    .. image:: /images/GettingStarted/20_softimage_synchOps.png
 

What's next?
---------------------------

Once you have successfully tested the :dfn:`Fabric Standalone` as well as :dfn:`Fabric for Maya` or :dfn:`Fabric for Softimage`, there are a couple more things you can start looking at:

- :ref:`CANVASUSERGUIDE`

.. toctree::
  :maxdepth: 2
  
  canvastutorials
  mayatutorials
  softimagetutorials

If you want to get more technical, learn about existing KL extensions, write new Canvas KL functions or KL extension, get into advanced topics such as GPU compute there is also more information here:

- :ref:`CANVASPROGRAMMERGUIDE`
- :ref:`KLPG`
- :ref:`KLEXTENSIONSGUIDE`
- :ref:`EXTRG`

You can find all links on the top-level documentation page here: :ref:`TOP`.
