#!/usr/bin/env python

import matplotlib.pyplot as plt
import  numpy as np

eigenvector = np.genfromtxt("plink.eigenvec", dtype = None, encoding = None, names = ["locus_one", "locus_two", "val1", "val2", "val3"])

fig, ax = plt.subplots(nrows = 2)
ax[0].set_ylabel("PC2")
ax[0].set_xlabel("PC1")
ax[1].set_ylabel("PC3")
ax[1].set_xlabel("PC1")
ax[0].scatter(eigenvector["val1"], eigenvector["val2"])
ax[1].scatter(eigenvector["val1"], eigenvector["val3"])


plt.savefig("ex2a&b")