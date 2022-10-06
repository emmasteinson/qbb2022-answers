#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

#need phenotypes from CB1908_IC50 column in file with same name 

# #using genotype and IC phenotype file use assoc.linear just to find the top SNP. vcf only has sample name and genotypes whereas phenotype only has sample name and phenotype not genotype want genotype and phenotype need to comine those using the sample name


#find most signficant SNP to plot, look in gwasIC50.assoc.linear
#seperate out samples by genotype, look at vcf file
#get corresponding phenotype, look at IC50 file
ref = []
het = []
alt = []
file = open("gwasGS451.assoc.linear")
pval = []
snp = []
bp = []
chrom = []
for i in file:
    new = i.rstrip("\n").split()
    if new[4] == "ADD":
        pval.append(float(new[8]))
        snp.append(new[1])
        bp.append(new[2])
        chrom.append(new[0])
min_value = min(pval) #lowest p val in list
position = pval.index(min_value) #index of lowest value in the list
significant = snp[position] #to find the most signficant snp
sigbp = bp[position]
sigchrom = chrom[position]
print(significant) #this prints the most significant snp
print(sigchrom) #this prints significant snp chromosme
print(sigbp) #this prints significant snp location

genotypes = []
sampleid = []
#loop through vcf file
genotype_file = open("genotypes.vcf")
pheno_file = open("GS451_IC50.txt") 
for i in genotype_file:
    if i.startswith("##"): #skip header line
        continue
    geno_list = i.rstrip("\n").split("\t")
    if geno_list[2] == significant:
        genotypes = geno_list[9:]
    if i.startswith("#"):
        sampleid = geno_list[9:]
        # print(sampleid)
new_dict = dict(zip(sampleid, genotypes))
for i in pheno_file:
    if i.startswith("F"):
        continue
    pheno_list = i.rstrip("\n").split("\t")
    id_A = pheno_list[0]
    id_B = pheno_list[1]
    combined =id_A + "_" + id_B
    if pheno_list[2] == "NA":
        continue
    sample_val =float(pheno_list[2])
    gt = new_dict[combined]
    if gt == "0/0":
        ref.append(sample_val)
    if gt == "0/1":
        het.append(sample_val)
    if gt == "1/1":
        alt.append(sample_val)
#now plot
fig, ax = plt.subplots()
ax.boxplot([ref, het, alt])
ax.set_xlabel("Genotype")
ax.set_ylabel("Phenotype")
plt.xticks([1, 2, 3], ["ref", "het", "alt"])
fig.savefig("boxplotGS451.png")
plt.show()









