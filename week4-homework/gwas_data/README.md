Step 1:
plink --vcf genotypes.vcf --pca 10 #this outputs first 10 principal components

Step 3:
plink --vcf genotypes.vcf --freq #this gets frequncies #this gives frequency need to make historgram from MAF column

Step 4:
plink --vcf genotypes.vcf --assoc --pheno CB1908_IC50.txt --allow-no-sex --covar plink.eigenvec --linear --out gwasCB1908
plink --vcf genotypes.vcf --assoc --pheno GS451_IC50.txt --allow-no-sex --covar plink.eigenvec --linear --out gwasGS451



Step 5:
Top SNP for CB1908: rs10876043 located on chromosome 12 at position 49190411. TUBA1A is a potential causal gene in the region (~chr12:49184795-49189080). This gene is one of three alpha-tubulin genes in a cluster on chromosome 12. 
Top SNP for GS451: rs7257475 located on chromosome 19 at position 20372113 which is located near a cluster of Zinc Finger protein encoding genes. 


