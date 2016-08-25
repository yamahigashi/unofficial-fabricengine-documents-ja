.. _canvas-user-guide-caches:

Caches
===============================

.. note:: If you are looking for a more technical explanation please refer to :ref:`canvas-programmer-guide-caches` in the programmer guide.

Caches are special nodes in Canvas. A cache node can be used to avoid computation on the left side of the cache in case nothing has changed. This is useful if you know that certain parts of a graph won't have to be executed again. To add a cache to the graph use the smart search hitting :dfn:`TAB` and type :dfn:`cache`.

.. image:: /images/Canvas/userguide_26.jpg

The result of a Cache node is immutable. This means that it cannot be changed further down the graph. If you need to change the content of a cache, you need to clone it first. Please be aware that cloning might be an expensive operation, so you should experiment a little bit with caches to see if they make sense in your scenario. To add a clone node to the graph use the smart search hitting :dfn:`TAB` and type :dfn:`clone`.

.. image:: /images/Canvas/userguide_25.jpg

