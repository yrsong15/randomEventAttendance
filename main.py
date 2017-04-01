import re
import sys
from random import sample

def randomSelection(names, num):
	return sample(xrange(len(names)), num) if len(names) > num \
		else "Sample size larger than population"

def startRead(filename):
	with open(filename) as f:
		content = [x.strip('\n') for x in f.readlines()]
	return content

if __name__=="__main__":
	filename = raw_input("Please input the filename: ")
	numInput = raw_input("How many people will be attending the event? ")
	# if len(sys.argv) != 3:
	# 	print "Incorrect number of arguments!\nExiting program."
	# 	sys.exit()
	try:
		# num = int(sys.argv[2])
		num = int(numInput)
	except ValueError: print "Second argument must be an integer."
	# names = startRead(sys.argv[1])
	# indices = randomSelection(names, num)
	names = startRead(filename)
	indices = randomSelection(names, num)
	if type(indices) is not list:
		print indices
		sys.exit()
	for i in indices:
		print names[i]


