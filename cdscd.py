# Import libraries
from pypfopt import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pypfopt import plotting
import cvxpy
import pypfopt.plotting as pplt

# Import data from Resources folder
xlsx_file_path = 'cbus_case_study/Resources/prices.xlsx'
all_stocks_prices = pd.read_excel(xlsx_file_path)

## Expected Returns
# Forcasts expected returns by taking the historical average returns from the stocks in the list
mu = expected_returns.mean_historical_return(prices = all_stocks_prices, compounding=False, frequency = 52)
print('Expected Returns')
print(mu)
print('\n')

## Risk Model
# Create the variance-covariance matrix of returns for the stocks in the list ---------------------------------------------need to be changed
cov_matrix = risk_models.sample_cov(prices = all_stocks_prices, frequency = 52)
print('Variance-Covariance Matrix')
print(cov_matrix)
print('\n')

# Calculate the portfolio weights that yield the maximum expected sharpe ratio
ef = EfficientFrontier(expected_returns = mu, cov_matrix = cov_matrix, weight_bounds = (0,1)) 
ef.add_constraint(lambda x: cvxpy.sum(x) == 1)

fig, ax = plt.subplots()
pplt.plot_efficient_frontier(ef, ax=ax, show_assets = True, showfig=True)

# ax.scatter(ef.portfolio_performance()[1], ef.portfolio_performance()[0], marker='*', color='r', s=200, label='Tangency Portfolio')
# ax.legend()