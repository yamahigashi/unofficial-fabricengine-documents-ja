import FabricEngine.Core
client = FabricEngine.Core.createClient()

myTypeSource = """
function MyType(String string, UInt32 uint32) {
  this.string = string;
  this.uint32 = uint32;
}

function MyType.tweet() {
  report("Tweet tweet!  string='" + this.string + "' uint32=" + this.uint32);
}

function MyType.append!(MyType that) {
  this.string += that.string;
  this.uint32 += that.uint32;
}
"""
myTypeDesc = {
  'members': [{'string': 'String'}, {'uint32': 'UInt32'}],
  'klBindings': {
    'filename': "(inline)",
    'sourceCode': myTypeSource
   }
}
client.RT.registerType('MyType', myTypeDesc)
print client.RT.getRegisteredTypes()['MyType']

myRTVal = client.RT.types.MyType("Hello", 42)
print myRTVal

myRTVal.tweet('')

myRTVal2 = client.RT.types.MyType(", there", 71)
print(myRTVal2)
myRTVal.append('', myRTVal2)
myRTVal.tweet('')

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RuntimeError: first parameter to method call must be result type (or empty string)
>>> myRTVal2.tweet('')
[FABRIC:MT] Tweet tweet!  string=', there' uint32=71
>>> ^D
