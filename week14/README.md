# QBB 2022 Week14

1. 
I made a bash script to call the kraken converter: ./parse_kraken.sh 
I made a bash script to call the ktImportText: ./kt.sh

The 

2. 
I made a bash script to call the kraken converter: ./map_sort.sh

Q1. 
Most of the gut microbiome is made up of Bacilli and Cutibacterium.  If the sample is in order, it looks like the Enterococcus faecalis makes up ~60% of the microbiota the first day and then becomes 81% of the population the second day.  The rest of the microbiota seems to recover after a few days as the amount of Enteroccocus faecalis returns to ~60% by the eighth day.  The population of Cutibacterium seems to shrink and then grow back to higher than previous levels by the last sample.


Q2.
You could group the contigs based on alignment, size of the bin, size of the contig, and coverage. 


Q3A. 
I got 6 bins.


Q3B. 
All of the bins represent 193/4103 (4.7%) of the assembly.
bin1: 55/4103 - 1.3%
bin2: 13/4103 - 0.3%
bin3: 27/4103 - 0.7%
bin4: 84/4103 - 2.0%
bin5: 8 /4103 - 0.2%
bin6: 6 /4103 - 0.1%
 

'for the total'
grep ">" ~/qbb2022-answers/week14/metagenomics_data/step0_givendata/assembly.fasta | wc -l
> 4103

'for all of the bins'
grep ">" ~/qbb2022-answers/week14/bam_files/bins_dir/*.fa | wc -l
> 193

'for each bin'
(metabat2) [~/qbb2022-answers/week14/bam_files/bins_dir $]grep '>' bin.1.fa | wc -l
      55
(metabat2) [~/qbb2022-answers/week14/bam_files/bins_dir $]grep '>' bin.2.fa | wc -l
      13
(metabat2) [~/qbb2022-answers/week14/bam_files/bins_dir $]grep '>' bin.3.fa | wc -l
      27
(metabat2) [~/qbb2022-answers/week14/bam_files/bins_dir $]grep '>' bin.4.fa | wc -l
      84
(metabat2) [~/qbb2022-answers/week14/bam_files/bins_dir $]grep '>' bin.5.fa | wc -l
       8
(metabat2) [~/qbb2022-answers/week14/bam_files/bins_dir $]grep '>' bin.6.fa | wc -l

Q3C.
There is variability in the sizes of the bins, but prokaryotic genomes are on the scale of Mbp
and the number of bp in each bin is on that scale.
tr -s '\n' '' = to remove new line characters

count the number of bp in the assembly
wc -c assembly.fasta
approx. num bp in assembly: 38856945

to count the number of characters in each bin
wc -c bin.6.fa 

bin		approx. num bp
bin 1:  2752195				
bin 2:  2525551
bin 3:  274280
bin 4:  2356343 
bin 5:  1683938
bin 6:  2910800 


Q3D.
You could estimate how complete each bin is by seeing how much of the sequences in each bin
align with the reference genome of the species.  Sequences from the bin that do not align are conatmination
while how complete the bin is can be determined by figuring out the coverage of the reference genome.

Q4A.
bin 1: NODE_12_length_269228_cov_106.168966 root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus aureus;Staphylococcus aureus subsp. aureus;Staphylococcus aureus subsp. aureus ST72;Staphylococcus aureus subsp. aureus CN1

bin 2: NODE_4_length_455101_cov_112.371015 root;cellular organisms;Bacteria;Terrabacteria group;Actinobacteria;Actinobacteria;Propionibacteriales;Propionibacteriaceae;Cutibacterium;Cutibacterium avidum;Cutibacterium avidum 44067

bin 3: NODE_219_length_36425_cov_40.833462 root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus epidermidis;Staphylococcus epidermidis ATCC 12228
bin 4: NODE_20_length_181746_cov_381.691663 root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus epidermidis;Staphylococcus epidermidis RP62A
bin 5: NODE_3_length_498518_cov_181.760000 root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Tissierellia;Tissierellales;Peptoniphilaceae;Anaerococcus;Anaerococcus prevotii;Anaerococcus prevotii DSM 20548
bin 6: NODE_1_length_1447137_cov_2268.097092 root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Lactobacillales;Enterococcaceae;Enterococcus;Enterococcus faecalis;Enterococcus faecalis OG1RF


Q4B.
You could align the contigs in the bin to reference genomes of varoius species to determine the species for each bin and then look at the number of contigs for each bin to give you a rough estimate of the abudance of the species.  The abudance would also depend on the size of the genome.