Part One: Call and phase variant for each region (matenal and patenal)

chr11   1900000 		2800000
chr14   100700000       100990000
chr15   23600000        25900000
chr20   58800000        58912000
```
medaka_variant -i methylation.bam -f hg38.fa -r "chr11:1900000-2800000" -o chr11 -p chr11_phased.vcf
medaka_variant -i methylation.bam -f hg38.fa -r "chr14:100700000-100990000" -o chr14 -p chr14_phased.vcf
medaka_variant -i methylation.bam -f hg38.fa -r "chr15:23600000-25900000" -o chr15 -p chr15_phased.vcf
medaka_variant -i methylation.bam -f hg38.fa -r "chr20:58800000-58912000" -o chr20 -p chr20_phased.vcf
```
not sure if my 14 worked i might have forgotten to change to 14 
*need to run 20

Part Two: Mark reads with the correct haplotype (mark with matenal and paternal haplotype)
```
whatshap haplotag -o haplotaggedchr11.bam --reference hg38.fa --region "chr11:1900000:2800000"  --output-haplotag-list haplotaggedchr11 chr11/round_0_hap_mixed_phased.vcf.gz methylation.bam 

whatshap haplotag -o haplotaggedchr14.bam --reference hg38.fa --region "chr14:100700000:100990000"  --output-haplotag-list haplotaggedchr14 chr14/round_0_hap_mixed_phased.vcf.gz methylation.bam 

whatshap haplotag -o haplotaggedchr15.bam --reference hg38.fa --region "chr15:23600000:25900000"  --output-haplotag-list haplotaggedchr15 chr15/round_0_hap_mixed_phased.vcf.gz methylation.bam 

whatshap haplotag -o haplotaggedchr20.bam --reference hg38.fa --region "chr20:58800000:58912000"  --output-haplotag-list haplotaggedchr20 chr20/round_0_hap_mixed_phased.vcf.gz methylation.bam 
```

Part 3: Split reads into two files based on their haplotype
```
whatshap split --output-h1 h1-chr11.bam --output-h2 h2-chr11.bam haplotaggedchr11.bam haplotaggedchr11
whatshap split --output-h1 h1-chr14.bam --output-h2 h2-chr14.bam haplotaggedchr14.bam haplotaggedchr14
whatshap split --output-h1 h1-chr15.bam --output-h2 h2-chr15.bam haplotaggedchr15.bam haplotaggedchr15
whatshap split --output-h1 h1-chr20.bam --output-h2 h2-chr20.bam haplotaggedchr20.bam haplotaggedchr20
```
```
samtools cat -o h1all.bam h1-chr11.bam h1-chr14.bam h1-chr15.bam h1-chr20.bam
samtools cat -o h2all.bam h2-chr11.bam h2-chr14.bam h2-chr15.bam h2-chr20.bam 
```

Part 4: Setting up IGV

./igv/build/IGV-dist/igv.sh 

samtools index h1all.bam
samtools index h2all.bam


Part 6: Find and plot differentially methylated regions

Do you expect each region in H1 or H2 to correspond to the same parent of origin (i.e. the same haplotype)? Explain your reasoning.

Answer: No. we assign the names H1 and H2 randomly to assign the two differennnnt chromosomes we distinguish. Phasing requires physical read overlaps can't phase between chromosomes no way to tell if they come form the same parent. 