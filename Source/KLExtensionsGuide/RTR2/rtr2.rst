.. _rtr2:

RealTime Renderer
=================

The `RTR` provides multiple components that can be assembled
for building a customized rendering pipeline. The RTR's goal is to provide
a good balance between performance and flexibility. The RTR is one of the
main components of the :ref:`SceneHub<scenehub>`, and is a client of the
:ref:`sceneassembly` graph.

.. _rtr2_overview:

RTR Overview
------------

As a framework, the `RTR` provides multiple building blocs that are
as much independent as possible, and at all levels ranging from
the higher-level renderer object to low-level tasks and render objects.

Additionally, the `RTR` separates the OpenGL-specific objects
from the ones that are not related to a specific drawing API.
The goal is to share most of the data processing tasks if more
drawing APIs such as DirectX are eventually supported.

Below is an illustration of the main components involved in the RTR,
using as an example the :kl-ref:`GLStandardRTR`:

.. image:: /images/SceneHub/RTRMainComponents.png

.. note::

  The :kl-ref:`GLStandardRTR` is a provided implementation
  for a standard (forward) OpenGL renderer, but others will be added
  in future releases, such as a deferred OpenGL renderer. Since
  this is a framework, custom renderer can be built too by reusing
  existing building blocs.

The principal steps that are part of the rendering processing of a scene
are, as illustrated above:

- A :ref:`SceneGraph<scenegraph_overview>` creates the scene data, which is filtered
  and processed by a :ref:`sceneassembly` procedural graph. A portion of that
  graph is RTR-specific, for example to cull the lights and geometries based on the
  camera fustum (volume).

- An higher-level renderer object, such as :kl-ref:`GLStandardRTR`, assembles the basic building blocs required for
  rendering the scene:

  - It connects to required inputs or :ref:`sceneassembly` groups, such as
    a :kl-ref:`RTRCamera`, and a scene geometries and scene lights :kl-ref:`BaseDynamicGroup`.

    The :kl-ref:`SceneGraphToGLStandardRTR` is a higher-level object that creates a
    default :ref:`sceneassembly` graph providing the required inputs for a :kl-ref:`GLStandardRTR`.

  - It creates a viewport object, such as the :kl-ref:`RTROGLViewport`, which wraps the main viewport.
    [multiple viewports support is planned in future releases]

  - It creates a RTR evaluation context, such as a :kl-ref:`RTROGLContext`, for providing
    the contextual data required by the rendering tasks (:kl-ref:`RTRCamera`,
    :kl-ref:`RTRDrawSurface`, :kl-ref:`RTRMaterialLibrary`, :kl-ref:`SWContext`).

  - It creates a :kl-ref:`RTRTaskScheduler`, which will collect and execute the various
    tasks for preparing and drawing RTR objects (:kl-ref:`RTRTask` and :kl-ref:`RTRDrawTask`).

  - It allows to define distinct rendering passes (layers), a which is simple way to
    draw overlays, selection or gizmos (see :kl-ref:`BaseRTR.insertPass`)

  - It is the starting point for data requests such as :kl-ref:`RaycastRequest`, which
    can traverse back from the RTR, through tasks and groups, to the SceneGraph (eg:
    :kl-ref:`BaseRTR.raycast`)

- A :kl-ref:`RTRTask` graph is defined for preparing RTR-specific data from the source
  scene data. Various steps might be involved:

  - Creating adaptors that will map scene objects to :kl-ref:`RTRInstance` objects.

  - Creating :kl-ref:`RTRDrawInstance` objects that will provide drawing parameters
    that depend on the camera and viewport (:kl-ref:`DrawSurface`) context.

    If preparation passes such as shadow map building are needed, a :kl-ref:`RTRDrawInstance`
    will be created for preparing the drawing for these tasks.

  Note that the created task graph is dynamic since it might change from
  frame to frame, for example if a new shadow-casting light enters
  camera's frustum.

- The :kl-ref:`RTRTask` will submit their associated :kl-ref:`RTRDrawTask` that
  will draw or setup their data for the draw API such as OpenGL.

- The :kl-ref:`RTRTaskScheduler` will run these tasks and draw tasks which
  will result in the final viewport image.

For more details about the SceneGraph to RTR translation steps, see
:ref:`sceneassembly_scenegraph_to_rtr` and :ref:`scenehub_adaptors`.

.. _rtr_related_extensions:

RTR related extensions
......................

The following extensions work in conjunction with the RTR extension at various levels:

- The Adaptors extension allows to define target-specific :kl-ref:`ObjectAdaptor`
  that can manage and cache the conversion from source objects (such as
  a :kl-ref:`PolygonMesh`) to a specific target (such as OpenGL RTR). These adaptors
  enable custom object types to be mapped to the RTR specific
  types and interfaces. See :ref:`scenehub_adaptors`

- The :ref:`sceneassembly` extension defines generic scene interfaces and objects
  that allow abstraction and processing of scene elements, and the :kl-ref:`SceneGraph`
  implement these interfaces. The RTR can augment this processing graph with its own
  nodes, for example to perform camera frustum culling.

- The :ref:`scenegraph_to_rtr_extension` defines adaptors for some :kl-ref:`SGObjectWrapper`
  objects to RTR objects, such as :kl-ref:`SGDirectionalLightToRTR`. It defines, too,
  higher-level wrappings of the :kl-ref:`SceneGraph` for configuring it as an RTR
  input, such as :kl-ref:`SceneGraphToRTR`.

- The OGLWrappers extension defines higher-level wrapping of OpenGL
  objects, such as :kl-ref:`OGLTexture` and :kl-ref:`OGLProgram`. It provides, too, functionality
  that is more closely related to RTR requirements, such as:

  - a `.glsl` preprocessor that can extract parameter meta-data and
    provide support for ``#include`` directives (see :ref:`simple_material`)

  - versioning of GL wrapped objects, and ability to prepare some data
    without a GL draw context

  - chaining of :kl-ref:`OGLProgramParamValues`: parameter value sets that can
    "inherit" from parent ones (see :kl-ref:`rtr_drawinstance`)

- The FabricOGL and OSOGL extensions define low-level wrapping of
  native OpenGL and OS-specific OpenGL extensions.

.. _rtr_drawinstance:

RTRDrawInstance and material parameters
---------------------------------------

One of the main purpose of the RTR tasks and draw tasks is to prepare and render a set of :kl-ref:`RTRDrawInstance`.
The :kl-ref:`RTRDrawInstance` contains the :kl-ref:`RTRMaterial` parameters values allowing to draw an object
such as a geometry.

For a single frame, a same draw object (:kl-ref:`RTRInstance`) might be rendered multiple times, for example:

- Once for each viewport and camera, if multiple viewports

- Once for additional draw passes, such as shadow map render

- Once for drawing its outline (selected)

Depending if the current frame, viewport, camera or render target changes, only a portion
of the material parameters might need to be updated. Different parameters of a draw instace
often depend on different source objects, such as:

- The input geometry, for example the triangles and positions buffer.
  Such parameters values are the same for all draw instances of a same geometry.

- The input instance, for example the color and the model transform.
  Such parameters values are the same for all draw instances with the same source
  instance, for example the drawing in each viewports.

- The camera and viewport, for example modelViewMatrix or viewport width.

- No specific input if constant for the material, for example a material default parameter that is not overriden.
  Such parameters values are the same for all draw instances with the same material.

Since some parameters are more likely to change, and in order to share as much as possible
the parameter data, the RTR builds a chain of :kl-ref:`RTRDrawInstance`. This is made possible
by the :kl-ref:`RTRDrawInstance.createSubDrawInstance` method, which will create another
:kl-ref:`RTRDrawInstance` inheriting the parameter set from its parent (base) draw instance.
The sub-instance can override parameter values. It is possible, too, to chain draw instances
that have a different material (with :kl-ref:`RTRDrawInstance.setBaseDrawInstance`).

Below is illustrated a typical chain of draw instances, along with the related tasks
and :kl-ref:`RTRInstance`:

.. image:: /images/SceneHub/RTRDrawInstanceChain.png

In the diagram above:

- A :kl-ref:`RTRSWGroupToInstanceTask` creates a `Phong` :kl-ref:`RTRSWGeometryInstance`
  (specialized :kl-ref:`RTRInstance`) for the corresponding scene element (`car1`) using the adaptors mechanism.
  Additionally, it creates a draw instance (:kl-ref:`RTROGLProgramDrawInstance`), and sets the
  `color` and `shininess` parameters (shared by all viewports or draw passes).

- The :kl-ref:`RTRSWGeometryInstance` creates a :kl-ref:`RTRSWGeometry` (specialized :kl-ref:`RTRInstance`)
  that represents the geometry (`mesh`) shared for all instances.
  The :kl-ref:`RTRSWGeometry` will create a draw instance (:kl-ref:`RTROGLProgramDrawInstance`)
  and set material parameters that are geometry-specific,
  such as the triangles list (from the :kl-ref:`PolygonMeshToRTR` adaptor) and
  the positions attribute (from the :kl-ref:`Vec3AttributeToRTR` adaptor).

- The :kl-ref:`RTRCreateSubInstanceTask` then creates a draw instance
  which specifies parameters that depends on the viewport and camera,
  such as the `modelViewProjMatrix` and the `modelViewMatrix`.

.. _rtr_materials:

RTR materials
--------------

The RTR defines simple materials, generic materials and meta-materials.

The materials (:kl-ref:`RTRMaterial` ) are loaded and cached by a material
library (:kl-ref:`RTRMaterialLibrary`). The material library will search
material files in a list of specified search paths.

The :kl-ref:`RTROGLContext` adds the default path
``${FABRIC_EXTS_PATH}/Builtin/RTR2/OpenGL/Shaders`` and more can
be added with the :kl-ref:`RTROGLContext.addShaderIncludePath` method.

The OpenGL RTR built-in material objects support three type or level
of materials: simple materials, meta materials and generic materials.

.. _rtr_simple_material:

Simple material
...............

The :kl-ref:`RTROGLProgram` object defines a simple GLSL material
which can be created by the material library from a group of ".glsl" files,
one for each shader type.

The OpenGL RTR assumes a specific naming convention for the shader files,
namely ``shadername_{vertex, fragment, geometry, tessControl, tessEvaluation, compute}.glsl``,
where the second part is the shader type. For example, when invoked with
``RTRMaterialLibrary.getOrCreateFromFile( 'Standard', 'phong', context )``,
the :kl-ref:`RTROGLMaterialLibrary` will search for shaders corresponding to
"Standard/phong_*.glsl" in the include paths, and will build a GLSL program
that links "Standard/phong_vertex.glsl" as the GL_VERTEX_SHADER and
"Standard/phong_fragment.glsl" as the GL_FRAGMENT_SHADER.

The OpenGL RTR has a basic built-in glsl preprocessor which extends the
GLSL functionality with the following features:

- A default value can be associated with uniform parameters, with the following syntax
  added just above the parameter declaration:

  .. code-block:: glsl

     /// \default [0.5,1,1,1]
    uniform vec4 color;

    /// \default 10.0
    uniform float shininess;

    /// \default false
    uniform bool modelNegativeScaling;

  Supported uniform types are bool, int, vec2, vec3, vec4, mat2, mat3 and mat4.

- A ``#include`` statement is supported, and the related file will be searched
  in the include paths registered with :kl-ref:`RTROGLContext.addShaderIncludePath`.
  For example, the ``#include "../Lighting/phong.glsl"`` statement found in
  ``Standard/phong_fragment.glsl`` will insert the source code of that relative file.

  If there is a .glsl error, the RTR will properly remap the line numbers of the reported
  shader errors so it is expressed relatively to the right source file, and will additionally
  dump the full preprocessed (merged) code.

- The following set of special parameters will be automatically set by the :kl-ref:`RTRDrawInstance`
  unless they are overriden by explicit values:

  - transform matrices:

    - `viewMatrix`: a mat4 parameter providing the World->Camera matrix

    - `invViewMatrix`: a mat4 parameter providing the Camera->World matrix

    - `projMatrix`: a mat4 parameter providing the Camera->Viewport matrix

    - `invProjMatrix`: a mat4 parameter providing the Viewport->Camera matrix

    - `viewProjMatrix`: a mat4 parameter providing the World->Viewport matrix

    - `invViewProjMatrix`: a mat4 parameter providing the Viewport->World matrix

    - `modelMatrix`: a mat4 parameter providing the Model->World matrix

    - `invModelMatrix`: a mat4 parameter providing the World->Model matrix

    - `modelViewMatrix`: a mat4 parameter providing the Model->Camera matrix

    - `invModelViewMatrix`: a mat4 parameter providing the Camera->Model matrix

    - `modelViewProjMatrix`: a mat4 parameter providing the Model->Viewport matrix

    - `viewProjToModelMatrix`: a mat4 parameter providing the Viewport->Model matrix

  - normals transform matrices: a mat3 parameter providing a transform matrix
    for vertex normals (transpose-inversed). These are the same as the
    transform matrices above, but named "*NormalsMatrix" instead of "*Matrix"
    (for example: `invModelViewNormalsMatrix`).

  - `viewportWidth`: an int parameter providing width of the draw surface

  - `viewportHeight`: an int parameter providing height of the draw surface

  - `viewportSamples`: an int parameter providing the number of samples of the draw surface (if multisampling)

  - `modelNegativeScaling`: a bool parameter which is true if the model transform has negative scaling (inverted normals)

Parameter values associated with a drawing object are stored in a :kl-ref:`RTRDrawInstance`; see :ref:`rtr_drawinstance`.

.. _rtr_meta_material:

Meta material
.............

A meta material is a set of simple materials that represent a same surface type
for different contexts. For example, a Phong textured surface might specify
a different shader to be used for deferred rendering, forward rendering, shadow map pass,
or for different GLSL versions.

The :kl-ref:`RTROGLMetaMaterial` sub-materials are specified by a `.json` file, which should be located
in the include paths of the material library.

The file must be structured as the following:

.. code-block:: json

  {
    "name": "Phong",
    "shaders": [
      {
        "filename": "phong",
        "directory": "Standard",
        "glsl": 120,
        "drawType": "standard",
        "default": true,
        "KLWrapper": "RTROGLGenericProgram"
      },
      {
        "filename": "phong150",
        "directory": "Standard",
        "glsl": 150,
      ...

- The `name` field contains the material name

- The `filename` is the prefix of the shader files (see :ref:`rtr_simple_material` for naming conventions)

- The `directory` is the relative path for the shader files

- `glsl` is shader's supported GLSL version (allows the RTR to choose the highest supported version)

- `drawType` is the type of drawing pass for using this shader, such as `standard` (forward), `deferred`, `shadow`...

- `default`, when set to `true`, identifies the material to use if multiple choices are possible

- `KLWrapper` is the specialized :kl-ref:`RTRMaterial` type to be created for wrapping that material in KL.
  This allows to specify custom material types. These types must have been previously registered in a
  global factory by the :kl-ref:`RegisterRTRMaterialType` function.

.. _rtr_generic_material:

Generic material
................

A generic material allows a GLSL material to be extended by specialized data sources.
It is somewhat similar to C++ templates.

This is required to avoid a combinatorial explosion of explicit shaders. For example,
in forward rendering, the combination of all light sources and their types must be specified
as part of the shader. Similarly, surface types could be textured or not, normal mapped or not,
vertices might be skinned or not, instanced or not.

For example, in the provided forward renderer (the :kl-ref:`GLStandardRTR`), the :kl-ref:`RTRStandardLitSubInstanceTask`
will assign required light sources to the draw instances.
Specialized OpenGL light types such as :kl-ref:`RTROGLAmbientLight_standard` and :kl-ref:`RTROGLShadowSpotLightInstance_standard`
are generic material sources. The diagram below illustrates the various involved types:

.. image:: /images/SceneHub/RTRGenericMaterial.png

The :kl-ref:`RTROGLGenericProgram` implements an OpenGL generic material.
The material sources must implement the :kl-ref:`RTRGenericMaterialSource` interface, which allows
to insert required code and parameters in the shader. The resulting shader that includes
the required sources' code is dynamically added to a shared library of material variations
(:kl-ref:`RTROGLProgramVariation`).

.. note::

  To reduce the number of generated shaders, the sources of a same type are regrouped and
  the inserted code must support a specific number of sources of the same type (for example with a loop).

In order to support common lighting code, the generic shaders use some naming conventions.
These are arbitrary and are only used to make the lighting and surface shading code
work together. Of course other conventions could be used in custom shaders if desired.

- The SurfaceParams structure should be defined to contain all the parameters required by the shading model,
  such as diffuse color and specular color.

- `vec4 illuminateSurface( in vec3 surfaceNormal, in vec3 surfaceToLight, in vec3 surfaceToEye, in SurfaceParams surface )`
  is assumed to apply the shading model based on the surface normal, light and eye vectors (BRDF + surface colors).

The generic material defines code insertion points (anchors) that the various data sources
can use to inject their own specialized code snippets. These insertion points use
an arbitrary naming convention that must be known by the specialized sources.

The insertion points are defined with the ``/// \insert <label>`` syntax, as shown below:

.. code-block:: glsl

  /// \insert fragmentParameters

  #include "../Lighting/phong.glsl"
  #include "../Lighting/lighting.glsl"
  /// \insert fragmentIncludes


  vec4 accumulateIllumination( in vec3 position, in vec3 surfaceNormal, in vec3 surfaceToEye, in SurfaceParams surface ) {
    vec4 illumination = vec4(0.0);

    /// \insert accumulateIllumination


Generic source's specialized shader code must be inserted in its implementation of
:kl-ref:`RTRGenericMaterialSource.mergeToMaterial`, by calling
:kl-ref:`RTROGLProgramVariation.insertGLSL` . If additional parameters are created,
the source must provide names that will not collide with other material sources, for example by
adding a suffix based on source's KL type.

A uniform shader parameter can be *generic*, in which case its value can be replaced with
another compatible source value, such as an attribute or a texture. In order to allow such
replacement, the glsl shader code must indicate where the alternate value has to be defined.
This is done with the `/// \fetch parameterName` syntax as illustrated below, which will declare
 an insertion point for source's data fetching code.

.. code-block:: glsl

  void main(){
    // Surface
    SurfaceParams surface;

    /// \fetch color
    surface.diffuse = color;

    /// \fetch specular
    surface.specular = specular;

If a :kl-ref:`RTRBaseInstance` binds a generic parameter (:kl-ref:`RTRGenericMaterialSource`) to a material,
the glsl code is transformed in the following way:

- the original parameter declaration (eg: `uniform vec4 color;`) is commented out

- the :kl-ref:`RTRGenericMaterialSource` must insert code (:kl-ref:`RTROGLProgramVariation.insertGLSL`) for
  adding the required parameters (eg: UVs attribute and sampler for a texture source), using
  insertion points such as `/// \insert vertexDefines` or `/// \insert fragmentDefines`.
  It should provide parameter names that will not collide with other material sources, for example by
  adding a suffix based on source's KL type.

- the :kl-ref:`RTRGenericMaterialSource` must define and set the value of a variable
  of the original parameter's name an type (eg: `vec4 color`) and insert the related
  code by calling the :kl-ref:`RTROGLProgramVariation.insertGenericParameterFetch`
  method. This code will be inserted at generic parameter `/// \fetch` location.


See :kl-ref:`BaseGeometryAttributeToRTRGenericSource`
and :kl-ref:`BaseImageToRTRGenericSource` for examples of generic parameter sources.

.. note::

  The generic source might require to request to additional RTRInstance data (eg: UV attribute value).
  These can be requested using :kl-ref:`RTRInstance.getExtraParameterBindingKey`
  and related functions. The :kl-ref:`RTRMaterialVariationParameterMapping` helper
  allows to efficiently store per-instance data for a :kl-ref:`RTRGenericMaterialSource`
  shared by multiple instances.

.. _environment_maps:

Environment Maps
----------------

Textures simulating the environment are looked-up with a vec3 direction. The code doing this projection is automatically injected in the following insertion points :

.. code-block:: glsl

  vec3 environmentMapLookUpDirection; // Look-up direction for the environment : must be normalized
  float environmentMapLookUpMipMapLevel; // MipMap level used when fetching the texture : in [0;1]

  /// \fetch<environmentMapLookUp>
  gl_FragColor = environmentProbe;

  /// \fetch<environmentMapLookUpMipMap>
  gl_FragColor = environmentProbe;

These special tags extend the \fetch insertion points, and indicate to the adaptors inserting glsl code that the required look-up vectors have been declared in the current scope. If they were not declared, using these insertion points might lead to glsl compilation errors. The <environmentMapLoopUp> tag requires a vec3 named environmentMapLookUpDirection; the <environmentMapLookUpMipMap> requires both a vec3 named environmentMapLookUpDirection, and a float named environmentMapLookUpMipMapLevel.

.. _rtr_lights:

RTR lights
-----------

The RTR provides some basic built-in light types, such as:

- The :kl-ref:`RTRAmbientLight`, which defines a constant ambient light

- The :kl-ref:`RTRPointLight`, which defines a positional light, with parameters for defining the attenuation
  type and cutoff distance. The :kl-ref:`RTRShadowPointLight` is a point light with shadow
  map parameters.

- The :kl-ref:`RTRSpotLight`, which defines a spot light, with parameters for defining the attenuation
  type and cutoff distance, and the spot angle soft or hard limit. The :kl-ref:`RTRShadowSpotLight` is a
  spot light with shadow map parameters.

- The :kl-ref:`RTRDirectionalLight`, which defines a directional light. The :kl-ref:`RTRShadowDirectionalLight` is a
  directional light with cascaded shadow map parameters.

The :ref:`scenegraph_to_rtr_extension`, which defines adaptor types that adapt the
SceneGraph light types to RTR light types, such as the :kl-ref:`SGPointLightToRTR`.

.. _rtr_debugging:

RTR debugging and profiling
---------------------------

Debugging the RTR can be quite challenging because of the various objects, steps and caches
involved. Of course, the more drawing instances, the harder it is to debug.

The following functions will activate some tracing functionality which can help to track down issues:

- The ``SetOGLWrappersTracing`` function will activate tracing at the OGLWrappers level,
  and log state changes such as material parameters being set or vertex buffers being
  activated. This will turn on OpenGL error checking.

- The ``cpglSetDebugTrace`` function will activate low-level OpenGL command logging.

- ``BaseRTR.enableProfiling`` will log tasks' spent time. Tasks are
  responsible for logging their spent time by inserting :kl-ref:`AutoProfilingEvent`
  in their update method (which is a no-op if profiling isn't activated).

.. _rtr_performance:

RTR coding practices for performance
------------------------------------

Below are presented various coding practices the RTR uses to improve its
runtime performance. However, the RTR tries to provide the critical building
blocks to minimize the requirement for complex optimizations in
custom or higher-level objects.

Being a realtime renderer, the RTR tries to deliver good performance while
being flexible, which can be challenging. The following practices are
followed by the RTR as much as possible to allow for a better performance:

- Use versioning (:kl-ref:`Versioned` interface) and caches when possible.
  This allows to skip data update if the input data's version didn't change. This requires
  that input dependencies are carefully taken into account.

- Incremental updates: avoid to fully rebuild and reallocate data structures
  when only a portion changed, so that a small scene change implies a small rendering
  data change.  This increases the complexity of the implementation of the objects but is essential
  for having a good performance.

- Write tasks that require the drawing API (OpenGL) efficiently,
  such that most processing can be done on preparation tasks (which could be multithreaded).
  To help this, the OpenGL wrapper objects, such as :kl-ref:`OGLTexture`, can be defined without
  creating the associated OpenGL objects.

- Minimize memory allocations and fragmentation: recycle existing allocated data or array
  items instead of recreating them, regroup structures in contiguous arrays and avoid KL
  dictionaries in performance sensitive situations (high fragmentation)

- Batch-process elements as much as possible.

- [in a future release] Separate drawing from processing tasks, such that the RTR can eventually process
  the next frame while rendering, and so that processing tasks can be evaluated
  by multiple threads

- [in a future release] Minimize thread locking: use spin locks (SimpleLock, LockedInitialize) for situations
  where locking is exceptional or occurs for a short period of time

- Avoid frequent Object type casts (converting from a type or interface to another one) and
  avoid setting Object variables (use Ref<Object> instead when possible to avoid atomic reference count changes)

- Use `inline` for small performance sensitive functions. When applicable, split smaller portions
  that treat the frequent cases as inlined functions, and put the complex treatment of exceptional
  cases in regular functions (non-inlined).
