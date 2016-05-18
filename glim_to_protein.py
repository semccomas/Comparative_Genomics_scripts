#glim2_to_prot.py

import sys
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

fasta_file= sys.argv[1]       #I used sys so that each time I could specify which genome and glimmer output I want to compare
glimmer_file= sys.argv[2]

def DNA_to_protein (seq):
        seq=Seq(str(seq), IUPAC.ambiguous_dna)   #convert the sequence into the proper format to read by Biopython. Ambiguous_dna because some genomes have 'N'
        print seq.translate(table="Bacterial")

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


data= parse(fasta_file, glimmer_file)    #using the parse function to have the FASTA file and the GLIMMER file outputs together
for frame in data[1]:              #reading the Glimmer output line by line to process one start and one stop codon at a time
        start= frame[1]-1
        stop = frame[2]-1    #to stop the star from being at the end- it doesn't affect protein sequence at all (i.e. the last letter is still printed)
        seq= data[0][2][start:stop]
        DNA_to_protein(seq)        #call the function of translating to protein


       