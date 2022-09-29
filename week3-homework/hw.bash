#!/bin/bash
#to index the sacCer3 reference genome using bwa index command
bwa index sacCer3.fa
for SAMPLE in 09 11 23 24 27 31 35 39 62 63
do
	bwa mem -R "@RG\tID:${SAMPLE}\tSM:${SAMPLE}" -t 4 -o ${SAMPLE}.sam sacCer3.fa A01_${SAMPLE}.fastq
done
for SAMPLE in 09 11 23 24 27 31 35 39 62 63
do
	samtools sort -@4 -O bam -o ${SAMPLE}.bam ${SAMPLE}.sam
done
for SAMPLE in 09 11 23 24 27 31 35 39 62 63
do
	samtools index ${SAMPLE}.bam > ${SAMPLE}.bam.bai
done
freebayes -f sacCer3.fa --genotype-qualities 09.bam 11.bam 23.bam 24.bam 27.bam 31.bam 35.bam 39.bam 62.bam 63.bam | vcffilter -f "QUAL > 20" > results.vcf

#Step 6:
vcfallelicprimitives -k -g results.vcf > allele.vcf
#Step 7:
snpeff ann R64-1-1.99 allele.vcf > var.vcf 

#sequencing different yeasst strains. aligrn reads to genome them variant call based on how reads align. frist 3 steps all alignment steps. sort bam aliignment and index it. cleaned up bam files then variant call. freebays variant calling do iiithink theres a SNP here call it. filter for high quality SNPs and decompose (seperate different SNPs that are at same postiion listed next to each other in file need to name into two seperate lines ). varaitn effect prediction is going to give estimate for what those SNPs are actually doing (intronic of exon).