# QBB 2022 - Week8 Homework

phasing - haplotype, haplotags
not great, more local than global
larger window = switch haplotypes

===1
medaka_variant -i methylation.bam -f hg38.fa -r [chr:start-end] -p -o [output_dir]

-p output phased vcf (switch, not flag)
-r region [chr:start-end]
-i input bam of reads aligned to ref

medaka_variant -i methylation.bam -f hg38.fa -r chr11:1900000-2800000 -p -o chr11_1900000-2800000 -t 4 
medaka_variant -i methylation.bam -f hg38.fa -r chr14:100700000-100880000 -p -o chr14_100700000-100880000 -t 4
medaka_variant -i methylation.bam -f hg38.fa -r chr15:23600000-25900000 -p -o chr15_23600000-25900000 -t 4
medaka_variant -i methylation.bam -f hg38.fa -r chr20:58800000-58912000 -p -o chr20_58800000-58912000 -t 4

####the order matters: -i -f then the other flags

===2
whatshap haplotag -o chr11_1900000-2800000.phased.bam -r ../hg38.fa --output-haplotag-list chr11_1900000-2800000.list.txt --regions chr11:1900000:2800000 round_0_hap_mixed_phased.vcf.gz methylation.bam

whatshap haplotag -o chr14_100700000-100880000.phased.bam -r ../hg38.fa --output-haplotag-list chr14_100700000-100880000.list.txt --regions chr14:100700000:100880000 round_0_hap_mixed_phased.vcf.gz methylation.bam

whatshap haplotag -o chr15_23600000-25900000.phased.bam -r ../hg38.fa --output-haplotag-list chr15_23600000-25900000.list.txt --regions chr15:23600000:25900000 round_0_hap_mixed_phased.vcf.gz methylation.bam

whatshap haplotag -o chr20_58800000-58912000.phased.bam -r ../hg38.fa --output-haplotag-list chr20_58800000-58912000.list.txt --regions chr20:58800000:58912000 round_0_hap_mixed_phased.vcf.gz methylation.bam

===3
whatshap split --output-h1 chr11_1900000-2800000_h1.phased.bam --output-h2 chr11_1900000-2800000_h2.phased.bam chr11_1900000-2800000.phased.bam chr11_1900000-2800000.list.txt

whatshap split --output-h1 chr14_100700000-100880000_h1.phased.bam --output-h2 chr14_100700000-100880000_h2.phased.bam chr14_100700000-100880000.phased.bam chr14_100700000-100880000.list.txt 

whatshap split --output-h1 chr15_23600000-25900000_h1.phased.bam --output-h2 chr15_23600000-25900000_h2.phased.bam chr15_23600000-25900000.phased.bam chr15_23600000-25900000.list.txt

whatshap split --output-h1 chr20_58800000-58912000_h1.phased.bam --output-h2 chr20_58800000-58912000_h2.phased.bam chr15_23600000-25900000.phased.bam chr20_58800000-58912000.list.txt

concatenate haplotype 1
samtools cat -o hap1.bam chr11_1900000-2800000/chr11_1900000-2800000_h1.phased.bam chr14_100700000-100880000/chr14_100700000-100880000_h1.phased.bam chr15_23600000-25900000/chr15_23600000-25900000_h1.phased.bam chr20_58800000-58912000/chr20_58800000-58912000_h1.phased.bam

samtools index hap1.bam

concatenate haplotype 2
samtools cat -o hap2.bam chr11_1900000-2800000/chr11_1900000-2800000_h2.phased.bam chr14_100700000-100880000/chr14_100700000-100880000_h2.phased.bam chr15_23600000-25900000/chr15_23600000-25900000_h2.phased.bam chr20_58800000-58912000/chr20_58800000-58912000_h2.phased.bam

samtools index hap2.bam

===5