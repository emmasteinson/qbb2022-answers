#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
#set variable join as jioned text file with info about each column
fig, ax = plt.subplots()
join = np.genfromtxt("joined_file.txt", dtype = None, encoding = None, names = ["locus_one", "locus_two", "pca1", "pca2", "pca3", "pop", "superpop", "sex"])
#start with superpop
superpop = (np.unique(join["superpop"])) #making variable superpop equal to unique elements from array superpop which is column in joined file

for each in superpop: #making a list of unique items in superpop
    x = [] #list of x values
    y = [] #list of y values
 #for each in superpop record an x and y value   
    for thing in join:
        if each == thing[6]: #for everything in colum 6 (superpop)
            x.append(thing[2]) #add PCA 1
            y.append(thing[3]) #add PCA 2
#the code above is how we add color
    ax.scatter(x, y, label = each) #make scatter with x and y and label each superpor (color)
    ax.legend()
ax.set_xlabel("PCA1")
ax.set_ylabel("PCA2")
ax.set_title("PCA 1 vs. 2 According to Superpop")
#plt.show()
plt.savefig("ex3_a.png")

#start gender plot similar structure
fig, ax = plt.subplots()
join = np.genfromtxt("joined_file.txt", dtype = None, encoding = None, names = ["locus_one", "locus_two", "pca1", "pca2", "pca3", "pop", "superpop", "sex"])
sex = ("female", "male") 
for each in sex:
    x = [] #list of x values
    y = [] #list of y values  
    for thing in join:
        if each == thing[7]: #for everything in colum 6 (superpop)
            x.append(thing[2]) #add PCA 1
            y.append(thing[3]) #add PCA 2
#the code above is how we add color
    ax.scatter(x, y, label = each) #make scatter with x and y and label each superpor (color)
    ax.legend()
ax.set_xlabel("PCA1")
ax.set_ylabel("PCA2")
ax.set_title("PCA 1 vs. 2 According to Gender")
#plt.show()
plt.savefig("ex3_b.png")

#start subpop plot
fig, ax = plt.subplots()
join = np.genfromtxt("joined_file.txt", dtype = None, encoding = None, names = ["locus_one", "locus_two", "pca1", "pca2", "pca3", "pop", "superpop", "sex"])
#start with superpop
subpop = (np.unique(join["pop"])) #making variable superpop equal to unique elements from array superpop which is column in joined file

for each in subpop: #making a list of unique items in superpop
    x = [] #list of x values
    y = [] #list of y values
 #for each in superpop record an x and y value   
    for thing in join:
        if each == thing[5]: #for everything in colum 6 (superpop)
            x.append(thing[2]) #add PCA 1
            y.append(thing[3]) #add PCA 2
#the code above is how we add color
    ax.scatter(x, y, label = each) #make scatter with x and y and label each superpor (color)
    ax.legend(loc = 'upper right', ncol = 4) #put legend in upper right corner and add columns
ax.set_xlabel("PCA1")
ax.set_ylabel("PCA2")
ax.set_title("PCA 1 vs. 2 According to Subpop")
#plt.show()
plt.savefig("ex3_c.png")
