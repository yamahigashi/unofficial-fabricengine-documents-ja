.. _canvas-programmer-guide-faq:

Frequently Asked Questions
====================================

This is a list of Frequently Asked Questions about Canvas.  Suggestions for
new entries are welcome!

In Canvas, how do I...
----------------------

... serialize execution of nodes?
  In Canvas there is no guarantee of order of execution of nodes unless it
  is explicit.  In version 2.0.x, nodes can be guaranteed to execute one
  after another by piping them through a serialization Canvas function, such as::

    dfgEntry {
      port1Out = port1In;
      port2Out = port2In;
    }

  Such a function will be guaranteed to "pull" its ports in the order given,
  which allows control over the seralization of execution.

  .. note::

    This way of forcing serialization is likely to change in a future version
    in which input values may be precomputed in parallel in cases where they
    are all known to be needed.
