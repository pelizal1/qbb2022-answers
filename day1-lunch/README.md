# QBB2022 - Day 1 - Lunch Exercises Submission

1. I'm excited to learn Textmate.

2. 
b. 	The mean number of exons per gene is 62.34.
	wc -l genes.chr21.bed #find no. of genes
	wc -l exons.chr21.bed #find no. of exons
	no. exons / no. genes = exons/gene

c.	We would have to find the number of exons for each gene, sort the genes by number of exons, and then find the median by subtracting to find the central term.

3. 
b.
305 chr21	13979679	13980279	1
 678 chr21	14086279	14087079	2
  79 chr21	14520479	14521079	3
 377 chr21	14373279	14378479	4
 808 chr21	10340056	10342056	5
 148 chr21	14487679	14488279	6
1050 chr21	13980279	13980679	7
 156 chr21	10330656	10331656	8
 654 chr21	10118172	10126172	9
  17 chr21	15729281	15729481	10
  17 chr21	14216679	14216879	11
  30 chr21	31559887	31560087	12
  62 chr21	17514282	17514482	13
 228 chr21	14215479	14215679	14
 992 chr21	10003860	10005054	15
 
 sort -k 4 -g chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | uniq -f 3 -c #sort numerically by the field4 then count unique occurences of field4
 
 c.	We would have to find the number of nucleotides that are in each state and divide by the total number of nucleotides.  We can find the number of nucleotides based on the start and end positions for each instance of each state.  The state with the largest proportion of nucleotides would comprise the largest fraction of the genome.
 
4. 
b.
  123 ACB
  112 ASW
  173 ESN
  180 GWD
  122 LWK
  128 MSL
  206 YRI
  
  grep AFR integrated_call_samples.panel | sort -k 2 | cut -f 2 | uniq -c
  
c. Sort by the superpop then by the pop. Cut out fields 2 and 3. Then find the unique instances of each superpop, pop combination.

5.
b.
cut -f1-9,13 random_snippet.vcf > HG00100.vcf #cut the info from the first 9 field plus HG00100

c.
0|0 has 9514 values
grep '0|0' HG00100.vcf | wc -l

0|1 has 127 values
grep '0|1' HG00100.vcf | wc -l

1|1 has 181 values
grep '1|1' HG00100.vcf | wc -l

d. 34 rows contain AF=1
grep '1|1' HG00100.vcf | wc -l

e. AF=1 can appear 6 times per row.

f. Cut field 8 and then cut field 7 which is semicolon delimited.


 