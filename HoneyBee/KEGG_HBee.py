# imports
import pandas as pd

# Opening and reading result files #################################
xls1 = pd.ExcelFile(PATH_TO_KEGG_FILE)
dico_sheet1 = pd.read_excel(xls1,sheet_name=None)

names1 = xls1.sheet_names

enrich2 = dico_sheet1[names1[4]]
enrich4 = dico_sheet1[names1[5]]

cols = [0,1,4,5,7]

# Enrichments - 2 Days #############################################
enrich2 = enrich2[enrich2.columns[cols]]
enrich2.insert(5,'measured_in@Contrast',['2Qvs2W' for i in range(len(enrich2))])

# enrichment - 4 Days ##############################################
enrich4 = enrich4[enrich4.columns[cols]]
enrich4.insert(5,'measured_in@Contrast',['4Qvs4W' for i in range(len(enrich4))])

# Concatenation ####################################################
enrich = pd.concat([enrich2,enrich4],axis=0)

# Spliting the multiple gene associations in different lines #######
lines_to_add = []
for i in range(len(enrich)) :
    line = [enrich.iat[i,0],enrich.iat[i,1],enrich.iat[i,2],enrich.iat[i,3],enrich.iat[i,5]]
    gene_list = enrich.iat[i,4].split("/")
    for j in range(len(gene_list)) :
        new_line = line + ["gene-" + gene_list[j]]
        lines_to_add.append(new_line)

# Creation of the final dataframe ###################################
df = pd.DataFrame(lines_to_add, columns =['KEGG_ID','Description','pvalue','padj','enriched_in@Contrast','concerns@gene'])
df.insert(0,'KEGG_enrichment',['KEGG_enr_' + str(i) for i in range(len(df))])

# Export ############################################################
df.to_csv(NEW_KEGG_FILE,sep='\t',index=False)

