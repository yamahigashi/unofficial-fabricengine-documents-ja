.. _SPLICEINTEGRATION:

Integrating Fabric:Splice
===========================

.. image:: /images/Splice/Splice_logo.png
   :width: 360px
   :height: 57px

| Splice version |FABRIC_VERSION|
| |FABRIC_COPYRIGHT|

Introduction
--------------------------
This document focuses on integrating Splice into a host application using a C++ plugin architecture. All of the current provided integrations ship with their source code, so you can use them as a reference. It's recommended to use the integration for :dfn:`Maya` as the main reference, since it is the most advanced.

The only thing you need to build against is the API package. The API package contains several versions of the libraries:

  - Shared FabricSplice using Shared FabricCore (Splice-|FABRIC_VERSION|, uses FabricCore-|FABRIC_VERSION|)
  - Static FabricSplice using Shared FabricCore (Splice-|FABRIC_VERSION|_s, uses FabricCore-|FABRIC_VERSION|_s)
  - Static FabricSplice using Static FabricCore (Splice-|FABRIC_VERSION|_ss, uses FabricCore-|FABRIC_VERSION|_s)

Splice can be build statically or dynamically against the FabricCore / FabricSplice libraries. The fully static library (suffixed _ss) makes linking straight forward. In terms of linking order please link against the FabricSplice library followed by the FabricCore library. (especially on unix based system the linking order is important, in case you have problems try the opposite order). On linux you might need to link against additional libraries, depending on the distribution. This order is confirmed to work on linux: [FabricSplice-|FABRIC_VERSION|_ss, FabricCore-|FABRIC_VERSION|_s, GL, pthread, dl]. On Windows you will need to additionally link against :dfn:`user32`, :dfn:`advapi32`, :dfn:`gdi32`, :dfn:`shell32`, :dfn:`ws2_32`, :dfn:`Opengl32`, :dfn:`glu32`.

.. versionadded:: 1.12.0

.. note:: The SpliceAPI needs the boost thread, system and filesystem libraries to be linked against. You need to specify the :env:`BOOST_INCLUDE_DIR` and :env:`BOOST_LIBRARY_DIR` environment variables for the Scons scripts to perform.

You will need add one of the two C defines :dfn:`FECS_STATIC` or :dfn:`FECS_SHARED`, depending on your build choice (usually :dfn:`FECS_STATIC`). The :dfn:`FECS_` prefix stands for :dfn:`Fabric Engine Core Splice`. You'll have to additionally define the corresponding :dfn:`Fabric Engine Core` define (:dfn:`FEC_STATIC` or :dfn:`FEC_SHARED`).  The defines have to be part of the build system settings (for example in scons) or can be hard-coded into the source files. In that case the defines have to be placed prior to including :dfn:`FabricSplice.h`. So using fully static linking for example like this:

.. code-block:: c++

    #define FEC_STATIC
    #define FECS_STATIC

    #include <FabricSplice.h>

You can get the latest API packages here: |FABRIC_DIST_URL|

We'll now go through the steps required to build an integration, but also how to follow our design which we have used in Maya and Softimage.

Source Control
-----------------------
Since we are using `GitHub <https://github.com/>`_, please create a GitHub account (if you don't have one already) and create a repository for your work on the specific integration. Also please inform the Splice team and add us as collaborators. This will allow us to review code, comment on code changes and help out by working on the same code if you get stuck. The repository can be public (if you consider your integration public) or private (if the integration is proprietary and to be protected). We still strongly encourage to provide the Splice team access though, since it will shorten development time and simplify support.

Documentation
-----------------------------

For documentation on the Splice C/C++ API, please refer to :ref:`SPLICECAPI`.

Since FabricSplice uses some of the FabricCore types, you'll also want to refer to the :ref:`CAPIPG`.

You can also inspect the two header files which come with the API packages (FabricCore.h and FabricSplice.h).

Overview
--------------

The way the integrations work essentially is that they provide a generic node (in maya a hypergraph node and in softimage an operator) which hosts the FabricSplice::DGGraph. All parameters / inputs and outputs are then converted by the integration from the host (Houdini in your case) to the FabricSplice::DGGraph.

The essential design as well is that we provide a scripting command for the host application which can perform any changes required. The user interface then utilizes that command. That way scripters can automate the usage of FabricSplice and general users can utilize the UI. The command uses an :dfn:`action` parameter to define the action it is performing. I strongly recommend to use the same action names (such as the maya implementation, for example), so that users switching from Maya to Houdini can use the same sort of syntax to interact with Splice.

Development steps
--------------------

- Implement generic node (just hosting a FabricSplice::DGGraph without functionality). This ensures that you are compiling correctly and your linker settings are correct.

- Implement the parameter synchronization for the basic types (Scalar, Integer, Boolean, String)

- Implement the scripting command to add / edit / remove KL operators and the KL source code.

- Test basic math implementations (Add / Subtract etc)

- Implement parameter synchronization for complex types (Vec3, Quat, Mat44, arrays of all types, PolygonMesh).

- Implement user interface.

We can advice along the way, so let us know if you need anything else to get started.


Indices and Tables
------------------

* :ref:`genindex`
* :ref:`search`
