""" In this file I will learn about abstract classes and multiple inheritances 
What is abstract class?
An abstract base class cannot be instantiated i.e. this kind of class can be used only to form subclasses. Abstract class is also called virtual class"""

from abc import ABCMeta, abstractmethod
class BaseClass( object ):
	__metaclass__ = ABCMeta		#declaring BaseClass as abstract base class		
	
	""" the following declaration of @abstractmethod is called decorator. Decorator is a way to alter functions or classes without having
	 to inherit of subclass"""
	@abstractmethod					
	def printsakib( self ):
		pass 

class InClass( BaseClass ):
	def printsakib( self ):
		print "sakib"
		
# x = BaseClass()   // Cannot instantiate BaseClass as it is an abstract class but inhariting the child class is allowed

x = InClass()
x.printsakib()

""" Multiple base class
	Why use multiple inheritance?
	Sometimes may be we want to mix multiple classes flavour in one class"""
class Enemy( object ):
	__metaclass__ = ABCMeta
	
	@abstractmethod
	def attackPlayer( self, player):
		pass
	
class EnvironmentAsset( object ):
	__metaclass__ = ABCMeta
	
	@abstractmethod
	def __init__( self ):
		self.mobile = False
	
class Trap( Enemy, EnvironmentAsset ):
	def __init__( self ):
		super( Trap, self).__init__()
	
	def attackPlayer( self, player ):
		return player.health - 10
		
x = Trap()

