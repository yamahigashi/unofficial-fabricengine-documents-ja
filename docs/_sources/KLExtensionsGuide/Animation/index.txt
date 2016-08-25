.. _animation_extension:

Animation Extension
====================================================================================

.. image:: /images/FE_logo_345_60.*
   :width: 345px
   :height: 60px

| |FABRIC_PRODUCT_NAME| version |FABRIC_VERSION|
| |FABRIC_COPYRIGHT|

The Animation extension provides classes for defining keyframes, keyframe tracks, track sets, and clips. 

The Keyframe type evaluation uses the same piecewize bezier interpolation found in the industry standard DCCs such as
Maya, Softimage, and 3dsmax. In Maya, when a KeyframeTrack is added and connected to a Curve type, the KL Track type
evaluates the the same results at the connected Maya FCurve node. 

The Animation classes are used by the :ref:`characters_extension` to drive the animation of characters. The :ref:`fbxwrapper_extension` generates a :kl-ref:`Clip` data type when loading animation data from an Fbx file.

Table of Contents
-----------------

.. toctree::
  :maxdepth: 2
  
  files
  types
  functions
  constants

Indices and Tables
------------------

* :ref:`genindex`
* :ref:`search`
