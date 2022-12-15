#!/usr/bin/env bash
# run metabat2 for all bam files

cd bam_files
# touch list_bam.txt
#
# for FILE in *.bam
# do
# 	echo $FILE >> list_bam.txt
# done

jgi_summarize_bam_contig_depths --outputDepth depth.txt SRR492183_1.bam SRR492183_2.bam SRR492186_1.bam SRR492186_2.bam SRR492188_1.bam SRR492188_2.bam SRR492189_1.bam SRR492189_2.bam SRR492190_1.bam SRR492190_2.bam SRR492193_1.bam SRR492193_2.bam SRR492194_1.bam SRR492194_2.bam SRR492197_1.bam SRR492197_2.bam
metabat2 -i ../metagenomics_data/step0_givendata/assembly.fasta -a depth.txt -o bins_dir/bin

