# QBB2022 - Day 1 - Homework Exercises Submission
1. In the interactive lecture, we looked at what’s the most common alternate allele for a reference allele of Cytosine using awk. You are going to use the script exercise1.sh in order to find the most common alternate allele for all of the reference allele bases, not just Cytosine. However, there is an error in the script that needs to be debugged.

Error message is awk: illegal field $(), name "nuc". 
we need to use define the bash variable for: awk -v var=$nuc '/^#/{next} {if ($4 == var) {print $5}}' $1 | sort | uniq -c

Considering  A
 354 C
1315 G
 358 T
Considering  C
 484 A
 384 G
2113 T
Considering  G
2041 A
 405 C
 485 T
Considering  T
 358 A
1317 C
 386 G
 
 Yes this makes sense because A to G is much more common because this is a transition (both purines) and not a traansversion (purine to pyrimadine)
 
 2. What’s the most common alternate allele for a Cytosine reference allele for variants occurring in promoter like regions of the genome? 

 -promoters are not objectively defined by this key. we have decided to treat active TSS (1) as indicating promoters.
 
 
  #stored as ex2.sh under day1-homework folder
 genefile=~/data/vcf_files/random_snippet.vcf #set variable for input file
 bedfile=~/data/bed_files/chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed #set variable for input file

 awk '{if ($4 == 1) {print}}' $bedfile > st1.bed #use awk to pull if column 4 = 1 (1=TSS we have decided is promoter identifier) and print to new file st1

 bedtools intersect -a $genefile -b st1.bed > intersect.bed #use bedtools to find genes that have chromatin state 1 TSS

 awk '{if ($4 == "C") {print $5}}' intersect.bed | sort | uniq -c #if column 4 = cytosine print column 5 to find most common alternate allele
 
 5 A
 7 G
 15 T
 
 Answer to 2: the most common alternate allele is cytosine for variants occurring in promoter regions.
 
 3. It is often of interest for biologists to find the closest gene to some variant or set of variants which are identified in a screen or as a significant GWAS hit. Debug the script that uses bedtools closest to find the closest gene for each variant.
 
 awk '/^#/{next} {print $1,$2-1, $2}' $1 > variants.bed #this is trying to create new file from random_snippet.vcf by printing  the first colum, print the second column but subtract 1 from the value, and then print the second column to new file (creating a bedfile with this info)
 
 sort -k1,1 -k2,2n ~/data/bed_files/genes.bed > genes.sorted.bed #sort based on column 1 and then sort based on column 2 numberically (puts in order along chromosome)
 
 bedtools closest -a variants.bed -b genes.sorted.bed #searches for ovelapping features in variants.bed and genes.sorted.bed In the event that no feature in B overlaps the current feature in A, closest will report the nearest (that is, least genomic distance from the start or end of A) feature in B.
 
 -errors: 
 Error 1: we need to make sure file is tab deliminated fix by adding "\t"
 Error 2: Sorted input specified, but the file variants.bed has the following out of order record-to fix this we need to sort the variants.bed file, so we need to pipe sort to the awk command 
 
 #new script: 
awk '/^#/{next} {print $1 "\t" $2-1 "\t" $2}' $1 | sort -k1,1 -k2,2n > variants.bed
sort -k1,1 -k2,2n ~/data/bed_files/genes.bed > genes.sorted.bed
bedtools closest -a variants.bed -b genes.sorted.bed
 
 (base) [~/qbb2022-answers/day1-homework $]bash exercise3.sh ~/data/vcf_files/random_snippet.vcf |  wc -l
    10293 #number of variants-this command  counts number of lines
 (base) [~/qbb2022-answers/day1-homework $]bash exercise3.sh ~/data/vcf_files/random_snippet.vcf |  sort -k 7 | uniq -f 6 -c | wc -l
      200 #number of genes-this command sorts by the 7th column (gene) then uniq -f 6 (ignore first 6 fields) -c gives us gene name and number of timees it occurred. wc -l gives count of # of gnenes
	  How many variants on average connected with a gene?
	  10293/200 = 51.5 on average
 