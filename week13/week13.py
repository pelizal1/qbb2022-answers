#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

def WF_sim(start_al_freq, pop_size):
    # Wright-Fisher simulation of allele frequencies
    # Input: starting allele frequency, population size
    # end simulation once allele frequency reaches 0 or 1
    # Output: list of allele frequencies
    
    al_freq = start_al_freq
    sel_strength = 0
    al_freq_list = []
    
    al_freq_list.append(al_freq)
    
    while (al_freq < 1) and (al_freq > 0):
        num_al = np.random.binomial(2*pop_size, al_freq)
        al_freq = (num_al*(1+sel_strength))/((2*pop_size) - num_al + (num_al*(1+sel_strength)))
        al_freq_list.append(al_freq)
    
    return al_freq_list



# plot single simulation
# pop_size = 100
# start_al_frq = 0.1
# WF_sim = WF_sim(start_al_frq, pop_size)
# fig, ax = plt.subplots()
# ax.plot(WF_sim)
# ax.set_xlabel(f"Generations\nPopulation Size: {pop_size}\nStarting Allele Freq.: {start_al_frq}")
# ax.set_ylabel("Allele Frequency")
# ax.set_title("Allele Frequency over generations")
# plt.tight_layout()
# plt.savefig("2.png")
# plt.close()

def run_sim(start_al_freq, pop_size, n_iters):
    # running the Wright-Fisher simulatio n_iters times
    # output: list of fixation times
    fix_times = []
    while n_iters > 0:
        freq_list = WF_sim(start_al_freq, pop_size)
        fix_time = len(freq_list)
        fix_times.append(fix_time)
        n_iters -= 1
    return fix_times
    
# 3 - time to fixation
# pop_size = 100
# start_al_frq = 0.5
# n_iters = 1000
# fix_times = run_sim(start_al_frq, pop_size, n_iters)
# fig, ax = plt.subplots()
# ax.hist(fix_times, density=True)
# ax.set_xlabel(f"Time to Fixation (Generations)\nPopulation Size: {pop_size}\nStarting Allele Freq.: {start_al_frq}\nRuns: {n_iters}")
# ax.set_title("Time to fixation")
# plt.tight_layout()
# plt.savefig("3.png")
# plt.close()

# 4 - plot fixation time vs. N (population)
# pop_size = 200
# start_al_frq = 0.5
# pop_sizes = []
# fix_times = []
# for i in range(6):
#     # run the simulation using six different population sizes
#     pop_sizes.append(pop_size)
#     # use the median fix time from several iterations
#     fix_time = len(WF_sim(start_al_frq, pop_size))
#     fix_times.append(fix_time)
#     pop_size = pop_size*2
#
# fig, ax = plt.subplots()
# ax.plot(pop_sizes, fix_times)
# ax.set_xlabel(f"Population Size (N)\nStarting Allele Freq.: {start_al_frq}")
# ax.set_ylabel("Fixation Time")
# ax.set_title("Effect of population on fixation time")
# ax.set_xscale("log")
# ax.set_xticks(pop_sizes)
# ax.set_xticklabels(pop_sizes)
# plt.tight_layout()
# plt.savefig("4.png")
# plt.close()

# 5 - simulation under different allele frequencies with same population size
pop_size = 200
al_frq = 0.998
n_iters=100
fix_times = []
al_freqs = []
for i in range(10):
    # run the simulation using six different population sizes
    al_freqs.append(al_freq)
    # NEED TO USE run_sim and save the iterations for the variability!!!
    fix_time = len(WF_sim(start_al_frq, pop_size))
    fix_times.append(fix_time)
    al_freq = al_freq/2

# fig, ax = plt.subplots()
# ax.plot(pop_sizes, fix_times)
# ax.set_xlabel(f"Starting Allele Frequency\nPopulation Size: {pop_size}\nRuns for each freq.: {n_iters}")
# ax.set_ylabel("Fixation Time")
# ax.set_title("Effect of allele frequency on fixation time")
# ax.set_xscale("log")
# ax.set_xticks(pop_sizes)
# ax.set_xticklabels(pop_sizes)
# plt.tight_layout()
# plt.savefig("5.png")
# plt.close()