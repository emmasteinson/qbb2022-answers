#!/usr/bin/env python
#import bed parser function
import bed_parser_extended
import statistics
# load a BED file
bed = bed_parser_extended.parse_bed("hg38_gencodev41_chr21.bed") #bed output is a list of lits and we need the 10th item of every list
# print(bed)

#find the median number of exons for genes in the BED file you copied under the instructions
#0. initialize list of exon numbers
exon_number = []
#1. loop through every item in 'bed' (which is a list)
#2. pull out column 10 from that item (count of exons within that gene)
for i in range(len(bed)):
    exon_number.append(bed[i][9]) #adding exon numbers to list exon_number
    #print(exon_number)
    
exon_number.sort() #sort the list
print(statistics.median(exon_number)) #find the median using statistics import
    


