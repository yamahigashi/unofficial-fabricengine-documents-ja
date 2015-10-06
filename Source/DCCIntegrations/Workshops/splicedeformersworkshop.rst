.. _SPLICEDEFORMERSWORKSHOP:

Fabric Splice for Deformers Workshop
======================================

.. image:: /images/Splice/Splice_logo.png
   :width: 360px
   :height: 57px

| Splice version |FABRIC_VERSION|
| |FABRIC_COPYRIGHT|

Description
--------------------------
In this workshop you'll learn how to use Splice in Maya to build deformers. The workshop covers everything from a basic wave deformer to a wrap mesh deformer supporting sliding. The workshop picks up topics from the :ref:`KLWORKSHOP` and uses PEX for multithreading.

You can find all of the videos embedded below in the `Fabric Engine Workshop Channel on Vimeo <https://vimeo.com/channels/629477>`_.

`All workshop videos are available for download as well. <http://dist.fabric-engine.com/Downloads/Tutorial-Videos.rar>`_

KNOWN ISSUES
--------------------------
Unfortunately the PolygonMesh class changed prior to the release, after the workshops were finished. It's a minimal change though.
The PolygonMesh no longer provides getAttributes. You can now call on the PolygonMesh itself to perform getOrCreateAttribute. The workshop files on Github below contain a fixed version of these scenes.

Material
--------------------------
Workshop files |FABRIC_GITHUB_TRAININGMATERIAL_URL|

PDF Presentation :download:`Splice for Deformers </images/Splice/05_Splice_Deformers.pdf>`

01 - Wave Deformer
--------------------------------
In this section we learn how to build deformers using Splice in Maya and create a simple sinus based wave deformer.

.. raw:: html

  <div style="margin-top:10px;">
    <iframe src="http://player.vimeo.com/video/79866175" width="640" height="360" byline="0" portrait="0" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
  </div>

02 - Jiggle Deformer
--------------------------------
In this video we use acquired knowledge from the Splice for Motion workshop and use the same spring algorithm  to create a simulated deformer: A jiggle.

.. raw:: html

  <div style="margin-top:10px;">
    <iframe src="http://player.vimeo.com/video/79824516" width="640" height="360" byline="0" portrait="0" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
  </div>

03 - Wrap Mesh Deformer
--------------------------------
In this section we make use of the raycast functionality within Splice to implement a Wrap Mesh deformer. It uses the GeometryLocation to bind geometry to a secondary surface.

.. raw:: html

  <div style="margin-top:10px;">
    <iframe src="http://player.vimeo.com/video/79824671" width="640" height="360" byline="0" portrait="0" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
  </div>

04 - Wrap Mesh with Sliding
--------------------------------
In this section we extend the previously implemented Wrap Mesh deformer with sliding features. This opens up new possibilities, for example in the area of simulating skin.

.. raw:: html

  <div style="margin-top:10px;">
    <iframe src="http://player.vimeo.com/video/79824515" width="640" height="360" byline="0" portrait="0" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
  </div>

Indices and Tables
------------------

* :ref:`genindex`
* :ref:`search`
