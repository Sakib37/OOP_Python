""" FSM(Fininite State Machine) is a design to simplify the algorithm of a OOP by showing transition from one class to another class and
 element that cause that transition. This program is to design FSM for a bulb between on and off state"""
 
from random import randint
from time import clock 		# This is used to keep track of time
 
 ##====================================================================
 
State = type( "State", (object,), {}) 		# This create the state base class
 
class LightOn( State ):
	def Execute( self ):
		print "Insdite LightOn"
 		print "Light is on"
 		
class LightOff( State ):
	def Execute( self ):
		print "Insdite LightOff"
 		print "Light is off"
 		
##====================================================================

class Transition( object ):
	def __init__( self, toState ):
		self.toState = toState
		
	def Execute( self ):
		print "Transitioning..."
		
##====================================================================

class SimpleFSM( object ):
	def __init__( self, char ):		#
		self.char = char
		self.states = {}
		self.transitions = {}
		self.curState = None
		self.trans = None
	
	def SetState( self, stateName ):
		self.curState = self.states[ stateName]
		
	def Transition( self, transName ):
		print "Inside Transition"
		print transName
		self.trans = self.transitions[transName]
	
	def Execute( self ):
		if( self.trans ):			# If there is a transition stored in self.trans then
			self.trans.Execute()	# Execute the transition
			self.SetState( self.trans.toState )	# set the current state to the tranferred state
			self.trans = None		# Reset self.trans 
		self.curState.Execute()		# Execute the current state
					
			
			
##====================================================================

class Char( object ):
	def __init__( self ):
		self.FSM = SimpleFSM( self )	# Creating an instance of SimpleFSM class. But why self is used to create an instance!!!! Consider it as a function inside Char class
		self.LightOn = True

##====================================================================

if __name__ == "__main__":
	light = Char()							# Instance of Char class
	light.FSM.states["On"] = LightOn()		# Instance of LightOn Class
	light.FSM.states["Off"] = LightOff() 	# # Instance of LightOff Class
	light.FSM.transitions["toOn"] = Transition("On")
	light.FSM.transitions["toOff"] = Transition("Off")
	
	light.FSM.SetState("On")
	
	for i in range( 20 ):					# run through the code 20 times
		startTime = clock()					# store the clock time
		timeInterval = 1			
		while( startTime + timeInterval > clock()):  # while the clock does not cross 1 second, continue looping
			pass
		if( randint( 1, 2 )):				# picks integer 0 or 1
			if( light.LightOn):
				light.FSM.Transition("toOff")
				light.LightOn = False
				print light.LightOn
			else:
				light.FSM.Transition( "toOn")
				light.LightOn = True
				print light.LightOn
	light.FSM.Execute()	
	
##====================================================================

