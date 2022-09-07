#!/bin/usr/env python

import numpy as np
from bed_parser import *

# call parser
parsed_bed = parse_bed("hg38_gencodev41_chr21.bed")


num_exons = []
# go through the parsed bed file
for line in parsed_bed:
    # <BED9 is 1 exon
    fieldN = len(line)
    if fieldN < 9:
        num_exons.append(int(1))
    # >BED12 then need to find number of exons
    else:
        num_exons.append(int(line[9]))
   
median_num_exons = int(np.median(num_exons))
print(f"The median number of exons is {median_num_exons}.")