from Bio.Blast import NCBIXML
import sys as s

script_name = s.argv[0]   
result_handle = s.argv[1]    #xml file
reference_genome = s.argv[2]    #genome 5
target_genome = s.argv[3]   #genome 0, 2, 4, 8, 9, a, b 


#parse the XML files

blast_records = NCBIXML.parse(open(result_handle,'rU'))
blast_record = next(blast_records)

#function that returns the first blast hit of each gene of the target proteome

def get_id_query(blast_record):
        x=[]
        for alignment in blast_record.alignments:
                x.append(alignment.title[4:13])
        return x[0]

#loop over the genes of the reference genome and print the corresponding ids of the target proteome

for blast_record in blast_records:
    print reference_genome, blast_record.query, target_genome, get_id_query(blast_record)