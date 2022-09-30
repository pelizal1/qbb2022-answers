# QBB 2022 Week 3 homework

===1
bwa index sacCer3.fa

===2
./align.sh

===3
./sort_index.sh

===4
freebayes -f sacCer3.fa -p 1 --genotype-qualities -L bam_list.txt > A01.vcf
-L flag adds bam list	

===5
vcffilter -f "QUAL > 20" A01.vcf > A01_filter.vcf

===6
-k flag = keep allele-level annotations
-g flag = keep genotype-level annotations
vcfallelicprimitives -k -g A01_filter.vcf > A01_filter_decomp.vcf

===7
snpeff ann R64-1-1.99 A01_filter_decomp.vcf > A01_filter_decomp_snpeff.vcf

===8
Do I need to set the number of bins for the read depth distribution?

./week3hw.py A01_filter_decomp_snpeff.vcf > key_predicted_effect.txt
I saved the keys for the Predicted Effect graph as a txt file because of formating issues.

grep "#" A01_filter_decomp_snpeff.vcf | wc -l
65 header lines

head -n 1065 > A01_1000.vcf
1065 to include header lines and 1000 snps