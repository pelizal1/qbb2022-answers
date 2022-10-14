#!/bin/bash


for FILE in *.bam 
do
	FILENAME=${FILE%.*}
	samtools view -h -q 10 $FILENAME.bam > $FILENAME.qual.bam
done