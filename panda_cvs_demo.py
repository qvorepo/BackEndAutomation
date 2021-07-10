import pandas as pd
pf=pd.read_csv("utilities/stock_data.csv", header=1, na_values=
    {'eps': ['not available', 'n.a.'],
     'revenue': ['not available', 'n.a.',-1]

    })
pf.to_csv('utilities/new_stock_data.csv', index=False, columns=['tickers', 'eps'])

