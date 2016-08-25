
Hello World
============

The sample below shows the most basic use of the SPLICECAPI. This can be used to test the library and establish the right linker settings etc.

.. code-block:: c++

    #include <FabricSplice.h>

    using namespace FabricSplice;

    int main( int argc, const char* argv[] )
    {
      Initialize();

      // create a graph
      DGGraph graph = DGGraph("myGraph");

      // construct a single DG node
      graph.constructDGNode();

      // create an operator
      std::string klCode = "";
      klCode += "operator helloWorldOp() {\n";
      klCode += "  report('Hello World from KL!');\n";
      klCode += "}\n";
      graph.constructKLOperator("helloWorldOp", klCode.c_str());

      // // evaluate the graph
      graph.evaluate();

      Finalize();

      return 0;
    }
