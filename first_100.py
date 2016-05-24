import sys

prot_file= open(sys.argv[1]).read().splitlines()

count=0
for line in prot_file:
#	print line
	if '>' in line:
		#fasta= line
		count= count + 1
	if count <= 100:
		print line
