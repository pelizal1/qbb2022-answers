# QBB2022 - Day 1 - Homework Exercises Submission

#Exercise 1
b. You get an error message about an illegal field because of the nuc variable.
Corrected script:
for nuc in A C G T
do
  echo "Considering " $nuc
  awk '/^#/{next} {if ($4 == nuc) {print $5}}' nuc="$nuc" $1 | sort | uniq -c
done

c.
Considering  A
 354 C
1315 G
 358 T
Considering  C
 484 A
 384 G
2113 T
Considering  G
2041 A
 405 C
 485 T
Considering  T
 358 A
1317 C
 386 G
 
d. It makes sense because the A and G as well as C and T switch more often because A and G are purines and C and T are pyrimidines.

#Exercise 2
Find all state1 and print rows to a separate bed file
awk '{if ($4 == 1) {print}}' ~/data/bed_files/chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed> st1.bed

find the intersection with the SNPs and send to intersect.vcf
bedtools intersect -a ~/data/vcf_files/random_snippet.vcf -b st1.bed > intersect.vcf

Find all with cytosine in reference, print alternate, and find occurances of each nucleotide
awk '{if ($4 == "C") {print $5}}' intersect.vcf | sort | uniq -c

The most common alternate allele for a cytosine reference is thymine.  It makes because both cytosine and thymine are pyrimadines.

#Exercise 3
awk '/^#/{next} {print $1,$2-1, $2}' $1 > variants.bed #skip the comment lines make a bed file
sort -k1,1 -k2,2n ~/data/bed_files/genes.bed > genes.sorted.bed #sort the bed file by position
bedtools closest -a variants.bed -b genes.sorted.bed #find the variants closest to the bed file

Error: unable to open file or unable to determine types for file variants.bed

- Please ensure that your file is TAB delimited (e.g., cat -t FILE).
- Also ensure that your file has integer chromosome coordinates in the 
  expected columns (e.g., cols 2 and 3 for BED).
  
Error: Sorted input specified, but the file variants.bed has the following out of order record
chr21	5218156	5218157

The variants.bed file has to be sorted as well.

Corrected:
awk '/^#/{next} {print $1 "\t" $2-1 "\t" $2}' $1 > variants.bed
sort -k1,1 -k2,2n variants.bed > variants.sorted.bed
sort -k1,1 -k2,2n ~/data/bed_files/genes.bed > genes.sorted.bed
bedtools closest -a variants.sorted.bed -b genes.sorted.bed > closest.bed


Count the number of variants: 10293
wc -l closest.bed

Count the number of genes: 200
sort -k7 closest.bed |  uniq -f5 -c | wc -l

There are 51.5 variants per gene.
