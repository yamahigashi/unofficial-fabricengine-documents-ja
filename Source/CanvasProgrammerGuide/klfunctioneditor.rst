.. _canvas-programmer-guide-klfunctioneditor:

KL Function Editor
===============================

Within Canvas you can directly create custom KL function nodes. These nodes run through the same just-in-time compilation process utilizing LLVM as do graphs. 

To create custom KL functions, right click the empty space in a graph view and choose :dfn:`New empty function`. This will create the function node and open the KL function editor. To open the KL function editor in an existing function node, double shift-click the node or open the context menu by right-clicking the node and choose :dfn:`Edit`.

.. image:: /images/Canvas/userguide_19.jpg

The KL function editor essentially contains two sections: The port list and the code window. 

KL function ports
---------------------
You can add and remove ports by defining their port type, name as well as data type. By default port types are polymorphic, but you can pick fixed types. If you want to know more about KL function polymorphism, please see :ref:`canvas-programmer-guide-polymorphism`. Alternatively you can also add a port by right clicking any entry in the port list and choose :dfn:`Add new port`.

To remove a port, right click it and choose :dfn:`Delete port` in the context menu.

.. note:: The KL function editor port list also supports the Ctrl-Enter (Add new port) and Ctrl-Backspace (Delete port) keyboard shortcuts.

Ports can be referenced by name in the KL code below.

.. note:: If you add a port with a data type which is implemented in a KL extension you have to add that extension to the :dfn:`Required Extensions` field on the top left.

.. note:: Reordering of ports in the KL function editor is not yet supported, but will be added in a future version.

Requirements field
----------------------
If a KL function node depends on an extension on disk, you will need to put the extension requirement definition into the requirements text field. For more information, please see :ref:`canvas-user-guide-graphview-requirements`.

KL code window
----------------------

The main entry point for the KL function node is the dfgEntry block. The Canvas compiler will replace the dfgEntry with the appropriate function declaration, containing all of the ports and features. Defining three :dfn:`Float32` ports as in image above, you can define an entry point like this:

.. code-block:: kl

    dfgEntry {
    
      result = cos(a) * b;

    }

Of course you can also implement operators directly within the KL function editor. So given you have two ports of type :dfn:`Float32[]`, for example, you can implement a task using PEX like this:

.. code-block:: kl

    operator task<<<index>>>(Float32 values[], io Float32 result[]) {
      result[index] = cos(values[index]);
    }

    dfgEntry {
      result.resize(values.size());
      task<<<values.size()>>>(values, result);
    }

To compile the KL function click on the :dfn:`Save` button on the top left. You can also reload the KL code for KL functions referencing an external preset file using the :dfn:`Reload` button. When leaving the KL function editor the UI will warn you in case you have unsaved changes.

For more information on KL's features, please see the :ref:`KLPG`.

.. note:: Even though it's possible to define data types within a KL function node, we highly recommend to implement KL types in a KL extension instead. This makes it much easier to track changes within the type for the Canvas compiler. You can ensure that the KL function loads the extension by adding the extension to the :dfn:`Required extensions` text field on the top left of the window.
