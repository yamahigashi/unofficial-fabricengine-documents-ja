.. _canvas-user-guide-valueeditor:

Value Editor
===============================

The Value Editor provides input widgets to drive values on Canvas nodes or the main graph.

.. image:: /images/Canvas/userguide_12.jpg

Each editable port of a node is shown as an entry in the widget list. Ports currently connected are not shown.

.. note:: You can edit the range and combo values of a port in the :dfn:`Edit Port` dialog, accessible through the port's context menu when editing a subgraph.


Editing Ports and Values
------------------------------

Port names can be changed on presets through the Value Editor as long as the preset has been split from the preset. Once split, you can double click on the name of a port in the value editor to edit.

The values of ports can be reset to their default values by right clicking on the widget label and selecting the ``Reset To Default`` menu option.

Array port size and range can be adjusted in the Value Editor. Array item widgets are added or removed as you adjust the array settings. Each array item can be set manually thereafter.


=================
Spin Box Widgets
=================

- Spin Box widgets can be manipulated by clicking and dragging on the up and down arrows to change the value along with the normal single clicks on the up and down arrows.

- Holding `Ctrl` while clicking and dragging will change the value with more precision.

- While clicking and draging, moving the cursor left, away from the widget, then moving up and down will increase precision. Moving the cursor right, away from the widget, will decrease precision and change the value more broadly.