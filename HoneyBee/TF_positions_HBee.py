# imports
import pandas as pd

# Opening and reading result files #################################
df1 = pd.read_csv("/home/ytirlet/Documents/honeybee/integr/result.tsv",sep="\t")
df2 = pd.read_csv("/home/ytirlet/Documents/honeybee/integr/Atf1_FT.txt",sep="\t")

# Creating a dictionnary of gene positions #########################
dico_posi = {}

for i in range(len(df1)) :
    chro = df1.iat[i,3]
    start = df1.iat[i,1] + df1.iat[i,5]
    end = start + 10
    dico_posi[df1.iat[i,4]] = [chro,start,end]

# Changing offsets into genomic positions ##########################
df2.insert(7,"Reference",['NA' for i in range(len(df2))])
df2.insert(8,"start",['NA' for i in range(len(df2))])
df2.insert(9,"end",['NA' for i in range(len(df2))])
list_index = []
for i in range(len(df2)) :
    if df2.iat[i,0] in dico_posi :
        list_posi = dico_posi[df2.iat[i,0]]
        df2.iat[i,7] = list_posi[0]
        df2.iat[i,8] = list_posi[1]
        df2.iat[i,9] = list_posi[2]
    else :
        list_index.append(i)

df2 = df2.drop(df2.index[list_index])

# Export ###########################################################
df2.to_csv("/home/ytirlet/Documents/honeybee/integr/ATF1.tsv",sep='\t',index=False)


