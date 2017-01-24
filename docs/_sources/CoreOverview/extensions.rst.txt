Extensions
==========

Extensions are libraries loaded at initialization time that can define libraries of KL functions and/or bind C++ code libraries and expose their interfaces to KL. The extension system is used to integrate existing libraries of code with Fabric Engine applications. Fabric Engine comes packaged with a wide range of extensions that provide a range of functionality including the Bullet physics library, the OpenCV computer vision library and the Microsoft Kinect SDK.

Integration of Existing Code Libraries
--------------------------------------

|FABRIC_PRODUCT_NAME| provides OpenGL bindings via an extension that uses the GLEW OpenGL wrapper system. Similarly, any API such as Microsoft DirectX or NVidia CUDA can be exposed via custom extensions.

All source code for the provided extensions is available in the |FABRIC_PRODUCT_NAME| github repository and can be used as the basis of a user's custom extensions.

Documentation
--------------------------------------

Documentation for the extensions provided with |FABRIC_PRODUCT_NAME| can be in the :ref:`EXTR`.

