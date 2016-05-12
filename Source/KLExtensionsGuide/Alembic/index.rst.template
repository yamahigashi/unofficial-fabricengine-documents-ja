.. _alembic_extension:

Alembic Extension
====================================================================================

.. image:: /images/FE_logo_345_60.*
   :width: 345px
   :height: 60px

| |FABRIC_PRODUCT_NAME| version |FABRIC_VERSION|
| |FABRIC_COPYRIGHT|

The ``Alembic`` extension provides complete wrapping of the Alembic C/C++ library.

http://www.alembic.io/

.. note:: You can find the source code for the Alembic extension here: http://github.com/fabric-engine/Alembic

Since the Alembic extension's KL code as well as the C++ bindings are auto generated, there's no documentation
attached to each type or method. Please refer to the Alembic.io documentation for specifics.

http://docs.alembic.io/

Aside from the :ref:`alembic_extension` |FABRIC_PRODUCT_NAME| also ships with the :ref:`alembicwrapper_extension`, a higher level extension for simpler use. 

.. kl-example:: 

  require Alembic;
  require FileIO;

  operator entry() {
    FilePath path = FilePath('${FABRIC_SCENE_GRAPH_DIR}/Python/Apps/Resources/Alembic/loreipsum.abc').expandEnvVars();

    AlembicIArchive archive(path.string());
    AlembicIObject objs[];
    objs.push(archive.getTop());

    for(Size i=0;i<objs.size();i++) {
      report(objs[i].getFullName());
      for(Size j=0;j<objs[i].getNumChildren();j++) {
        objs.push(objs[i].getChild(j));
      }
      if(i == 24)
        break;
    }
  }

Table of Contents
-----------------

.. toctree::
  :maxdepth: 2
  
  files
  types
  functions
  constants

Indices and Tables
------------------

* :ref:`genindex`
* :ref:`search`
