from Bio import SeqIO
import sys

def getSeqRec(seq_id): 
	fasta = SeqIO.parse(open(proteome_name),'fasta')          #print the fasta version of each file
	for record in fasta:
		if seq_id == record.id:          # access the correct file in each record 
			return record

clusters = sys.argv[1]         # choose proteome_0, proteome_2, and so on
file = open(clusters,'rU').readlines()
for lines in file:
	ref_seqid = lines[11:19]      #find the name of the orf
	info = lines.split()           #find the sequences following it
	with open(ref_seqid,'w') as f:    #write the sequences into the file, named after the orf
		for word in info:
			proteome_name = word[0:10]     #keep the name    
			orfname_targ =  word[11:19]       
			seq_rec = getSeqRec(orfname_targ)
			f.write(">" + seq_rec.id + '\n')    #getting the protein name that belongs to the 'orf' (by using it as a fasta file)
			x = str(seq_rec.seq + '\n')         #getting the sequence that belongs to the 'orf' by using it as a fasta file 
			f.write(x)
