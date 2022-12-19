#!/usr/bin/env bash

cd bam_files/bins_dir/
for FILE in *.fa
do
	cd ~/qbb2022-answers/week14/bam_files/bins_dir/
	FILENAME=${FILE:0:5}'_taxon_comp.txt'
	for ND in $(grep ">" $FILE | cut -f2 -d ">")
	do
		cd ~/qbb2022-answers/week14/metagenomics_data/step0_givendata/KRAKEN/
		TAXON=$(grep $ND assembly.kraken | cut -d ';' -f7)
		cd ~/qbb2022-answers/week14/bam_files/bins_dir/
		echo $TAXON >> $FILENAME
	done
done

cd ~/qbb2022-answers/week14/bam_files/bins_dir/
for FL in *.txt
do
	LINES=$(wc -l $FL)
	printf '\n' >> $FL
	echo $(sort $FL | uniq -c) >> $FL
done





