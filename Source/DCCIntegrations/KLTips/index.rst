.. _KLTIPS:

Splice KL Tips
====================================

.. image:: /images/Splice/Splice_logo.png
   :width: 360px
   :height: 57px

| Splice version |FABRIC_VERSION|
| |FABRIC_COPYRIGHT|

Reporting an error using setError
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As a debugging or error reporting facility KL provides the setError statement. This can be useful for reporting errors back to the user specifically in the context of Splice. The code below for example will catch a division by zero and report that back to the user.

.. code-block:: javascript

  operator myOp(Scalar factor, Vec3 pos, io Vec3 result) {
    if(factor <= 0.0)
    {
      setError("Invalid factor specified. Please use a factor above 0.0.");
      return;
    }
    result = pos / factor;
  }

This will report back this error to the host application's console, prefixed with the Splice container and operator name.

Indices and Tables
^^^^^^^^^^^^^^^^^^^^^^^^^^^

* :ref:`genindex`
* :ref:`search`
