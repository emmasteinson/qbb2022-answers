Part 1

What percentage of reads are valid interactions (duplicates do not count as valid)?

dCTCF: 34.7% (92% of 37.8%)
ddCTCF: 32.2% are valid (80% of 36.6%)
   
What constitutes the majority of invalid 3C pairs? What does it actually mean (you may need to dig into the HiC-Pro manual)?

dangling end pairs: error in ligation of restriction enzyme fragments (only see one restriction enzyme site).

Part 2: 
bins = particular area of the genome. score is how many interactions (score). 

Command line arguments for running Hi-C script:
```
python HiCplot.py analysis/hic_results/matrix/dCTCF/iced/6400/dCTCF_ontarget_6400_iced.matrix	 analysis/hic_results/matrix/ddCTCF/iced/6400/ddCTCF_ontarget_6400_iced.matrix analysis/hic_results/matrix/dCTCF/raw/6400/dCTCF_ontarget_6400_abs.bed output
```

Command line arguments for running Hi-C2 script: 
```
./HiCplot2.py matrix/dCTCF_full.40000.matrix matrix/40000_bins.bed output
```
1.Were you able to see the highlighted difference from the original figure?
no I didn't see the highlighted difference. 

2.What impact did sequencing depth have?

it didn't appear to have an affect based on our graphs

3.What does the highlighted signal indicate?

The highlighted signal represents interacting distant TADs (not adjacent TADs).
