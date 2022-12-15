Step 1b
`
./kraken.py SRR492190.kraken SRR492190
./kraken.py SRR492183.kraken SRR492183 
./kraken.py SRR492186.kraken SRR492186
./kraken.py SRR492188.kraken SRR492188
./kraken.py SRR492189.kraken SRR492189
./kraken.py SRR492193.kraken SRR492193
./kraken.py SRR492194.kraken SRR492194
./kraken.py SRR492197.kraken SRR492197
`

Step 1c
`
ktImportText -q *krona.txt  -o kronaout.html
`

Question 1: For the first few days the amount of Staphylococcus epidermis decreases and then begins to increasse in days 5-7. Enterococcus faecalis is consistently present at the largest amounts through the sampling period. s

Step 2:

Question 2: We could use the amount of overlap and sequence similarity. Comparing to reference assembly will also be useful. 

`
bwa index assembly.fasta
`
`
bwa mem -t 4 -o SRR492183.sam ../assembly.fasta SRR492183_1.fastq SRR492183_2.fastq
bwa mem -t 4 -o SRR492186.sam ../assembly.fasta SRR492186_1.fastq SRR492186_2.fastq
bwa mem -t 4 -o SRR492188.sam ../assembly.fasta SRR492188_1.fastq SRR492188_2.fastq
bwa mem -t 4 -o SRR492189.sam ../assembly.fasta SRR492189_1.fastq SRR492189_2.fastq
bwa mem -t 4 -o SRR492190.sam ../assembly.fasta SRR492190_2.fastq SRR492190_2.fastq
bwa mem -t 4 -o SRR492193.sam ../assembly.fasta SRR492193_1.fastq SRR492193_2.fastq
bwa mem -t 4 -o SRR492194.sam ../assembly.fasta SRR492194_1.fastq SRR492194_2.fastq
bwa mem -t 4 -o SRR492197.sam ../assembly.fasta SRR492197_1.fastq SRR492197_2.fastq
`

sort the bam files
`
samtools sort -o SRR492183.bam SRR492183.sam
samtools sort -o SRR492186.bam SRR492186.sam
samtools sort -o SRR492188.bam SRR492188.sam
samtools sort -o SRR492189.bam SRR492189.sam
samtools sort -o SRR492190.bam SRR492190.sam
samtools sort -o SRR492193.bam SRR492193.sam
samtools sort -o SRR492194.bam SRR492194.sam
samtools sort -o SRR492197.bam SRR492197.sam
`
`
jgi_summarize_bam_contig_depths --outputDepth depth.txt *.bam
metabat2 -i ../assembly.fasta -a depth.txt -o bins_dir/bin
`
Question3A:
6 bins (metabat could only confidently identify 6 species from all of the assembled fastas)

Question 3B: 

how many conntigs in our bins =194 total
`
grep ">" bin.1.fa | wc -l     53
grep ">" bin.2.fa | wc -l     78
grep ">" bin.3.fa | wc -l     8 
grep ">" bin.4.fa | wc -l     36    
grep ">" bin.5.fa | wc -l     6
grep ">" bin.6.fa | wc -l     13
`
how many contigs in original assembly =4103
`
grep ">" assembly.fasta | wc -l  
`  

194/4103 = 5%. We could confidently identify 5% of total number of contigs. 

Question 3C:
find the number of bases in each contig and add them all up to find total length of sequences

`
samtools faidx bin.1.fa
samtools faidx bin.2.fa
samtools faidx bin.3.fa
samtools faidx bin.4.fa
samtools faidx bin.5.fa
samtools faidx bin.6.fa
`
`
cut -f 2 bin.1.fa.fai | paste -sd+ - | bc  2693493
cut -f 2 bin.2.fa.fai | paste -sd+ - | bc  2257331
cut -f 2 bin.3.fa.fai | paste -sd+ - | bc  1656034
cut -f 2 bin.4.fa.fai | paste -sd+ - | bc  1224069
cut -f 2 bin.5.fa.fai | paste -sd+ - | bc  2862852
cut -f 2 bin.6.fa.fai | paste -sd+ - | bc  2483660
`
`
Normally around 5 million base pairs so we assembled about half the genome for each bacteria. That seems about right. 
`


Question 3D: 
I would take the reference genome for the bacteria and compare it to our suquences to get an idea of how complete or contaminated our sequenced samples are. 

Part 3:
Question 4A: bin1 = Staphylococcus aureus, bin2 = Staphylococcus epidermins, bin3 = Anaerococcus pervotili, bin4 = staphylococcus  haemolyticus, bin5 = enterococcus faecalis, bin6 = cutibacterium avidum

Question 4B: If a bind isn't more than 70% one species I wouldn't classify it. set a threshold. require percent match of you bind to one species in the reference genome and a lesser percent match to other species in the reference genome. 


