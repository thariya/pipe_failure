import pandas as pd
import numpy as np
import csv

suffix_file = '_suburbs.csv'

listx=[2015 ,2016 ,2017]
percentage_overlaps=[]
dic={}

for x in listx:
    zone_file=str(x)+suffix_file
    cell1='data_'+str(x)+'_cell1'
    cell2 = 'data_' + str(x) + '_cell2'
    cell3 = 'data_' + str(x) + '_cell3'

    df_1 = pd.read_csv(zone_file)
    df_1.sort_values(by=[cell2], ascending=[0], inplace=True)
    smallest_value=float(df_1.iloc[28,1])
    df_1 = df_1[pd.to_numeric(df_1[cell2])>=smallest_value]
    length=len(df_1)
    df_fail=df_1[cell1]
    print("Highest failing suburbs as ranked by predictions")
    print(len(df_1))
    print(df_fail)

    df_1=pd.read_csv(zone_file)
    df_1.sort_values(by=[cell3], ascending=[0], inplace=True)
    df_1=df_1.iloc[:length,]
    df_pred=df_1[cell1]
    print("Highest failing suburbs as ranked by failures")
    print(len(df_pred))
    print(df_pred)

    overlapping_zones=set(df_pred).intersection(df_fail)
    print(overlapping_zones)
    print(len(overlapping_zones))
    overlaps = len(overlapping_zones)*100.0 / length
    percentage_overlaps.append(overlaps)


dic['number']=listx
dic['overlap']=percentage_overlaps
df=pd.DataFrame(dic)
df.to_csv('result.csv',index=False)
