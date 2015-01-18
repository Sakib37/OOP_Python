""" Creating class in two different ways """
class MyClass( object ):
	def __init__( self ):
		self.x = 5

# new method
TypeClass = type("TypeClass", ( object, ), { "x" : 5 })  
"""TypeClass inside the type() is the actual class where the variable will be stored. After the class name the name of the class from which 
it is inherited, here 'object', with an additional comma. And then the variable and functions."""

m = MyClass()
t = TypeClass()

print m.x, t.x

# Now function in new method

def printsakib( self ):
	print 'sakib'

TypeClass2 = type("TypeClass2", ( object, ), { "x" : 10,  "pH" : printsakib }) 

z = TypeClass2()
z.pH()

""" Why use this new method
	it allows creation of class on the fly and it has small number of code"""
	
# Now lets create the metaclass
class Singleton( type ):		# Inherited from 'type' class that allow the creation of other classes 
	_instances = {}				# stores instances in a dictionary
	def __call__( cls, *args, **kwargs ):
		if cls not in cls._instances:
			cls._instances[cls] = super( Singleton, cls).__call__( *args, **kwargs )
			cls.x = 5
		return cls._instances[cls]
		
		
class MyClass( object ):
	__metaclass__ = Singleton	# When MyClass is defined python will search for a metaclass and we declared Singleton as the metaclass here
	
m = MyClass()					# As MyClass is a Metaclass of Singleton, only one instance can be created
v = MyClass()					# So instance m and v refers to the same instance
print m.x
m.x = 20						# This change the value  of v also
print v.x						# v.x will be 20 now
