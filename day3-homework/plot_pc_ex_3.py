#!/usr/bin/env python
# make a dictionary for each category
# key: category
# value: list >> 2 lists [0]=PC1, [1]=PC2
# plot categories as different series

import matplotlib.pyplot as plt
import numpy as np


integ__plink_joined = np.genfromtxt("integ_call_plink_joined.txt",
                        dtype = None,
                        encoding = None,
                        names = ["ID", "pop", "superpop", "sex", "ID", "first_pc", "second_pc", "third_pc"])

# # plot population
# fig, ax = plt.subplots()
# for i, line in enumerate(integ__plink_joined):
#     for
# ax.scatter(plink["first_pc"], plink["second_pc"])
# ax.set_xlabel("first_pc")
# ax.set_ylabel("second_pc")
# ax.legend()
# plt.savefig("ex3_a.png")
# plt.close(fig)
#
# # plot superpopulation
# fi, a = plt.subplots()
# a.scatter(plink["first_pc"], plink["second_pc"])
# a.set_xlabel("first_pc")
# a.set_ylabel("third_pc")
# plt.savefig("ex3_b.png")
# a.legend()
# plt.close(fi)

# plot sex
f, z = plt.subplots()
sex = {}
sexes = []
# find unique entries in field
sexes = np.unique(integ__plink_joined["sex"])
# add PC1, PC2 to corresponding list in dict entry
for h, sx in enumerate(sexes):
    pcs = []
    pc1_list = []
    pc2_list = []
    for i, line in enumerate(integ__plink_joined):
        # line[i] changes depending on the graph
        if line[3] == sx:
            pc1 = line[5]
            pc2 = line[6]
            pc1_list.append(pc1)
            pc2_list.append(pc2)
    pcs = [pc1_list, pc2_list]
    sex[sx] = pcs
    z.scatter(sex[sx][0], sex[sx][1], label = sx)
z.set_xlabel("pc1")
z.set_ylabel("pc2")
z.legend()
plt.title(label = "PCA: SNPs and Sex")
plt.savefig("ex3_c.png")
plt.close(f)

# plot superpop
fi, a = plt.subplots()
superpop = {}
superpop_types = []
# find unique entries in field
superpop_types = np.unique(integ__plink_joined["superpop"])
# add PC1, PC2 to corresponding list in dict entry
for h, superp in enumerate(superpop_types):
    pcs = []
    pc1_list = []
    pc2_list = []
    for i, line in enumerate(integ__plink_joined):
        # line[i] changes depending on the graph
        if line[2] == superp:
            pc1 = line[5]
            pc2 = line[6]
            pc1_list.append(pc1)
            pc2_list.append(pc2)
    pcs = [pc1_list, pc2_list]
    superpop[superp] = pcs
    a.scatter(superpop[superp][0], superpop[superp][1], label = superp)
a.set_xlabel("pc1")
a.set_ylabel("pc2")
a.legend()
plt.title(label = "PCA: SNPs and Superpopulation")
plt.savefig("ex3_b.png")
plt.close(fi)

# plot superpop
fig, ax = plt.subplots()
pop = {}
pop_types = []
# find unique entries in field
pop_types = np.unique(integ__plink_joined["pop"])
# add PC1, PC2 to corresponding list in dict entry
for h, popl in enumerate(pop_types):
    pcs = []
    pc1_list = []
    pc2_list = []
    for i, line in enumerate(integ__plink_joined):
        # line[i] changes depending on the graph
        if line[1] == popl:
            pc1 = line[5]
            pc2 = line[6]
            pc1_list.append(pc1)
            pc2_list.append(pc2)
    pcs = [pc1_list, pc2_list]
    pop[popl] = pcs
    ax.scatter(pop[popl][0], pop[popl][1], label = popl)
ax.set_xlabel("pc1")
ax.set_ylabel("pc2")
ax.legend(ncol=4)
plt.title(label = "PCA: SNPs and Population")
plt.savefig("ex3_a.png")
plt.close(fig)
