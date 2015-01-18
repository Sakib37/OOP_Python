""" Factory is a design pattern which allows a function to choose the class to be created"""

# Class creation in a new method
BaseClass = type("BaseClass", ( object,), {})	# Inherited from 'object' class of python
C1 = type ("C1", (BaseClass,), {"x" : 1})		# Inherited from BaseClass
C2 = type ("C2", (BaseClass,), {"x" : 30})		# Inherited from BaseClass

def MyFactory( myBool ):						# Factory created
	return C1() if myBool else C2()				# Choosing class to be returned
	
m = MyFactory( True )
v = MyFactory( False )

print m.x, v.x
""" Factory design is possible only when the subclasses are inherited from a common baseclass. Here C1 and C2 both inherited from BaseClass"""




# Now lets learn @classmethod
class MyClass:
	@classmethod
	def printsakib( self ):
		print 'Sakib'
		
MyClass.printsakib() 			# without using any instance we access the function of a class. @classmethod allows this feature

"""Now consider the first part. If we have 100's of subclasses like C1, C2...C100 then a lot of if statement will be needed which is pretty
difficult to manage. So lets find out a cleaner method"""


BaseClass2 = type("BaseClass2", (object,), {})

@classmethod
def Check1( self, myStr ):			# Function to bind with class C12
	return myStr == "sakib"
	
@classmethod
def Check2( self, myStr ):			# Function to bind with class C22
	return myStr == "hamba"
	

C12 = type ("C12", (BaseClass2,), {"x" : 1, "Check" : Check1})		# Inherited from BaseClass2 and Check1 function is bind in the class C12 with the function  name 'Check'
C22 = type ("C22", (BaseClass2,), {"x" : 30, "Check" : Check2})		# Inherited from BaseClass2 and Check2 function is bind in the class C22 with the function name 'Check'

def MyFactory2( myStr ):
	for cls in BaseClass2.__subclasses__():			# For each subclass of BaseClass2
		if cls.Check( myStr ):						# Call the function Check in that class by passing myStr in the argument. 
			return cls()							# if it is true then create a instance of that class and return it
			
a = MyFactory2( "sakib" )
b = MyFactory2( "hamba" )
print a.x, b.x
