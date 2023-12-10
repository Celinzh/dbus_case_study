# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read .xlsx into dataframe
excel_file_path = 'cbus_case_study/Resources/stock_data.xlsx'
excel_file = pd.ExcelFile(excel_file_path)
sheet_names = excel_file.sheet_names

# Concat all portfolio prices into a dataframe
dfs = []
column_name = ['Adj Close', 'Date']
for sheet_name in excel_file.sheet_names:
    df = pd.read_excel(excel_file, sheet_name, usecols=column_name)
    df.set_index('Date', inplace=True)
    df.rename(columns={'Adj Close': sheet_name}, inplace=True)
    dfs.append(df)

all_stocks_prices = pd.concat(dfs, axis=1, join = 'inner')

# Exprt the data to Resources folder
all_stocks_prices.to_excel('cbus_case_study/Resources/prices.xlsx')

# Change weekly stock prices into weekly returns
all_stocks_returns = all_stocks_prices.pct_change().dropna()

# Save the weekly stock returns into the Resources folder
all_stocks_returns.to_excel('cbus_case_study/Resources/returns.xlsx')

#   step two: how are stock returns 







# Defining a function of checking data quality
# def data_cleaning_check (prices_data):
#     # Assess data quality by checking for nulls
#     print("The number of nulls in the sheet:" + "\n" + prices_data.isnull().sum())
#     # Assess data quality by checking duplicated rolls
#     print("Whether there are dupicated rows in the sheet:" + "\n" + prices_data.duplicated())
#     # Assess data quality by checking data types
#     print("The data types of each column:" + "\n" + prices_data.dtypes)

#     return 


# # Defining a function of checking outliers/normality
# for sheet_name in sheet_names:
#     sheet_df = pd.read_excel(excel_file, sheet_name)
#     print(f"Sheet Name: {sheet_name}")
#     print(sheet_df.describe())  # Display the first few rows of each sheet
#     print("\n")


# date quality checking
#   step one: checking if the data has nulls and duplicates
# print("The number of nulls in the dataframe:")
# print(all_stocks_prices.isnull().sum())
# print("Whether there are dupicated rows in the dataframe:")
# print(all_stocks_prices.duplicated())