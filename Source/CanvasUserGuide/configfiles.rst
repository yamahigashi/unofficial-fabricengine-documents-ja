.. _canvas-user-guide-configfiles:

Configuration Files
=====================

Most of the options in the UI are gathered in a config file, which is located in :file:`Resources/default.config.json`. This is a JSON file which looks like this :

.. code-block:: javascript

  {
    "GraphView" : {
      "mainPanelBackgroundColor" : {
        "r" : 55,
        "g" : 55,
        "b" : 75
        },
      "nodeDefaultColor" : {
        "r" : 175,
        "g" : 120,
        "b" : 120
        },
      "nodeCornerRadius" : 12.0,
      "nodeFont" : {
        "family" : "Verdana",
        "pointSize" : 16,
        "weight" : 75
        },
      "pinFont" : {
        "family" : "Verdana",
        "pointSize" : 8,
        "weight" : 50,
        "pointSizeF" : 8.0,
        "styleHint" : 5,
        "hintingPreference" : 3
        },
      "middleClickDeletesConnections" : true
      }
    }

The options can be modified there, or in the file :file:`Resources/user.config.json` (empty by default). The values added to the `user` config will override the values of the `default` config.
