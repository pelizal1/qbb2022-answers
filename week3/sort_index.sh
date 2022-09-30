# sort and index the sam files

for FILE in *.sam
do 
	FILENAME=${FILE:0:6}
	samtools sort -@ 4 -O bam -o $FILENAME.bam $FILENAME.sam
	samtools index $FILENAME.bam
done
