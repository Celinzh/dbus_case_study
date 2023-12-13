# Import libraries
from pypfopt import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns
from pypfopt import base_optimizer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pypfopt import plotting
import cvxpy
import pypfopt.plotting as pplt
from collections import OrderedDict

# Import data from Resources folder
xlsx_file_path = '/home/qian/Documents/cbus_case_study/Resources/cleaned_returns.xlsx'
returns = pd.read_excel(xlsx_file_path)
returns.set_index('Date', inplace =True)

## Expected Returns
# Forcasts expected returns by taking the historical average returns from the stocks in the list   --- Notice: pypfopt doesnt support calculating weekly returns
mu = expected_returns.mean_historical_return(prices=returns, returns_data = True, compounding=False, frequency=52)
print('Expected Returns')
print(mu)
print('\n')

# Risk Model: Create the variance-covariance matrix of returns for the stocks
cov_matrix = risk_models.sample_cov(prices=returns, returns_data = True, frequency=52)
print('Variance-Covariance Matrix')
print(cov_matrix)
print('\n')

# Extract tiskers and respective sectors
xlsx_file_path = '/home/qian/Documents/cbus_case_study/Resources/Stock List.xlsx'
sector_df = pd.read_excel(xlsx_file_path)

# Get the sector mapper ready for the section constrains
sector_df = sector_df[['Stock ID', 'Sector']]
sector_dict = sector_df.set_index('Stock ID')['Sector'].to_dict()

# Set sectors constrains
sector_lower = {'Financials': 0, 'Consumer Goods': 0.25, 'Energy': 0.1, 'Industrials': 0.25, 'Healthcare': 0}  
sector_upper = {'Financials': 0.10, 'Consumer Goods': 0.50, 'Energy': 0.30, 'Industrials': 0.50, 'Healthcare': 0.20}

# Create an EfficientFrontier instance and set sector constrains
ef = EfficientFrontier(expected_returns=mu, cov_matrix=cov_matrix, weight_bounds=(0, 1))
ef.add_constraint(lambda x: cvxpy.sum(x) == 1)
ef.add_constraint(lambda x: x<=0.1)
ef.add_sector_constraints(sector_mapper=sector_dict, sector_lower=sector_lower, sector_upper=sector_upper)
weights = ef.max_sharpe()

# Output weight plot of the tangency portfolio under the constrains
fig, ax = plt.subplots()
plotting.plot_weights(weights)

# Save the weights plot into the Resources folder
plt.savefig('/home/qian/Documents/cbus_case_study/Resources/Images/weights_sector_constrained_1png')

# Show the portfolio performance data
optimal_portfolio = base_optimizer.portfolio_performance(
    weights, expected_returns=mu, cov_matrix=cov_matrix, verbose=True, risk_free_rate=0.02
)

# Convert and join the two dictionaries:  the stock ticker with sectors and stock tickers with weights
linked_data = {ticker: {'value': value, 'sector': sector_dict[ticker]} for ticker, value in weights.items()}
labels = sector_dict.values()
values = [sum(data['value'] for data in linked_data.values() if data['sector'] == sector) for sector in set(labels)]

# Plot the pie chart of sectors distribution in the optimal portfolio
fig, ax = plt.subplots()
ax.pie(values, labels=set(labels), autopct='%1.1f%%', startangle=90)
plt.title('Sectors Distribution by Weight')

# Output and save the pie chart to the Resources folder
plt.savefig('/home/qian/Documents/cbus_case_study/Resources/Images/pie_chart_1.png')

# Starsign the Tangency Portfolio on the graph
ef_plot = EfficientFrontier(expected_returns=mu, cov_matrix=cov_matrix, weight_bounds=(0, 1))
ef_plot.add_constraint(lambda x: cvxpy.sum(x) == 1)
fig, ax = plt.subplots()
pplt.plot_efficient_frontier(ef_plot, ax=ax, show_assets=False)

# Starsign the Tangency Portfolio on the graph
ax.scatter(optimal_portfolio[1], optimal_portfolio[0], marker='*', color='g', s=200,label='Constrained Optimal Portfolio')
ax.legend()

# Plot the more advanced efficient frontier graph
# Generate 1000 random portfolios and put them on the graph
n_samples = 10000
w = np.random.dirichlet(np.ones(len(mu)), n_samples)
rets = w.dot(mu)
stds = np.sqrt(np.diag(w @ cov_matrix @ w.T))
sharpes = rets / stds
ax.scatter(stds, rets, marker=".", c=sharpes, cmap="viridis_r")

# Change the graph setting and output the graph into the Resources Folder
ax.set_title("Efficient Frontier with random portfolios")
ax.legend()
plt.tight_layout()
plt.savefig("/home/qian/Documents/cbus_case_study/Resources/Images/efficient_frontier_sectors_1.png", dpi=200)
