# Import libraries
from pypfopt import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from pypfopt import plotting
import cvxpy
import pypfopt.plotting as pplt

# Import data from Resources folder
xlsx_file_path = '/home/qian/Documents/cbus_case_study/Resources/cleaned_returns.xlsx'
returns = pd.read_excel(xlsx_file_path)
returns.set_index('Date', inplace =True)

## Expected Returns
# Forcasts expected returns by taking the historical average returns from the stocks in the list
mu = expected_returns.mean_historical_return(prices=returns, returns_data = True, compounding=False, frequency=52)
print('Expected Returns')
print(mu)
print('\n')

# Plot and output the return graph
cmap = cm.get_cmap('Purples')
plt.figure(figsize=(10, 6))
mu.plot(kind='bar', color=cmap(mu / mu.max()), edgecolor='black')
plt.title('Expected Returns')
plt.xlabel('Stocks')
plt.ylabel('Expected Returns')
plt.xticks(rotation=30, ha='right') 
plt.savefig('/home/qian/Documents/cbus_case_study/Resources/Images/mean.png')

## Risk model
# Create the variance-covariance matrix of returns for the stocks
cov_matrix = risk_models.sample_cov(prices=returns, returns_data = True, frequency=52)
print('Variance-Covariance Matrix')
print(cov_matrix)
print('\n')

# Plot and save the correlation matrix
fig, ax = plt.subplots()
plt.figure(figsize=(10, 6))
plotting.plot_covariance(cov_matrix, ax=ax, plot_correlation=True)
plt.savefig('/home/qian/Documents/cbus_case_study/Resources/Images/covariance_matrix.png')

# Calculate individual stock sharpe ratios
sharpe_ratios = (mu - 0.02) / np.sqrt(np.diag(cov_matrix))

# Plot the sharpe ratios for each stock
cmap = cm.get_cmap('Blues')
plt.figure(figsize=(10, 6))
sharpe_ratios.plot(kind='bar', color=cmap(mu / mu.max()), edgecolor='black')
plt.title('Sharpe Ratios of Individual Stocks')
plt.xlabel('Stocks')
plt.ylabel('Sharpe Ratio')
plt.xticks(rotation=45, ha='right')

# Adjust layout to prevent xticks overlap
plt.tight_layout()

# Save the graph in the Resources folder
plt.savefig('/home/qian/Documents/cbus_case_study/Resources/Images/Sharpe_ratio.png')

## Compute the efficient frontier - long-only - no other constrains
# Create an EfficientFrontier instance
# Create a new Efficient Frontier instance for plotting
ef_plot = EfficientFrontier(expected_returns=mu, cov_matrix=cov_matrix, weight_bounds=(0, 1))

# Get the weights for plotting
weights_plot = ef_plot.max_sharpe()
print('The weight plot of the portfolio:')
print(weights_plot)

# Output the weight plot into the Resources folder
fig, ax = plt.subplots()
plotting.plot_weights(weights_plot)
plt.savefig('/home/qian/Documents/cbus_case_study/Resources/Images/weights_unconstrained.png')

# Calculate and display the portfolio performance
ef_plot.portfolio_performance(verbose=True)

# Create a new EfficientFrontier instance to make sure all the weights add up to one
ef_constraints = EfficientFrontier(expected_returns=mu, cov_matrix=cov_matrix, weight_bounds=(0, 1))
ef_constraints.add_constraint(lambda x: cvxpy.sum(x) == 1)

# Plot the efficient frontier
fig, ax = plt.subplots()
pplt.plot_efficient_frontier(ef_constraints, ax=ax, show_assets=False)

# Starsign the tangency portfolio on teh graph
ax.scatter(ef_plot.portfolio_performance()[1], ef_plot.portfolio_performance()[0], marker='*', color='r', s=200,label='Tangency Portfolio')
ax.legend()

# Generate random portfolios to advance the graph
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
plt.savefig('/home/qian/Documents/cbus_case_study/Resources/Images/efficient_frontier_unconstrained.png', dpi=200)
