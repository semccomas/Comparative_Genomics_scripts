import sys
f=open(sys.argv[1]).read().splitlines()

count_end= 0    #stop the file from indexing too far at the end

for line in f:
        count_end= count_end+ 1           #this number will then mark the end of the file

for n, line in enumerate(f): 
        orf= line.split()          
        orf=orf[1]                   #being able to just access the number for the protein
        if n+1 != count_end:             #if you are not at the end of the script, stops the index from going out of range
                if orf in f[n+1]:             #does the protein exist in the next line as well?
                        f[n]= line.rstrip()           #if so, keep it in the same line
                else:
                        f[n]=  line.rstrip() + '\n'    #if not, write a new line
print ' '.join(f)




##This file will take a bunch of sequences and if there are the same sequences on the next line (in the second column), it will print the sequences on the same line