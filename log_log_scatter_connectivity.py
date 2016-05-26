import sys
import matplotlib.pyplot as plt
import numpy as np

##### first read the file and access the values######
f= open(sys.argv[1]).read().splitlines()    #use *species*_links
out= sys.argv[2]
out= open(out, 'w')

count= 0
num_links= [ ]
s= []
for line in f:
	count= count + 1    				 #assign a variable to mark the end of the line so that you don't index too far
for n, fileline in enumerate(f):
	line=fileline.split()				   #access only protein number
	protein= line[0][-5:]				 #obs some plots might be -4 depending on the numbers in the seq don't forget. it was always -4 in the connectivity script though

	if n+1 != count:  				 #don't go over the count so list isn't indexted too far
		if protein in f[n+1]: 	         	   #check next line
			s.append(protein)	         #add to the list
		else:	                                 #can't forget the last protein in the list, if there is no match in the next line, add the last value, and start over
			s.append(protein)
			num_links.append(len(s))    	 #do this as soon as the list is ending, if you have it in the if statement above, it'll add the length each time it grows
			s= []                       	 #if not in next line, empty the list and start over
num_links.append(len(s)+1)                           	 #you have to do this again to account for the last s list, which won't be included otherwise. Also has to be outside all other loops to stop iteration. The final s will only be included then, and to account for the last line in the file, where n+1 == count, you just add a 1 

#### sum(num_links) should == total line count for file. This num_links will become the distribution for each node, and we are plotting a log function of it, found below


########### find the freq of the values ############
d= {}
for item in num_links: 
	d[item]=num_links.count(item)           #the key is the number of links (aka node degree) and the value is the frequency of that number

########## input for graph & graph itself. len X coord must == len Y cord ###############
node_degree= [ ] 
freq= [ ]
for key in d:
	node_degree.append(key)     		#prepare for numpy arrays
	freq.append(d[key])

node_degree=np.log10(node_degree)		#apply log function
freq= np.log10(freq)
plt.loglog(node_degree, freq)			#plt.loglog gives the necessary plot for this
plt.xlabel('Node degree') 
plt.ylabel('Frequency')
#plt.show()
plt.savefig(out)
