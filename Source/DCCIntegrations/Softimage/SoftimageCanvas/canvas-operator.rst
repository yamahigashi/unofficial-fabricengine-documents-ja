Custom Operator "CanvasOp"
================================

The *CanvasOp* operator ensures communication between Softimage and Fabric and allows controlling Fabric graph's inputs using conventional Softimage parameters and objects. The operator then executes the graph and passes the results of the calculations back to Softimage.

The operator is always attached under the global kinematics of an object, regardless of the object's type. It can, however, be connected with other parts of the same object, as well as with parts of other objects. For example you can have a null with a Canvas operator that controls the geometry of one, two or more polygon meshes.

Its property page contains a set of tools to set up connections between the graph and Softimage and to open *Fabric Canvas*, the node editor.

Property Page - Tab "Main"
---------------------------

This tab contains the exposed Canvas graph's ports.

  - **Execute Graph**

    Enables/disables the execution of the graph.

    Unchecking this parameter is similar to muting the operator.

  - **Open Canvas**

    Opens a modal floating window showing Fabric Canvas node editor.

    *Note: Softimage's main window is disabled as long as the Canvas window is open! Once you close Canvas Softimage's main window will be active and responsive again.*

  - **Parameters**

    The parameters of the graph's exposed ports.


Property Page - Tab "Ports and Tools"
---------------------------

This tab displays the list of available input and output ports of the Canvas graph and provides information on how they are currently exposed to Softimage. It also provides a set of tools to define the types of exposed ports, connect and disconnect ports, import/export graphs and log information into the history log.

  - **Execute Graph**

    See tab "Main" above.

  - **Open Canvas**

    See tab "Main" above.

  - **Graph Ports**

    The list of input and output ports of the graph with each port's name, type, mode and target.

  - **Update UI**

    Forces the property page to update itself, ensuring that the list of graph ports is up to date. Generally you do not need to do this (it is done automatically).

  - **Define Type/Target**

    Opens a window to define in what way a port is to be exposed.

    Ports can either be internal (i.e. not exposed) or exposed as Softimage parameters, Softimage ports or ICE ports.

  - **Connect (Pick)**

    Lets you pick the target for a Softimage port: first select a port in the above list, then click on "Connect (Pick)" and finally pick the target.

  - **Connect with Self**

    This will connect a Softimage port with the object to which the Canvas operator belongs to.

  - **Disconnect**

    Disconnects the target from a Softimage port: first select a port in the above list, then click on "Disconnect" to disconnect the target..

  - **Sync Op**

    Synchronizes the Canvas graph and the Softimage Canvas operator in the sense that all exposed Fabric parameters have their respective Softimage parameter or port. This is usually done automatically but in certain cases the graph and the operator could get out of sync (e.g. renaming or reordering ports in Canvas).

    *Note: the property page notices when synchronization has been lost and will display a little red exclamation mark next to this button to inform you about it. Then just click the "Sync Op" button to resync again.*

  - **Select connected Objects**

    The buttons "All", "Inputs" and "Outputs" let you select all the objects that are in some way connected to the operator. This is a convenient way to quickly check what objects in your scene are connected to an operator.

  - **File**

    Use "Import Graph" to replace the current graph by a graph contained in a file.

    Use "Export Graph" to save the current graph to disk.

  - **Log Graph Info**

    Logs information about the graph into the history log.

  - **Log Graph File**

    Logs the text representation of the current graph into the history log. This is the exact same text that is written to disk when using "Export Graph".

    *Note: those texts can get quite big and Softimage might not display the entire text in the history log.*

Property Page - Tab "Advanced"
---------------------------

This tab displays more advanced parameters that define the operator's behavior and how the graph is executed. 

  - **Verbose**

    If enabled then some (rather extensive) verbose is outputted into the history log whenever the operator gets called. This is mainly for debugging purpose.

  - **Exec Mode**

    Controls how the graph gets executed:
      - "execute graph only if necessary" will keep track of whether the graph is up to date or not and only execute it if necessary. This is the default.
      - "always execute graph" will execute the graph each time the operator gets evaluated.

  - **persistenceData**

    This is used internally.

  - **Mute**

    Mutes the operator.

  - **Always Evaluate**

    Forces Softimage to always evaluate the operator.

  - **Debug**

    Logs debug information into the history log.

  - **Name**

    The name of the operator.

  - **-**

    This button is for debugging and development and can be ignored.
