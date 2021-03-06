""" singleton is a design pattern in which only one instance of 
a object may ever be created. In this file both longer way and the way 
using decorator is shown"""
# longer way
class MySingleton( object ):
	_instance = None
	def __new__( self ):
		if not self._instance:
			self._instance = super( MySingleton, self).__new__( self )
			self.y = 10
		return self._instance
		
x = MySingleton()
print x.y
x.y = 20

z = MySingleton()
print z.y


# Using decorator
def singleton( myClass ):
	instances = {}
	def getInstance( *args, **kwargs ):
		if myClass not in instances:
			instances[myClass] = myClass( *args, **kwargs )
		return instances[myClass]
	return getInstance
 
@singleton
class TestClass( object ):
 	pass
 
x = TestClass()
