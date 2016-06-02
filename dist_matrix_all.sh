for i in genome_?_parsegenom; do
	for j in genome_?_parsegenom; do
	echo $i $j
	python dist_matrix.py $i $j
done
done
