# imports
import pandas as pd

# Opening and reading result files #################################
xls4 = pd.ExcelFile("/home/ytirlet/Documents/HCM/Supplemental_tables/Table4.xlsx")
dico_sheet4 = pd.read_excel(xls4,sheet_name=None)
names4 = xls4.sheet_names
DMRhyper = dico_sheet4[names4[0]]
DMRhypo = dico_sheet4[names4[1]]

# Hypermethylated DMRs #############################################
DMRhyper.insert(4,'methylation',['Hypermethylation' for i in range(len(DMRhyper))])
DMRhyper = DMRhyper.drop(columns = ['gene'])
DMRhyper = DMRhyper.drop_duplicates()

# Hypomethylated DMRs ##############################################
DMRhypo.insert(4,'methylation',['Hypomethylation' for i in range(len(DMRhypo))])
DMRhypo = DMRhypo.drop(columns = ['gene'])
DMRhypo = DMRhypo.drop_duplicates()

# Concatenation and export ##########################################
DMRs = pd.concat([DMRhyper,DMRhypo],axis=0)
DMRs.insert(0,'Differential Methylated Regions',['DiffMeth_' + str(i) for i in range(len(DMRs))])
DMRs.insert(5,'measured_in@Contrast',["HCMvsC" for i in range(len(DMRs))])

DMRs.to_csv("/home/ytirlet/Documents/HCM/Supplemental_tables/integr/DMRs.tsv",sep='\t',index=False)