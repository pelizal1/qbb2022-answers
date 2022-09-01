#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

plink = np.genfromtxt("plink.eigenvec",
                        dtype = None,
                        encoding = None,
                        names = ["ID", "ID", "first_pc", "second_pc", "third_pc"])

# plot first_pc and second_pc
fig, ax = plt.subplots()
ax.scatter(plink["first_pc"], plink["second_pc"])
ax.set_xlabel("first_pc")
ax.set_ylabel("second_pc")
plt.savefig("ex2_a.png")
plt.close(fig)

# plot first_pc and third_pc
fi, a = plt.subplots()
a.scatter(plink["first_pc"], plink["third_pc"])
a.set_xlabel("first_pc")
a.set_ylabel("third_pc")
plt.savefig("ex2_b.png")
plt.close(fi)
