import sys
import math

####### comparing genomes. genome 1 must == p1g1
output_p1_g1= open(sys.argv[1]).read().splitlines()    #use the output from parsegenomQT.py. We have to do this because they say so
output_p1_g2= open(sys.argv[2]).read().splitlines()

############################ define all variables to do math on in the matrix #######################################
GC1= output_p1_g1[0]
GC1=float((GC1.split())[3])
GC2=output_p1_g2[0]
GC2=float((GC2.split())[3])


####### first method- compare GC content #########

D_GC_12=math.sqrt(math.pow((GC1-GC2), 2))
D_GC_21=math.sqrt(math.pow((GC2-GC1), 2))
if D_GC_12 == D_GC_21:
	print "Distance values are valid: ", D_GC_12

