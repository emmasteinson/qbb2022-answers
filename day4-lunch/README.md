
#QBB Lunch Day4

Exercise 1 

1.1 Output of do_all.sh:
```
Subsetting exons.chr21.bed.vcf
    + Covering 1107407 bp
--- Subsetting processed_pseudogene.chr21.bed.vcf
    + Covering 956640 bp
--- Subsetting protein_coding.chr21.bed.vcf
    + Covering 13780687 bp
```
1.2 Strategies to confirm that reproduced plots are the same as in the cache/ directory:

They look the same when I open them. I could also use the diff command to compare the two vcf files and see whether there are any differences. Diff doesn't work as well at comparing binary compressed files or files that might have different meta data.

1.3 three other gene_types in GENCODE that you find interesting and why 

"transcribed_unprocessed_pseudogene" :psuedogenes are segments of DNA that do not code for proteins and are likely derived from genes that have lost their protein coding ability due to accumulated mutations. Usually transcribed but not necissarily translated. 

"lncRNA" : these regulate gene expression at a variety of different levels (ex. epigenetic, transcriptional, translational)

"miRNA" : miRNAs are inportant for controlling gene expression by preforming post trnascriptional gene silencing 

All of these are interesting because non-coding. Would number and frquency of mutations be different/higher because not being selected against as strongly?

Exercise 2

2.5 Decribe possible trends among plots

The trends in these plots made sense as most alternate alleles occur at low frequencies. There is a shift in psuedogenes which makes sense becase there would be more alternate alleles in psuedogenes as there isn't as strong selections against them because they are not coding. 

Exercise 3 
```
SYNOPSIS: Takes information about genetic location from bed file and applies it to a vcf file. This allows for aligning SNPs with where they are in the genome and gene_type they reside in. Gives information about how many base pairs each gene-type covers in genome and creates histogram using python script with this information to visualize whether some gene_types contain more alternate alleles at higher frequencies than others.
```
USAGE: bash do_all.sh <VCF> <GTF>
Dependencies: bash, bedtools, matplotlib, python3, bcftools
Description: 
1. checks that vcf and gtf input from command line can be found
2. then calls subset_regions.sh which subsets the .gtf file by pulling out the feature of interest 
```
Description:

1. Create .bed files for features of interst 
2.Run subset_regions.sh BASH script wich subsets .gtf file into bed file pulling out feature of interesest with locations on chromosome (bed file has chr21 and start end)
3.do_all.sh then uses the gene_type from newly created bed file and intersects the vcf file inputted at command line (contains information about whether a given genome has a SNP in a specific location) and bed file (contains info on genomic locations of SNPs and what gene_type they are in)
4.we now have file that has information about how many alleles in the sample poppulation with a given SNP and what gene type the SNP resides within 
5.uses this to calculate and give output of how many bp's each gene_type covers
6.do_all.sh then feeds this info python script that creates a histogram out of this information 

```
output example for "processed psuedogenes" gene_type:

processed_pseudogene.chr21.bed #contains chr1 start stop
processed_pseudogene.chr21.bed.vcf #contains chrom, pos, info about SNP, and individual allele info from samples
processed_pseudogene.chr21.bed.vcf.png #histogram of allele count vs frequency for SNPs within this gene_type
```



