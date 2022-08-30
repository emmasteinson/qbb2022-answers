#!/bin/bash

#USAGE: bash exercise3.sh input_VCF

awk '/^#/{next} {print $1 "\t" $2-1 "\t" $2}' $1 | sort -k1,1 -k2,2n > variants.bed #this is trying to create new file from random_snippet.vcf by printing  the first colum, print the second column but subtract 1 from the value, and then print the second column to new file (creating a bedfile with this info) also need to sort based on column 1 and then sort based on column 2 numerically (puts in order along chromosome)
sort -k1,1 -k2,2n ~/data/bed_files/genes.bed > genes.sorted.bed #sort based on column 1 and then sort based on column 2 numberically (puts in order along chromosome)
bedtools closest -a variants.bed -b genes.sorted.bed ##searches for ovelapping features in variants.bed and genes.sorted.bed In the event that no feature in B overlaps the current feature in A, closest will report the nearest (that is, least genomic distance from the start or end of A) feature in B.
