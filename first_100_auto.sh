INPUT_DIR=/scratch/Comparative-Genomics-2016/Group1/Practical_7/proteomes_hmm

for i in $INPUT_DIR/proteome_?; do
	base=`basename $i`
	python first_100.py $i first_100_$base
	echo $base
done
