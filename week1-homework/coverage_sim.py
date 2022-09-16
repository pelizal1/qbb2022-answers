#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# initialize variables for read length and coverage for np array
read_length = 100
coverages = np.zeros(1000000, dtype=int)

# initialize coverage
# coverage = 50000
coverage = 150000

# assign coverage values
for i in range(coverage):
    start = np.random.randint(0, high=999900)
    for j in range(read_length):
        coverages[start] += 1
        start += 1

# the highest coverage in the array        
max_cov = np.amax(coverages)

# plot the 5X coverage
# fig, ax = plt.subplots()
# ax.hist(coverages, bins=max_cov)
# ax.set_xlabel("Coverage")
# ax.set_ylabel("Frequency of coverage")
# plt.title("5X Coverage of Genome")
# plt.tight_layout()
# plt.savefig("coverage_5x.png")
#
# # close and clear 5X
# plt.close()
# fig.clear()
# ax.clear()

# Poisson distribution
# fig, ax = plt.subplots()
# ax.hist(coverages, bins=max_cov)
# ax.set_xlabel("Coverage")
# ax.set_ylabel("Frequency of coverage")
#
# mu = 5
# ax1 = ax.twinx()
# ax1.plot(coverages, poisson.pmf(coverages, mu)*1000000, 'bo', ms=8, label='poisson pmf')
# plt.title("5X Coverage of Genome")
# plt.legend()
# plt.tight_layout()
# plt.savefig("coverage_5X_poisson.png")

# count zeros
# num_zero_cov = np.count_nonzero(coverages==0)
# print(num_zero_cov)
#
# calculate expected frequency count
# freq_zero = poisson.pmf(k=0, mu=5)
# print(freq_zero*1000000)


# plot the 15X coverage
# fig, ax = plt.subplots()
# ax.hist(coverages, bins=max_cov)
# ax.set_xlabel("Coverage")
# ax.set_ylabel("Frequency of coverage")
# plt.title("15X Coverage of Genome")
# plt.tight_layout()
# plt.savefig("coverage_15x.png")

# close and clear 15X
# plt.close()
# fig.clear()
# ax.clear()

# Poisson distribution
# fig, ax = plt.subplots()
# ax.hist(coverages, bins=max_cov)
# ax.set_xlabel("Coverage")
# ax.set_ylabel("Frequency of coverage")
#
# mu = 15
# ax1 = ax.twinx()
# ax1.plot(coverages, poisson.pmf(coverages, mu)*1000000, 'bo', ms=8, label='poisson pmf')
# plt.title("5X Coverage of Genome")
# plt.legend()
# plt.tight_layout()
# plt.savefig("coverage_15X_poisson.png")

# count zeros
num_zero_cov = np.count_nonzero(coverages==0)
print(num_zero_cov)

# calculate expected frequency count
freq_zero = poisson.pmf(k=0, mu=15)
print(freq_zero*1000000)
