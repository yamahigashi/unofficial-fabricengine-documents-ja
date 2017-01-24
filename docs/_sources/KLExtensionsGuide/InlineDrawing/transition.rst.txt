.. _inlinedrawing_extension_transition:

Transitioning from Pre-1.12.0 InlineDrawing
============================================

.. versionadded:: 1.12.0

Prior to version 1.12.0 the InlineDrawing type was used to create shapes and draw content into them. This is quite different to the functionality provided with 1.12.0. However there is an easy path for transition. Previously code would look like this:

.. code-block:: kl

    InlineDrawing draw = InlineDrawing();
    InlineShape shape = draw.getNewShape('debug');

    shape.drawTrianglesSphere(Xfo(), 2.0, 12);

    draw.drawShape('debug', Xfo(), Color(1.0, 0.0, 0.0));

All of the methods of the previous :dfn:`InlineShape` are now provided on the :ref:`inlinedebugshape`, so all of that code can be transitioned to use that type instead:

.. code-block:: kl

    InlineDrawing draw = handle.getDrawing();
    InlineDebugShape shape = draw.registerShape(InlineDebugShape('debug'));

    shape.drawTrianglesSphere(Xfo(), 2.0, 12);

    InlineShader flat = draw.registerShader(OGLFlatInlineShader());
    InlineMaterial red = flat.getOrCreateMaterial('red');
    red.addInstance(SimpleInlineInstance('redSphere', draw.getTransform(), shape));

.. note:: Instances, Materials etc build up in the drawing main container. Catch your scene building code in an if statement, or reset the drawing prior to building the scene.