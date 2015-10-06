.. _SPLICEAPIWORKSHOP:

Fabric Splice API Workshop
=======================================

.. image:: /images/Splice/Splice_logo.png
   :width: 360px
   :height: 57px

| Splice version |FABRIC_VERSION|
| |FABRIC_COPYRIGHT|

Description
--------------------------
This workshop covers the Splice API (including the Core API). You'll learn how you can use the power of KL in your own C/C++ applications, and how to integrate Splice into other (yet unsupported) host applications. This workshop targets the C/C++ programmer type and RnD departments.

You can find all of the videos embedded below in the `Fabric Engine Workshop Channel on Vimeo <https://vimeo.com/channels/629477>`_.

`All workshop videos are available for download as well. <http://dist.fabric-engine.com/Downloads/Tutorial-Videos.rar>`_

.. note:: With version 1.10.1 of the API the FabricSplice::addRTFolder function has been deprecated.

Material
--------------------------
Workshop files |FABRIC_GITHUB_TRAININGMATERIAL_URL|

PDF Presentation :download:`Splice API </images/Splice/02_Splice_API.pdf>`

01 - Introduction
------------------------
This video provides a general overview of the Splice API and how you deploy the libraries on your machine.

.. raw:: html

  <div style="margin-top:10px;">
    <iframe src="http://player.vimeo.com/video/79823097" width="640" height="360" byline="0" portrait="0" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
  </div>

02 - Scons
------------------------
In this section we learn how to use the SCons build system to build executable tools using the Splice API.

.. raw:: html

  <div style="margin-top:10px;">
    <iframe src="http://player.vimeo.com/video/79823098" width="640" height="360" byline="0" portrait="0" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
  </div>

03 - Hello World
------------------------
In this section we implement our very first Splice API based application, a "Hello World" sample. This deploys KL withing C/C++ and includes the complete LLVM toolchain.

.. raw:: html

  <div style="margin-top:10px;">
    <iframe src="http://player.vimeo.com/video/79823513" width="640" height="360" byline="0" portrait="0" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
  </div>

04 - Logging Callbacks
------------------------
In this section we learn how to set callbacks for any log output, including std::out as well as error messages.

.. raw:: html

  <div style="margin-top:10px;">
    <iframe src="http://player.vimeo.com/video/79823100" width="640" height="360" byline="0" portrait="0" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
  </div>

05 - KL Types
------------------------
In this section we cover how to use custom KL types, how to load them and how to even programmatically create them using C/C++.

.. raw:: html

  <div style="margin-top:10px;">
    <iframe src="http://player.vimeo.com/video/79823102" width="640" height="360" byline="0" portrait="0" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
  </div>

06 - Ports
------------------------
This video covers the DGPort and how to read / write data with Splice. We also cover advanced high performance IO on ports for moving large amounts of data.

.. raw:: html

  <div style="margin-top:10px;">
    <iframe src="http://player.vimeo.com/video/79823104" width="640" height="360" byline="0" portrait="0" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
  </div>

07 - RTVals
------------------------
This section covers RTVals and how you can use KL types directly within C/C++, how you can call methods on them. We'll learn how to deploy RTVals without using any graph.

.. raw:: html

  <div style="margin-top:10px;">
    <iframe src="http://player.vimeo.com/video/79823677" width="640" height="360" byline="0" portrait="0" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
  </div>

08 - Subgraphs
------------------------
This video covers subgraphs with the Splice API. PLEASE NOTE THAT SUBGRAPHS MIGHT BE CHANGED / REMOVED in the release of 1.10.0.

.. raw:: html

  <div style="margin-top:10px;">
    <iframe src="http://player.vimeo.com/video/79823515" width="640" height="360" byline="0" portrait="0" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
  </div>

09 - Persistence
------------------------
In this section we learn how to save Splice tools to a file and how to load it again. This section is essential for building portable tools.

.. raw:: html

  <div style="margin-top:10px;">
    <iframe src="http://player.vimeo.com/video/79823514" width="640" height="360" byline="0" portrait="0" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
  </div>

10 - KL Parser
------------------------
This video covers the KLParser. We learn how to parse KL code for contents, and how it can be deployed to build code completion tools.

.. raw:: html

  <div style="margin-top:10px;">
    <iframe src="http://player.vimeo.com/video/79823106" width="640" height="360" byline="0" portrait="0" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
  </div>


Indices and Tables
------------------

* :ref:`genindex`
* :ref:`search`
