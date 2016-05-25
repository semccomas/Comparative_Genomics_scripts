import sys

file1= open(sys.argv[1]).read().splitlines()
file2= open(sys.argv[2]).read().splitlines()

def pairing (file):
	count_end=0
	count_genome=0
	d= {}
	l= []
	for n, line in enumerate(file):	
		count_end= count_end +1
		if '>' in line:
			orf_name= line
			count_genome= count_genome +1
			orf_name= orf_name + ' from line ' + str(count_genome)
			l.append(orf_name)
			d[orf_name]= file1[(n+1):(n+19)]

	#print d[orf_name]
	#print orf_name
	return l

l = pairing (file1)
l2 =pairing (file2)

count_again= 0 
for seq, seq2 in zip(l, l2):
	if seq[-1]== seq2[-1]:
		print 'wahoo'
	count_again= count_again + 1