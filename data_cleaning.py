# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from scipy.stats import zscore
import seaborn as sns

# Read .xlsx into dataframe
excel_file_path = '/home/qian/Documents/cbus_case_study/Resources/stock_data.xlsx'
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

# Export the data to Resources folder
all_stocks_prices.to_excel('/home/qian/Documents/cbus_case_study/Resources/prices.xlsx')

# Date quality checking
# Step one: Check if the data has nulls and duplicates 
print("The number of nulls in the dataframe:")
print(all_stocks_prices.isnull().sum())
print("Whether there are dupicated rows in the dataframe:")
print(all_stocks_prices.duplicated())

# Change the weekly stock prices into weekly stock returns
all_stocks_returns = all_stocks_prices.pct_change().dropna()

# Save the weekly stock returns into the Resources folder
all_stocks_returns.to_excel('/home/qian/Documents/cbus_case_study/Resources/returns.xlsx')

# Step two: Check the level of outliers of the data and convert the data
# Calculate the zscores of the stock returns
df_zscore = zscore(all_stocks_returns)

# Check the zscores of the stock returns
print(df_zscore)

# Draw the zscore plot for the origianl data
plt.figure(figsize=(10, 6))
for column in df_zscore.columns:
    plt.plot(df_zscore[column], label=column)

# Plot the cap lines
plt.axhline(y=3, color='r', linestyle='--', label='y=3')
plt.axhline(y=-3, color='g', linestyle='--', label='y=-3')

# Detail the graph information
plt.legend()
plt.xlabel('Index')
plt.ylabel('Values')
plt.show()
plt.savefig('/home/qian/Documents/cbus_case_study/Resources/Images/stock_returns_original.png')

# Cap the outliers at z-score: 3, -3
plt.figure(figsize=(10, 6))
for column in df_zscore.columns:
    df_zscore[column] = np.clip(df_zscore[column], -3, 3)
    plt.plot(df_zscore[column], label=column)

# Plot the cap lines
plt.axhline(y=3, color='r', linestyle='--', label='y=3')
plt.axhline(y=-3, color='g', linestyle='--', label='y=-3')

# Detail the graph information
plt.legend()
plt.xlabel('Index')
plt.ylabel('Values')
plt.show()
plt.savefig('/home/qian/Documents/cbus_case_study/Resources/Images/stock_returns_capped.png')

# Calculate the origianl mean and stadard deviation to prepare for the convertion
mean_original = all_stocks_returns.mean()
std_original = all_stocks_returns.std()

# Convert the outliers into capped figures
stock_returns_converted = df_zscore * std_original + mean_original
print("Stock Returns after converting from capped z-scores:")
print(stock_returns_converted)

# Save the cleaned stock return data for further analysis
stock_returns_converted.to_excel('/home/qian/Documents/cbus_case_study/Resources/cleaned_returns.xlsx')

# Step three: check the normality of data
# 1) Are returns symmetric?
percentage_df = (stock_returns_converted > stock_returns_converted.mean()).mean()

# Display the new DataFrame with percentage values
print("Percentage of values greater than mean for each column:")
print(percentage_df.to_frame(name='Percentage'))

# 2) Is volatility constant?
vols = stock_returns_converted.rolling(50).std().dropna()
vols.reset_index()

# Adjust the details of the graph
plt.figure(figsize=(15,6))
vols.plot(legend=True)
plt.legend(vols.columns, loc='upper center', bbox_to_anchor=(1, 1))
plt.title('Rolling STD of Multiple Columns')
plt.savefig('/home/qian/Documents/cbus_case_study/Resources/Images/vol_check.png', bbox_inches='tight')

# 3) Visualise the data using the hist() method
stock_returns_converted.hist(bins=100)
plt.savefig('/home/qian/Documents/cbus_case_study/Resources/Images/histogram.png', bbox_inches='tight')