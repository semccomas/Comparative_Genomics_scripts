
###############RUNNING PHOBIUS ######################

for i in /scratch/Comparative-Genomics-2016/Group1/Practical_7/proteomes_pract_7/proteome_?; do
	base=`basename $i`
	echo $base
#	phobius -short $i  >> phobius_sarah_$base
done

############RUNNING PARSER FILE ###########
for o in /scratch/Comparative-Genomics-2016/Group1/Practical_7/Phobius/phobius_sarah_proteome_?; do
	base_o=`basename $o`
	echo $base_o
	python get_TF_nums.py $base_o
done
