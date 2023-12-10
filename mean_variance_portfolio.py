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
all_stocks_prices.set_index('Date', inplace =True)

## Expected Returns
# Forcasts expected returns by taking the historical average returns from the stocks in the list
mu = expected_returns.mean_historical_return(prices=all_stocks_prices, compounding=False, frequency=52)
print('Expected Returns')
print(mu)
print('\n')

# Risk Model: Create the variance-covariance matrix of returns for the stocks
cov_matrix = risk_models.sample_cov(prices=all_stocks_prices, frequency=52)
print('Variance-Covariance Matrix')
print(cov_matrix)
print('\n')

# Create an EfficientFrontier instance
ef = EfficientFrontier(expected_returns=mu, cov_matrix=cov_matrix, weight_bounds=(0, 1))

# Optimize for the maximum Sharpe ratio
raw_weights = ef.max_sharpe()

# Convert OSQP_results to a picklable format
sharpe_results = {
    'weights': dict(raw_weights),
    'performance': ef.portfolio_performance(verbose=True)
}

# Display portfolio weights
print('Portfolio Weights')
print(sharpe_results['weights'])
print('\n')

# Display expected return, volatility, and Sharpe ratio
print('Portfolio Performance')
print(sharpe_results['performance'])
print('\n')

# Plot the efficient frontier
fig, ax = plt.subplots()
pplt.plot_efficient_frontier(ef, ax=ax, show_assets=True)

# Highlight the tangency portfolio
ax.scatter(sharpe_results['performance'][1], sharpe_results['performance'][0], marker='*', color='r', s=200,
           label='Tangency Portfolio')
ax.legend()

# Save the graph into the Resources folder
plt.savefig('cbus_case_study/Resources/Images/efficient_frontier_output2.png')
# mu = expected_returns.mean_historical_return(prices=all_stocks_prices, compounding=False, frequency=52)
# print('Expected Returns')
# print(mu)
# print('\n')

# # Risk Model: Create the variance-covariance matrix of returns for the stocks
# cov_matrix = risk_models.sample_cov(prices=all_stocks_prices, frequency=52)
# print('Variance-Covariance Matrix')
# print(cov_matrix)
# print('\n')

# # Create an EfficientFrontier instance
# ef = EfficientFrontier(expected_returns=mu, cov_matrix=cov_matrix, weight_bounds=(0, 1))

# # Optimize for the maximum Sharpe ratio
# ef.max_sharpe()

# # Display portfolio weights
# print('Portfolio Weights')
# print(ef.weights)
# print('\n')

# # Display expected return, volatility, and Sharpe ratio
# portfolio = ef.portfolio_performance(verbose=True)
# print('Portfolio Performance')
# print(portfolio)
# print('\n')

# # Plot the efficient frontier
# fig, ax = plt.subplots()
# pplt.plot_efficient_frontier(ef, ax=ax, show_assets=True)

# # Highlight the tangency portfolio
# ax.scatter(portfolio[1], portfolio[0], marker='*', color='r', s=200, label='Tangency Portfolio')
# ax.legend()

# # Save the graph into the Resources folder
# plt.savefig('cbus_case_study/Resources/Images/efficient_frontier_output2.png')

# After we finish drawing the efficient frontier, we are ready to explore different constraints
#




#----------------------------------------------------------------------------------------------------------------------
# print('Portfolio Weights')
# print(ef.max_sharpe()) 
# print('\n')



# # Display expected return, volatility, and sharpe ratio
# portfolio = ef.portfolio_performance(verbose=True)
# print('Portfolio Performance')
# print(portfolio)
# print('\n')

# # Create a new EffcientFrontier instance for plotting
# ef_plot = EfficientFrontier(mu, cov_matrix, weight_bounds=(0,1))

# # Get the efficient frontier weights for plotting
# weights_plot = ef_plot.max_sharpe()

# # Calculate and display the portfolio performance
# ef_plot.portfolio_performance(verbose=True)

# # Create a new EfficienFrontier instance for adding constraints
# ef_constraints = EfficientFrontier(mu, cov_matrix, weight_bounds=(0,1))

# # Add the new desired constraints to the new instance: sum of weights = 1
# ef_constraints.add_constraint(lambda x: cvxpy.sum(x) == 1)

# # Plot the efficient frontier and risky investment set
# fig, ax = plt.subplots()
# pplt.plot_efficient_frontier(ef_constraints, ax=ax, show_assets = True)

# # Starsign the tangency portfolio
# # ax.scatter(ef_plot.portfolio_performance()[1], ef_plot.portfolio_performance()[0], marker='*', color='r', s=200, label='Tangency Portfolio')
# # ax.legend()

# ##Save the plot into the Images folder
# plt.savefig('cbus_case_study/Resources/Images/efficient_frontier_plot.png')
