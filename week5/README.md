# QBB2022 - Week 5 Homework

==Part 1
===2 
macs2 callpeak -t D2_Sox2_R1.qual.bam -c D2_Sox2_R1_input.qual.bam --outdir macs2_R1 -n D2_SOX2_R1 -B
macs2 callpeak -t D2_Sox2_R2.qual.bam -c D2_Sox2_R2_input.qual.bam --outdir macs2_R2 -n D2_SOX2_R2 -B

===3
bedtools intersect -a macs2_R1/D2_SOX2_R1_peaks.narrowPeak -b macs2_R2/D2_SOX2_R2_peaks.narrowPeak > sox2_intersect_peaks.bed

# redo with -wa to retain the full peaks
===4 
wc -l D2_Klf4_peaks.bed
There are Klf4 60 peaks on chromosome 17.

wc -l sox2_intersect_peaks.bed
There are 652 Sox2 peaks on chromosome 17.

bedtools intersect -a sox2_intersect_peaks.bed -b D2_Klf4_peaks.bed > sox2_klf2_intersect_peaks.bed
wc -l sox2_klf2_intersect_peaks.bed
There is an overlap of 39 peaks on chromosome 17 between Sox2 and Klf4.

39/60 or 65% of the Klf4 peaks colocalize with Sox2.

===5
python scale_bdg.py macs2_R1/D2_SOX2_R1_treat_pileup.bdg D2_SOX2_treat.bdg

awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' D2_SOX2_treat.bdg > D2_SOX2_treat_scaled_cropped.bdg

==Part 2
sort -k 5 -r -n macs2_R1/D2_SOX2_R1_peaks.narrowPeak | head -n 300 | awk '{ printf "%s:%i-%i\n", $1, $2, $3 }' > sox2_R1_300.bed

samtools faidx -r sox2_R1_300.bed mm10.fa > sox2_R1_300.fa

