.. _canvas-user-guide-variables:

Variables
===============================

.. note:: If you are looking for a more technical explanation please refer to :ref:`canvas-programmer-guide-variables` in the programmer guide.

Variables are special nodes in Canvas. A Variable is a container that carries a value (state) through different graph evaluations.  This can be especially useful to do simulations where the previous state of the system is usually required.

You can create a variable by right clicking the empty space in a graph view and choose "New variable". Alternatively you can type :dfn:`var` into the smart search (hit :dfn:`TAB` to open it).

.. image:: /images/Canvas/userguide_14.jpg

Variable nodes have a special color, which makes it easy to identify them in the graph.

You can read and write variables using the :dfn:`Get` and :dfn:`Set` nodes. These can also be created through the context menu or typing :dfn:`get` or :dfn:`set` and the name of the variable into the smart search.

For example, this subgraph below implements a simple simulation of a :dfn:`Float32` which adds up values over time: 

.. image:: /images/Canvas/userguide_15.jpg

Similarly, the graph below can be used to record a trail of a position value changing over time:

.. image:: /images/Canvas/userguide_16.jpg
