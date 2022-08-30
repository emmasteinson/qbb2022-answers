genefile=~/data/vcf_files/random_snippet.vcf #set variable for input file
bedfile=~/data/bed_files/chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed #set variable for input file

awk '{if ($4 == 1) {print}}' $bedfile > st1.bed #use awk to pull if column 4 = 1 (TSS we have decided is promoter) and print to new file st1

bedtools intersect -a $genefile -b st1.bed > intersect.bed #use bedtools to find genes that have chromatin state 1 TSS

awk '{if ($4 == "C") {print $5}}' intersect.bed | sort | uniq -c #if column 4 = cytosine print column 5 to find most common alternate allele 



