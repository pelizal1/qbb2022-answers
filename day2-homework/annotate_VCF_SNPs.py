#!/usr/bin/env python

#import everything from vcfParser - don't need .py because python looks for .py
from vcfParser import *

randSnip = parse_vcf("random_snippet.vcf")
fs = open("dbSNP_snippet.vcf", "r")
# initialize variables
snp_dict = {}
fields = []
# read lines in dbSNP file
for line in fs:
    # skip the header
    if line.startswith("#"):
        continue
    # add SNP to position to the snp dictionary
    else:
        # store in the line in a list separated by spaces
        fields = line.strip().split("\t")
        position = int(fields[1])
        value = fields[2]
        # add position, value to the SNP dictionary
        snp_dict[position] = value

# initialize list to store file and counter
# for records without annotation
snippet_ids = []
num_recs_no_annot = 0
# there is stuff in the dictionary
# annotate random_snippet with the dbSNP
# index and line for each line in randSnip
# searching the dictionary and finding the keys works.
for i,line in enumerate(randSnip):
    if i == 0:
        continue
    else:
        key = line[1]
        try:
            ident = snp_dict[key]
            line[2] = ident
            snippet_ids.append(line)
        except:
            num_recs_no_annot += 1

print(f"There are {num_recs_no_annot} records without a corresponding ID in dbSNP.", file=sys.stderr)

count = 0

with open("random_snippet_annotated.vcf", "w") as f:
    for line in snippet_ids:
        for cell in line:
            f.write(str(cell))
            f.write('\t')
        count += 1
        f.write('\n')
f.close()

        

