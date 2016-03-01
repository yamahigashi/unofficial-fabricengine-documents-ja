.. _canvas-user-guide-graphview:

Canvas Graph View
===============================

The Fabric Canvas Graph View interface is Fabric's node based editor. It lets you build graphs by adding and removing nodes, defining connections between them and creating new, custom nodes that contain either a sub-graph, KL code or a combination of both.

Canvas is available in all Fabric integrations, including Fabric Standalone, and the way you work with it is the same no matter which host application you use.

Creating nodes
----------------------

Nodes can be created in several ways.

  * Preset Tree: Look for the node you want to create in the preset tree. It provides access to all Fabric factory presets, as well as any presets found in the "Fabric/Presets/User" location from the user home folder and in the directories defined on the :envvar:`FABRIC_DFG_PATH` environment variable. Drag the preset you want to instantiate as a node into the graph view to create a node.
  * Tab Search: When focusing the graph view, hit the :dfn:`TAB` key to bring up the smart search. Then type the name of a part of the name of the preset you want to instantiate. For example try :dfn:`Math.Vec3.ComposeVec3` or :dfn:`MaVComp`.
  * Context menu: Special nodes, such as backdrops, empty graph nodes and function nodes can be created by right-clicking into Canvas and then choosing the respective entry of the context menu.

.. image:: /images/Canvas/userguide_02.jpg

.. image:: /images/Canvas/userguide_03.jpg

.. note:: Certain nodes can not be found using the type and the method name, for example :dfn:`Vec3.unit` does not exist, but you can find it looking for :dfn:`Math.unit`. The reason for this is that the preset is :ref:`polymorphic  <canvas-user-guide-polymorphism>`, and supports multiple types.

Node UI features
----------------------

.. image:: /images/Canvas/userguide_04.jpg

Nodes in Canvas provide a series of features through the UI:

  - Collapse Button

    Each node can be collapsed by clicking on the small icon on the right of the header of the node. 
    You can cycle through three states

      - Show all ports
      - Show only connected ports
      - Show no ports
      
    You can also collapse all the selected nodes at a specific state by respectively pressing 1, 2 or 3.

  - Header Ports

    All ports of a node can be accessed by clicking on the header ports next to the node label. This is especially useful when the node is currently collapsed.

  - Relaxation

    If you press Ctrl+R hotkey with a node selected, an automatic layout will be applied to all its children nodes.

    .. image:: /images/Canvas/userguide_05.jpg


  - Zoom

    If you press A hotkey, the view is framed so all the nodes are visible.
    If you press F hotkey, the view is framed on the current selected nodes.

  - Editing

    If you shift and double click over a node you will jump inside it. This will either
    show you the subgraph contained in the node, or the KL function defining the node. For more information on
    subgraphs and custom KL nodes see the sections further down on this page.

  - You can daisy chain inputs as well. To get to the daisy chain port of an input, just hover the right side of a node and it will show up.


Connecting nodes
----------------------

.. image:: /images/Canvas/userguide_06.jpg

You can connect nodes by clicking and dragging in a port. You can also shift click on a port to connect to multiple ports sequentially. Additionally you can use the header ports to get access to all ports of a node, even if the node is currently collapsed.

.. image:: /images/Canvas/userguide_07.jpg

You may only connect ports which are compatible. If you try to connect incompatible ports a tooltip will explain the reason for connection failure.

When clicking on the header port of a node you will get a list of ports decorated either with a '=' for in ports (to suggest that the port value is passed through) or '>' for out and io ports.

.. image:: /images/Canvas/header_port_connection.png

Exposing ports
----------------------

To make ports available to either the host application or the node hosting a subgraph, ports can be exposed. There are several ways to expose a port.

  - Right click on the side panel and choose :dfn:`Create port`. In the dialog you can then choose the respective name and, if you are creating the port on the top level graph, the data type of the port. If the data type is part of a specific extension, you should add the name of that extension in the :dfn:`advanced -> extension` field.

  - Connect the black :dfn:`Expose` port from either side panel to a port on a node. This will create the right exposed port and also connect it as well.

.. _canvas-user-guide-port-options:

Port options
----------------------

When doing :dfn:`Create port` or :dfn:`Edit port`, additional port options can be specified by expanding the `metadata` section.

- The :dfn:`visibility` combo box specifies how the port should be exposed to the host application (such as Maya).

  - `normal`: the port value should be mapped and converted, if possible, to host application's data type (attribute)

  - `opaque`: the port value should be handled as an opaque data type by the host application, which can allow to transport KL volatile objects between different host's graphs

  - `hidden`: the port should be unkown by the host application

- The :dfn:`persist value` checkbox is only available for top level graphs. When checked, it indicates that the port value must be persisted (saved) with the graph, else re-loading the graph will reset the value to its default. See :ref:`canvas-programmer-guide-valuepersistance` for technical details about value persistance.

  .. note:: The option is automatically set for edited values, or simple types reflected in the host application when in Maya or Softimage.

- The :dfn:`use range` checkbox allows to specify a range for UI value editing purposes (value is not clamped at runtime)

- The :dfn:`use combo` checkbox allows to set a list of combo box items for the UI, that will be mapped to 0..N-1 values

.. note:: Port dialogs for the top level graph may offer additional features in a specific host application, such as Maya, for example.

Execute ports
----------------------

Some nodes may offer a special port, called the :dfn:`Execute` port. It doesn't carry any data, it purely exist to allow daisy chaining of certain nodes. You can use it with the :dfn:`Execute.Merge` nodes, to describe a data flow. Please see :ref:`canvas-programmer-guide-kl2dfg` in the programmer guide for more information.

Subgraphs
----------------------

You can create subgraphs by right clicking on the empty space in a graph view and choosing :dfn:`New empty graph`. This will create a new node which contains a subgraph. To edit the subgraph, shift-double click the node or use its context menu and choose :dfn:`Edit`. You can leave the subgraph again by clicking on the :dfn:`Go up` button on the top right.  

.. image:: /images/Canvas/userguide_08.jpg

Imploding / exploding subgraphs
----------------------------------

A selection of nodes can be imploded into a new subgraph. For this, right click on a selection of nodes and choose :dfn:`Implode`. This will create a new node with a subgraph containing the selection of nodes. Any existing connections will be kept, and ports going into the subgraph will be exposed automatically.

With a subgraph node selected you can also perform the opposite operation: Explode. This will remove the subgraph node but insert all of its contained nodes into the current graph, maintaining all existing connections.

Copy and paste
--------------------
You can copy and paste nodes within Canvas using the system specific keyboard shortcuts. Canvas saves selected nodes or graphs as text to the system clipboard. The encoded JSON text can also be pasted into other applications, text editors or other open Canvas environments. This allows to directly copy and paste graphs between different DCCs.

.. _canvas-user-guide-graphview-requirements:

Defining extension requirements
-----------------------------------
Some graphs can depend on KL extensions on disk. If you wrote your own custom KL data structure, for example or if you downloaded a third party KL extension, you should specify that dependency in the :dfn:`Required Extensions` field in the top. This is useful if you are defining ports which use data types from a KL extension. The field can take a comma separated list of extensions, providing the name and the version required. Use a star for any version. The field is available both in the graph view as well as in the KL function editor. For example:

.. code-block:: bash

    Math:*,Utils:1.1

Saving / exporting presets
---------------------------------
Canvas nodes not attached to a preset are called :dfn:`inlined` nodes. They are saved with the graph which contains them. You can identify inlined nodes by their italic title as well as the :dfn:`*` in the header.

.. image:: /images/Canvas/userguide_20.jpg

Canvas nodes can be saved to disk in two ways. Exporting a node to an external file can be done by right-clicking any node and choosing :dfn:`Export graph`. This is useful if you want to share a preset with other users or upload it to a server, for example. This will NOT make the preset available to your canvas session however. Exporting a graph will retain the current types and values of the inputs.

Alternatively you can also create a preset out of any node. You can only create presets in directories on the :envvar:`FABRIC_DFG_PATH` environment variable. By default this contains the Fabric Engine factory installation folder (where you are not allowed to create presets) and a user folder below your system user's home folder. 

To create a preset out of a node, right-click the node and choose :dfn:`Create preset`.

.. image:: /images/Canvas/userguide_21.jpg

Pick the location where to create the preset. Note that you can also create new folders below any writable directory (not below the Fabric Engine factory installation path) by right-clicking the parent folder. Choose a folder and a name and hit :dfn:`Ok`. Now the node reflects the change by using a normal title font as well as missing the :dfn:`*` indicator.

You can also now create the node once more by using the name of the folder and the node name in the smart search.

.. image:: /images/Canvas/userguide_22.jpg

Custom KL nodes
----------------------

Canvas nodes can also contain a KL function. To create a KL function node right click on the empty space of the graph view and choose :dfn:`New empty function`. To edit the KL function shift-double click the node or use its context menu and choose :dfn:`Edit`. To learn more about custom KL function, please see :ref:`canvas-programmer-guide-klfunctioneditor` in the programming guide.

Backdrops
----------------------

Backdrops are special nodes which can be used to organize your work space. To create a backdrop right click the empty space in a graph view and choose :dfn:`New backdrop`. You can resize a backdrop by dragging on its corners. You can also change the backdrops color by right clicking it and choosing :dfn:`Properties`. Backdrops also will move the nodes contained in them. Just layout a node inside of the backdrop and then move the backdrop itself.

.. image:: /images/Canvas/userguide_09.jpg

Comments
----------------------

Any node in Canvas can contain comments. This is especially useful for users not familiar with a saved graph authored by someone else. You can add a comment by right clicking any node and choosing :dfn:`Set comment`. Likewise comments can be removed choosing :dfn:`Remove comment`. You can edit an existing comment by double clicking on it. Additionally you can collapse the comment by right clicking on it. Double clicking the yellow sticker brings it back up.

.. image:: /images/Canvas/userguide_10.jpg

.. note:: Comments can also be attached to Backdrops, which is useful to describe a whole section of nodes.
