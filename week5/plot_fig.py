#!/usr/bin/env python

import matplotlib.pyplot as plt
from bdg_loader import load_data


# plot D0_H3K27ac_treat.bdg
"""
Read in the bedgraph file.
col4 in the file is the normalized number of reads covering the bases in that range
"""
d0_H3K27ac = load_data("D0_H3K27ac_treat.bdg")

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4,1)
ax1.plot(d0_H3K27ac['X'], d0_H3K27ac['Y'])
ax1.set_title("Day 0 H3K27ac")
ax1.get_xaxis().set_visible(False)

# plot D2_H3K27ac_treat.bdg
d2_H3K27ac = load_data("D2_H3K27ac_treat.bdg")
ax2.plot(d2_H3K27ac['X'], d2_H3K27ac['Y'])
ax2.set_title("Day 2 H3K27ac")
ax2.get_xaxis().set_visible(False)

# plot D2_Klf4_treat.bdg
klf4 = load_data("D2_Klf4_treat.bdg")
ax3.plot(klf4['X'], klf4['Y'])
ax3.set_title("Day 2 Klf4")
ax3.get_xaxis().set_visible(False)

# plot D2_SoX2_treat.bdg
sox2 = load_data("D2_SOX2_treat_scaled_cropped.bdg")
ax4.plot(sox2['X'], sox2['Y'])
ax4.set_title("Day 2 Sox2")
ax4.get_xaxis().set_visible(False)

plt.tight_layout()
plt.savefig("week5hw.png")