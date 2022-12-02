#!/usr/bin/env python

import pandas as pd
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
# adata.write(results_file)
# sc.pl.rank_genes_groups(adata, save='_ttest.png')

# rank genes - logistical regression
# sc.tl.rank_genes_groups(adata, 'leiden', method='logreg')
# sc.pl.rank_genes_groups(adata, save='_logreg.png')

# marker genes
marker_genes = ['Igfbpl1', 'Tsc22d1', 'Basp1', 'Nrxn3', 'Gria2', 'Fabp7', 'Dbi', 'Tuba1a', 'Mdk', 'Eomes', 'Stmn2']
# marker_genes = ['Sfrp2', 'Nodal', 'Ccl24', 'Mgl2', 'Gdpd2', 'Wnt7b', 'Opalin', 'Gjb1', 'Asgr1', 'Agtr2', 'Cytl1', 'Hbb-y']
pd.DataFrame(adata.uns['rank_genes_groups']['names']).head(5)

new_cluster_names = [
    'pericytes',
    'microglia',
    'other2',
    'other3',
    'other4',
    'other5',
    'other6',
    'other7',
    'vasular fibroblast-like cells',
    'other9',
    'other10',
    'other11',
    'astrocytes',
    'arterial endothelial cells',
    'other14',
    'other15',
    'other16',
    'other17',
    'other18',
    'other19',
    'other20',
    'other21',
    'other22',
    'other23',
    'oligodendrocyte',
    'other25',
    'other26',
    'other27',
    'other28'
]
adata.rename_categories('leiden', new_cluster_names)

result = adata.uns['rank_genes_groups']
groups = result['names'].dtype.names
pd.DataFrame(
    {group + '_' + key[:1]: result[key][group]
    for group in groups for key in ['names', 'pvals']}).head(5)

sc.pl.dotplot(adata, marker_genes, groupby='leiden', save=".png")
sc.pl.umap(adata, color='leiden', legend_loc='on data', title='Labeled UMAP', frameon=False, save='_labeled.png')






