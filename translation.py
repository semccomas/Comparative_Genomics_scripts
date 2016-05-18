from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

#function for translating the sequence from glimmer parsing

def translatedna(orfseq):
	coding_dna = Seq(orfseq, generic_dna)
	return coding_dna.translate()

#function that retrieves the string between start and stop position

def orfs(data):
	for row in data[1]:
		start = row[1]-1
		stop = row[2]-1
		print '>'+row[0]
		if int(stop) < int(start):
			dna = data[0][2][start:stop:-1]
			my_dna = Seq(dna,generic_dna)
			orfseq = my_dna.complement()
			aa = translatedna(str(orfseq))
			print aa
		else:
			orfseq = data[0][2][start:stop]
			aa = translatedna(orfseq)	
			print aa
		
#function for parsing glimmer output and combining it with a fasta file

def parse(fasta,glimmer):

    SEQUENCE_FILE = open(fasta).read()
    header,sequence=SEQUENCE_FILE.split('\n',1)
    sequence=sequence.strip()
    sequence=sequence.replace('\n','')
    seqData=[fasta,header,sequence]

    GLIMMER_FILE = open(glimmer,"r")
    header = GLIMMER_FILE.readline()
    genes=[]
    for line in GLIMMER_FILE:
        line=line.strip()
        items=line.split()
        genes.append([items[0],int(items[1]),int(items[2]),int(items[3].strip("+"))])
    return [seqData,genes]

data = parse('genome_b','/scratch/mateuszk/Comparative-Genomics-2016/Group1/GLIMMER/genome_b.output.predict')
orfs(data)
