from Bio import SeqIO
import sys
from Bio.SeqUtils import GC
genome = sys.argv[1]
x = open(genome,"rU")
for record in SeqIO.parse(x,"fasta"):
	leng = len(record.seq)
	AG_count = float(record.seq.count('AG'))
	GC_count = float(record.seq.count('GC'))
	CC_count = float(record.seq.count('CC'))
	CA_count = float(record.seq.count('CA'))
	AA_count = float(record.seq.count('AA'))
	GA_count = float(record.seq.count('GA'))
	AC_count = float(record.seq.count('AC'))
	AT_count = float(record.seq.count('AT'))
	TA_count = float(record.seq.count('TA'))
	GT_count = float(record.seq.count('GT'))
	TG_count = float(record.seq.count('TG'))
	CT_count = float(record.seq.count('CT'))
        TC_count = float(record.seq.count('TC'))
        TT_count = float(record.seq.count('TT'))
        GG_count = float(record.seq.count('GG'))

print record.id, "GC content", GC(record.seq), "%"
print 'AG', AG_count/float(leng)*100, '%'
print 'GC', GC_count/float(leng)*100, '%'
print 'CC', CC_count/float(leng)*100, '%'
print 'CA', CA_count/float(leng)*100, '%'
print 'AA', AA_count/float(leng)*100, '%'
print 'GA', GA_count/float(leng)*100, '%'
print 'AC', AC_count/float(leng)*100, '%'
print 'AT', AT_count/float(leng)*100, '%'
print 'TA', TA_count/float(leng)*100, '%'
print 'GT', GT_count/float(leng)*100, '%'
print 'TG', TG_count/float(leng)*100, '%'
print 'CT', CT_count/float(leng)*100, '%'
print 'TC', TC_count/float(leng)*100, '%'
print 'TT', TT_count/float(leng)*100, '%'
print 'GG', GG_count/float(leng)*100, '%'



x.close()

import sys

f= open(sys.argv[2]).read() 		#use proteome file

seq= 'ARNDCEQGILKMFPSTWYV' 		#all protein characters

count=0
for line in f: 				#need to be able to count the amino acids in the file
	if line in seq:			#look in seq because you don't want to include the header (>orf0001)
		count= count +1
#print count
def counter (char, char2):
        out= f.count(char+char2)	#count the occurence of the first char and second char, (ex AA, AP, PN, PA)
	freq= (float(out)/count) * 100
        print char,char2, 'frequency: ' , freq, '%'


for char in seq:			#looping through the sequence the first time will get ARNDCE... but as you move from A to R to N to D, you will go through a second loop, going through ARNDCE again before moving on
	for char2 in seq:
		counter(char,char2) 	#easier to find the count when you have a function for it for whatever reason
