
.. _scenemanagement:

FabricSplice::SceneManagement
===============================

The SceneManagement class provides static methods to perform certain scene management related tasks, such as draw all drawable :ref:`dgport` object, as well deal with interactive manipulation.

Class Outline
---------------------------------

.. code-block:: c++

    namespace FabricSplice
    {
      struct ManipulationData {
        int event;
        void * userData;
        const char * graphName;
        const char * portName;
        const FabricCore::RTVal * manipulationContext;
        const FabricCore::RTVal * manipulationResult;
      };

      typedef int(*ManipulationFunc)(ManipulationData * data);

      class SceneManagement
      {
      public:

        // sets the callback for manipulation
        static void setManipulationFunc(ManipulationFunc func);

        // returns true if there is anything to render
        static bool hasRenderableContent();

        // draw all drawable ports
        // ensure to only call this with a valid
        // OpenGL context set, otherwise it might
        // cause instabilities
        static void drawOpenGL(FabricCore::RTVal & drawContext);

        // raycast against all raycastable objects
        static bool raycast(FabricCore::RTVal & raycastContext, DGPort & port);
      };
    };
