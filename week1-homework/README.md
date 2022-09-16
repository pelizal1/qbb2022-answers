# QBB 2022 - Week 1
##Question 1
###1.1
One would need 5*10^6 / 100 or 5*10^4 reads to sequence a 1Mbp genome to 5x coverage 
and 15*10^6 / 100 or 15*10^4 reads to to sequence a 1Mbp genome with 100bp reads.
###1.3
There are 6934 base pairs that have not been sequenced. The expected 
frequency count is about 6738 base pairs.  The simulation is pretty close
to the Poisson expectations.
###1.4 
There are 2 base pairs that have not been sequenced.  The expected
frequency count is abou 0.3 base pairs.  The simulation is pretty close to
the Poisson expectations

##Question 2
###2.1
/Users/cmdb/SPAdes-3.15.5-Darwin/bin/spades.py --pe1-1 frag180.1.fq / 
--pe1-2 frag180.2.fq --mp1-1 jump2k.1.fq --mp1-2 jump2k.2.fq -o asm -t 4 -k 31
There were four contigs produced.
###2.2
samtools faidx contigs.fasta > contigs.fasta.fai

NODE_1_length_105830_cov_20.649193      105830  36      60      61
NODE_2_length_47860_cov_20.367392       47860   107665  60      61
NODE_3_length_41351_cov_20.528098       41351   156358  60      61
NODE_4_length_39426_cov_20.336388       39426   198434  60      61

The total length of the contigs is 234467 bp.
###2.3
The largest contig is 105830 bp.
###2.4 
The contig N50 size would be 47860 bp.

##Question 3
###3.1
dnadiff ref.fa asm/contigs.fa
less -S out.report

The average identity is 99.9955.
###3.2
nucmer ref.fa asm/contigs.fasta
show-coords out.delta

The longest alignment is 105830 bp.
###3.3
There are 5 insertions in the reference and one in the query sequence.

##Question 4
###4.1
show-coords out.mdelta


