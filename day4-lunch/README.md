# QBB2022 - Day 4 Lunch Exercises!)
##Exercise 1
###1
*** Creating .bed files for features of interest
--- Creating protein_coding.chr21.bed
--- Creating processed_pseudogene.chr21.bed
--- Creating exons.chr21.bed
*** Subsetting .vcf for each feature
--- Subsetting exons.chr21.bed.vcf
    + Covering 1107407 bp
--- Subsetting processed_pseudogene.chr21.bed.vcf
    + Covering 956640 bp
--- Subsetting protein_coding.chr21.bed.vcf
    + Covering 13780687 bp
###2
One strategy is to look at the plots in the cache and compare them to the ones that we created.  Another strategy is to code it to see if the two are equal. 
###3
miRNA is interesting because they are involved in regulating gene expression.
lncRNA are also involved in gene regulation.
protein_coding is interesting because these are the parts of the genome that code for proteins.

##Exercise 3: Create documentation
SYNOPSIS
    bxlab/cmdb-plot-vcfs used to plot genotype, allele frequencies for different features of the genome.

USAGE
    bash do_all.sh <FILE.vcf> <FILE.gtf>

DEPENDENCIES
conda version  : 4.13.0
python version : 3.9.7.final.0
bedtools       : 2.30.0 
matplotlib     : 3.5.1
numpy          : 1.22.3


DESCRIPTION
    1. Create .bed files for features of interest
        - Run subset_regions.sh Bash script
		
	2. Subset .vcf for each feature
	
	
	3. Plot AC for each .vcf
		- Run plot_vcf_ac.py Python script
	
OUTPUT
	*** Creating .bed files for features of interest
	--- Creating protein_coding.chr21.bed
	--- Creating processed_pseudogene.chr21.bed
	--- Creating lncRNA.chr21.bed
	--- Creating exons.chr21.bed
	*** Subsetting .vcf for each feature
	--- Subsetting exons.chr21.bed.vcf
	    + Covering 1107407 bp
	--- Subsetting lncRNA.chr21.bed.vcf
	    + Covering 8663528 bp
	--- Subsetting processed_pseudogene.chr21.bed.vcf
	    + Covering 956640 bp
	--- Subsetting protein_coding.chr21.bed.vcf
	    + Covering 13780687 bp
	*** Plotting AC for each .vcf
	--- Plotting AC for exons.chr21.bed.vcf
	--- Plotting AC for lncRNA.chr21.bed.vcf
	--- Plotting AC for processed_pseudogene.chr21.bed.vcf
	--- Plotting AC for protein_coding.chr21.bed.vcf
	--- Plotting AC for random_snippet.vcf
	