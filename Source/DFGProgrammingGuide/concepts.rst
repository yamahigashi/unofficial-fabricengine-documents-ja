DFG Concepts
====================

The DFG has some important underlying concepts that are the basis for its design.

Note that we will often refer to "a DFG"; we will use this to mean a DFG executable bound to argument values that can therefore be executed.

The DFG is a KL Generator
-------------------------

The Fabric DFG is a visual programming language that generates KL code from data flow graphs.  This process is mostly hidden from the user. This is important for several reasons:

- DFG graphs are always JIT compiled and never interpreted.  There will be little if any performance difference between a DFG and hand-written KL code.

- Visual programming and KL code can be intermixed within a DFG.  If there are parts of a DFG that would be easier to write in KL then it is easy to do so.  In fact, all of the lowest-level DFG presets are all written in KL.

- A DFG has access to the full range of KL features; for instance, a DFG can access all of the Fabric Extensions.

- Values flowing through a DFG are simply KL types.  If you need to add a new type to the DFG it is just a matter of adding it in a Fabric extension.

Note that while the DFG internally generates KL code the API used to run DFG programs takes care of this for you automatically; there is no need to manually compile the KL code to execute it.

Instancing
---------------------

The DFG makes a strong distinction between entities and instances of those entities.  For example, one type of entity is called an Executable, and instances of those executables are called Nodes.  Nodes are contained within Graphs, which themselves are a type of Executable.

Another example is Ports, which belong to Executables, and Pins, which belong to Nodes: for each Port of the Executable there is one Pin on each Node that is an instance of the executable.  When connections are made between Nodes in a Graph they are made between the Pins; therefore, the connections are not shared between the instances (which would make no sense).

The distinction between entities and instances is important because it encapsulates the sharing of functionality in the DFG.  When edits are made to an Executable those edits effect each Node instance of the executable.  If a Port of an Executable is renamed then ever Pin instance of the Port is also renamed.

This sharing is important for performance reasons.  If we were to make a copy of each preset each time it was instanced then we would potentially have to compile the same preset code many times in order to compile the graph.

It is possible to clone executables to make independent copies by simply exporting the executable as JSON and then reimporting it.  This will eventually be implmented in the UI as a "Clone" command.

Port Types
--------------------

There are three port types in the DFG: In, Out and IO.  In and Out work exactly as expected.  The IO port type refers to a value that is modified in place, similar to an 'io' parameter in KL.  The IO port has important use in the DFG because it allows you to reduce temporary copies of data; for example, a MeshMerge operation is more efficient if the second mesh is merged into the first.

We envision that IO ports will be a natural fit for building simulations using the DFG: the simulation "context" would be passed through the graph as an IO port.

Addressing
------------------

In the DFG API we use string addressing to access everything.  A Binding is an Executable that is bound to a set of RTVals that are passed to the Executable's Ports; a Binding also provides a root for addressing the elements below it.

For example, a Binding may be to a Graph which contains a Node called "Add".  The "Add" Node has a Pin called "lhs" since the Node is an instance of an Executable with a Port called "lhs".  Then, within the context of the binding, the Pin is addressed by "Add.lhs".

When creating new entities and instance we automatically ensure that there names are unique.  For example, if you try to create a new Port called "value" on an Executable and there is already a Port with this name the new Port will be renamed to "value2".  Note that while names need to be unique Executables have a title which does not need to be unique; however, these titles are purely cosmetic and not used for addressing.
