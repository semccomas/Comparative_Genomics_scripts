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




