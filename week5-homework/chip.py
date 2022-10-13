#!/usr/bin/env python

from bdg_loader import load_data
import matplotlib.pyplot as plt

sox2 = load_data("Sox2_scalecrop.bdg")
klf4 = load_data("D2_Klf4_scalecrop.bdg")
h3k27acD0 = load_data("D0_H3k27ac_scalecrop.bdg")
h3k27acD2 = load_data("D2_H3K27ac_scalecrop.bdg")
#print(sox2)


fig, ax = plt.subplots(ncols = 1, nrows = 4 )



ax[0].fill_between(sox2['X'], sox2['Y'])
ax[0].set_ylabel("Sox2")
ax[0].xaxis.set_visible(False)

plt.xticks([])
ax[1].fill_between(klf4['X'], klf4['Y'])
ax[1].set_ylabel("Klf4")
ax[1].xaxis.set_visible(False)


ax[2].fill_between(h3k27acD0['X'], h3k27acD0['Y'])
ax[2].set_ylabel("H3k27acD0")
ax[2].xaxis.set_visible(False)



ax[3].fill_between(h3k27acD2['X'], h3k27acD2['Y'])
ax[3].set_ylabel("H3k27acD2")

plt.xticks([])
plt.tight_layout()
plt.show()
fig.savefig("finalCHIP.png")
