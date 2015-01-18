import time as t				
# This will import time and we can use it as t
from os import path
# This will double check that the path is not already created in the path


	

def createFile(dest):
	# After every ':' indentation is must, no exception for comments
	"""This script creates a text file at the passed in location, names file based on date """

	date = t.localtime( t.time() ) 	
	# t.time() will grab the local time and t.localtime will convert it to a usable form in a list

	name = '%d_%d_%d.txt' % ( date[2], date[1], (date[0] % 100))
	# filename = date_month_year(2 digit).txt
	
	if not ( path.isfile( dest + name )):
	# path.isfile( dest + name ) will return true if there is already a file existing 
	
		f = open( dest + name, 'w') 
		# open a file by name with write permission
		f.write( '\n' * 30 )
		# press ENTER 30 times
		f.close()
	

if __name__=='__main__':
# If filename == main or if this is the main file 
	destination = '/home/sakib/Desktop/python/py'
	
	createFile(destination)
	raw_input("done!!!")


