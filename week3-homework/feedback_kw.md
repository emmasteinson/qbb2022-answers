# Week 3 Variant Calling -- Feedback

1 + 1 + 1 + 0.75 + 1 + 1 + 1 + 1 + 1 + 1 = 9.75 points out of 10 possible points

1. Index genome

  * good --> +1

2. align reads

  * great --> +1

3. sort bam files and index sorted bam files (0.5 points each)

  * good; consider using just one for loop for questions 2 and 3 --> +1

4. variant call with freebayes

  * want to use the `-p` argument to specify the ploidy of the yeast (1)
  * --> +0.75

5. filter variants

  * --> +1

6. decompose complex haplotypes

  * --> +1

7. variant effect prediction

  * --> +1

8. python plotting script

  * great script! --> +1
  * fascinating way to get the unique and count values for the variant effect annotations! Really like the `set` approach. Also consider the [numpy function `unique`](https://numpy.org/doc/stable/reference/generated/numpy.unique.html) which will return the unique values and the corresponding counts for you if you use the the `return_counts` argument

9. 4 panel plot (0.25 points each panel)

  * great! --> +1

10. 1000 line vcf

  * --> +1
