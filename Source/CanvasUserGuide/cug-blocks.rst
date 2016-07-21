.. _canvas-user-guide-blocks:

.. versionadded:: 2.3.0

Blocks
===============================

Blocks are containers for user-provided code.  Using blocks, users can customize the execution of complex nodes, and more advanced users can create new presets whose functionality is driven by user-provided blocks.

Blocks can be used to perform operations similar to for loops in traditional programming languages, but they are much more powerful that just that.  Blocks can also be used to check conditions, or multiple blocks can be used to do different things based on state.

As an example, the ``Fabric.Compounds.Blocks.Geometry.PolygonMesh.Deform`` preset (usually accessed via the tab menu through ``PolygonMesh.Deform``), takes both a ``mesh`` port that is to be deformed and a ``deform`` block that is the deformation itself:

.. image:: /images/Canvas/cug_blocks_deform_preset.png

By shift-double-clicking the node we enter into the definition of the block, more precisely referred to as the :dfn:`block instance`:

.. image:: /images/Canvas/cug_blocks_deform_preset_block_inst.png

Inside the block instance we see its default definition; in this case, it simply sets the value of the ``newPosition`` port to the value of the ``originalPosition`` port, i.e. doesn't actually deform anything.  However, we can edit this definition to produce the deformation effect that we want.

The block instance definition is unique to each Deform node; each Deform node can potentially specify a different deformation.

"Fixed" Block Ports
----------------------

The ports in the block instance shown with lock icons are called the :dfn:`fixed block ports`.  These ports are defined by the preset (in this case, the ``Deform`` preset) and not by the block instance; as such, they cannot be renamed, removed or reordered.  However, when the block instance is executed, the preset will provide input and IO fixed ports with a value to use and the preset will receive the values of IO and output ports to continue its work..  In the ``Deform`` case, the ``originalPosition`` and ``originalNormal`` values are provided to the block instance, and the block instance provides the resulting value ``newPosition`` back to the ``Deform`` preset.

Exposing Block Ports
-----------------------

In order to drive the functioning of the graph inside the block instance, you can expose ports outside to outside of the block.  For example, we might define our deformation as a simple push deformation driven by a single port ``amount``:

.. image:: /images/Canvas/cug_blocks_deform_push.png

Notice the non-fixed port ``amount``; this is the exposed block port.  Exposed block ports work just like regular block ports; for instance, they use the same polymorphism rules (see :ref:`canvas-user-guide-polymorphism`).  However, only input port can be exposed on blocks; it is not possible to expose IO or output ports.

If you use the "Back" button to go back to the previous graph, you see the exposed port:

.. image:: /images/Canvas/cug_blocks_deform_preset_exposed_port.png

Notice that the ``amount`` port is now available to connect to.  You can also expose new block instance ports using the block instance's header menu, just as for regular node ports.

Looking Inside Nodes with Blocks
--------------------------------------

By default, shift-double-clicking on a preset that has one or more block instance will edit the block instance under the mouse (or the first block instance if the top part of the node is under the mouse); this is because you usually want to edit the block when you're using a preset that uses blocks.  However, it is still possible to look inside the node itself to see how it works; to do so, right-click on the node to see the context menu, where you will find an "Edit Node" menu option.

Blocks Samples
--------------------

Fabric ships with several examples that highlight the use of blocks; they can be found in the directory :file:`$FABRIC_DIR/Samples/Canvas/Blocks`.  It is recommended to examine how these sample scene works to better understand how blocks work.

Blocks Presets
------------------

There are several new presets that ship with Fabric that are specifically for use with blocks; many of them can be found under ``Fabric.Compounds.Blocks`` in the Canvas Explorer window.  In addition to the ``PolygonMesh.Deform`` preset mentioned above, a few other that bear specific mention include:

``Fabric.Core.Control.ForLoop``
  A simple serial for loop that pulls its ``exec`` port for each iteration of the loop.

``Fabric.Compounds.Blocks.Array.Filter``
  Filters out elements of an array based on a condition that is exposed as a block.

``Fabric.Compounds.Blocks.Array.Modify``
  Creates a new array in a one-to-one fashion from an existing array.  In other programming systems this operation is often referred to as "Map".

``Fabric.Compounds.Blocks.Math.Accumulate``
  Replaces a value with a new value for a given number of iterations.  This is a very general purpose operation that can be used to create arrays, sum values, etc.  In some programming systems this operation is referred to as "Fold".

``Fabric.Compounds.Blocks.Math.AccumulateWhile``
  Like ``Fabric.Compounds.Blocks.Math.Accumulate`` except that it continues only while a certain condition (exposed by a block) is true.

``Fabric.Compounds.Blocks.Array.AnyElementMatches``
  Tests whether any element of an array matches the test in a block.

Using Blocks in Custom Graphs and Functions
--------------------------------------------------

You can use blocks in your own custom graphs and functions, either inline or exposed as presets.  For more information, see :ref:`the blocks section of the Canvas Programming Guide <canvas-programming-guide-blocks>`
