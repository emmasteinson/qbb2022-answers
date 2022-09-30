#!/usr/bin/env python

import matplotlib.pyplot as plt
from vcfParser import * #import vcfParser script

parsed = parse_vcf("var.vcf") #runs vcfparser on vcf files sets as variabl. parser takes vcf items and turnn into list. every item in list a line of the vcf. everyline itself is also a list. list of lists
#print(parsed)

#start with Allele frequency
AFlist = []
#for every line in the file pull out info field and then pull ouf AF within the INFO field
for line in parsed: #look in every line in vcf
    info = line[7] #want to pull out 8th item in each list (info field)
    if line[0] == "CHROM": #this skips header line
        continue
    allele = float(info["AF"]) #pull out value for key AF. also need to convert string to float
    AFlist.append(allele) #add allele fequency to AFlist



read_depth = []
#
for line in parsed: #look in every line in vcf
#nee to go thorugh all sample columns     
    format = line[8] #want to pull out 9th item in each list (Format field)
    if line[0] == "CHROM": #this skips header line
        continue
    for i in range(9,18): #column numbers we want to loop through
        column = line[i] #pull out the column you are on
        dp = column[2] #change  this to 2?
        if dp == ".": #skip if dp is a .
            continue
        read_depth.append(int(dp)) #this pulls out the DP (second column) and adds to list read_depth


annotation = []

for line in parsed: #look in every line in vcf
    info = line[7] #want to pull out 8th item in each list (info field)
    if line[0] == "CHROM": #this skips header line
        continue
    Ann = info["ANN"] #pull out value for key ANN. remember info is dictionary
    ann_list = Ann.split("|") #ann is a string need to split along |
    first_annotation = ann_list[1] #pull out first annotation
    annotation.append(first_annotation) #add first annotation to list

barplotitem = []
barheights = []

list_set = list(set(annotation)) #gives list of unique items
for unique in list_set:
    #print(unique)
    anot = annotation.count(unique)
    barheights.append(anot)
    
quality = []

for line in parsed: #look in every line in vcf
#nee to go thorugh all sample columns
    format = line[8] #want to pull out 9th item in each list (Format field)
    if line[0] == "CHROM": #this skips header line
        continue
    for i in range(9,18): #column numbers we want to loop through
        column = line[i] #pull out the column you are on
        gq = column[1] #pull out second value
        if gq == ".": #skip if dp is a .
            continue
        quality.append(float(gq))
#print(quality)


# #this puts all the plots into one figure with subpanels
fig, axes = plt.subplots(ncols=2, nrows=2)


# read depth plot
axes[0,0].hist(read_depth)
axes[0,0].set_xlabel("read depth")
axes[0,0].set_ylabel("frequency")
axes[0,0].set_yscale("log")
axes[0,0].set_title("Read Repth")

#quality plot
axes[0,1].hist(quality)
axes[0,1].set_xlabel("quality")
axes[0,1].set_ylabel("frequency")
axes[0,1].set_yscale("log")
axes[0,1].set_title("Quality")

# AFS
axes[1,0].hist(AFlist)
axes[1,0].set_xlabel("allele frequency")
axes[1,0].set_ylabel("number of alleles")
axes[1,0].set_title("Allele Frequency")



# predicted variant effects
axes[1,1].bar(list_set, barheights)
axes[1,1].set_xlabel("annotation")
axes[1,1].set_ylabel("number of alleles")
axes[1,1].set_yscale("log")
plt.xticks(fontsize = 6, rotation = 90)
plt.title("Predicted Variant Affects")


plt.tight_layout()

plt.autoscale()
fig.savefig("plots.png")
plt.show()
