#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

#define function for wright fisher simulation



def wright_fisher(pop_size, af):
    af_list = []

    Fixed = False
    while Fixed == False:

        number_nextgen = np.random.binomial(pop_size, af)
        af = number_nextgen/pop_size
        af_list.append(af)

        if af ==1 or af==0:
            Fixed = True
    return(af_list) #show us allele frequencies
output_allelefreq = wright_fisher(1000, .2)

def plot(result):

    gen_number = np.arange(len(output_allelefreq))

    fig, ax = plt.subplots()
    ax.plot(gen_number, output_allelefreq)
    ax.set_xlabel("generation number")
    ax.set_ylabel("allele frequency")
    #plt.show()
    fig.savefig("allelefreqvsgen.png")
plot(output_allelefreq)

num_gens = []
for i in range(1000):
    output = wright_fisher(100, .5)
    gens_to_fix = len(output)
    num_gens.append(gens_to_fix)
#print(num_gens)

fig, ax = plt.subplots()
ax.hist(num_gens)
ax.set_xlabel("number of generations to fix")
ax.set_ylabel("frequency")
#plt.show()
fig.savefig("fixgenhistogram.png")


#vary starting population size

all_numgens = [] #list of lists for number of generations for each pop size
sizes = [100, 1000, 10000, 100000, 1000000, 10000000]
for i in sizes:
    num_gens = []
    for iteration in range(1000):
        output = wright_fisher(i, .5)
        gens_to_fix = len(output)
        num_gens.append(gens_to_fix)
    all_numgens.append(num_gens)
#print(all_numgens)

fig, ax = plt.subplots()
ax.boxplot(all_numgens, labels = sizes)
ax.set_xlabel("population size")
ax.set_ylabel("number of generations to fix")
plt.yscale('log')
#plt.show()
fig.savefig("numgensfixvspopsizeboxplt.png")


#vary allele frequency
all_numgens = [] #list of lists for number of generations for each pop size

diff_freq = [.1, .2, .3, .4, .5, .6, .7, .8, .9, 1] 
for i in diff_freq:
    num_gens = []
    for iteration in range(1000):
        output = wright_fisher(100, i)
        gens_to_fix = len(output)
        num_gens.append(gens_to_fix)
    all_numgens.append(num_gens)
#print(all_numgens)
fig, ax = plt.subplots()
ax.boxplot(all_numgens, labels = diff_freq)
ax.set_xlabel("allele freq")
ax.set_ylabel("number of generations to fix")
plt.yscale('log')
plt.show()
fig.savefig("numgensfixvsallelfreqboxplt.png")


