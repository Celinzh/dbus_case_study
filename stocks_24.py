# Import libraries
import yfinance as yf
import pandas as pd

# Read the stock list into dataframe
xlsx_file_path = '/home/qian/Documents/cbus_case_study/Resources/Stock List.xlsx'
df = pd.read_excel(xlsx_file_path)

# Write an Excel file with multiple sheets
excel_writer = pd.ExcelWriter('/home/qian/Documents/cbus_case_study/Resources/stock_data.xlsx', engine='xlsxwriter')

# Extract data for the 24 stocks and save them in an excel file in multiple sheets
for stock_id in df['Stock ID']:
    stock_data = yf.download(stock_id, start = '2020-12-01', end = '2023-12-01', interval = '1wk')
    stock_data.to_excel(excel_writer, sheet_name=str(stock_id))

# Save the excel file into Resources folder
excel_writer.save()
