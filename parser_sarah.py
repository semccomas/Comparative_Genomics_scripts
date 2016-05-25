result_handle = open("Blast_XML_q.output")    #open whatever XML output available
from Bio.Blast import NCBIXML
blast_records = NCBIXML.read(result_handle)     #command Biopython to read the outputs
for alignment in blast_records.alignments:       #access the alignments from the records
       	print '>' , alignment.title                 #writing in FASTA format 
	print alignment.hsps[0].sbjct             #accessing the first HSP of each hit

