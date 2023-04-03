# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 18:57:08 2023
@author: ansia
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import seaborn as sns


def read_Bar_Line_Plot_Data(filename):
    """ 
    Function which takes an excel filename as argument, read the file into a dataframe and returns two dataframes: one with years as columns and one with
    countries as columns.
    """
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
    df_Arable_Land_countries_as_columns = df_Arable_Land_countries_as_columns[[
        'Ethiopia', 'Ghana', 'Guinea', 'Madagascar', 'Malawi', 'Rwanda', 'Sierra Leone', 'Uganda']]
    df_Arable_Land_countries_as_columns = df_Arable_Land_countries_as_columns.reset_index(
        drop=False)
    return df_Arable_Land_year_as_columns, df_Arable_Land_countries_as_columns


def read_Heat_Map_Data(filename1):
    """ 
     Function which takes an excel filename as argument, read the file into a dataframe and returns one dataframe with indicators as columns.
     """
    df_Climate_Change_Indicators = pd.read_excel(filename1)
    df_Climate_Change_Indicators_updated = df_Climate_Change_Indicators.iloc[
        532:539, 0:]
    df_Climate_Change_Indicators_updated = df_Climate_Change_Indicators_updated.drop(
        ['Country Name', 'Country Code', 'Series Code'], axis=1)
    df_Climate_Change_Indicators_updated = pd.DataFrame.transpose(
        df_Climate_Change_Indicators_updated)
    df_Climate_Change_Indicators_updated.columns = df_Climate_Change_Indicators_updated.iloc[
        0]
    df_Climate_Change_Indicators_updated.reset_index(
        drop=True, inplace=True)
    df_Climate_Change_Indicators_updated = df_Climate_Change_Indicators_updated.drop(
        labels=0, axis=0)
    df_Climate_Change_Indicators_updated = df_Climate_Change_Indicators_updated.fillna(
        0)
    return df_Climate_Change_Indicators_updated


def read_CO2_emission_data(filename):
    """ 
    Function which takes an excel filename as argument, read the file into a dataframe and returns one dataframe with Country Name and Indicator as columns.
    """
    df_CO2_Emission = pd.read_excel(filename)
    df_CO2_Emission = df_CO2_Emission.drop(['Time Code'], axis=1)
    df_CO2_Emission = df_CO2_Emission.dropna(axis=0)
    df_CO2_Emission = df_CO2_Emission.fillna(0)
    df_CO2_Emission = df_CO2_Emission.set_index('Time')
    df_CO2_Emission = df_CO2_Emission.iloc[0:, 170:186]
    df_CO2_Emission.replace("..", 0, inplace=True)
    return df_CO2_Emission


def barplot(filename, title, ylim, figure_name):
    """ 
    Function to plot Barplots of Agricultural land and Arable Land and save figure.
    Arguments: Excel filename, title of barplot, y limits, Figure name 
    """
    df1, df2 = read_Bar_Line_Plot_Data(filename)
    legends_years = ['2020', '2019', '2018', '2017', '2016', '2015']
    plt.figure(dpi=300)
    df1.plot.bar(x='Country Name', y=['2020.0', '2019.0', '2018.0', '2017.0', '2016.0', '2015.0'], rot=90, figsize=(30, 25),
                   fontsize=25, label=legends_years)
    plt.title(title, fontsize=30)
    plt.xlabel("Country Name", fontsize=30)
    plt.ylabel("Land area (% Percentage)", fontsize=30)
    plt.ylim(0, ylim)
    plt.legend(title='Years', title_fontsize=25, fontsize=25)
    plt.savefig(figure_name)
    plt.show()
    return


def lineplot(filename, title, y_label, ylimin, ylimax, figure_name):
    """ 
    Function to plot Lineplots of Forest Area and Forest Area Depletions and save figure.
    Arguments: Excel filename, title of lineplots, y label, start value of ylim, End value of ylim and Figure name 
    """
    df1, df2 = read_Bar_Line_Plot_Data(filename)
    countries = [['Ethiopia', 'Ghana', 'Guinea', 'Madagascar', 'Malawi', 'Rwanda', 'Sierra Leone', 'Uganda']
                 ]
    plt.figure(dpi=300)
    for i in range(len(countries)):
        plt.plot(df2['Year'], df2[countries[i]], label=countries[i])
    plt.title(title, fontsize=8)
    plt.xlabel("Years", fontsize=8)
    plt.ylabel(y_label, fontsize=8)
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)
    plt.xlim(2012, 2020)
    plt.ylim(ylimin, ylimax)
    plt.legend(title='Country Names', title_fontsize=4,
               fontsize=4, loc='upper right')
    plt.savefig(figure_name)
    plt.show()
    return


def heatMap1(filename):
    """ 
    Function to compute correlation between different climate change indicators, to plot heatmap and save figure.
    Arguments: Excel filename. 
    """
    df1 = read_Heat_Map_Data(filename)
    labels = ['Net forest depletion', 'Agricultural land', 'Agricultural irrigated land',
              'Agriculture_ forestry_fishing', 'Arable land', 'Forest area']
    corr = df1.corr(method='pearson', min_periods=1)
    plt.figure()
    sns.heatmap(data=corr, annot=True, cbar_kws={
                "label": "Correlation of Climate Change Indicators"})
    plt.title('Greece')
    plt.xlabel('')
    plt.ylabel('')
    plt.xticks([.5, 1.5, 2.5, 3.5, 4.5, 5.5], labels, ha='center')
    plt.yticks([.5, 1.5, 2.5, 3.5, 4.5, 5.5], labels, va='center')
    plt.savefig('HeatMap_Greece.jpg', dpi=300, bbox_inches='tight')
    plt.show()
    return


def stat_analysis_CO2_emission(filename):
    """ 
    Function to compute and analyze statical data of different CO2 Emission indicators using describe, average, std. deviation, skew & kurtosis and print & save the output as csv file.
    Arguments: Excel filename. 
    """
    df_CO2_Emission = read_CO2_emission_data(filename)
    df_stats = pd.DataFrame(
        columns=('Average', 'Std. deviation', 'Skew', 'Kurtosis'))
    country_nam_indicators = [
        ['Hong Kong', 'Hong Kong', 'Hungary', 'Hungary', 'Iceland', 'Iceland', 'India',
         'India', 'Indonesia', 'Indonesia', 'Iran', 'Iran', 'Iraq', 'Iraq', 'Ireland', 'Ireland'],
        ['Liquid', 'Solid', 'Liquid', 'Solid', 'Liquid', 'Solid', 'Liquid',
         'Solid', 'Liquid', 'Solid', 'Liquid', 'Solid', 'Liquid', 'Solid', 'Liquid', 'Solid'],
    ]
    tuples = list(zip(*country_nam_indicators))
    index = pd.MultiIndex.from_tuples(
        tuples, names=['Country Name', 'CO2 emissions'])
    for i in range(16):
        aver = np.mean(df_CO2_Emission.iloc[:, i])
        std = np.std(df_CO2_Emission.iloc[:, i])
        skew = stats.skew(df_CO2_Emission.iloc[:, i])
        Kurtosis = stats.kurtosis(df_CO2_Emission.iloc[:, i])
        df_stats.loc[i] = [aver] + [std] + [skew] + [Kurtosis]
    df_stats = df_stats.round(1)
    df_stats = df_stats.set_index(index)
    print(df_stats.groupby('Country Name')['Skew'].describe())
    print(df_stats)
    df_stats.to_csv('Statical_Analysis of CO2 Emission.csv')


if __name__ == "__main__":
    #calling function to visualize BarPlot by passing arguments as Excel filename, title of barplot, y limits, Figure name
    barplot("Arable_Land.xls", 'Arable Land', 40, 'BarPlot1.jpg')
    #calling function to visualize BarPlot by passing arguments as Excel filename, title of barplot, y limits, Figure name
    barplot("Agricultural_Land.xls", 'Agricultural Land', 80, 'BarPlot2.jpg')
    #calling function to visualize LinePlot by passing arguments as Excel filename, title of lineplots, y label, start value of ylim, End value of ylim and Figure name
    lineplot('Forest_Area.xls', 'Forest_Area',
             'Land area (% Percentage)', 10, 45, 'LinePlot1.jpg')
    #calling function to visualize LinePlot by passing arguments as Excel filename, title of lineplots, y label, start value of ylim, End value of ylim and Figure name
    lineplot('Forest Depletion.xls', 'Forest Depletion',
             'Net forest depletion (% Percentage)', 3, 15, 'LinePlot2.jpg')
    #calling function to visualize HeatMap by passing arguments as Excel filename
    heatMap1("World_Development_Indicators.xlsx")
    #calling function to compute and analyse statical data of CO2 Emission by passing arguments as Excel filename
    stat_analysis_CO2_emission('CO2_emission_by_liquids_solids_fuels.xlsx')
