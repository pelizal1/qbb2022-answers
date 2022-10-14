#!/usr/bin/env python

# import libraries
import pandas as pd
from scipy.stats import uniform
from scipy.stats import randint
import numpy as np
import matplotlib.pyplot as plt



plink = np.genfromtxt("plink.eigenvec",
                        dtype = None,
                        encoding = None,
                        names = ["ID", "ID", "first_pc", "second_pc", "third_pc",
                                    "fourth_pc", "fifth_pc", "sixth_pc", "seventh_pc", 
                                "eigth_pc", "ninth_pc", "tenth_pc"])

# plot first_pc and second_pc
# fig, ax = plt.subplots()
# ax.scatter(plink["first_pc"], plink["second_pc"])
# ax.set_xlabel("first_pc")
# ax.set_ylabel("second_pc")
# ax.set_title("Genetic Relatedness of Cell Lines")
# plt.savefig("ex1.png")
# plt.close(fig)

# allele frequency
af_file = np.genfromtxt("plink_no1.frq",
                        dtype = None,
                        encoding = None,
                        names = ["CHR", "SNP", "A1", "A2", "MAF", "NCHROBS"])
                        
# # plot first_pc and second_pc
# fig, ax = plt.subplots()
# ax.hist(af_file["MAF"])
# ax.set_xlabel("Allele Freq.")
# ax.set_ylabel("Freq of Allele Freq")
# ax.set_title("Spectrum of Allele Freq.")
# plt.tight_layout()
# plt.savefig("ex3.png")
# plt.close(fig)


# read in CB1908_IC50 phenotype data
df_CB = np.genfromtxt("CB1908_IC50/phenotype_gwas_CB1908_IC50.assoc.linear",
                        dtype = None,
                        encoding = None,
                        names = True)

CB_minuslog10pvalue = -np.log10(df_CB['P'])

# print(np.shape(df_CB))
# print(np.shape(CB_minuslog10pvalue))
# df_CB_all = np.concatenate((df_CB,CB_minuslog10pvalue), axis = 0)


# How to plot gene vs. -log10(pvalue) and colour it by chromosome?
# df['ind'] = range(len(df))
# df_grouped = df.groupby(('chromosome'))

# manhattan plot
fig,ax = plt.subplots()
x_labels = []
x_labels_pos = []
for num, (name, group) in enumerate(df_grouped):
    group.plot(kind='scatter', x='ind', y='minuslog10pvalue',color=colors[num % len(colors)], ax=ax)
    x_labels.append(name)
    x_labels_pos.append((group['ind'].iloc[-1] - (group['ind'].iloc[-1] - group['ind'].iloc[0])/2))
ax.set_xticks(x_labels_pos)
ax.set_xticklabels(x_labels)

# set axis limits
ax.set_xlim([0, len(df)])
ax.set_ylim([0, 3.5])

# x axis label
ax.set_xlabel('Chromosome')

# show the graph
plt.show()
                        