#QBB day 3 homework
1.
plink --vcf ALL.chr21.shapeit2_integrated_v1a.GRCh38.20181129.phased.vcf.gz --pca 3 

-performs PCA with PLINK and returns first 3 principal components.

2. Do you notice any structure among the points? What do you think this structure represents?
Answer: there appears to be a few main clusters-maybe there is a correlation between geographic region the sample are from and the presence of certain SNPs.

3. 
join <(sort plink.eigenvec) <(sort integrated_call_samples.panel) > joined_file.txt #makes joined file from terminal with pca values and pop, superpop, gender

