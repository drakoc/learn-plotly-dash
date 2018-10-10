# creating a chart with real data

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('nst-est2017-alldata.csv')


# select only rows where DIVISION is 1

df2 = df[df['DIVISION'] == '1']


# set NAME column as DataFrame index & don't create a new object (inplace=True)

df2.set_index('NAME', inplace=True)

# selecting columns which start with 'POP'

list_of_pop_col = [col for col in df2.columns if col.startswith('POP')]
df3 = df2[list_of_pop_col]

# creating traces for all indexes using List Comprehensions

data = [go.Scatter(x=df3.columns,
                   y=df3.loc[name],
                   mode='lines',
                   name=name) for name in df3.index]

pyo.plot(data, filename='line-chart-3-plot.html')
