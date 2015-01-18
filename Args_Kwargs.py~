def Func( *args ):
	""" *ARGS is used to take unlimited number of arguments. This prevent a program from crashing if argument number exceeds. same in C, C++. *args save arguments in a "list". so to read the arguments we can use the for loops as follows"""
	for arg in args:
		print arg
		
Func( 1, 2, 3, 'sakib' )
		
li = [1, 2, 3, "sakib"]
Func( li )
Func( li[2], li[3] )
Func( *li )


def Fu( x = 234, y = 9 ):
	""" This way we can send default argument. If no argument value is declared then x =234 and y =9 will be used"""
	print x, y
	
Fu ()
Fu (x = 340, y = 20)

# here comes **Kwargs (keywordaraguments)

def func(**kwargs):
	"""  **kwargs use dictionary to store the arguments value. we can read the arguments from Kwargs dictionary as follows"""
	for item in kwargs.items():
		print item

func( x = 370, y = 2 )


# Now lets use both of them 

def Function ( *args, **kwargs):
	for arg in args:
		print arg
	for item in kwargs.items():
		print item

# while calling the order of argument and keywordarguments has to be remain. If we declare kwargs first and then the args, it will create an error
Function( 1, 3, 'sakib', x = 30, y = 40 )



