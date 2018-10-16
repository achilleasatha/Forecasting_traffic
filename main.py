import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
import functions
from pandas import Series


ts = Series.from_csv('data.csv', header=None)
ts.plot()

new_index = pd.date_range('2013-01','2017-12', freq='MS').strftime("%Y-%m").tolist()
ts.index = new_index

test = pd.Grouper(ts.values)

# groups = ts.groupby(test)
functions.test_stationarity(ts)

def return_output():
    output = ''
    for line in predictions:
        output += line
    return output
