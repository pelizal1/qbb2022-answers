#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt

vcf = sys.argv[1]
fs = open( vcf )

ac = []
for i, line in enumerate( fs ):
    # skip the header
    if "#" in line:
        continue
    fields = line.split()
    info = fields[7].split(";")
    # adding AC - Total number of alternate alleles in called genotypes
    ac.append( int(info[0].replace("AC=","")) )

fig, ax = plt.subplots()
ax.hist( ac, density=True )
ax.set_xlabel("AC")
ax.set_ylabel("AC Freq.")
plt.yscale('log')
plt.title(vcf)
plt.tight_layout()
fig.savefig( vcf + ".png" )

fs.close()

