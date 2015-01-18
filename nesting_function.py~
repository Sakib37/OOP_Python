def outside():
	x = 5
	def printsakib():		# printsakib() is an object of outside()
		print x
	return printsakib		# Function outside is returning function printsakib
	
myFunc = outside()			# myFunc = printsakib() cz outside() returns printsakib() function

""" myFunc is not a variable but function. The cool thing is 
myFunc has access to the local variable 'x' of outside() function.
Usually from outside of function outside() function we should not be 
able to access that local variable x """
myFunc()					

# Alternatively we can use the same feature as follow
def A_outside( x = 5 ):
	def printsakib():
		print x 
	return printsakib

myFunc = A_outside( 340)
myFunc()


# Lets pass function as an argument to another function
def addOne( myFunc ):
	def addOneInside():
		return myFunc() + 1
	return addOneInside
	
def oldFunc():
	return 3
	
newFunc = addOne( oldFunc )		# oldFunc is decorated to create a newFunc
print oldFunc(), newFunc()

# The above feature is called decorator
def addOne( myFunc ):
	def addOneInside():
		return myFunc() + 1
	return addOneInside

""" this @addOne above oldfunction means the line 
oldFunc() = addOne( oldFunc )  in the the code. If a fucntion is decorated
when we call the decorated function (here oldFunc ) it will always
run through the function (here addOne ) which decorate it"""
@addOne	
def oldFunc():
	return 3
	
	
print oldFunc()

# Now we will do the same thing with argument passing opportunity
def addOne( myFunc ):
	def addOneInside(*args, **kwargs):
		return myFunc(*args, **kwargs) + 1
	return addOneInside

@addOne	
def oldFunc( x = 30 ):
	return x
	
	
print oldFunc()

