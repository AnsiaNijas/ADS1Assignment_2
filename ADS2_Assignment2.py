# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 18:57:08 2023
@author: ansia
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def read_Bar_Line_Plot_Data(filename):
    """ 
    Function which takes an excel filename as argument, read the file into a dataframe and returns two dataframes: one with years as columns and one with
    countries as columns.
    """
    df_Arable_Land = pd.read_excel(filename)
    countries = ['Ethiopia', 'Ghana', 'Greece', 'Guinea',
                 'India', 'Malaysia', 'Myanmar', 'Uganda']
    years = ['Country Name', '1990.0', '1995.0',
             '2000.0', '2005.0', '2010.0', '2015.0', '2020.0']
    df_Arable_Land.columns = df_Arable_Land.iloc[2].astype(str)
    df_Arable_Land_year_as_columns = df_Arable_Land.iloc[3:, 0:].fillna(0)
    df_Arable_Land_year_as_columns = df_Arable_Land_year_as_columns.drop(
        ['Country Code', 'Indicator Name', 'Indicator Code'], axis=1)
    df_Arable_Land_year_as_columns = df_Arable_Land_year_as_columns.set_index(
        'Country Name')
    df_Arable_Land_year_as_columns = df_Arable_Land_year_as_columns.loc[countries]
    df_Arable_Land_year_as_columns.reset_index(drop=False, inplace=True)
    df_Arable_Land_year_as_columns = df_Arable_Land_year_as_columns.loc[:, years]
    df_Arable_Land_countries_as_columns = pd.DataFrame.transpose(
        df_Arable_Land_year_as_columns)
    df_Arable_Land_countries_as_columns.columns = df_Arable_Land_countries_as_columns.iloc[0].astype(
        str)
    df_Arable_Land_countries_as_columns = df_Arable_Land_countries_as_columns.iloc[1:, 0:]
    df_Arable_Land_countries_as_columns.reset_index(drop=False, inplace=True)
    df_Arable_Land_countries_as_columns.columns.values[0] = "Years"
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
    legends_years = ['1990', '1995', '2000', '2005', '2010', '2015', '2020']
    plt.figure(dpi=300)
    df1.plot.bar(x='Country Name', y=['1990.0', '1995.0', '2000.0', '2005.0', '2010.0', '2015.0', '2020.0'], rot=90, figsize=(30, 25),
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
    countries = [['Ethiopia', 'Ghana', 'Greece', 'Guinea',
                  'India', 'Malaysia', 'Myanmar', 'Uganda']]
    year_xtick_o = ['1990.0', '1995.0', '2000.0',
                    '2005.0', '2010.0', '2015.0', '2020.0']
    year_xtick_n = ['1990', '1995', '2000', '2005', '2010', '2015', '2020']
    plt.figure(dpi=300)
    for i in range(len(countries)):
        plt.plot(df2['Years'], df2[countries[i]], label=countries[i])
    plt.title(title, fontsize=8)
    plt.xlabel('Years', fontsize=8)
    plt.ylabel(y_label, fontsize=8)
    plt.xlim('1990.0', '2020.0')
    plt.ylim(ylimin, ylimax)
    plt.xticks(year_xtick_o, year_xtick_n, fontsize=8)
    plt.yticks(fontsize=8)
    plt.legend(title='Country Names', title_fontsize=4,
               fontsize=4, loc='upper right')
    plt.savefig(figure_name)
    plt.show()
    return


def heatMap(filename):
    """ 
    Function to compute correlation between different climate change indicators, to plot heatmap and save figure.
    Arguments: Excel filename. 
    """
    df1 = read_Heat_Map_Data(filename)
    labels1 = ['Net forest depletion', 'Agricultural land', 'Agricultural irrigated land',
               'Agriculture_ forestry_fishing', 'Arable land', 'Forest area']
    corr = df1.corr(method='pearson', min_periods=1).round(1)
    fig, ax = plt.subplots(figsize=(8, 6))
    im = ax.imshow(corr, cmap="Blues")
    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.ax.set_ylabel(
        "Correlation of Climate Change Indicators", rotation=-90, va="bottom")
    ax.set_xticks(np.arange(len(labels1)), labels=labels1, fontsize=10)
    ax.set_yticks(np.arange(len(labels1)), labels=labels1, fontsize=10)
    plt.setp(ax.get_xticklabels(), rotation=-90, ha="left",
             rotation_mode="anchor")
    for i in range(len(labels1)):
        for j in range(len(labels1)):
            text = ax.text(
                j, i, corr.iloc[i, j], ha="center", va="center", color="orange", fontsize=10)
    ax.set_title("Greece")
    fig.tight_layout()
    plt.show()
    fig.savefig('HeatMap_Greece.jpg')
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
    return


if __name__ == "__main__":
    #calling function to visualize BarPlot by passing arguments as Excel filename, title of barplot, y limits, Figure name
    barplot("Arable_Land.xls", 'Arable Land', 50, 'BarPlot1.jpg')
    #calling function to visualize BarPlot by passing arguments as Excel filename, title of barplot, y limits, Figure name
    barplot("Agricultural_Land.xls", 'Agricultural Land', 80, 'BarPlot2.jpg')
    #calling function to visualize LinePlot by passing arguments as Excel filename, title of lineplots, y label, start value of ylim, End value of ylim and Figure name
    lineplot('Forest_Area.xls', 'Forest_Area',
             'Land area (% Percentage)', 10, 80, 'LinePlot1.jpg')
    #calling function to visualize LinePlot by passing arguments as Excel filename, title of lineplots, y label, start value of ylim, End value of ylim and Figure name
    lineplot('Forest Depletion.xls', 'Forest Depletion',
             'Net forest depletion (% Percentage)', -5, 35, 'LinePlot2.jpg')
    #calling function to visualize HeatMap by passing arguments as Excel filename
    heatMap("World_Development_Indicators.xlsx")
    #calling function to compute and analyse statical data of CO2 Emission by passing arguments as Excel filename
    stat_analysis_CO2_emission('CO2_emission_by_liquids_solids_fuels.xlsx')
