import sys
f=open(sys.argv[1]).read().splitlines()


zeros=[ ]
not_zero=[ ]
signal_pep= [ ]
SP_TM = [ ]
length_of_file= 0


for line in f:

	if "orf" in line:    #skip the first line of the file
		length_of_file=length_of_file +1    #this will make it so you can have fractions later on
		line=line.split()        #access each value
		TF_num=line[1]     #get each individual number for line"TF"
		SP_num= line[2]

		if float(TF_num) == 0:
			zeros.append(float(TF_num))
		
		if float(TF_num)!= 0:
			not_zero.append(float(TF_num))     #these have to be floats to be able to divide things
		
		if SP_num == 'Y':                      #in short version it shows Y or 0 so you want Y to show it is a signal peptide
			signal_pep.append(SP_num)

		if SP_num == 'Y' and float(TF_num) != 0:
			SP_TM.append(TF_num)



print float(len(zeros))/length_of_file, "= percent of not transmembrane"
print float(len(not_zero))/length_of_file, "= percent of transmembrane"
print sum(not_zero)/len(not_zero), "= average number of transmembrane"
print float(len(signal_pep))/length_of_file, "= percent of signal peptides"
print float(len(SP_TM))/length_of_file, "= percent of signal peptide and transmembrane" 
