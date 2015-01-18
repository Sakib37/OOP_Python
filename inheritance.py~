""" learning of OOP in Python by Mohammad Badruzzaman
	All the programs will contain detail explanation for my understanding"""
class BaseClass( object ):
	"""This class is inherited form a base class 'object' which is a base class of python which allows inheritance to happen. If we delete
	 the object and inherit only functions from the baseclass then no error will occur. But if we want to access to a variable or instance
	 of the base class an error will occur. So it is a good practice to inherit object class form python"""
	def printfish( self ):
		print 'fish'

class InheritingClass( BaseClass ):	# Child class of BaseClass
	pass

x = InheritingClass()
x.printfish()

# Another baseclass
class Character( object ):
	def __init__(self, name ):
		self.health = 100
		self.name = name 
	
	def printName( self ):
		print self.name 
	
		
		
class Blacksmith( Character ):
	def __init__( self, name, forgeName):
		""" super is used to accessing the constructor of the base class from the child class. If the base class is not inherited from the
		'object' class of python we would not be able to access the constructor of the base class like this. When dealing with OOP it is
		good parctice to use a visualizing diagram called UML(Unified Modeling Language)"""
		super( Blacksmith, self ).__init__( name )    # as base constructor takes one parameter
		self.forge = Forge( forgeName ) # creating an instance of Forge class inside Blacksmith class


class Forge():
	def __init__( self, forgeName ):
		self.name = forgeName
		
		
		
bs = Blacksmith( 'smith', 'Rick\'s Forge' )
# accessing a variable of baseclass from an instance of childclass
print bs.health	
bs.printName()
print bs.forge.name	   # accessing forge object of Blacksmith then accessing name object of Forge class

# Testing child of child can access the base class or not
class SuperBlacksmith(Blacksmith):
	def __init__( self ):
		super( SuperBlacksmith, self).__init__('Stefan', 'Clement\'s forge')

sbs = SuperBlacksmith()
print sbs.health 
sbs.printName()
print sbs.forge.name	
# wow it is possible :)"""
