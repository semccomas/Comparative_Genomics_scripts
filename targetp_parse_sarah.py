import sys

filename= open(sys.argv[1]).read().splitlines()

mito= [ ]
signal= [ ]
count=0

for line in filename:
	if "genome" in line:
		count= count+1
		line= line.split()
		if sys.argv[1]== 'targetp_proteome_1':     #some of the files have different locations, this is just to check that
			location= line[5]
		if sys.argv[1] == 'targetp_proteome_3_NEW':
			location= line[6]
			if location == 'M':
				mito.append(location)      #find the number of mitochondrial genes
print len(mito), ' = Number of predicted mitochondrial genes'
print count, ' = Number of total genes' 
print float(len(mito))/count , ' = Fraction of predicted mitochondrial genes ' 



