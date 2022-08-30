# QBB2022 - Day 1 - Lunch Exercises Submission
1. I'm excited to learn python.

2.
b.The mean numnber of exons per gene is 63.24
wc -l exons.chr21.bed #find no. of exons
wc -l genes.chr21.bed #find no. genes
no. exons / no. genes  

c. find nubmer of exons for each gene then sort genes by number of exons and then select the median.

3.
b.(base) [~/qbb2022-answers/day1-lunch $]sort -k 4 -g chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | uniq -f 3 -c
 #sorted by the fourth column numerically and then found number of unique terms skip the first 3 columns and count (sort because uniq needs it to be in order (can also cut out fourth column and then sort and count)
 
 305 chr21	13979679	13980279	1
 678 chr21	14086279	14087079	2
  79 chr21	14520479	14521079	3
 377 chr21	14373279	14378479	4
 808 chr21	10340056	10342056	5
 148 chr21	14487679	14488279	6
1050 chr21	13980279	13980679	7
 156 chr21	10330656	10331656	8
 654 chr21	10118172	10126172	9
  17 chr21	15729281	15729481	10
  17 chr21	14216679	14216879	11
  30 chr21	31559887	31560087	12
  62 chr21	17514282	17514482	13
 228 chr21	14215479	14215679	14
 992 chr21	10003860	10005054	15
 
 c. we would find the toal number of nuelcotides using the start and end positions for each state and nubmer of times it occurs. Then we would find the number of nucleotides in each state and then divide by total number of nucleotides to find the state that encompasses the largest fraction. 
 
 4.
 b.
 (base) [~/qbb2022-answers/day1-lunch $]grep AFR integrated_call_samples.panel | sort -k 2 |cut -f 2 | uniq -c
  123 ACB
  112 ASW
  173 ESN
  180 GWD
  122 LWK
  128 MSL
  206 YRI
  
c. cut superpop aand pop fields and sort those. then count nubmer of unique instances. 

5.
b. cut -f1-9,13 random_snippet.vcf > HG00100.vcf #want lines 1-9 and 13 write to new file
c. 

  
  