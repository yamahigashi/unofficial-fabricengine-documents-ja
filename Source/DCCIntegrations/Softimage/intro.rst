Introduction
============

* **Fabric for Softimage**

  Fabric for Softimage is the integration of Fabric Canvas in Autodesk Softimage.

  The plugin allows you to use Fabric inside your Softimage projects for tasks such as creating complex procedural geometry, loading assets (e.g. Alembic, FBX), drawing directly into the viewports and controlling the transformation of objects (e.g. for rigging).

  The heart of Fabric for Softimage is a custom operator, called *CanvasOp*, which ensures communication between Softimage and Fabric and which can access kinematic states and polygon meshes.

  Furthermore, an extensive set of custom commands is provided to create Fabric operators and entire graphs via scripting.

* **Splice for Softimage** (legacy)

  Splice for Softimage is the legacy integration of Fabric Engine inside Autodesk Softimage.
  
  The plugin provides custom user interfaces and a custom operator called :dfn:`SpliceOp` that can access kinematic states as well as polygon meshes. 
  
  This custom operator can drive elements in the scene and is perfectly suited for implementing rigging as well as procedural geometry tools.

  Splice for Softimage is not integrated into ICE (but can access ICE data), and geometry types other than polygon meshes such as Curves, Nurbs or Particles are not supported.