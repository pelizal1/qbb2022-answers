#!/usr/bin/env bash


cd bam_files/bins_dir/
touch taxon_comps.txt
for FILE in *.fa
do
	cd ~/qbb2022-answers/week14/bam_files/bins_dir/
	NODE=$(head $FILE | grep ">")
	NODE=${NODE:1}
	
	cd ~/qbb2022-answers/week14/metagenomics_data/step0_givendata/KRAKEN/
	TAXON=$(grep $NODE assembly.kraken)
	
	cd ~/qbb2022-answers/week14/bam_files/bins_dir
	echo $TAXON >> taxon_comps.txt
done