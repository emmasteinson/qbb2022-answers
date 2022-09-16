

Question 1 Coverage simulator

Question 1.1: How many 100bp reads are needed to sequence a 1Mbp genome to 5x coverage? How many are needed for 15x coverage?

1,000,000 X 5 = 5,000,000 / 100 = 50,000 reads required for 5x coverage


1,000,000 x 15 = 15,000,000 / 100 = 150,000 reads required for 15x coverage

Question 1.2: Write a program (in Python) to simulate sequencing 5x coverage of a 1Mbp genome with 100bp reads. Using this array, plot a histogram of the coverage. 

Question 1.3: Using your output array of coverages from Q1.2, how much of the genome (e.g., how many base pairs) has not been sequenced (has 0x coverage)? How well does this match Poisson expectations?

```
v = np.array(genome)
zeros = np.where(v==0)
print(len(zeros[0]))

```

I get around 6834 base pairs with 0X coverage. Based on the poisson distribution I would expect that about .005% of the base pairs would have 0X coverage. 6834/1,000,000= .0068% that is close enough. 

Question 1.4: Now repeat the analysis with 15X coverage. Compute the number of bases with 0x coverage, and evaluate how well it matches the Poisson expectation.

```
v = np.array(genome)
zeros = np.where(v==0)
print(len(zeros[0]))

```

I get around 7 base pairs with 0X coverage. This matches well the more reads you do the fewer base pairs with have 0X coverage. Based on the poisson distribution I would expect very close to 0% to have 0X coverage and 7/1,000,000 is very close to 0%.


Question 2.1. How many contigs were produced? 
```
grep -c '>' contigs.fasta
```
4 contigs were produces 


Question 2.2: What is the total length of the contigs? 
```
grep '>' contigs.fasta #this prints header lines which tells you the length of the contigs

>NODE_1_length_105830_cov_20.649193
>NODE_2_length_47860_cov_20.367392
>NODE_3_length_41351_cov_20.528098
>NODE_4_length_39426_cov_20.336388
```
Total length is 234,467 bp 

Question 2.3. What is the size of your largest contig?

Using the output from 2.2 I can see that the length of the longest contig is 105,830 base pairs.

Question 2.4. What is the contig N50 size?

The N50 contig size is 47,860 bp. This is the length of the shortest contig for which longer and equal contigs cover atlesat 50% of genome (lined up contigs by length N50 is the contig that gets you to 50% coverage of the genome) 

105,830 + 47,860 + 41,351 + 39,426 = 234,467/2 = 117,233 -> second largest contig (Node 2) gets you to this point. 


Questions 3 Note: I did alignment with scaffolds.fasta instead of contigs.fasta.

Question 3.1. What is the average identify of your assembly compared to the reference?

```
less -S out.report
```

Avg Identity = 99.98 

Question 3.2. What is the length of the longest alignment

```
show-coords out.delta
```

207,000 in assembly 

207007 in reference 


Question 3.3. How many insertions and deletions are in the assembly? 

```
less -S out.report
```
Looked at insertions column said there were 2 for reference and 1 for qry. Insertions in the reference are really deletions in the assemby (two places with base pairs that are in the reference that are not found in the assembly). There is one insertion and two deletions in the assembly. **maybe change this wording


Question 4.1. What is the position of the insertion in your assembly? Provide the corresponding position in the reference. 

```
show-coords out.delta
```

The position is 26788-27497. Scaffold assembly jumps from 26787 to 27498.  


Question 4.2. How long is the novel insertion? 

The novel insertion is 26787-27498 = 711 base pairs long 

Question 4.4. What is the DNA sequence of the encoded message?
```
samtools faidx ~/qbb2022-answers/week1-homework/asm/asm/scaffolds.fasta NODE_1_length_234497_cov_20.506978:26788-27499 > NODE_1_length_234497_cov_20.506978:26788-27499 #this pulls out inserted region


python dna-decode.py -d --input NODE_1_length_234497_cov_20.506978\:26788-27499 #this runs 

Message: Congratulations to the 2022 CMDB @ JHU class!  Keep on looking for little green aliens...
```






Notes: 
care about coverage over 1M bp genome. effectively throwing darts at board (random number generator) simulated start of read. we know reads are 100 bases long. first reads starts as all zeros (0 signifies no reads yet). get a read turns into 1's. after throwing enough darts get new vector with coverage of what we have at each position. just keeping track of what coverage will be. this will give 1 mil points want to turn into histogram. 

logical process is initilalize to zeros 
for loop for number of reads we want throw dart (need random number)
increment next 100 slots

for(number reads)
pick random nubmer
for(100)
increment cov[pos] = cov[pos] + 1

q 2,3,4

aligner tell you wehre alignment is need to look at coordinates in between where there isn't alignment 

less contigs you have more resolution you have

#fasta are scaffolds
samtools faidx deals with fasta files summarizes informatin about all of the contigs. spits of re.fa.fai gives files iwht general information about fasta file 

we did denovo assembly with spades. also have ref genome take denovo assembly and compare to reference genome suing MUMER. 

contigs are first step-> scaffolds are contigs put together (qry). #record that i suced scaffolds instread of contigs