

Question 1 Coverage simulator

Question 1.1: How many 100bp reads are needed to sequence a 1Mbp genome to 5x coverage? How many are needed for 15x coverage?

1,000,000 X 5 = 5,000,000 / 100 = 50,000 reads required for 5x coverage


1,000,000 x 15 = 15,000,000 / 100 = 150,000 reads required for 15x coverage

Question 1.2: Write a program (in Python) to simulate sequencing 5x coverage of a 1Mbp genome with 100bp reads. Using this array, plot a histogram of the coverage. 

```
for i in range(50000): #size of 
    randstart = np.random.randint(0, 999900) #set possible start and end positions for random reads
    for j in range(randstart, randstart + 100): #random read start and read end = start + 100
        genome[j] += 1 #turn zeros in array into 1's to represent they have been read once
```
Question 1.3: Using your output array of coverages from Q1.2, how much of the genome (e.g., how many base pairs) has not been sequenced (has 0x coverage)? How well does this match Poisson expectations?

I get around 6834 base pairs with 0X coverage. Based on the poisson distribution I would expect that about .005% of the base pairs would have 0X coverage. 6834/1,000,000= .0068% that is close enough. 

Question 1.4: Now repeat the analysis with 15X coverage. Compute the number of bases with 0x coverage, and evaluate how well it matches the Poisson expectation.

I get around 7 base pairs with 0X coverage. This matches well the more reads you do the fewer base pairs with have 0 coverage

Question 2: (created conda envornment called spafes) ~/Downloads/SPAdes-3.15.5-Darwin/bin/spades.py

Question 2.1. How many contigs were produced? 
```
grep -c '>' contigs.fasta
4 contigs were produces 
```

Question 2.2: What is the total length of the contigs?
```
grep '>' contigs.fasta #this prints header lines which tells you the length of the contigs

>NODE_1_length_105830_cov_20.649193
>NODE_2_length_47860_cov_20.367392
>NODE_3_length_41351_cov_20.528098
>NODE_4_length_39426_cov_20.336388
```

Question 2.3. What is the size of your largest contig?

Using the output from 2.2 I can see that the length of the longest contig is 105,830

Question 2.4. What is the contig N50 size?
To answer this I added up the length of the contigs to get total length and divided by two to find where N50 would be and determined which contig that point was contained in. 

105,830 + 47,860 + 41,351 + 39,426 = 234,467/2 = 117,233 -> this point lies within the second contig which has a length of 47,860 bp.

Question 3.1. What is the average identify of your assembly compared to the reference?

Avg Identity = 99.98

Question 3.2. What is the length of the longest alignment

207,000 in assembly 

207007 in reference 

(length 1 is length is reference length 2 is length is assembly)

Question 3.3. How many insertions and deletions are in the assembly? *** go over this 

1 insertion for an average nubmer of 712 base pairs and 14 deletiions (got nubmer of deletions by subtracting 1 from the number of indels because indels can be insertions or deletions). ****what does GINDEL mean what is the actual number 

Question 4.1. What is the position of the insertion in your assembly? Provide the corresponding position in the reference. **ask steph about this 

The position is 26788-27497. there is a gap in our scaffold the first alignment goes from 1-26787 and then 27498-234497. Have to adjust by one because that number is still part of the alignment. 


Question 4.2. How long is the novel insertion? 

The novel insertion is 26787-27498 = 711 base pairs long 

Question 4.4. What is the DNA sequence of the encoded message?
```
samtools faidx ~/qbb2022-answers/week1-homework/asm/asm/scaffolds.fasta NODE_1_length_234497_cov_20.506978:26788-27499 > NODE_1_length_234497_cov_20.506978:26788-27499 #this pulls out inserted region

```

python dna-decode.py -d --input NODE_1_length_234497_cov_20.506978\:26788-27499

Message: Congratulations to the 2022 CMDB @ JHU class!  Keep on looking for little green aliens...







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