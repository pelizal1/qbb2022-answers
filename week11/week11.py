#!/usr/bin/env python

import scanpy as sc
# Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
# Make variable names (in this case the genes) unique
adata.var_names_make_unique()


#unfiltered pca
# sc.tl.pca(adata)
# sc.pl.pca(adata, save='pca_unfil.png')

#filtered pca
sc.pp.recipe_zheng17(adata)
sc.tl.pca(adata)
# sc.pl.pca(adata, save='pca_fil.png')

#neighbors, umap, leiden, umap
sc.pp.neighbors(adata)
sc.tl.umap(adata, maxiter=1000)
sc.tl.leiden(adata)
# sc.pl.umap(adata, color=['leiden'], save='.png')

#tsne plot
# sc.tl.tsne(adata)
# sc.tl.leiden(adata)
# sc.pl.tsne(adata, color=['leiden'], save='.png')

# rank genes - t-test
sc.tl.rank_genes_groups(adata, 'leiden', method='t-test')
sc.pl.rank_genes_groups(adata, save='_ttest.png')

# rank genes - logistical regression
# sc.tl.rank_genes_groups(adata, 'leiden', method='logreg')
# sc.pl.rank_genes_groups(adata, save='_logreg.png')





