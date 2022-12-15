#!/usr/bin/env bash

for FILE in ./metagenomics_data/step0_givendata/KRAKEN/*_krona.txt
do 
	FILENAME=${FILE:43:45}".html"
	echo $FILENAME
	ktImportText -q $FILE -o $FILENAME
done