.. _canvas-user-guide-timeline:

Timeline Widget
===============================

Timeline widget provides access to playback functionality.

.. image:: /images/Canvas/userguide_11.jpg

Features of the Timeline widget include:

  - Frame slider

    You can use the frame slider to scrub through time.

  - Buttons

    Through the buttons you get access to play, pause, step frames, step to in and step to out.

  - Loop mode

    The timeline can loop continuously, oscillate (ping pong) or simply play back once.

  - Playback mode

    You can either playback interactively (any time change causes a single evaluation) or 
    in a simulated fashion, where every time change forward causes the evaluation of all in between frames.

.. note:: You can pull the time into the graph by adding an input port called :dfn:`timeline` of type :dfn:`Float32` or :dfn:`SInt32`. This only works in Fabric Standalone. In a DCC like Maya you will have to hook up a specific port to the time using a expression.
