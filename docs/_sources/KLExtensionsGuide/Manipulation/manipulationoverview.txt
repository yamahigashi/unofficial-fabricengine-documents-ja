.. _manipulation_overview:

Manipulation 2.0 Overview
===================

The new manipulation system provides an abstraction layer making it more flexible, more scalable and independant of the rendering.
Furthermore, this new design makes the system safely usable within Canvas.
For the moment, only :kl-ref:`SRTManipulator` are supported, but others as Surface painting manipulator will also be implemented. 


SRTManipulator
------------
SRTManipulator is a special implementation of manipulator used to scale, rotate and translate any rendered objects : geometries, instances, lights, groups, ...
The manipulation can either be global or applied along a specfic axis.

The SRT manipulation system has two general components : a :kl-ref:`SRTManipulatorBase` and a :kl-ref:`SRTManipulatorTargetBase`: 

- The :kl-ref:`SRTManipulatorBase` is the manipulator, which represents a gizmo that can be manipulated either freely or along its X,Y,Z axis only. The components process the mouse/key events it receives and, depending of the manipulation mode (S,R,T - global or per-axis), tranforms itself. The manipulator doesn't know any of the objects it's manipulating. Instead, it owns a :kl-ref:`SRTManipulatorTargetBase` container and gets/sets its transformation.  

- The :kl-ref:`SRTManipulatorTargetBase` is a container that refers one or several transforms, which are the transforms of the target objects to manipulate. In SceneHub, the target objects are :kl-ref:`SWElementHandle` (cf. :kl-ref:`SGSRTManipulatorTarget`), in InlineDrawing it could be :kl-ref:`InlineTransform`. This component sets the targets transforms accordingly the manipulator's transform and updates the :kl-ref:`Host` DCC scene. 

In SceneHub, :kl-ref:`RTRSRTManipulator` and :kl-ref:`SGSRTManipulatorTarget` are the specialized classes derived from :kl-ref:`SRTManipulatorBase` and :kl-ref:`SRTManipulatorTargetBase`. 
They are responsible of respectively drawing the manipulator and refreshing the objects of the scene if their transforms have been changed by the manipulator.
Finally, the :kl-ref:`RTREventDispatcher` class owns and manages one or several :kl-ref:`Manipulator`.
It provides high level controls such as selecting the current manipulator, dispatch the user events to the right manipulator and active/deactive the system.

Here is an overview of the manipulation system in SceneHub :

.. image:: /images/Manipulation/ManipulationSchema.png

See `Samples/SceneHub/SelectedAndManipulate.kl` for an example of simple manipulation setup.
