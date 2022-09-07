#!/usr/bin/env python

import vcfParser
kgp = vcfParser.parse_vcf("random_snippet.vcf") #read in random snippet
dbsnp = vcfParser.parse_vcf("dbSNP_snippet.vcf") #read in dbSNP.vcf
#print(dbsnp)

dbsnp_dict = {} #make dictionary 

#for every SNP in dbSNP list we want to add that SNP to the dictionary
dbsnp_dict = {}
for snp in dbsnp: #for every snp in dbsnp list
    #print(snp)
    #dict_name[key] = value -> this is how you add stuff to a dictionary
   chrom = snp[0] #pulls out chrom
   pos = snp [1] #pos
   newkey = (chrom, pos) #this is key
   
   newvalue = snp[2] #gives value which is snpID
   dbsnp_dict[newkey] = newvalue #add that SNP (key and value) to the dictionary 
#print(dbsnp_dict)

#look up random_SNP in the dbSNP dicionary using their chromosome and postition. We cant to match each SNP to dbSNP ID
no_id_counter = 0 #need to initialize outside the for loop will reset every time if not outside
for snp in kgp: #need to look through every SNp in kgp
    #snp looks like this: ['chr21', 38222409, '.', 'A', 'G', '.', 'PASS', {'AC': 3, 'AN': 5096, 'DP': 17862, 'AF': 0.0, 'EAS_AF': 0.0, 'EUR_AF': 0.0, 'AFR_AF': 0.0, 'AMR_AF': 0.0, 'SAS_AF': 0.0, 'VT': 'SNP', 'NS': 2548},
    
    chrom = snp[0]
    pos = snp[1]
    query_key = (chrom, pos) #query key to look in dbSNP dictionary
    #look for SNP in dbsnp_dict, we have to create query key that looks like (chrom, pos)
    if query_key in dbsnp_dict: #if this is true we want to extract assocaited valie
        #dict_name[key] -> how you extract assocaited value
        id_of_interest = dbsnp_dict[query_key]
    #report the number of random_snippet snps that don't have an ID
    else: 
        #increment a counter variable that stores how many SNP's don't have an ID
        no_id_counter += 1
print(no_id_counter) #will print out the number of snps with no id
    
    
    
    
    #get SNP chromosome and position
    #print(snp)
    #look for SNP in dbsnp_dict
    #if SNP in dictionary, get ID
    # report the number of random_snippet snps that don't have an ID


#need to look through every SNP in 


#dictionary entry: { key : value}
#for every dictionary entry should have: key  is chrom + position and value is ID
#key1: (chrom, pos) -> ("chr21, 90230) tuple basically a list
#key2: "chrom_pos" -> "chr21_90233333" store as string
#{("chr21", 9018392) : 'rs13w234' }



#want to create a dictionary to store the dbSNP information 
#and then look up random_snippet SNPs in the dbSNP dictoinary using their chromosomme and positions 
#we want to match each SNP to a dbSNP ID