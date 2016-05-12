.. _fabricvideo_extension:

Fabric Video Extension
====================================================================================

.. image:: /images/FE_logo_345_60.*
   :width: 345px
   :height: 60px

| |FABRIC_PRODUCT_NAME| version |FABRIC_VERSION|
| |FABRIC_COPYRIGHT|

The ``FabricVIDEO`` extension provides a very simple wrapping of the ffmpeg library. This only works with :kl-ref:`RGB` byte video right now. The data type used both for reading and writing video is called :kl-ref:`VideoHandle`.

https://www.ffmpeg.org/

.. kl-example::

  require FabricVIDEO;
  require FileIO;

  operator entry() {

    FilePath inputPath = FilePath('${FABRIC_SCENE_GRAPH_DIR}/Python/Apps/Resources/Video/bee_960.mov').expandEnvVars();
    FilePath outputPath = FilePath('${TEMP}/video.mpeg').expandEnvVars();

    VideoHandle videoIn, videoOut;

    // open one for reading
    videoIn.openFileHandle(inputPath.string());

    // open one for writing with the same dimensions
    videoOut.createFromFileHandle(outputPath.string(), videoIn.width, videoIn.height);

    // allocate enough pixels
    RGB pixels[];
    pixels.resize(videoIn.width * videoIn.height);

    // copy 10 frames
    Scalar time = 0.0;
    for(Size i=0;i<10;i++) {
      videoIn.getAllPixels(pixels);
      videoOut.writeAllPixels(pixels);

      // step one frame
      videoIn.seekTime(time);
      time += 1.0 / videoIn.fps;

      // report some pixel
      report(pixels[400]);
    }

    videoIn.clear();
    videoOut.clear();

    report('Written '+outputPath.string());
    report(outputPath.exists());
  }

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
