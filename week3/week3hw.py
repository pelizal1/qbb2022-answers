#!/usr/bin/env python
# USAGE: ./week3hw.py <file.vcf>

import sys
import matplotlib.pyplot as plt
import numpy as np

vcf = sys.argv[1]
fs = open(vcf)


rd = []
gq = []
af = []
pe = []
float_err = 0
for i, line in enumerate(fs):
    # skip the header
    if "#" in line:
        continue
    fields = line.split()
    # estimated allele freq
    info = fields[7].split(";")
    af_f = info[3]
    allele_freq = af_f.split("=")
    try:
        af.append(float(allele_freq[1]))
    except:
        float_err += 1
    # predicted effects
    snpeff = info[-1]
    if "ANN" in snpeff:
        pred_eff = snpeff.split("|")
        pe.append(pred_eff[1])
    # looping through samples
    for j in range(9, len(fields)):
        sample = fields[j].split(":")
        # read depth
        read_depth = sample[2]
        # genotype quality
        gen_qual = sample[1]
        if read_depth == ".":
            continue
        elif gen_qual == ".":
            continue
        # add read depth and genotype quality to lists
        rd.append(int(read_depth))
        gq.append(float(gen_qual))

# make arrrays and determine number of bins
coverages = np.array(rd)
qualities = np.array(gq)
al_freq = np.array(af)
max_cov = np.amax(coverages)
max_qual = np.amax(qualities)
max_al_freq = np.amax(al_freq)

# plot read depth distribution
fig, ax = plt.subplots(2,2)
ax[0,0].hist(coverages)
ax[0,0].set_xlabel("Read Depth")
ax[0,0].set_ylabel("Read Depth Freq.")
ax[0,0].set_yscale('log')
ax[0,0].set_title("Read Depth Distribution")

# plot genotype qualitites
ax[0,1].hist(qualities)
ax[0,1].set_xlabel("Phred Score")
ax[0,1].set_ylabel("Phred Score Freq.")
ax[0,1].set_yscale('log')
ax[0,1].set_title("Genotype Qualities Distribution")

# plot allele frequencies spectrum
ax[1,0].hist(al_freq)
ax[1,0].set_xlabel("Allele Freq.")
ax[1,0].set_ylabel("Freq. of Allele Freq.")
ax[1,0].set_yscale('log')
ax[1,0].set_title("Allele Freq. Spectrum")

# finding unique effects and the counts for each
values, counts = np.unique(pe, return_counts=True)
values_num = []
for o, v in enumerate(values):
    values_num.append(o)
# plot predicted effects
ax[1,1].bar(values_num, counts)
ax[1,1].set_xlabel("Predicted Effects")
ax[1,1].set_ylabel("Predicted Effects Freq.")
ax[1,1].set_yscale('log')
ax[1,1].minorticks_on()
ax[1,1].tick_params(axis='x', labelrotation = 30)
ax[1,1].set_title("Summary of Predicted Effects")

print(f"Conversion to float errors:{float_err}", file=sys.stderr)

plt.tight_layout()
plt.savefig("week3hw.png")

# print key for predicted effects
print("Key \t Predicted Effect")
for i, eff in enumerate(values):
    print(f"{i} \t {eff}")

fs.close()