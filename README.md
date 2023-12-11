# Dbus Case Study 🚎
## Project Overview
[![Slides](/Resources/Images/Pictures/ppt_cover.png)](https://www.canva.com/design/DAF2omzYPZ0/7We1rvkrmcWJcc1cug6byw/edit?utm_content=DAF2omzYPZ0&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

Dbus Super Fund has identified 24 stocks in which it wants to invest. This case study aims to analyse historical data to construct various mean-variance optimal portfolios with suitable constraints

## Executive Summary
This case study found that even though the mean-variance optimal portfolio has the maximum sharpe ratio among all the possible portfolio, it is very less diversified, with only a few stocks invested in a few sectors.

This case study explores the opportunity to integrate macroeconomics into a quantitative investment approach by imposing constraints using the portfolio optimiser library and functions. The adjusted portfolio is invested in more diversified sectors, covering a larger number of stocks among the 24 available, thereby avoiding the risks associated with putting all eggs in one basket.

![Image_1](/Resources/Images/weights_unconstrained.png)
![Image_1](/Resources/Images/efficient_frontier_unconstrained.png)

The red star represents the tangency portfolio, which has the highest Sharpe ratio when there are no constraints in the long-only mean-variance portfolio. In this portfolio, only 6 out of the 24 stocks and 4 out of 5 sectors are invested. Therefore, the second portfolio aims to invest in more diversified sectors and include more stocks to mitigate individual stock risks.

![Image_2](/Resources/Images/weights_sector_constrained_1png.png)
![Image_2](/Resources/Images/efficient_frontier_sectors_1.png)

The green star represents the optimal portfolio when sector constraints are applied. Please find the details of these constraints in the logistic section.

## Logistic
The project logistics can be divided into two main parts:

1. Data Collection
The project utilized the Yahoo Finance API to extract weekly prices of the 24 stocks over the past three years. Adjusted close prices were calculated to derive weekly historical returns. Data quality was assessed, and outliers were capped at the 90th percentile.


2. Portfolio Constructions
The second part of the project primarily employed the pypfopt library for the portfolio construction process. The library facilitated the calculation of expected annual returns and risk models. It is noteworthy that the documentation provides extensive information on scholarly research regarding how to preprocess dataset and choose appropriate mathematical models and solvers.

Two main portfolios were composed: one being the long-only, unconstrained, mean-variance optimal portfolio, and the other incorporating sector constraints.

My ideal sector composition for the five sectors among the given 24 stocks is based on my long-term sector growth forecast:
- Energy 20%
- Consumers 25%
- Healthcare 15%
- Industrial 25%
- Financials 15%

Adjusting the optimal portfolio to the default model is essential, given that the initial solution is purely quantitative. The embedded constraints will also account for the current economic landscape and macroeconomics projections, factors that is not likely to be reflected in historical returns.

Despite the portfolio performance forecast indicating that the second portfolio has a lower Sharpe ratio than the unconstrained first portfolio, it is expected to outperform the latter if the macroeconomy follows the broad projection.

Bsed on current data, the world is currently experiencing peaking interest rates over the past several years, implying that interest rates are likely to decrease in the near future. This could potentially have a bearish impact on the financials sector, given that banks often thrive on high-interest loan rates. Conversely, it might be largely bullish for the industrial and consumer goods sectors. If interest rates continue to decrease, there's a chance that customers could gain increased purchasing power, and industrials might have more borrowing power to develop their infrastructures. The energy sector, in theory, could also benefit as more funding might flow in during periods of low interest rates. However, it's worth noting that this sector is speculated to be overvalued due to regulatory shifts and extensive public discussions. Healthcare, on the other hand, is estimated to be neutral or potentially bearish. The industry experienced a boost during the Covid pandemic, and now there's uncertainty about whether it will recede from the peak post-pandemic.

However, the world is changing quickly now, and the current balance may not be suitable for the near future. Constant monitoring and forecasting of future trends are required to rebalance the portfolio towards a different macro environment.


## Reference

Analytics Vidhya. (2021, May 5). Detecting and Treating Outliers: Treating the Odd One Out. Analytics Vidhya. https://www.analyticsvidhya.com/blog/2021/05/detecting-and-treating-outliers-treating-the-odd-one-out/

Besser, N. (2022, March 3). Python for Finance: Portfolio Optimization and the Value of Diversifying. Medium. https://nicobesser.medium.com/python-for-finance-portfolio-optimization-and-the-value-of-diversifying-99ef8e5cfbdc

Doeswijk, R., & Van Vliet, P. (2011). Global tactical sector allocation: A quantitative approach. The Journal of Portfolio Management, 38(1), 29-47.

Francis, J. C., & Kim, D. (2013). Modern portfolio theory: Foundations, analysis, and new developments. John Wiley & Sons.

Ledoit, O., & Wolf, M. (2003). Honey, I Shrunk the Sample Covariance Matrix The Journal of Portfolio Management, 30(4), 110–119. https://doi.org/10.3905/jpm.2004.110