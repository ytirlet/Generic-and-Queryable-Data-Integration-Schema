# imports
import pandas as pd

# Opening and reading result files #################################
xls1 = pd.ExcelFile(PATH_TO_DEGs_FILE)
dico_sheet1 = pd.read_excel(xls1,sheet_name=None)
xls2 = pd.ExcelFile(PATH_TO_CO_DEGs_FILE)
dico_sheet2 = pd.read_excel(xls2,sheet_name=None)

names1 = xls1.sheet_names
names2 = xls2.sheet_names

upD = dico_sheet1[names1[0]]
downD = dico_sheet1[names1[1]]
upL = dico_sheet1[names1[2]]
downL = dico_sheet1[names1[3]]
upCo = dico_sheet2[names2[0]]
downCo = dico_sheet2[names2[1]]

cols = [0,2,3,4,5]

# DEGs ##############################################################
upD = upD[upD.columns[cols]]
upD.insert(5,'Expression',['UP' for i in range(len(upD))])
upD.insert(6,'in@Contrast',['HCMvsC' for i in range(len(upD))])
upD.insert(7,'Type',['Gene expression' for i in range(len(upD))])

downD = downD[downD.columns[cols]]
downD.insert(5,'Expression',['DOWN' for i in range(len(downD))])
downD.insert(6,'in@Contrast',['HCMvsC' for i in range(len(downD))])
downD.insert(7,'Type',['Gene expression' for i in range(len(downD))])

# lncRNA ############################################################
upL = upL[upL.columns[cols]]
upL.insert(5,'Expression',['UP' for i in range(len(upL))])
upL.insert(6,'in@Contrast',['HCMvsC' for i in range(len(upL))])
upL.insert(7,'Type',['lncRNA expression' for i in range(len(upL))])

downL = downL[downL.columns[cols]]
downL.insert(5,'Expression',['DOWN' for i in range(len(downL))])
downL.insert(6,'in@Contrast',['HCMvsC' for i in range(len(downL))])
downL.insert(7,'Type',['lncRNA expression' for i in range(len(downL))])

# co-DEGs ###########################################################
cols = [0,2]
upCo = upCo[upCo.columns[cols]]
upCo.insert(1,'logFC',['NA' for i in range(len(upCo))])
upCo.insert(2,'Pvalue',['NA' for i in range(len(upCo))])
upCo.insert(3,'FDR',['NA' for i in range(len(upCo))])
upCo.insert(5,'Expression',['UP' for i in range(len(upCo))])
upCo.insert(6,'in@Contrast',['HCM_FvsC' for i in range(len(upCo))])
upCo.insert(7,'Type',['Gene Co-expression' for i in range(len(upCo))])

downCo = downCo[downCo.columns[cols]]
downCo.insert(1,'logFC',['NA' for i in range(len(downCo))])
downCo.insert(2,'Pvalue',['NA' for i in range(len(downCo))])
downCo.insert(3,'FDR',['NA' for i in range(len(downCo))])
downCo.insert(5,'Expression',['DOWN' for i in range(len(downCo))])
downCo.insert(6,'in@Contrast',['HCM_FvsC' for i in range(len(downCo))])
downCo.insert(7,'Type',['Gene Co-expression' for i in range(len(downCo))])


# Concatenation and export ##########################################
DEGs = pd.concat([upD,downD,upL,downL,upCo,downCo],axis=0)
for i in range(len(DEGs)) :
    DEGs.iat[i,0] = DEGs.iat[i,0].split('_')[0]

DEGs.insert(0,'Differential Expression',['DEG_' + str(i) for i in range(len(DEGs))])
DEGs = DEGs.rename(columns={'gene':'concerns@gene'})

DEGs.to_csv(PATH_TO_NEW_DEG_FILE,sep='\t',index=False)
