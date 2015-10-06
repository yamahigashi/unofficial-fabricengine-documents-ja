.. _canvas-programmer-guide-caches:

Caches
===============================

.. note:: If you are looking for a less technical explanation please refer to :ref:`canvas-user-guide-caches` in the user guide.

Caches in Canvas are data points which save a copy of the computed value and refrain from recomputing it if none of the upstream inputs have changed. This is useful for branches in graphs which are expensive to compute.

Caches return immutable values, since it should not be possible for you to change the content of a reference counted data structure down stream (please see :ref:`canvas-programmer-guide-referencetypes` for more information). If you want to modify the returned value you'll have to use a :dfn:`Clone` node.

.. image:: /images/Canvas/userguide_25.jpg

Caches are not to be mixed up with :ref:`canvas-programmer-guide-variables`. Caches are not guaranteed to be kept in memory. A memory manager might decide to clear them. The assumption is that it's always possible to recompute the cache deterministically. You can not rely on the cache to always be kept around, if you need a guaranteed container please use a variable.

Any Canvas node supports caching, however for simplicity and visibility we've chosen to expose it to the user as a special node. Essentially that node is just a pass through node which has caching turned on. You can enable caching on your own presets only through the :ref:`canvas-programmer-guide-kl2dfg`, using the :dfn:`dfgPresetCacheRule` doxygen qualifier and choosing :dfn:`always` as the value.
