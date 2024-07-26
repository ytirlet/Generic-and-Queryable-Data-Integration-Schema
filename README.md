# Generic-and-Queryable-Data-Integration-Schema

## Description
Here are the scripts we created to process the results data in our article "Generic and Queryable Data Integration Schema for Transcriptomics and Epigenomics studies".
We used datasets from 2 recent articles: one about human health (HCM) and the other about insects cast differentiation (HoneyBee).

## HCM Use-case
Dataset from the following article : "Integrative analysis of transcriptome, DNA methylome and chromatin accessibility reveals candidate therapeutic targets in hypertrophic cardiomyopathy" published in 2024 by Gao et al.

#### DEGs_HCM.py
Python file processing the data about differentially expressed genes

#### DMR_HCM.py
Python file processing the data about differentially methylated regions

#### TF_HCM.py
Python file processing the data about Transcription Factors and their binding sites

#### gene_names_ID.tsv
Necessary table, created to have the corresponding names and IDs of each gene. Used in TF_HCM.py to create a dictionnary.

#### sparql_genename.rq
SPARQL query used to create the gene_names_ID.tsv table.


## HoneyBee Use-case
Dataset from the following article : "The diverging epigenomic landscapes of honeybee queens and workers revealed by multiomic sequencing" published in 2023 by Zhang et al.

#### ATAC_HBee.py
Python file processing the data about ATAC peaks

#### Chip_HBee.py
Python file processing the data about Chip peaks

#### DEGs_HBee.py
Python file processing the data about differentially expressed genes, lncRNA and co-differentially expressed genes.

#### KEGG_HBee.py
Python file processing the data about KEGG enrichments

#### TF_positions_HBee.py
Python file processing the data about Transcription Factors and their binding sites

#### gene_positions.tsv
Necessary table, created to have the gene positions of ech gene concerned by a TF binding site. Used in TF_positions_HBee.py to create a dictionnary.

#### sparql_geneposition.rq
SPARQL query used to create the gene_positions.tsv table.


