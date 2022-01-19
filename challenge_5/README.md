# Module 5 Challenge
## Financial Planning with APIs and Simulations
The project has two parts: A financial planner for emergencies. The members will be able to use this tool to visualize their current savings. The members can then determine if they have enough reserves for an emergency fund.

A financial planner for retirement. This tool will forecast the performance of their retirement portfolio in 30 years. To do this, the tool will make an Alpaca API call via the Alpaca SDK to get historical price data for use in Monte Carlo simulations.


- - - 

## Technologies
### Libraries

The project was buildt using Python 3.7 and several python libraries listed below in a code block. 

```
import os
import requests
import json
import pandas as pd
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
from MCForecastTools import MCSimulation

%matplotlib inline

```
### API Calls
Links to API Calls for Cryptocurriency Assets

[Bitcoin](https://api.alternative.me/v2/ticker/Bitcoin/?convert=USD)


[Ethereum](https://api.alternative.me/v2/ticker/Ethereum/?convert=USD)

### Alpaca SDK
```
alpaca_api_key = os.getenv('ALPACA_API_KEY')
alpaca_secret_key = os.getenv('ALPACA_API_SECRET')

# Create the Alpaca tradeapi.REST object

alpaca = tradeapi.REST(
    alpaca_api_key,
    alpaca_secret_key,
    api_version='v2')
```

### Environment variables 
You'll need an alpaca api key and an alpaca secret key in order to use the alpaca REST api. Click this [link](https://app.alpaca.markets/login) to register and get your keys.

Once you get the keys you will need to store them locally outside of the financial planning tool.

### 
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




