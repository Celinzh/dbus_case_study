# Dbus Case Study 🚎

[![Slides](/Resources/Images/Pictures/ppt_cover.png)](https://www.canva.com/design/DAF2omzYPZ0/7We1rvkrmcWJcc1cug6byw/edit?utm_content=DAF2omzYPZ0&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

## Project Overview
![Dbus](/Resources/Images/Pictures/DBUS.webp)

Dbus Super Fund has identified 24 stocks in which it wants to invest. This case study aims to analyze historical data to construct various mean-variance optimal portfolios with suitable constraints

## Executive Summary
![Image_1](/Resources/Images/weights_unconstrained.png)
![Image_2](/Resources/Images/weights_sector_constrained_10%cap.png)

![Image_1](/Resources/Images/efficient_frontier_unconstrained.png)
![Image_2](/Resources/Images/efficient_frontier_constrained.png)

## Logistic
The project logistics can be divided into two main parts:

1. Data Collection
The project utilized the Yahoo Finance API to extract weekly prices of the 24 stocks over the past three years. Adjusted close prices were calculated to derive weekly historical returns. Data quality was assessed, and outliers were capped at the 90th percentile.


2. Portfolio Constructions
The second part of the project primarily employed the pypfopt library for the portfolio construction process. The library facilitated the calculation of expected annual returns and risk models. It is noteworthy that the documentation provides extensive information on scholarly research regarding how to preprocess your dataset and choose appropriate mathematical models.

For instance, 'expected_returns.mean_historical_return' and 'risk_models.sample_cov' were utilized for expected returns and covariance, respectively. The documentation includes options such as cov_exp and semi-covariance. Due to time constraints in this project, default settings were used to calculate these two variables. However, I would be interested in dedicating more time to exploring different solvers and other parameters.

Two main portfolios were composed: one being the long-only, unconstrained, mean-variance optimal portfolio, and the other incorporating sector constraints.

My ideal sector composition for the five sectors among the given 24 stocks is based on my long-term sector growth forecast:
- Energy 20%
- Consumers 25%
- Healthcare 15%
- Industrial 25%
- Financials 15%

Adjusting the optimal portfolio to the default model is essential, given that the initial solution is purely quantitative. The embedded constraints will also account for the current economic landscape and macroeconomic projections, factors not reflected in historical returns.

Despite the portfolio performance forecast indicating that the second portfolio has a lower Sharpe ratio than the unconstrained first portfolio, it is expected to outperform the latter if the macroeconomy follows the broad projection.

To further explain the sectors allocation, the world is currently experiencing peaking interest rates over the past several years, implying that interest rates are expected to decrease in the near future. This is bearish for the financials sector, as banks thrive on high-interest loan rates. Conversely, it is largely bullish for the industrial and consumer goods sectors. With decreasing interest rates, customers will have increased purchasing power, and industrials will have more borrowing power to develop their infrastructures. The energy sector may also do well as more funding flows in when interest rates are low. However, the sector is estimated to be overvalued due to regulatory shifts and extensive public discussions. Healthcare is estimated to be neutral or bearish, as the industry experienced a boost during the Covid pandemic, and now it might recede from the peak post-pandemic.


Reference

Analytics Vidhya. (2021, May 5). Detecting and Treating Outliers: Treating the Odd One Out. Analytics Vidhya. https://www.analyticsvidhya.com/blog/2021/05/detecting-and-treating-outliers-treating-the-odd-one-out/

Ledoit, O., & Wolf, M. (2003). Honey, I Shrunk the Sample Covariance Matrix The Journal of Portfolio Management, 30(4), 110–119. https://doi.org/10.3905/jpm.2004.110
