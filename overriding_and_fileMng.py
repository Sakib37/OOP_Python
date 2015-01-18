""" This file will show variable overriding in the child class and file management in python. Overriding is usually required to ensure that
the variable is attached with the class and prevent program from crashing when variable dont exist"""
class BaseClass( object ):
	def __init__ ( self ):
		self.x = 10 
	
	def test( self ):
		print "Sakib"

class InClass( BaseClass ):
	def __init__( self ):
		super( InClass, self ).__init__		# Inherit constructor of Base Class
		self.x = 20		# Overriding the variable of base class
	def test( self ):
		print "Sakib is trying to learn python"

ob = InClass()
print ob.x
ob.test()

""" Why separating a file into multiple file? 
	If the classes are kept in a separate file then it is very easy to analyse and access classes in other prpgrams just by importing those clasess by using filename."""
	
print BaseClass.__subclasses__()		# This way we can check which classes are inheriting from base class
	


