#!/usr/bin/env bash

for FILE in metagenomics_data/step0_givendata/READS/*.fastq
do 
	FILENAME=${FILE:40:11}.bam
	echo $FILENAME
	bwa mem  -t 4 metagenomics_data/step0_givendata/assembly.fasta $FILE | samtools sort -o bam_files/$FILENAME
done