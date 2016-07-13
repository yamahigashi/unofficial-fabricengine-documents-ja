.. _images_extension:

Images Extension
====================================================================================

.. image:: /images/FE_logo_345_60.*
   :width: 345px
   :height: 60px

| |FABRIC_PRODUCT_NAME| version |FABRIC_VERSION|
| |FABRIC_COPYRIGHT|

The Images extension is a new class to support image data in Fabric Engine.
It will totally replace the :ref:`Images` extension in the official new release.

The Images extension defines two type of images : 

-  The :kl-ref:`Image32Bits`, :kl-ref:`Image32BitsRGBA`, :kl-ref:`Image8BitsRGB` and :kl-ref:`Image8BitsRGBA` classes that define 2D buffer-specialized images. They can be used to open most of the images and are suitable for texturing operations. 

-  The :kl-ref:`ImagePasses` class that defines a generic 2D or 3D image of any type (uint8, half, float) containing any numbers of channels. Most of the time, an image contains 3 or 4 channels : R,G,B (A) that define a pass, usually called the beauty or main pass. However, an image (.exr or .tiff) can have any numbers of channels, organized as passes (http://3drender.com/light/compositing/index.html). The :kl-ref:`ImagePasses` allows to define and extract passes from an existing image and its pixel data is casted in 32 bits float that makes it suitable for image-processing.



Table of Contents
-----------------

.. toctree::
  :maxdepth: 2
  
  files
  types

Indices and Tables
------------------

* :ref:`genindex`
* :ref:`search`
