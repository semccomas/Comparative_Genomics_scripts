import sys

filename= open(sys.argv[1]).read().splitlines()  #output from the zgrep so it'll be like campylobacter_links osv

d= {}               #dictionary because it only allows for one key at a time to be present with as many values as you want 
count= 0

for line in filename:
	count= count +1
	line= line.split()
	protein= line[0][-4:]       
	protein2=line[1][-4:]	#the protein number in both columns of the line. Just including both for a sanity check to make sure the whole file is represented
	d[protein]=count      #add each value to the dict. It'll automatically reassign the new value to the key if the key exists
	d[protein2]=count
print 'number of proteins: ' ,  len(d)
print 'number of links: ' , count
print 'average connectivity (links/proteins): ', float(count)/len(d)

