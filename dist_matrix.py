from Bio import SeqIO 
import sys
from Bio.SeqUtils import GC 
import math


####### comparing genomes. genome 1 must == p1g1
#genome1= open(sys.argv[1])   #first genome to compare
#genome2=open(sys.argv[2])   #second genome to compare
output_p1_g1= open(sys.argv[1]).read().splitlines()    #use the output from parsegenomQT.py. We have to do this because they say so
output_p1_g2= open(sys.argv[2]).read().splitlines()

############################ define all variables to do math on in the matrix #######################################
GC1= output_p1_g1[0]
GC1=float((GC1.split())[3])
GC2=output_p1_g2[0]
GC2=float((GC2.split())[3])






'''
    		#### find the frequencies- use genomes file####
################ YOU HAVE TO DIVIDE BY LEN FIRST BEFORE THIS WORKS ################# 
for record1,record2 in zip(SeqIO.parse(genome1, 'fasta'), SeqIO.parse(genome2, 'fasta')):          #be able to parse both at the same time
#	GC1 = GC(record1.seq)
#	GC2 = GC(record2.seq)
	
	A1=(record1.seq).count('A')
	A2=(record2.seq).count('A')
	
	T1=(record1.seq).count('T')
        T2=(record2.seq).count('T')
	
	C1=(record1.seq).count('C')
        C2=(record2.seq).count('C')

	G1=(record1.seq).count('G')
        G2=(record2.seq).count('G')
	


'''	
####### first method- compare GC content #########

D_GC_12=math.sqrt(math.pow((GC1-GC2), 2))
D_GC_21=math.sqrt(math.pow((GC2-GC1), 2))
if D_GC_12 == D_GC_21:
	print "Distance values are valid: ", D_GC_12













##### second method- compare frequencies ##########

#D_F_12=math.sqrt(math.pow(math.pow((T1-T2), 2) + math.pow((A1-A2), 2) + math.pow((C1-C2), 2) +math.pow((G1-G2), 2) , 2))
#D_F_21=math.sqrt(math.pow(math.pow((T2-T1), 2) + math.pow((A2-A1), 2) + math.pow((C2-C1), 2) +math.pow((G2-G1), 2) , 2))
#if D_F_12 == D_F_21:
#	print "Distance values are valid: " , D_F_12
#else:
#	print "Distance values are not valid!!! " , D_F_12, "!=" , D_F_21 

#### 

