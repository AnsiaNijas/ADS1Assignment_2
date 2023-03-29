# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 18:57:08 2023
df_Arable_Land_updated= pd.DataFrame.transpose(df_Arable_Land_year_as_columns)
df_Arable_Land_countries_as_columns=df_Arable_Land_updated.iloc[4:]
df_Arable_Land_countries_as_columns.columns=df_Arable_Land_updated.iloc[0]
df_Arable_Land_countries_as_columns.columns.values[0] = 'Year'
print(df_Arable_Land_countries_as_columns['Year'])
@author: ansia
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import seaborn as sns

def readBarPlotData(filename):
    df_Arable_Land=pd.read_excel(filename)
    df_Arable_Land.columns=df_Arable_Land.iloc[2].astype(str)
    df_Arable_Land_year_as_columns=df_Arable_Land.iloc[170:182,0:].fillna(0)
    df_Arable_Land_updated= pd.DataFrame.transpose(df_Arable_Land)
    df_Arable_Land_countries_as_columns=df_Arable_Land_updated.iloc[4:]
    df_Arable_Land_countries_as_columns.columns=df_Arable_Land_updated.iloc[0].astype(str)
    df_Arable_Land_countries_as_columns=df_Arable_Land_countries_as_columns.rename(columns={'Country Name':'Year'})
    # print(df_Arable_Land_year_as_columns.groupby('Country Name').describe())
    return df_Arable_Land_year_as_columns, df_Arable_Land_countries_as_columns

   
def readHeatData(filename1):
    df_World_Development_Indicators=pd.read_excel(filename1)
    df_World_Development_Indicators_updated=df_World_Development_Indicators.iloc[532:539,0:]
    df_World_Development_Indicators_updated=df_World_Development_Indicators_updated.drop(['Country Name','Country Code','Series Code'],axis=1)
    df_World_Development_Indicators_updated=pd.DataFrame.transpose(df_World_Development_Indicators_updated)
    df_World_Development_Indicators_updated.columns=df_World_Development_Indicators_updated.iloc[0]
    df_World_Development_Indicators_updated.reset_index(drop=True, inplace=True)
    df_World_Development_Indicators_updated = df_World_Development_Indicators_updated.drop(labels=0, axis=0)
    df_World_Development_Indicators_updated=df_World_Development_Indicators_updated.fillna(0)
    return df_World_Development_Indicators_updated


def barplot1()   :
    df1,df2=readBarPlotData("Arable_Land.xls")
    legends_years = ['2020','2019','2018','2017','2016','2015']
    plt.figure(dpi=300)
    df1.plot.bar(x='Country Name', y=['2020.0','2019.0','2018.0','2017.0','2016.0','2015.0'],rot=90,figsize=(25,20),title='Arable Land',
    xlabel="Country Name",ylabel="Years", fontsize='large', label=legends_years);
    plt.ylim(0, 40)
    plt.legend(title='Years',fontsize=20) 
    plt.savefig('BarPlot.jpg')
    plt.show()
    return
    
def heatMap1()   : 
    
    df1=readHeatData("World_Development_Indicators.xlsx")
    corr=df1.corr(method='pearson', min_periods=1)
    sns.heatmap(data=corr,annot=True)
    labels=['Net forest depletion','Agricultural land','Agricultural irrigated land','Arable land Agriculture_ forestry_fishing','Arable land','Forest area']
    plt.title('Greece')
    plt.xticks([0,1,2,3,4,5],labels)
    plt.yticks([0,1,2,3,4,5],labels)
    plt.savefig('HeatMap_Greece.jpg',dpi=300,bbox_inches='tight')
    plt.show()
    return
    
if __name__ == "__main__":
    barplot1()
    heatMap1()
    