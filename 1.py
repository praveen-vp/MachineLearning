import pandas as pd
import quandl

df = quandl.get('WIKI/GOOGL')

## Adj. Open    Adj. High     Adj. Low   Adj. Close
df['HLT_PCT'] = (df['Adj. High'] - df['Adj. Close'])/df['Adj. Open'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open'])/df['Adj. Open'] * 100.0

df = df[['Adj. Close', 'HLT_PCT', 'PCT_change', 'Adj. Volume']]
print(df.head())

