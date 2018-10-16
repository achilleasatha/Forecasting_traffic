import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
import functions


ts = pd.Series.from_csv('data.csv', header=None)
ts.plot()

new_index = pd.date_range('2013-01','2017-12', freq='MS').strftime("%Y-%m").tolist()
ts.index = new_index

functions.test_stationarity(ts)

ts.index = pd.to_datetime(ts.index)
groups = ts['2013-01':'2017-12'].groupby(pd.TimeGrouper('A'))
years = pd.DataFrame()
plt.figure()
i = 1
n_groups = len(groups)
for name, group in groups:
    plt.subplot((n_groups*100) + 10 + i)
    i += 1
    plt.plot(group)
# plt.show()

ts.hist()
ts.plot(kind='kde')
# plt.show()

def return_output():
    output = ''
    for line in predictions:
        output += line
    return output
