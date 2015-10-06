
Introduction
============

.. note:: You can find the source code for the SpliceAPI here: http://github.com/fabric-engine/SpliceAPI

The Fabric:Splice C/C++ API, referred to as :dfn:`SPLICECAPI` in this document, is an abstraction layer to the `Fabric Core CAPI <http://documentation.fabric-engine.com/CreationPlatform/latest/HTML/CAPIProgrammingGuide/index.html>`_. The SPLICEAPI provides a simpler way to integrate Fabric Core based functionality into C/C++ hosts applications and wraps lots of the rudimentary facilities. The :dfn:`SPLICECAPI` also supports additional facilities, such as persistence, for example.

Aside from this documentation API you can find a general description of how to integrate Splice into a host application here: :ref:`SPLICEINTEGRATION`. This also includes recommendations for build settings and C defines.

One API, Two Interfaces
-----------------------

:dfn:`SPLICECAPI` is implemented as a pure C API with a thin, inlined C++ interface that makes it easier to use in C++ applications.  This is done to minimize linking issues, as the C linking interface on the platforms that Fabric:Splice supports is much more controlled than the C++ linking interface. The C++ interface is thus purely a C++ programmer convenience; however, it is a big programmer convenience, and as such it is recommended that you use the C++ language interface when possible.  Both interfaces link with exactly the same shared library (DLL).

Since the host application targeted with the :dfn:`SPLICECAPI` are mainly C++ based, when discussing the API in this guide, we will only present the C++ version.

