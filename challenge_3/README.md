# Module 3 Challenge

This project was created to sort through historical data for Bitcoin (BTC) on two exchanges: Bitstamp and Coinbase. 

Panda was used to identify any arbitrage opportunities existing by trading BTC between the two exchanges.


## Technologies

The project was buildt using Python 3.7 and several Python Libraries. 

```
import pandas as pd
from pathlib import Path
%matplotlib inline

```

Two csv datasets are used in this project: bitstamp.csv and coinbase.csv. The data range is the first quarter of 2018 (Jan 01 - Mar 31). Both datasets have approx. 129,000 rows of pricing information. In this analysis the closing price was used.
  