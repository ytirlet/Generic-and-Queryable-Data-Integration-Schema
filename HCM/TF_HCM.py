# imports
import pandas as pd

# Dictionnary of gene names and IDs ################################
def get_dict_from_df (key_name, value_name) : 
    file = "gene_names_ID.tsv"
    df = pd.read_csv(file, delimiter='\t')
    result_dict = df.set_index(key_name)[value_name].to_dict()
    return result_dict

dico_genes = get_dict_from_df('gene1_gene_name','gene1_Label')

# Opening and reading result files #################################
xls3 = pd.ExcelFile(PATH_TO_TF_FILE)
dico_sheet3 = pd.read_excel(xls3,sheet_name=None)
names3 = xls3.sheet_names

# CONTROL ##########################################################
C_dist = dico_sheet3[names3[0]]
C_dist.insert(5,'Type',['Distal' for i in range(len(C_dist))])
C_dist.insert(6,'in@Condition',['Control' for i in range(len(C_dist))])

C_prox = dico_sheet3[names3[2]]
C_prox.insert(5,'Type',['Proximal' for i in range(len(C_prox))])
C_prox.insert(6,'in@Condition',['Control' for i in range(len(C_prox))])

# HCM ##############################################################
H_dist = dico_sheet3[names3[1]]
H_dist.insert(5,'Type',['Distal' for i in range(len(H_dist))])
H_dist.insert(6,'in@Condition',['HCM' for i in range(len(H_dist))])

H_prox = dico_sheet3[names3[3]]
H_prox.insert(5,'Type',['Proximal' for i in range(len(H_prox))])
H_prox.insert(6,'in@Condition',['HCM' for i in range(len(H_prox))])

# FETUS ############################################################
F_dist = dico_sheet3[names3[4]]
F_dist.insert(5,'Type',['Distal' for i in range(len(F_dist))])
F_dist.insert(6,'in@Condition',['Fetus' for i in range(len(F_dist))])

F_prox = dico_sheet3[names3[5]]
F_prox.insert(5,'Type',['Proximal' for i in range(len(F_prox))])
F_prox.insert(6,'in@Condition',['Fetus' for i in range(len(F_prox))])

# Concatenation and export ##########################################
TFs = pd.concat([C_dist,H_dist,C_prox,H_prox,F_dist,F_prox],axis=0)
TFs.insert(0,'concerns@gene',['NA' for i in range(len(TFs))])

for i in range(len(TFs)) :
    name = TFs.iat[i,1]
    if name in dico_genes :
        TFs.iat[i,0] = dico_genes[name]
TFs.insert(0,'Enriched Motifs',['TF_' + str(i) for i in range(len(TFs))])

TFs.to_csv(NEW_TF_FILE,sep='\t',index=False)
