.. _singletons_extension:

Singletons Extension
====================================================================================

.. image:: /images/FE_logo_345_60.*
   :width: 345px
   :height: 60px

| |FABRIC_PRODUCT_NAME| version |FABRIC_VERSION|
| |FABRIC_COPYRIGHT|

The :ref:`singletons_extension` provides a way to persist KL objects from one operator and scope to another. The objects are stored in a static C++ map which is opaque to the user. This is used for example in the :ref:`inlinedrawing_extension` to store the :kl-ref:`InlineDrawing` singleton.

.. note:: You can only store KL objects in the global map, not KL structs.

The :kl-ref:`Singleton_set`, :kl-ref:`Singleton_has` and :kl-ref:`Singleton_get`.

.. note:: Starting with 1.12.0 of |FABRIC_PRODUCT_NAME| the singletons are automatically destroyed when the core client is closed.

.. kl-example::

  require Singletons;

  object MySettings {

    /// \internal
    String values[String];

  };

  function MySettings.set!(String key, String value) {
    this.values[key] = value;
  }

  function String MySettings.get!(String key) {
    return this.values.get(key, '');
  }

  function setupSettings() {

    MySettings settings = MySettings();
    settings.set('language', 'english');
    settings.set('localization', 'us');

    // in this function's scope we create an object and
    // store it in the singletons extension's memory.
    // note that it otherwise would run out of scope and
    // get destroyed.
    Singleton_set('settings', settings);
  }

  operator entry() {

    setupSettings();

    // check if we have the singleton in this scope.
    if(Singleton_has('settings')) {

      MySettings settings = Singleton_get('settings');
      if(!settings) {
        setError('Singleton settings is set, but not of KL type MySettings!');
      } else {
        report('Language setting: '+settings.get('language'));      
        report('Localization setting: '+settings.get('localization'));      
      }
    }

  }

One of the Singletons unittests:

.. kl-fileexample:: ${FABRIC_SCENE_GRAPH_DIR}/Tests/Singletons/Singletons_Test1.kl

Table of Contents
-----------------

.. toctree::
  :maxdepth: 2
  
  files
  functions

Indices and Tables
------------------

* :ref:`genindex`
* :ref:`search`
