.. _canvas-user-guide-polymorphism:

Polymorphic nodes
===============================

.. note:: If you are looking for a more technical explanation please refer to :ref:`canvas-programmer-guide-polymorphism` in the programmer guide.

Nodes in Canvas can be polymorphic. A polymorphic node supports more than one data type. Polymorphic ports appear black, since they don't have a data type yet. Upon connection the port will change its color and data type.

.. image:: /images/Canvas/userguide_17.jpg

.. note:: Polymorphic presets are put below the :dfn:`Func` category of each KL extension, so you need to use :dfn:`Func.unit` for example to find it.

Polymorphism is also supported in subgraphs. Any port defined on a subgraph by default is polymorphic until you connect something to it. If you in turn connect a polymorphic port to it, you can create full subgraphs which stay polymorphic until they are used for a specific data type.

.. image:: /images/Canvas/userguide_18.jpg
