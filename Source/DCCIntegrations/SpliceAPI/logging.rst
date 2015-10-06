
.. _logging:

FabricSplice::Logging
=========================

The Logging class provides static methods to redirect the log outputs of the SPLICECAPI. This includes output for KL report statements, KL queueStatusMessage statements as well as KL errors and compiler errors. Furthermore this class provides helper functions for profiling, measuring time and getting access to internal timers. Please refer to the 08_profiling sample in the api samples for an example of that.

Example
---------------------------------

The sample below shows how to use log redirection.

.. code-block:: c++

    #include <FabricSplice.h>

    using namespace FabricSplice;

    void myLogFunc(const char * message, unsigned int length)
    {
      printf("[MyCallback] %s\n", message);
    }

    void myLogErrorFunc(const char * message, unsigned int length)
    {
      printf("[MyCallback] Error: %s\n", message);
    }

    void myCompilerErrorFunc(
      unsigned int row, 
      unsigned int col, 
      const char * file,
      const char * level,
      const char * desc
    ) {
      printf("[MyCallback] KL Error: %s, Line %d, Col %d: %s\n", file, (int)row, (int)col, desc);
    }

    void myKLReportFunc(const char * message, unsigned int length)
    {
      printf("[MyCallback] KL Reports: %s\n", message);
    }

    void myKLStatusFunc(const char * topic, unsigned int topicLength,  const char * message, unsigned int messageLength)
    {
      printf("[MyCallback] KL Status for '%s': %s\n", topic, message);
    }

    int main( int argc, const char* argv[] )
    {
      Initialize();

      // setup the callback functions
      Logging::setLogFunc(myLogFunc);
      Logging::setLogErrorFunc(myLogErrorFunc);
      Logging::setCompilerErrorFunc(myCompilerErrorFunc);
      Logging::setKLReportFunc(myKLReportFunc);
      Logging::setKLStatusFunc(myKLStatusFunc);

      // create a graph
      DGGraph graph = DGGraph("myGraph");

      // create a DG node
      graph.constructDGNode();

      // create a member
      graph.addDGNodeMember("value", "Vec3");

      // create a port
      DGPort port = graph.addDGPort("value", "value", Port_Mode_IO);

      // create an op
      graph.constructKLOperator("testOp");

      // on purpose create a compiler error
      try
      {
        graph.setKLOperatorSourceCode("testOp", "operator testOp(Vec3 value) {adsadsd;}");
      }
      catch(Exception e)
      {
        printf("Caught error: %s\n", e.what());
      }

      // update the operator to report from KL
      graph.setKLOperatorSourceCode("testOp", "operator testOp() { report('my message');}");

      // evaluate will invoke all operators
      // and in this case also call the myKLReportFunc
      graph.evaluate();

      // update the operator to send a status update from KL
      graph.setKLOperatorSourceCode("testOp", "operator testOp() { queueStatusMessage('info', 'nothing going on!');}");

      // evaluate will invoke all operators
      // and in this case also call the myKLStatusFunc
      graph.evaluate();

      Finalize();
      return 0;
    }

Class Outline
---------------------------------

.. code-block:: c++

    namespace FabricSplice
    {
      typedef void(*LoggingFunc)(const char * message, unsigned int messageLength);
      typedef void(*CompilerErrorFunc)(unsigned int row, unsigned int col, const char * file, const char * level, const char * desc);
      typedef void(*StatusFunc)(const char * topic, unsigned int topicLength, const char * message, unsigned int messageLength);

      class Logging
      {
      public:

        // sets the callback for generic log messages
        static void setLogFunc(LoggingFunc func);

        // sets the callback for error log messages
        static void setLogErrorFunc(LoggingFunc func);

        // sets the callback for KL compiler error messages
        static void setCompilerErrorFunc(CompilerErrorFunc func);

        // sets the callback for KL report statements
        static void setKLReportFunc(LoggingFunc func);

        // sets the callback for KL queueStatusMessage statements
        static void setKLStatusFunc(StatusFunc func);

        // enable timers
        static void enableTimers();

        // disable timers
        static void disableTimers();

        // reset a timer
        static void resetTimer(const char * name);

        // start a timer
        static void startTimer(const char * name);

        // stop a timer and accumulate the time
        static void stopTimer(const char * name);

        // log a given timer
        static void logTimer(const char * name);      

        // return the number of existing timers
        static unsigned int getNbTimers();

        // return the name of a specific timer
        char const * getTimerName(unsigned int index);

        // a timer which records time on construction and destruction
        class AutoTimer
        {
        public:
          AutoTimer(std::string const &name);
          ~AutoTimer();

        private:
          std::string mName;
        };        
      };
    };
