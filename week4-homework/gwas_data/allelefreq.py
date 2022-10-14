#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np


freq = np.genfromtxt("plink.frq", dtype = None, encoding = None, names = ["chr", "snp", "A1", "A2", "MAF", "NCHROBS"])

val = []

for each in freq[1:]:
    val.append(float(each[4]))
    
fig, ax = plt.subplots()
ax.hist(val)
ax.set_xlabel("allele frequency")
ax.set_ylabel("frequency")
ax.set_title("Allele Frequency")

fig.savefig("allelefrequency.png")
#plt.show()