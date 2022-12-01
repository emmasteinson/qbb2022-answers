#!/usr/bin/env python

import scanpy as sc
import matplotlib.pyplot as plt


# Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
# Make variable names (in this case the genes) unique
adata.var_names_make_unique()

#make unfiltered PCA plot
sc.tl.pca(adata, svd_solver='arpack')
sc.pl.pca(adata, save = '.png')

#make filtered PCA plot
sc.pp.recipe_zheng17(adata, n_top_genes = 1000, log = True, plot = False, copy = False)
sc.tl.pca(adata, svd_solver='arpack')
sc.pl.pca(adata, save = '-afterfilter.png' )

#clustering
sc.pp.neighbors(adata, n_neighbors=10, n_pcs=40)
sc.tl.leiden(adata)
sc.tl.umap(adata, maxiter=1000)
sc.pl.umap(adata, save = 'umap.png')
sc.tl.tsne(adata)
sc.pl.tsne(adata, save='tsne.png', show = False)

#step 3 distinguishing genes
sc.tl.rank_genes_groups(adata, 'leiden', method='t-test')
sc.pl.rank_genes_groups(adata, n_genes=25, sharey=False, save = 'ttest.png')
#sc.pl.pca(adata, save='t-test.png')
sc.tl.rank_genes_groups(adata, 'leiden', method='logreg')
sc.pl.rank_genes_groups(adata, n_genes=25, sharey=False, save = 'logreg.png', show = False)
#sc.pl.pca(adata, save='logreg.png')

# figure out of my gene of interest is in the dataset 
genes = adata.var.gene_ids.index
candidates = ['Sox17', 'Sst', 'Slc1a3', "Mbp1", "Olig1", "Olig2", "Sal1", "Hexb", "Pax6", "Gad1", "Gad2"]
present = [x for x in candidates if x in genes]
print(present)

#plots that label my genes of interest in the data set on the overall tsne (help identify cluster IDs)
sc.pl.tsne(adata, color=['Sox17', 'Sst', 'Slc1a3', 'Olig1', 'Olig2', 'Hexb', 'Pax6', 'Gad1', 'Gad2'], save = 'clustersgenes.png', show = False)
sc.pl.tsne(adata, color="leiden", save = 'clusersleiden.png' , show = False)

#Part 4
# create a dictionary to map cluster to annotation label
cluster2annotation = {
    "0": "",
    "1": "",
    "2": "",
    "3": "",
    "4": "",
    "5": "",
    "6": "Bergmann Glia",
    "7": "Astrocytes",
    "8": "",
    "9": "",
    "10": "",
    "11": "",
    "12": "",
    "13": "",
    "14": "",
    "15": "",
    "16": "",
    "17": "Radial Glia",
    "18": "",
    "19": "",
    "20": "Oligodendrocyte Progenitor Cell",
    "21": "Oligodendrocyte",
    "22": "",
    "23": "",
    "24": "",
    "25": "Microglia",
    "26": "",
    "27": ""
}
# add a new `.obs` column called `cell type` by mapping clusters to annotation using pandas `map` function
adata.obs['cell type'] = adata.obs['leiden'].map(cluster2annotation).astype('category')

# tsne plot
sc.pl.tsne(adata, color='cell type', legend_loc='on data',
	save="_labeled.png", show = False)








