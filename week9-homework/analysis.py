#!/usr/bin/env python
import numpy as np
import numpy.lib.recfunctions as rfn
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm
from scipy import stats
from statsmodels.stats import multitest

input_arr = np.genfromtxt("dros_gene_expression.csv", delimiter=',', names=True, dtype=None, encoding='utf-8')

col_names = list(input_arr.dtype.names)
row_names = input_arr[col_names[0]]
fpkm_values = input_arr[col_names[1:]]
stage_names = col_names[1:]

#pull out row names

fpkm_values_2d = rfn.structured_to_unstructured(fpkm_values, dtype=float)

median = np.median(fpkm_values_2d, axis=1) 
   
new_array = fpkm_values_2d[np.where(median > 0)]
final_array = np.log2(new_array + .1)
#print(final_array)


# cluster based on genes
Z1 = linkage(final_array)
idx1 = leaves_list(Z1)

# cluster based on samples
Z2 = linkage(final_array.T)
idx2 = leaves_list(Z2)

# reorder data matrix based on gene and sample clustering
D = final_array[idx1,:]
D = D[:,idx2]

#plot heatmap
fig, ax = plt.subplots()
plt.imshow(D, interpolation = "nearest", aspect = "auto", cmap="YlGnBu")
ax.set_xticks(np.arange(len(stage_names)))
ax.set_xticklabels(np.array(stage_names)[idx2], rotation=90)
plt.colorbar()
plt.tight_layout()
plt.savefig("heatmap.png")
plt.close()

# plot dendrogram
fig,ax = plt.subplots()
dendrogram(Z2, distance_sort = "ascending", labels = stage_names, leaf_rotation = 45)
plt.tight_layout()
plt.savefig("dendrogram.png")
plt.close()

#make data table for fpkm, stage and sex
pvals = []
betas = []
for row in range(final_array.shape[0]):

    list_of_tuples = []
    for i in range(len(stage_names)):
        fpkm = final_array[row, i]
        name = stage_names[i]
        name_split = name.split("_")
        stage = name_split[1]
        sex = name_split[0]
        list_of_tuples.append((fpkm, stage, sex))
    longdf = np.array(list_of_tuples, dtype=[('fpkm', float), ('stage', int), ('sex', 'S6')])
    #print(longdf)
    fit = smf.ols("fpkm ~ stage", data = longdf).fit()
    #print(fit.summary())
    #pull out pvalue and beta for each
    pvals.append(fit.pvalues["stage"]) #spits out pvalue
    betas.append(fit.params["stage"]) #spits out beta 
    
#make qq plots to compare to thepretical values deviaate from horizontal line something is happening in the data
# qqplot using uniform distribution as comparison
# under null hypothesis, significant pvalues occur completely by chance
# so they should be uniformly distributed, with 5% significant by chance

fig, ax = plt.subplots()
sm.qqplot(np.array(pvals), dist = stats.uniform, line='45')
plt.tight_layout()
plt.savefig("qqplot.png")
plt.close()

#10%flase discovery rate
fdr = multitest.multipletests(pvals, alpha = 0.1, method = "fdr_bh")
#print(fdr)
#value is false can't reject null can't say something significant is happening want to pull out all genes that have TRUE after FDR
boollist = fdr[0]
new_row = row_names[median > 0] #gives all rows in final array
sig_transcripts = new_row[boollist]
#print(sig_transcripts)

#now need to do with sex as a covariate
#make data table for fpkm, stage and sex
pvalssex = []
betassex = []
for row in range(final_array.shape[0]):

    list_of_tuples = []
    for i in range(len(stage_names)):
        fpkm = final_array[row, i]
        name = stage_names[i]
        name_split = name.split("_")
        stage = name_split[1]
        sex = name_split[0]
        list_of_tuples.append((fpkm, stage, sex))
    longdf = np.array(list_of_tuples, dtype=[('fpkm', float), ('stage', int), ('sex', 'S6')])
    #print(longdf)
    fit = smf.ols("fpkm ~ stage + sex", data = longdf).fit() #sex as covariate
    #print(fit.summary())
    #pull out pvalue and beta for each
    pvalssex.append(fit.pvalues["stage"]) #spits out pvalue
    betassex.append(fit.params["stage"]) #spits out beta 

#10%flase discovery rate
fdrsex = multitest.multipletests(pvalssex, alpha = 0.1, method = "fdr_bh")
#print(fdr)
#value is false can't reject null can't say something significant is happening want to pull out all genes that have TRUE after FDR
boollistsex = fdrsex[0]
new_row = row_names[median > 0] #gives all rows in final array
sig_transcriptssex = new_row[boollistsex]
#print(sig_transcriptssex)

#find percent overlap
overlap = set(sig_transcripts) & set(sig_transcriptssex)
percent_overlap = len(overlap) / len(sig_transcripts) * 100
print(percent_overlap)


#Volcano plot (by stage with sex as covariate)
color = []
for item in boollistsex:
	if item == True:
		color.append("red")
	else:
		color.append("black")


fig, ax = plt.subplots()
ax.scatter(betassex, -np.log10(pvalssex), color = color)
ax.set_xlabel("betas")
ax.set_ylabel("pvals")
ax.set_title("FDR by stage with sex as covariate")

fig.savefig("volcanoplot.png")


    






