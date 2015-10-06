Documentation System Prerequisites
======================================

.. image:: /images/FE_logo_345_60.*
   :width: 345px
   :height: 60px

| |FABRIC_PRODUCT_NAME| version |FABRIC_VERSION|
| |FABRIC_COPYRIGHT|

Once you have installed sphinx (`http://sphinx-doc.org/ <http://sphinx-doc.org/>`_) you can test it in python like this:

.. code-block:: python

    import sphinx
    print sphinx.__version__

You need to have the Python subfolder of the Fabric Engine deployment on you python path (for example :dfn:`$FABRIC_DIR/Python/2.7`) to gain access to the Fabric Core python client as well as the Documentation System's sphinx directives.

You can test both of these modules like this:

.. code-block:: python

    import FabricEngine.Core as fe
    from FabricEngine.Sphinx.ASTWrapper import *

Once all of these snippets work without errors you are ready to generate docs.

Indices and Tables
------------------

* :ref:`genindex`
* :ref:`search`
