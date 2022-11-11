#!/usr/bin/env python

import numpy as np
import scipy
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt
import seaborn as sns



input_arr = np.genfromtxt("dros_gene_expression.csv", delimiter=',', names=True, dtype=None, encoding='utf-8')
col_names = list(input_arr.dtype.names)
transcript_names = input_arr['t_name']
print(col_names)
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
print(subset_fpkm_arr.shape)

# log transform data
subset_fpkm_log = np.log2(subset_fpkm_arr + 0.1)
print(subset_fpkm_log.dtype.names)

# linkage and leaves list
subset_tran = np.transpose(subset_fpkm_log)
print(subset_tran.shape)
linkage = scipy.cluster.hierarchy.linkage(subset_tran)
linkage_tran = np.transpose(linkage)
print(linkage_tran.shape)
linkage_2 = scipy.cluster.hierarchy.linkage(linkage_tran)
print(linkage_2.shape)
leaves_list = scipy.cluster.hierarchy.leaves_list(linkage_2)
print(leaves_list.shape)

# heatmap
fig, ax = plt.subplots()
ax = sns.heatmap(linkage)
# ax.set_xlabel("Number of tosses")
# ax.set_ylabel("Probability of heads")
plt.title("Clustered Gene Expression Data")
# plt.show()
plt.savefig("heatmap.png")
plt.close(fig)


# dendrogram
dendrogram(leaves_list)
plt.show()
    