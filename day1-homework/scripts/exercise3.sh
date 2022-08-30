#!/bin/bash

#USAGE: bash exercise3.sh input_VCF

awk '/^#/{next} {print $1 "\t" $2-1 "\t" $2}' $1 > variants.bed
sort -k1,1 -k2,2n variants.bed > variants.sorted.bed
sort -k1,1 -k2,2n ~/data/bed_files/genes.bed > genes.sorted.bed
bedtools closest -a variants.sorted.bed -b genes.sorted.bed > closest.bed

