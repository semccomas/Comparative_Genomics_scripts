
import sys
import matplotlib.pyplot as plt
import numpy as np
##### first read the file and access the values######
filename= open(sys.argv[1]).read().splitlines()    #use TF_and_SP_sarah
out= sys.argv[2] 
out= open(out, 'w')

TM_fractions=[ ]
avg_TM = [ ] 
for line in filename:
	number=line.split()
	number=number[0]
	if "percent of transmembrane" in line:
		TM_fractions.append(number)           #this will print the fractions in order
	if "average number of transmembrane" in line:
		avg_TM.append(number)               #this will also print the numbers in order, therefore the two will match in a plot

print TM_fractions
print avg_TM



##################plot the values ##############

x= np.asarray(TM_fractions)
y=np.asarray(avg_TM)
plt.scatter(x, y)
plt.xlabel('Fraction of Transmembrane (out of 1)')
plt.ylabel('Average Number of Transmembrane segments')
#plt.show()
plt.savefig(out)
