import sys

# acquire first needed data

geneOrderList = []

aHandle = open (sys.argv [1])   #proteome_?

lines = aHandle.readlines ()

for aLine in lines:

	aLine = aLine.replace ("\n", "")

	if aLine.startswith (">"):

		#print aLine [1:len (aLine)],      #this is just the protein names so like proteome_2-orf00001, proteome_2-orf00002 blah blah
		geneOrderList.append (aLine [1:len (aLine)])

# acquire second needed data

partOfCluster = {}

bHandle = open (sys.argv [2])   #prot_parsed_?.NEW?????

lines = bHandle.readlines ()

id = 0

for aLine in lines:

	aLine = aLine.replace ("\n", "")
#	words = aLine.split ("\t") #just a list of the each line   #HEY I COMMENTED THIS ONE OUT LOOK HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	words= aLine.split()
	
	
	for aWord in words:   #aWord is the orf name. It is the WHOLE LINE. Ex: proteome_5-orf00001 proteome_2-orf00232 proteome_5-orf00001 proteome_4-orf02342

		if not partOfCluster.has_key (aWord):

			partOfCluster [aWord] = id    #making some kind of count. Gets up to like 3400 which is number of orfs in proteome_5
#			print partOfCluster         #dictionary of 'proteome_5 orf00005 proteome_9 orf01275' : number (id) . They don't match though... 
#			print aWord

	id = id + 1

# put together

for aGene in geneOrderList:
#	print aGene          #aGene is proteome_2_orf00002, proteome_2-orf000023 if you are using proteome_2. It's coming from your first input, the proteome file
	if partOfCluster.has_key (aGene):     #nothing prints so far.... I think because aGene is not == aWord so there are no keys in this dic at all 

		print partOfCluster [aGene],         # aGene

#print partOfCluster
