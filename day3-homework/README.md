#QBB day 3 homework
Exercise 1
```
plink --vcf ALL.chr21.shapeit2_integrated_v1a.GRCh38.20181129.phased.vcf.gz --pca 3 
```

--This command line  code performs PCA with PLINK and returns first 3 principal components.

Exercise 2

code to generate PCA graphs uploaded as: pca_plot.py

Do you notice any structure among the points? What do you think this structure represents?

Answer: there appears to be a few main clusters-maybe there is a correlation between geographic region the sample are from and the presence of certain SNPs.



Exercise 3 
```
join <(sort plink.eigenvec) <(sort integrated_call_samples.panel) > joined_file.txt 
```
--This command line code makes joined file from terminal with pca values and pop, superpop, gender. 

code to generate plots uploaded as: exercise3_script.py

observation from superpop plot: non african populations seperating from african. african american have mixed ancestry with european which is why you see that stratification 
