#!/usr/bin/env python

import numpy as np
import scipy
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
import statsmodels.api as sm
import pylab


input_arr = np.genfromtxt("dros_gene_expression.csv", delimiter=',', names=True, dtype=None, encoding='utf-8')
col_names = list(input_arr.dtype.names)
transcript_names = input_arr['t_name']
fpkm_data = []

for i, row in enumerate(input_arr):
    r = list(row)
    fields = r[1:]
    fpkm_data.append(fields)

# make 2d array  
fpkm_values_2d = np.reshape(fpkm_data, (34718, 10))

# find median for each transcript
median_exp = np.median(fpkm_values_2d, axis=1)
# find indeces where median > 0
subset_fpkm_ind = np.where(median_exp > 0)[0]

# subset names and data
t_name_subset = input_arr['t_name'][subset_fpkm_ind]
subset_fpkm = median_exp[subset_fpkm_ind]

subset_arr = input_arr[subset_fpkm_ind]
subset_fpkm = []
for i, row in enumerate(subset_arr):
    r = list(row)
    fields = r[1:]
    subset_fpkm.append(fields)

subset_fpkm_count = len(subset_fpkm)
subset_fpkm_arr = np.reshape(subset_fpkm, (subset_fpkm_count,10))

# log transform data
subset_fpkm_log = np.log2(subset_fpkm_arr + 0.1)

# linkage and leaves list
subset_tran = np.transpose(subset_fpkm_log) #samples
subset_tran2 = np.transpose(subset_tran) #genes
linkage = scipy.cluster.hierarchy.linkage(subset_tran) #samples
linkage2 = scipy.cluster.hierarchy.linkage(subset_tran2) #genes
leaves_list = scipy.cluster.hierarchy.leaves_list(linkage) #samples
leaves_list2 = scipy.cluster.hierarchy.leaves_list(linkage2) #genes

gene_arr = subset_fpkm_log[leaves_list2]
sample_arr = gene_arr.T[leaves_list]
samp_plot = sample_arr.T

# heatmap
fig, ax = plt.subplots()
ax = sns.heatmap(samp_plot,
                xticklabels=col_names[1:])
ax.set_xlabel("Samples")
ax.set_ylabel("Genes")
plt.title("Clustered Gene Expression Data")
plt.tight_layout()
plt.savefig("genes_heatmap.png")
plt.close(fig)


# dendrogram
labels = np.array(col_names[1:])[leaves_list]
dendrogram(linkage, labels=labels)
plt.title("Dendrogram")
plt.tight_layout()
plt.savefig("dendrogram.png")
plt.close()

# values for each gene, sex and time period
sexes=[]
stages=[]
for sample in col_names[1:]:
    sexes.append(sample.split('_')[0])
    stages.append(sample.split('_')[1])

p_vals = []
for i in range(samp_plot.shape[0]):
    list_of_tuples = []
    for j in range(len(col_names[1:])):
        list_of_tuples.append((transcript_names[i],samp_plot[i,j], sexes[j], stages[j]))
    longdf = np.array(list_of_tuples, dtype=[('transcript', 'S11'), ('fpkm', float), ('sex', 'S6'), ('stage', int)])
    model = smf.ols(formula="fpkm ~ 1 + stage", data=longdf, subset=None, drop_cols=None)
    results = model.fit()
    p_vals.append([results.params[0],results.params[1]])
qq_data = np.array(p_vals)

sm.qqplot(qq_data, line='q')
plt.title("QQ Plot")
plt.tight_layout()
plt.savefig("qqplot.png")
plt.close(fig)
