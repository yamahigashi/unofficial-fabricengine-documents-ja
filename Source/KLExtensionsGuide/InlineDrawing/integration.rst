.. _inlinedrawing_extension_integration:

Integrating InlineDrawing in DCCs
===========================================================

.. versionadded:: 1.12.0

The Inline Drawing extension can be used directly with the provided OpenGL types to render into DCC viewports. This integration is provided for several DCCs, however it can be extended for additional products or in-house systems.

.. note:: You can find all of the KL types in the :ref:`inlinedrawing_extension`.

To ensure that the InlineDrawing is rendered, you'll need to construct a FabricCore::RTVal of the :ref:`drawcontext` object in C++:

.. code-block:: C++

    FabricCore::RTVal drawContext = FabricSplice::constructObjectRTVal("DrawContext");

You will then need to fill all of its members accordingly. See the KL snippet below for more detail.

.. kl-type:: DrawContext
  methods=0;
  example=0;
  inheritancegraph=0;

Once that is done you will need to call into Splice's rendering callback, as seen below, in C++:

.. code-block:: C++

      try
      {
        FabricSplice::SceneManagement::drawOpenGL(drawContext);
      }
      catch(FabricCore::Exception e)
      {
        myLogFunc(e.getDesc_cstr());
      }
      catch(FabricSplice::Exception e)
      {
        myLogFunc(e.what());
      }

This will render the content into the DCCs viewport directly.