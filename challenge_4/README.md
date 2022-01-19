# Module 4 Challenge
## Analyzing Portfolio Risk and Return
This project is a quantitative analysis for a FinTech investing platform. Algorithms were created to provide best investment options to clients from a selection of top tier funds (whales). The goal is to determine the fund with the most investment potential based on key risk-management metrics: the daily returns, standard deviations, Sharpe ratios, and betas.

At the completion of the analysis, two funds are recommened as investments for the client. The funds returns are compared against the returns of the overall market index of the S&P 500. 



- - - 

## Technologies
The project was buildt using Python 3.7 and several python libraries. 

```
import pandas as pd
from pathlib import Path
import numpy as np
%matplotlib inline

```

The daily closing price (nav) of the four funds and the S&P 500 is stored in a single csv file. Pathlib is used to import the file for analysis. There are approx 1500 rows of data. We then create a dataframe and analyze the data in Panda.

```
NAV_df = pd.read_csv(
    Path("./Resources/whale_navs.csv"),
    index_col = "date",
    parse_dates=True,
    infer_datetime_format=True)

NAV_df.head()

```
- - - 
## Installation Guide
If you need help with installing Python 3.7 please use this link to Python guides.

[Python documentation](https://docs.python.org/3.7/)


- - - 
## Contributors
This was a student project but that had criticial contributions from the head instructor and very able TA's.


- - - 
## License
Any usage of this app should be authorized from Columbia Univesity bookcamp.

- - - 
- - -
## Notebook naming
The finished project is in the Notebook named whale_analysis.ipynb
