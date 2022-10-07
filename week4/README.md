# QBB 2022 - Week 4 - Homework Exercises

===1
plink --pca 10 --vcf genotypes.vcf

===3
plink --pca 10 --freq --vcf genotypes.vcf

===4
plink --allow-no-sex --covar plink.eigenvec --hide-covar --linear --pheno CB1908_IC50.txt --out CB1908_IC50/phenotype_gwas_CB1908_IC50 --vcf genotypes.vcf

--covar
give eigenvec from pca

--allow-no-sex

--vcf
vcf file

--pheno
phenotype file

--out

want association_analysis.txt.assoc.linear for analysis

plink --allow-no-sex --covar plink.eigenvec --hide-covar --linear --pheno GS451_IC50.txt --out GS451_IC50/phenotype_gwas_GS451_IC50 --vcf genotypes.vcf