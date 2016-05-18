import sys

aHandle = open (sys.argv [1])      #this is the random sequence we created from randseq.py

lines = aHandle.readlines ()

aMap = {}

id = 0

for aLine in lines:

	aLine = aLine.replace ("\n", "")    #each random sequence generated 

	aMap [id] = aLine    #aMap is the line number for the randseq file (aka the second input from the randseq script). the ID (number 0-2535) is the key, aLine is the sequence so the value
	
	id = id + 1

bHandle = open (sys.argv [2])   #the numbers from the output of the getGeneOrder.py (getGeneOrder_proteome?) 

lines = bHandle.readlines ()

genome = ""

for aLine in lines:
	
	aLine = aLine.replace ("\n", "")
	words = aLine.split (" ")
	
	for aWord in words:
#		print aWord         #aWord is the numbers from the getGeneOrder, one by one
		genome = genome + aMap [int (aWord)]       #this is making a string called genome. It appends to the string the dictionary. It uses the GetOrder output (the number ...
								#for each line) and prints the sequence that corresponds to that number (original key)
		
print ">pseudo" + sys.argv [2] + "\n" + genome     #this is printing the stuff in the order from the getGeneOrder file, not like 0,1,2,3,4, etc. 
