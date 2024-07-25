# imports
import pandas as pd

# Opening and reading result files #################################
xls1 = pd.ExcelFile("/home/ytirlet/Documents/honeybee/Table5.xlsx")
dico_sheet1 = pd.read_excel(xls1,sheet_name=None)
xls2 = pd.ExcelFile("/home/ytirlet/Documents/honeybee/Table6.xlsx")
dico_sheet2 = pd.read_excel(xls2,sheet_name=None)

names1 = xls1.sheet_names
names2 = xls2.sheet_names

Ch_2Q = dico_sheet1[names1[0]]
Ch_2W = dico_sheet1[names1[1]]
Ch_4Q = dico_sheet2[names2[0]]
Ch_4W = dico_sheet2[names2[1]]

cols = [0,1,2,34,35,36,43,50,53]

# Queens - 2 Days ##################################################
Ch_2Q = Ch_2Q[Ch_2Q.columns[cols]]
Ch_2Q.insert(9,'measured_in@Condition',['2Q' for i in range(len(Ch_2Q))])

# Workers - 2 Days #################################################
Ch_2W = Ch_2W[Ch_2W.columns[cols]]
Ch_2W.insert(9,'measured_in@Condition',['2W' for i in range(len(Ch_2W))])

# Queens - 4 Days ##################################################
Ch_4Q = Ch_4Q[Ch_4Q.columns[cols]]
Ch_4Q.insert(9,'measured_in@Condition',['4Q' for i in range(len(Ch_4Q))])

# Workers - 4 Days #################################################
Ch_4W = Ch_4W[Ch_4W.columns[cols]]
Ch_4W.insert(9,'measured_in@Condition',['4W' for i in range(len(Ch_4W))])


# Concatenation and export ##########################################
Chip = pd.concat([Ch_2Q,Ch_2W,Ch_4Q,Ch_4W],axis=0)
Chip.insert(0,'Chip peak',['Chip_' + str(i) for i in range(len(Chip))])

for i in range(len(Chip)) :
    if "(" in Chip.iat[i,7] :
        Chip.iat[i,7] = Chip.iat[i,7].split(' (')[0]

Chip.to_csv("/home/ytirlet/Documents/honeybee/integr/Chip.tsv",sep='\t',index=False)