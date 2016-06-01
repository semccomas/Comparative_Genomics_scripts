from Bio import SeqIO
import sys


record = SeqIO.read(open(sys.argv[1],'rU'),'fasta')

table = 11
min_pro_len = 100
orf_count = 0

for strand, nuc in [(+1, record.seq), (-1, record.seq.reverse_complement())]:
     for frame in range(3):
         length = 3 * ((len(record)-frame) // 3) #Multiple of three
         for pro in nuc[frame:frame+length].translate(table).split("*"):
             if len(pro) >= min_pro_len:
		 orf_count = orf_count + 1                 		
		 print '>orf' + str(orf_count) + '\n' + str(pro)
		 
 
