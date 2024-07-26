# imports
import pandas as pd

# Opening and reading result files #################################
xls1 = pd.ExcelFile(PATH_TO_ATAC_FILE_2DAYS)
dico_sheet1 = pd.read_excel(xls1,sheet_name=None)
xls2 = pd.ExcelFile(PATH_TO_ATAC_FILE_4DAYS)
dico_sheet2 = pd.read_excel(xls2,sheet_name=None)

names1 = xls1.sheet_names
names2 = xls2.sheet_names

At_2Q = dico_sheet1[names1[0]]
At_2W = dico_sheet1[names1[1]]
At_4Q = dico_sheet2[names2[0]]
At_4W = dico_sheet2[names2[1]]

cols = [0,1,2,22,23,24,31,38,39]

# Queens - 2 Days ##################################################
At_2Q = At_2Q[At_2Q.columns[cols]]
At_2Q.insert(9,'measured_in@Condition',['2Q' for i in range(len(At_2Q))])

# Workers - 2 Days #################################################
At_2W = At_2W[At_2W.columns[cols]]
At_2W.insert(9,'measured_in@Condition',['2W' for i in range(len(At_2W))])

# Queens - 4 Days ##################################################
At_4Q = At_4Q[At_4Q.columns[cols]]
At_4Q.insert(9,'measured_in@Condition',['4Q' for i in range(len(At_4Q))])

# Workers - 4 Days #################################################
At_4W = At_4W[At_4W.columns[cols]]
At_4W.insert(9,'measured_in@Condition',['4W' for i in range(len(At_4W))])


# Concatenation and export ##########################################
Atac = pd.concat([At_2Q,At_2W,At_4Q,At_4W],axis=0)
Atac.insert(0,'Atac peak',['Atac_' + str(i) for i in range(len(Atac))])

for i in range(len(Atac)) :
    if "(" in Atac.iat[i,7] :
        Atac.iat[i,7] = Atac.iat[i,7].split(' (')[0]

Atac.to_csv(NEW_ATAC_FILE,sep='\t',index=False)
