def addSandwich( meat ):
	def addingSandwich():
		return meat() + "sandwich"
	return addingSandwich

@addSandwich		# decorating meat by making sandwich		
def meat():
	return "chicken "

print meat()
		
