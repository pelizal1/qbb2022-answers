#!/usr/bin/env bash

for FILE in ./metagenomics_data/step0_givendata/KRAKEN/*.kraken
do 
	FILENAME=${FILE:-15:-7}
	echo $FILENAME
	python kraken_parse.py $FILE $FILENAME
done