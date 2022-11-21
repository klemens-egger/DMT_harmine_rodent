#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 15:36:33 2022

@author: Edge
"""
import seaborn as sns
import os
import pandas as pd


def bold_extreme_values(data, data_max=-1):

    if data == data_max:
        return "\\bfseries %s" % data

    return data


if __name__ == "__main__":

    # Load data and
    # calculate mean of each column
    df = pd.read_excel('/Users/Edge/Desktop/PhD_Projekt/III_rat_PET_experiment/01_extracted_data_PMOD/Analysis/03_statistics/stats_table.xlsx', header = 0, engine = 'openpyxl')

    # Specify in which columns to make the maximum bold
    #col_show_max = ["sepal_length", "sepal_width",
     #               "petal_length", "petal_width"]

   # # Iterate through columns
    #for k in col_show_max:
     #   df[k] = df[k].apply(
      #      lambda data: bold_extreme_values(data, data_max=df[k].max()))

    # Set column header to bold title case
    df.columns = (df.columns.to_series()
                  .apply(lambda r: "\\textbf{}".format(
                      r.replace("_", " ").title())))

    # Write to file
    with open(
        os.path.splitext(
            os.path.basename(__file__))[0] + ".tbl", "w") as f:

        format = "l" + \
            "@{\hskip 12pt}" +\
            4*"S[table-format = 2.2]"

        f.write(df
                .to_latex(index=False,
                          escape=False,
                          column_format=format)
                )