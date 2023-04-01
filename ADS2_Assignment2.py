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
    df_Arable_Land = pd.read_excel(filename)
    df_Arable_Land.columns = df_Arable_Land.iloc[2].astype(str)
    df_Arable_Land_year_as_columns = df_Arable_Land.iloc[170:182, 0:].fillna(0)
    df_Arable_Land_updated = pd.DataFrame.transpose(df_Arable_Land)
    df_Arable_Land_countries_as_columns = df_Arable_Land_updated.iloc[4:]
    df_Arable_Land_countries_as_columns.columns = df_Arable_Land_updated.iloc[0].astype(
        str)
    df_Arable_Land_countries_as_columns = df_Arable_Land_countries_as_columns.rename(
        columns={'Country Name': 'Year'})
    df_Arable_Land_countries_as_columns = df_Arable_Land_countries_as_columns.set_index(
        'Year')
    df_Arable_Land_countries_as_columns = df_Arable_Land_countries_as_columns.iloc[
        51:61, 0:]
    #countries=[[]]
    df_Arable_Land_countries_as_columns = df_Arable_Land_countries_as_columns[[
        'Andorra', 'Bulgaria', 'Croatia', 'Germany', 'Ghana', 'Lithuania', 'Norway', 'Sri Lanka', 'United States']]
    df_Arable_Land_countries_as_columns = df_Arable_Land_countries_as_columns.reset_index(
        drop=False)
    return df_Arable_Land_year_as_columns, df_Arable_Land_countries_as_columns


def readHeatData(filename1):
    df_World_Development_Indicators = pd.read_excel(filename1)
    df_World_Development_Indicators_updated = df_World_Development_Indicators.iloc[
        532:539, 0:]
    df_World_Development_Indicators_updated = df_World_Development_Indicators_updated.drop(
        ['Country Name', 'Country Code', 'Series Code'], axis=1)
    df_World_Development_Indicators_updated = pd.DataFrame.transpose(
        df_World_Development_Indicators_updated)
    df_World_Development_Indicators_updated.columns = df_World_Development_Indicators_updated.iloc[
        0]
    df_World_Development_Indicators_updated.reset_index(
        drop=True, inplace=True)
    df_World_Development_Indicators_updated = df_World_Development_Indicators_updated.drop(
        labels=0, axis=0)
    df_World_Development_Indicators_updated = df_World_Development_Indicators_updated.fillna(
        0)
    return df_World_Development_Indicators_updated


def barplot(filename, title, ylim, figure_name):
    df1, df2 = readBarPlotData(filename)
    legends_years = ['2020', '2019', '2018', '2017', '2016', '2015']
    plt.figure(dpi=300)
    df1.plot.bar(x='Country Name', y=['2020.0', '2019.0', '2018.0', '2017.0', '2016.0', '2015.0'], rot=90, figsize=(30, 25),
                   fontsize=25, label=legends_years)
    plt.title(title, fontsize=25)
    plt.xlabel("Country Name", fontsize=25)
    plt.ylim(0, ylim)
    plt.legend(title='Years', fontsize=25)
    plt.savefig(figure_name)
    plt.show()
    return


def lineplot(filename, title, ylimin, ylimax, figure_name):
    df1, df2 = readBarPlotData(filename)
    df2.to_csv('data123.csv')
    countries = [['Andorra', 'Bulgaria', 'Croatia', 'Germany', 'Ghana', 'Lithuania', 'Norway', 'Sri Lanka', 'United States']
                 ]
    plt.figure(dpi=300)
    for i in range(len(countries)):
        plt.plot(df2['Year'], df2[countries[i]], label=countries[i])

    plt.title(title, fontsize=5)
    plt.xlabel("Years", fontsize=5)
    plt.xlim(2012, 2020)
    plt.ylim(ylimin, ylimax)
    plt.legend(fontsize=5)
    plt.savefig(figure_name)
    plt.show()
    return


def heatMap1():
    df1 = readHeatData("World_Development_Indicators.xlsx")
    corr = df1.corr(method='pearson', min_periods=1)
    sns.heatmap(data=corr, annot=True)
    labels = ['Net forest depletion', 'Agricultural land', 'Agricultural irrigated land',
              'Agriculture_ forestry_fishing', 'Arable land', 'Forest area']
    plt.title('Greece')
    plt.xlabel('')
    plt.ylabel('')
    plt.xticks([0, 1, 2, 3, 4, 5], labels)
    plt.yticks([0, 1, 2, 3, 4, 5], labels)
    plt.savefig('HeatMap_Greece.jpg', dpi=300, bbox_inches='tight')
    plt.show()
    return


if __name__ == "__main__":
    barplot("Arable_Land.xls", 'Arable Land', 40, 'BarPlot1.jpg')
    barplot("Agricultural_Land.xls", 'Agricultural Land', 80, 'BarPlot2.jpg')
    lineplot('Forest_Area.xls', 'Forest_Area', 32.5, 37, 'LinePlot1.jpg')
    heatMap1()
