.. _inlinedrawing_extension_intro:

Introduction
============

.. versionadded:: 1.12.0

:ref:`inlinedrawing_extension` provides functionality for direct rendering into DCC viewports (such as Maya etc). For this the extension provides a series of KL interfaces. The inheritance hierarchy of the data structures is as follows:

.. kl-inheritance:: InlineEntity

The :kl-ref:`InlineDrawing` is the master object. It manages the :kl-ref:`InlineShader`, :kl-ref:`InlineShape` and :kl-ref:`InlineTransform` objects. It also provides a root :kl-ref:`InlineTransform`, which can be used to build up a transform hierarchy. The :kl-ref:`InlineTransform` is nestable, and can be used to represent a scene hierarchy.

.. image:: /images/Splice/inlinedrawing02.png
   :width: 550px
   :height: 236px

Each :kl-ref:`InlineTransform` can contain a series of :kl-ref:`Xfo` values, so it can be used to represent a single scene entity or the same scene entity instanced a series of times.

So building up a renderable scene involves:

- Defining shaders and materials
- Defining shapes
- Building a transform hierarchy
- Defining instances by combining shapes + transforms

For rendering textures the :kl-ref:`InlineTexture` interface is provided. Users can implement their own textures as well, but the InlineDrawing comes with a series of implementations already.

Shapes and textures are defined in a renderer-agnostic way. Special objects, called :dfn:`adaptors` are used to perform the translation of the shape data to the renderer specific version. The generic objects provided by the InlineDrawing extension are:

- :kl-ref:`InlinePointsShape`: A specialized shape for efficient rendering of :kl-ref:`Points` objects.
- :kl-ref:`InlineLinesShape`: A specialized shape for efficient rendering of :kl-ref:`Lines` objects.
- :kl-ref:`InlineMeshShape`: A specialized shape for efficient rendering of :kl-ref:`PolygonMesh` objects.
- :kl-ref:`InlineDebugShape`: A specialized shape, providing debugging facilities, formerly known as the old InlineShape (pre 1.12.0).
- :kl-ref:`InlineFileBasedTexture`: A texture using the OpenImageIO extension to read a texture image.
- :kl-ref:`InlineProceduralTexture`: A texture driven by procedural content from KL.
- :kl-ref:`InlineMatrixArrayTexture`: A texture driven by a matrix array. This is particularly useful for crowd rendering.

Since most of the InlineDrawing objects required are just interfaces, a specialized implementation has to be used. For OpenGL direct rendering the extension provides a series of KL objects:

- :kl-ref:`OGLInlineDrawing`: The OpenGL version master InlineDrawing object
- :kl-ref:`OGLInlineShader`: A generic GLSL shader which performs GLSL code compilation.
- :kl-ref:`OGLPointsShapeAdaptor`: A specialized adaptor for handing rendering of :kl-ref:`InlinePointsShape` shapes.
- :kl-ref:`OGLLinesShapeAdaptor`: A specialized adaptor for handling rendering of :kl-ref:`InlineLinesShape` shapes.
- :kl-ref:`OGLMeshShapeAdaptor`: A specialized adaptor for handling rendering of :kl-ref:`InlineMeshShape` shapes.
- :kl-ref:`OGLDebugShapeAdaptor`: A specialized adaptor for handling rendering of :kl-ref:`InlineDebugShape` shapes.
- :kl-ref:`OGLColorTextureAdaptor`: A specialized adaptor for handling textures such as the :kl-ref:`InlineFileBasedTexture` or the :kl-ref:`InlineProceduralTexture`.
- :kl-ref:`OGLMatrixArrayTextureAdaptor`: A specialized adaptor for handling :kl-ref:`InlineMatrixArrayTexture` textures.

Furthermore presets of the :kl-ref:`OGLInlineShader` are provided.
