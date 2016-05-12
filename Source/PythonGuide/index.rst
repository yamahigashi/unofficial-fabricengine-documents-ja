.. _PYTHONPG:

Python Programming Guide
=========================

.. image:: /images/FE_logo_345_60.*
   :width: 345px
   :height: 60px

| |FABRIC_PRODUCT_NAME| version |FABRIC_VERSION|
| |FABRIC_COPYRIGHT|

.. contents:: Table of Contents
  :local:

Introduction
------------

Fabric has offered Python bindings for the Core C++ API for some time but new to version 2.2.0 is a PySide-compatible wrapping of the FabricUI user-interface library, allowing users to build complete standalone Fabric-based tools in Python. There is also a higher-level Canvas Python module which wraps much of the FabricUI functionality and makes it accessible in a way that's easier for building custom Python applications.

The Canvas standalone has been rebuilt in Python using the Canvas module and provides a good example of how another standalone application may be built using Python. The Canvas standalone can be found in `FABRIC_DIR/bin/canvas.py`.

The Canvas module and the FabricUI Python bindings are still a work in progress. Over the next few releases we will be working on cleaning up and stabilizing the API as well as providing more detailed documentation. In the meantime we welcome users to begin experimenting with it to build applications, though the API may be changing from release to release as we make improvements to both functionality and ease of use.

Currently we are only providing the bindings for Python 2.7 with Qt 4.8.x and PySide 1.2.4. Users can however visit the `FabricUI repository <http://github.com/fabric-engine/FabricUI>`_ to check out and build the bindings against any version of Python or Qt that's required. In a future release we will also add FabricUI Python support for supported DCCs.

Canvas Module
---------------

Here you can find documentation on the main Canvas module classes and their most relevant methods. Not all classes are documented here and you may still want to look at the Python code itself which can be found under `FABRIC_DIR/Python/2.7/FabricEngine/Canvas`, however this should give you enough of a starting point to begin building your own Python applications.

CanvasWindow
+++++++++++++++

.. automodule:: FabricEngine.Canvas.CanvasWindow
  :members:
  :private-members:

ScriptEditor
+++++++++++++++

.. automodule:: FabricEngine.Canvas.ScriptEditor
  :members:
  :private-members:

UICmdHandler
+++++++++++++++

.. automodule:: FabricEngine.Canvas.UICmdHandler
  :members:
  :private-members:
  :undoc-members:

BindingWrapper
+++++++++++++++

.. automodule:: FabricEngine.Canvas.BindingWrapper
  :members:
  :private-members:
  :undoc-members:

LogWidget
+++++++++++++++

.. automodule:: FabricEngine.Canvas.LogWidget
  :members:
  :private-members:

RTValEncoderDecoder
+++++++++++++++

.. automodule:: FabricEngine.Canvas.RTValEncoderDecoder
  :members:
  :private-members:

FabricParser
+++++++++++++++

.. automodule:: FabricEngine.Canvas.FabricParser
  :members:
  :private-members:

