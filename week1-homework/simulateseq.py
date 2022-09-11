#!/usr/bin/env python3
import numpy as np


genome = np.zeros(1000000, dtype=int) #makes array with 1 mil zeros with each zero standing for a base pair standing for genome
from scipy.stats import poisson 
import matplotlib.pyplot as plt



#this is for 5x coverage
#for i in range(50000): #number of reads required
    #randstart = np.random.randint(0, 999900) #set possible start and end positions for random reads
    #for j in range(randstart, randstart + 100): #random read start and read end = start + 100
        #genome[j] += 1 #turn zeros in array into 1's to represent they have been read once

#this is to count the number of zeros for 1.3 for 5x coverage
#v = np.array(genome)
#zeros = np.where(v==0)
#print(len(zeros[0]))


#this is to make hitogram for 5x coverage
#x = np.array(genome) #make array of our reads for each position 
#fig, ax = plt.subplots()
#ax.plot(x, poisson.pmf(x, mu=5), 'bo', ms=8) 
#ax.hist(x, density =True)
#ax.set_ylabel("frequency")
#ax.set_xlabel("coverage")
#plt.title("Frequency of Coverage")
#plt.savefig("5xhist.png")


#this is for 15x coverage
for i in range(150000): #number of reads required
    randstart = np.random.randint(0, 999900) #set possible start and end positions for random reads
    for j in range(randstart, randstart + 100): #random read start and read end = start + 100
        genome[j] += 1 #turn zeros in array into 1's to represent they have been read once


#this is to make hitogram for 15x coverage
x = np.array(genome) #make array of our reads for each position 
fig, ax = plt.subplots()
ax.plot(x, poisson.pmf(x, mu=15), 'bo', ms=8) 
ax.hist(x, density =True)
ax.set_ylabel("frequency")
ax.set_xlabel("coverage")
plt.title("Frequency of Coverage")
#plt.savefig("15xhist.png")

#this is to count the number of zeros for 1.3 for 15x coverage
v = np.array(genome)
zeros = np.where(v==0)
print(len(zeros[0]))






