#take the proteome_?_frequency as the input
import math
import sys
proteome1=open(sys.argv[1]).read().splitlines()
proteome2=open(sys.argv[2]).read().splitlines()


def calculate(freq1, freq2):
	distance=math.pow((float(freq1)-float(freq2)), 2)
	return distance
	
############### first access the values in the file, have to add them to a list because they need to be accessible at the same time ###########
line1= []
line2= [] 
for line, linee in zip(proteome1, proteome2):
	if 'frequency' in line:
		line= line.split()
		line1.append(line[3])
	if 'frequency' in linee:
		linee=linee.split()
		line2.append(linee[3])


################### now to run the function on both at the same time ###################
all_dists1= [ ]
all_dists2= [ ]

for freq,freq2 in zip(line1, line2):
	dist1= calculate(freq,freq2)				#now we can just talk about the numbers themselves, not the line values in the file
	all_dists1.append(dist1)
	dist2= calculate(freq2, freq)
	all_dists2.append(dist2)				#need a list so you can make a sum of the values
						

final_d1=math.sqrt(math.fsum(all_dists1))   			#the end calculation, do for both to make sure they're equal
final_d2=math.sqrt(math.fsum(all_dists2))

####the final check####
if final_d1==final_d2:
	print "distances are valid: ", final_d1
else:
	print "distances are not valid!!"
