# imports
import pandas as pd

# Opening and reading result files #################################
xls1 = pd.ExcelFile(PATH_TO_DEG_FILE)
dico_sheet1 = pd.read_excel(xls1,sheet_name=None)

names1 = xls1.sheet_names

Deg_UP2 = dico_sheet1[names1[0]]
Deg_DOWN2 = dico_sheet1[names1[1]]
Deg_UP4 = dico_sheet1[names1[2]]
Deg_DOWN4 = dico_sheet1[names1[3]]

cols = [12,9,10,11,18]

# Up-DEGs 2 Days ####################################################
Deg_UP2 = Deg_UP2[Deg_UP2.columns[cols]]
Deg_UP2.insert(5,'measured_in@Contrast',['2Qvs2W' for i in range(len(Deg_UP2))])
Deg_UP2.insert(6,'Expression',['UP' for i in range(len(Deg_UP2))])

# Down-DEGs 2 Days ##################################################
Deg_DOWN2 = Deg_DOWN2[Deg_DOWN2.columns[cols]]
Deg_DOWN2.insert(5,'measured_in@Contrast',['2Qvs2W' for i in range(len(Deg_DOWN2))])
Deg_DOWN2.insert(6,'Expression',['DOWN' for i in range(len(Deg_DOWN2))])

# Up-DEGs 4 Days ####################################################
Deg_UP4 = Deg_UP4[Deg_UP4.columns[cols]]
Deg_UP4.insert(5,'measured_in@Contrast',['4Qvs4W' for i in range(len(Deg_UP4))])
Deg_UP4.insert(6,'Expression',['UP' for i in range(len(Deg_UP4))])

# Down-DEGs 4 Days ##################################################
Deg_DOWN4 = Deg_DOWN4[Deg_DOWN4.columns[cols]]
Deg_DOWN4.insert(5,'measured_in@Contrast',['4Qvs4W' for i in range(len(Deg_DOWN4))])
Deg_DOWN4.insert(6,'Expression',['DOWN' for i in range(len(Deg_DOWN4))])

# Concatenation and export ##########################################
DEGs = pd.concat([Deg_UP2,Deg_DOWN2,Deg_UP4,Deg_DOWN4],axis=0)
DEGs.insert(0,'Differential Expression',['DEG_' + str(i) for i in range(len(DEGs))])
DEGs = DEGs.rename(columns={'gene_name':'measured_in@gene'})

DEGs.to_csv(NEW_DEG_FILE,sep='\t',index=False)
