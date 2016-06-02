from Bio import SeqIO 
import sys
from Bio.SeqUtils import GC 
import math

genome1= open(sys.argv[1])   #first genome to compare
genome2=open(sys.argv[2])   #second genome to compare

    		#### find the frequencies- use genomes file####
################ YOU HAVE TO DIVIDE BY LEN FIRST BEFORE THIS WORKS ################# 
for record1,record2 in zip(SeqIO.parse(genome1, 'fasta'), SeqIO.parse(genome2, 'fasta')):          #be able to parse both at the same time
	
	A1=(record1.seq).count('A')
	A1= (float(A1)/len(record1.seq))*100
	A2=(record2.seq).count('A')
        A2= (float(A2)/len(record2.seq)) *100
	
	T1=(record1.seq).count('T')
        T1= (float(T1)/len(record1.seq)) *100
        T2=(record2.seq).count('T')
        T2= (float(T2)/len(record2.seq)) *100
	
	C1=(record1.seq).count('C')
        C1= (float(C1)/len(record1.seq)) *100
        C2=(record2.seq).count('C')
        C2= (float(C2)/len(record2.seq)) *100

	G1=(record1.seq).count('G')
        G1= (float(G1)/len(record1.seq)) *100
        G2=(record2.seq).count('G')
        G2= (float(G2)/len(record2.seq)) *100
	
#	print A1,A2,T1,T2,C1,C2,G1,G2, len(record1.seq)
##### second method- compare frequencies ##########

D_F_12=math.sqrt(math.pow(math.pow((T1-T2), 2) + math.pow((A1-A2), 2) + math.pow((C1-C2), 2) +math.pow((G1-G2), 2) , 2))
D_F_21=math.sqrt(math.pow(math.pow((T2-T1), 2) + math.pow((A2-A1), 2) + math.pow((C2-C1), 2) +math.pow((G2-G1), 2) , 2))
if D_F_12 == D_F_21:
	print "Distance values are valid: " , D_F_12
else:
	print "Distance values are not valid!!! " , D_F_12, "!=" , D_F_21 
