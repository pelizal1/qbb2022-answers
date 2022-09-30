# aligning reads to reference

for FILE in *.fastq
do 
	FILENAME=${FILE:0:6}
	bwa mem -t 4 -R "@RG\tID:$FILENAME\tSM:$FILENAME" -o $FILENAME.sam sacCer3.fa $FILE &
done