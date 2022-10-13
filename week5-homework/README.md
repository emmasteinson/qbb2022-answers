Step 1:
```
samtools view -b -e "mapq >= 10" D2_Sox2_R1.bam > D2_Sox2_R1_filt

samtools view -b -e "mapq >= 10" D2_Sox2_R1_input.bam > D2_Sox2_R1_input_filt


samtools view -b -e "mapq >= 10" D2_Sox2_R2.bam > D2_Sox2_R2_filt

samtools view -b -e "mapq >= 10" D2_Sox2_R2_input.bam > D2_Sox2_R2_input_filt
```
Step 2: 

```
macs2 callpeak -t D2_Sox2_R1_filt -c D2_Sox2_R1_input_filt -f BAM -B -g 8.7e7 --outdir Sox2_R1 #these call the peaks outputs files with region of genome where peaks are
macs2 callpeak -t D2_Sox2_R2_filt -c D2_Sox2_R2_input_filt -f BAM -B -g 8.7e7 --outdir Sox2_R2
```
Step 3: 
```
bedtools intersect -a Sox2_R1/NA_peaks.narrowPeak -b Sox2_R2/NA_peaks.narrowPeak > commonpeaks.bed #two replicates intersect peak calls from two peak calls
```
Step 4: Colocalization of Sox2 and Klf4 #find places in genome where both of these TFs are binding

```
bedtools intersect -a D2_Klf4_peaks.bed -b commonpeaks.bed > D2_Sox2_peaks.bed
```
Colocalization: 
```
wc -l D2_Sox2_peaks.bed = 40. there are 40 overlapping peaks with Sox2
wc -l D2_Klf4_peaks.bed = 60. there are 60 total peaks for K1f4
```

66.6% of peaks colocalize with Sox2

Step 5:
Scale:
```
python scale_bdg.py D0_H3K27ac_treat.bdg D0_H3k27ac_scale.bdg
python scale_bdg.py D2_H3K27ac_treat.bdg D2_H3K27ac_scale.bdg
python scale_bdg.py D2_Klf4_treat.bdg D2_Klf4_scale.bdg
python scale_bdg.py NA_treat_pileup.bdg Sox2_scale.bdg
```
Crop:
```
awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }'  D0_H3k27ac_scale.bdg > D0_H3k27ac_scalecrop.bdg
 
awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }'  D2_H3K27ac_scale.bdg > D2_H3K27ac_scalecrop.bdg

awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }'  D2_Klf4_scale.bdg > D2_Klf4_scalecrop.bdg

awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }'  Sox2_scale.bdg > Sox2_scalecrop.bdg
```

Part 2:
1&2.
```
sort -n -r -k 5 commonpeaks.bed | head -300 > 300peaks.bed
```
3.
```
awk '{ printf "%s:%i-%i\n", $1, $2, $3 }' 300peaks.bed > new300peaks.bed
```
4.
```
samtools faidx mm10.fa -r new300peaks.bed -o peakseq.fa
```
5.
```
meme-chip -maxw 7 peakseq.fa
```
Part 3:
2.
```
tomtom memechip_out/combined.meme motif_databases/MOUSE/HOCOMOCOv11_full_MOUSE_mono_meme_format.meme
```
4.
```
grep KLF4 tomtom.tsv > tomtomklf4.tsv
grep SOX2 tomtom.tsv > tomtomsox2.tsv
```

Submission:
intersecting peaks file = D2_Sox2_peaks.bed