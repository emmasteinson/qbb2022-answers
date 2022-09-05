
#QBB Lunch Day4

Exercise 1 

Output of do_all.sh:

Subsetting exons.chr21.bed.vcf
    + Covering 1107407 bp
--- Subsetting processed_pseudogene.chr21.bed.vcf
    + Covering 956640 bp
--- Subsetting protein_coding.chr21.bed.vcf
    + Covering 13780687 bp
	
-Strategies to confirm that reproduced plots are the same as in the cache/ directory:

They look the same when I open them. I could also use the diff command to compare the two vcf files and see whether there are any differences. Diff doesn't work as well at comparing binary compressed files or files that might have different meta data.

-three other gene_types in GENCODE that you find interesting and why 

"transcribed_unprocessed_pseudogene" :psuedogenes are segments of DNA that do not code for proteins and are likely derived from genes that have lost their protein coding ability due to accumulated mutations. Usually transcribed but not necissarily translated.
"lncRNA" : these regulate gene expression at a variety of different levels (ex. epigenetic, transcriptional, translational)
"miRNA" : miRNAs are inportant for controlling gene expression by preforming post trnascriptional gene silencing 

Exercise 2

Exercise 3 (psuedogene might be slightly different -more alternate alleles in psuedogenes because theere isnt as strong selection against psuedogenes because they aren't coding. see higher AC in psuedogenes)

how many variants are in this bin that many variants have an allele count betwee 0 10 -> in solutions logged the x-axis


