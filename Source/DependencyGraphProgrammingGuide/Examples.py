# Obtaining the FABRIC object
import fabric
FABRIC = fabric.createClient()

# Registered types
class Vec3():
  def __init__( self, x = None, y = None, z = None ):
    if type( x ) is float and type( y ) is float and type( z ) is float:
      self.x = x
      self.y = y
      self.z = z
    elif x is None and y is None and z is None:
      self.x = 0
      self.y = 0
      self.z = 0
    else:
      raise Exception( 'Vec3: invalid arguments' )

FABRIC.RT.registerType('Vec3', {
  'members': [{'x': 'Scalar'}, {'y': 'Scalar'}, {'z': 'Scalar'}],
  'constructor': Vec3,
  'klBindings': {
    'filename': "(inline)",
    'sourceCode': """
// Construct a Vec3 from three Scalars
function Vec3(Scalar x, Scalar y, Scalar z) {
  this.x = x;
  this.y = y;
  this.z = z;
}
// Add two Vec3s
function Vec3 + (Vec3 a, Vec3 b) {
  return Vec3(a.x + b.x, a.y + b.y, a.z + b.z);
}
"""
  }
})
FABRIC.RT.getRegisteredTypes()['Vec3']

# Node creation
node = FABRIC.DG.createNode('verticies')

# Getting a Node's name
node.getName()

# Adding and getting members
node.addMember("position", "Vec3", Vec3(0.0, 0.0, 0.0))
node.getMembers()['position']

# getData and setData
vars(node.getData('position', 0))
node.setData('position', 0, Vec3(1.0, 2.0, 3.0))
vars(node.getData('position', 0))

# Node slice counts
node.getCount()
node.getData('position', 1)
node.setCount(2)
node.getCount()
vars(node.getData('position', 1))

# Node dependencies
anotherNode = FABRIC.DG.createNode("originalVertices")
node.setDependency(anotherNode, "original")
node.getDependencies()

# Node evaluation
op = FABRIC.DG.createOperator("offsetPosition")
op.setEntryPoint("offset")
op.setSourceCode("require Vec3; operator offset(io Vec3 position, io Vec3 newPosition) { newPosition = position + Vec3(1.0,1.0,1.0); }")
binding = FABRIC.DG.createBinding()
binding.setOperator(op)
binding.setParameterLayout(["self.position", "self.newPosition"])
node.addMember("newPosition", "Vec3")
node.bindings.append(binding)
vars(node.getData("position", 0))
vars(node.getData( "newPosition", 0 ))
node.evaluate();
vars(node.getData( "newPosition", 0 ))

# Event creation
event = FABRIC.DG.createEvent("anEvent")
event.getName()

# Creating EventHandlers and appending them to Events
eventHandler = FABRIC.DG.createEventHandler("trivialEventHandler")
event.appendEventHandler(eventHandler)
event.getEventHandlers()

# Operators and EventHandlers
op = FABRIC.DG.createOperator("trivialOperator")
op.setSourceCode("operator entry() { report('Ran trivialOperator'); }")
op.setEntryPoint('entry')
binding = FABRIC.DG.createBinding()
binding.setOperator(op)
binding.setParameterLayout([])
eventHandler.preDescendBindings.append(binding)
event.fire()
anotherOp = FABRIC.DG.createOperator("trivialOperatorTwo")
anotherOp.setSourceCode("operator entry() { report('Ran trivialOperatorTwo'); }")
anotherOp.setEntryPoint('entry')
binding = FABRIC.DG.createBinding()
binding.setOperator(anotherOp)
binding.setParameterLayout([])
eventHandler.postDescendBindings.append(binding)
event.fire()

# Child EventHandlers
binding = FABRIC.DG.createBinding()
binding.setOperator(op)
binding.setParameterLayout([])
ceh = FABRIC.DG.createEventHandler("childEventHandler")
ceh.preDescendBindings.append(binding)
eventHandler.appendChildEventHandler(ceh)
event.fire()

# The setScope method
node = FABRIC.DG.createNode("someNode")
node.addMember( "x", "Scalar" )
node.addMember( "y", "Scalar" )
squareOp = FABRIC.DG.createOperator("squareOp")
squareOp.setSourceCode("operator entry( io Scalar x, io Scalar y ) { y = x * x; }")
squareOp.setEntryPoint("entry")
binding = FABRIC.DG.createBinding()
binding.setOperator(squareOp)
binding.setParameterLayout(['self.x','self.y'])
node.bindings.append(binding)
displayOp = FABRIC.DG.createOperator("displayOp")
displayOp.setSourceCode( "operator entry( io Scalar x, io Scalar y ) { report(x + ' squared is ' + y); }" )
displayOp.setEntryPoint("entry")
binding = FABRIC.DG.createBinding()
binding.setOperator(displayOp)
binding.setParameterLayout(['mynode.x','mynode.y'])
eventHandler.setScope("mynode",node)
eventHandler.postDescendBindings.append(binding)
event.fire()
node.setData('x',5.0)
event.fire()

# EventHandler data 
eventHandler.setScopeName("childEventHandler")
eventHandler.addMember("x","Scalar")
eventHandler.addMember("y","Scalar")
binding = FABRIC.DG.createBinding()
binding.setOperator(squareOp)
binding.setParameterLayout(['childEventHandler.x','childEventHandler.y'])
ceh.preDescendBindings.append(binding)
binding = FABRIC.DG.createBinding()
binding.setOperator(displayOp)
binding.setParameterLayout(['childEventHandler.x','childEventHandler.y'])
ceh.preDescendBindings.append(binding)
event.fire()
eventHandler.setData("x",7.31)
event.fire()

# Operator creation
op = FABRIC.DG.createOperator("doSomething")

# Setting operator source code
op.setSourceCode("operator entry( io Scalar result, in Size index, in Container self ) { result = 3.14 }")
op.getDiagnostics()
op.setSourceCode("operator entry( io Scalar result, in Size index, in Container self ) { result = 3.14; }")
op.getDiagnostics()

# Setting the operator entry point
op.setEntryPoint('entry')
op.getEntryPoint()

# Binding creation
binding = FABRIC.DG.createBinding()
binding.setOperator(op)
binding.getOperator()

# Binding parameters
binding.setParameterLayout( ["self.result","self.index","self"] )
node = FABRIC.DG.createNode("foo")
node.bindings.append(binding)
node.getErrors()
node.addMember("result","Scalar")
node.getErrors()

