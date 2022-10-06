#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

plink = np.genfromtxt("plink.eigenvec", dtype = None, encoding = None, names = ["locus_one", "locus_two", "pca1", "pca2", "pca3", "pca4", "pca5", "pca6", "pca7", "pca8", "pca9", "pca10"])


x = []
y = []

for each in plink:
    x.append(each[2])
    y.append(each[3])

    
fig, ax = plt.subplots()
ax.scatter(x, y)
ax.set_xlabel("PCA1")
ax.set_ylabel("PCA2")
ax.set_title("PCA 1 vs. 2 for Genotypes")
#plt.show()
fig.savefig("pca1vs2.png")


    
    


