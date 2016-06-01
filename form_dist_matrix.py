import numpy as np
import sys as s
f= open(s.argv[1]).read().splitlines()		# this is the dist_matrix_all file. 
matrix= [ ]
for n, line in enumerate(f):
	numbers = line.split()
	if n % 2 == 1:				# odd numbered lines only
		numbers = numbers [4]		# add the numbers from the output file only
		matrix.append(float(numbers))   # otherwise it's a string
		array= np.asarray(matrix)	# add all the values to the array and then shape the array to how we want it (12 x 12) afterwards
array.shape= (12,12)
print array

