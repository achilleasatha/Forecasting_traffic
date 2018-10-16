import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


with open('data.txt', 'r') as fin:
    data = fin.read().splitlines(True)
with open('data2.txt', 'w') as fout:
    fout.writelines(data[1:])

data = pd.read_csv('data2.txt', sep=" ", header=None)
data.columns = ['month', 'nan', 'count']
data = data.drop(['nan'], axis=1)
data = data.set_index('month')
print(data.head())
plt.plot(data['count'])
plt.savefig('traffic.png')

def return_output():
    output = ''
    for line in predictions:
        output += line
    return output
