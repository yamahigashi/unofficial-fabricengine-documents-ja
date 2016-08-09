.. _canvas-programmer-guide-blocks:

.. versionadded:: 2.3.0

Blocks
===============================

This section describes some of the finer ports of using blocks within Canvas.  If you are not already familiar with blocks, please read :ref:`the blocks section of the Canvas User Guide first <canvas-user-guide-blocks>`.

To discuss blocks in more detail, it helps to be specific about certain terminology.  "Blocks" live in graphs and functions, and act as placeholders for graphs provided by instances of the graphs and functions (which are commonly referred to as "nodes").  These graphs provided by the instances are called "Block Instances". A node will have one block instance for each block in the graph or function that defines the node.  There can also be additional block instance exposed through "nested blocks", which are described further below.

Parallel Execution and Blocks
-------------------------------------

At this time Canvas is not safe for parallel evaluation of blocks.  However, future support for parallel evaluation is part of the design, and this will be addressed in the near future.

Using Blocks in Custom Graphs and Functions
--------------------------------------------------

You can expose blocks in custom graphs and functions that you use inline in your graph or that you save as presets; however, the way in which you do so is quite different in each case.

Exposing Blocks in Graphs
--------------------------------

To expose a block in a graph, right-click on the graph background and select "New Block" from the context menu.  You will be prompted to choose a name for the block.  The block will appear with a block-like shape so it is easily distinguished in the graph.

.. note:: It is not possible to create a block within the root graph or within a block instance graph; it is only possible in a subgraph of the root graph or of a block instance graph.  This is because it would not be possible to provide a definition for the resulting block!

.. image:: /images/Canvas/cpg-blocks-graph.gif

Once the block has been created, you can add ports to the block like you would any other node.  You can also edit, reorder and remove the ports by shift-double-clicking the block, where you will see the block port editor for the block.

Exposing Blocks in Functions
--------------------------------------

To expose a block inside a custom function, first open the function editor as usual.  Near the top of the editor are a set of tabs: a "Ports" tab where the ports can be added, edited, removed and rearranged, and a "Blocks" tab where the blocks can be added and removed.  To add a block, go to the "Blocks" tab, enter a name for the block and click "Add Block".  Once the block is added a new, additional tab will appear for the block where you can add ports to the block; these ports will appear as fixed ports in the block instances.

.. image:: /images/Canvas/cpg-blocks-func.gif

Once blocks have been added, you can pull a port of a block in the KL function code using the ``dfgPullBlockPort`` construct.  The syntax of ``dfgPullBlockPort`` is very specific:

  - The first parameter of ``dfgPullBlockPort`` is a string of the form ``"blockName.portName"``.  This is the name of the block port to be pulled.

  - One additional parameter for each input or IO parameter *of non-Execute type*.  These are the values that are provided to the input and IO fixed ports when the block instances are executed.

As a example, the ``Fabric.Core.Control.ForLoop`` preset has a single block ``body`` which has a single input port ``index`` and a single output port ``exec``.  The KL function code that defines it is:

.. code::

  dfgEntry {
    for ($TYPE$ index = 0; index < count; ++index)
      dfgPullBlockPort('body.exec', index);
  }

Nested Blocks
-----------------

A node will have one block instance for each block in the graph or function that defines the node.  In the case that a graph defines the node, the node will also have one block instance for each block defined inside a block instance inside the graph.  This is difficult to understand theoretically, but straightforward in practice: it allows you, for instance, to drop a ``ForLoop`` into the graph, and then put a block into the body of the loop; then this block will result in block instances on nodes backed by the graph.  The following animated GIF shows the process of creating a graph that prints a series of values produced by a nested block inside a ``ForLoop`` preset:

.. image:: /images/Canvas/cpg-blocks-nested.gif

For an example of how this is used in one of the presets, look at the definition of the ``Fabric.Compounds.Blocks.Image.Modify`` preset.

Polymorphism and Blocks
------------------------------

Block ports follow the same rules for polymorphism as normal graph and function ports.  The polymorphism matching for types is an operation that happens on both nodes and their block instance together; the ``ForLoop`` example above is a case where the ``count`` input port and the ``index`` input port for the block have the same polymorphic type ``$TYPE``.

Variables Inside of Blocks
----------------------------------

You can use variables within block instances.  However, variables declared inside the block instances will be reinitialized each time the block instance executes.
