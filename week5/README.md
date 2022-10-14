# QBB2022 - Week 5 Homework

==Part 1
===1 
see week5.sh

===2 
macs2 callpeak -t D2_Sox2_R1.qual.bam -c D2_Sox2_R1_input.qual.bam -g 94987271 --outdir macs2_R1 -n D2_SOX2_R1 -B
macs2 callpeak -t D2_Sox2_R2.qual.bam -c D2_Sox2_R2_input.qual.bam -g 94987271 --outdir macs2_R2 -n D2_SOX2_R2 -B

===3
bedtools intersect -a macs2_R1/D2_SOX2_R1_peaks.narrowPeak -b macs2_R2/D2_SOX2_R2_peaks.narrowPeak -wa > sox2_intersect_peaks.bed

===4 
wc -l D2_Klf4_peaks.bed
There are Klf4 60 peaks on chromosome 17.

wc -l sox2_intersect_peaks.bed
There are 593 Sox2 peaks on chromosome 17.

bedtools intersect -a sox2_intersect_peaks.bed -b D2_Klf4_peaks.bed > sox2_klf2_intersect_peaks.bed
wc -l sox2_klf2_intersect_peaks.bed
There is an overlap of 39 peaks on chromosome 17 between Sox2 and Klf4.

41/60 or 68% of the Klf4 peaks colocalize with Sox2.

===5
python scale_bdg.py macs2_R1/D2_SOX2_R1_treat_pileup.bdg D2_SOX2_treat.bdg

awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' D2_SOX2_treat.bdg > D2_SOX2_treat_scaled_cropped.bdg

==Part 2
sort -k 5 -r -n sox2_intersect_peaks.bed | head -n 300 | awk '{ printf "%s:%i-%i\n", $1, $2, $3 }' > sox2_300.bed

samtools faidx mm10.fa -r sox2_300.bed > sox2_300.fa

meme-chip -maxw 7 sox2_300.fa

tomtom memechip_out/combined.meme ~/Downloads/motif_databases/MOUSE/HOCOMOCOv11_full_MOUSE_mono_meme_format.meme

grep "KLF4_" tomtom_out/tomtom.tsv > KlF4_peaks.txt
grep "SOX2_" tomtom_out/tomtom.tsv > SOX2_peaks.txt

