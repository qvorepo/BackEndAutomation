import pandas as pd

def convert_people_cell(cell):
    if cell=='n.a.':
        return 'sam walton'
    return cell
pf=pd.read_excel("utilities/stock_data.xlsx", "Sheet1", converters= {'people': convert_people_cell})
pf.to_excel("utilities/new_stock_data.xlsx", sheet_name="stocks", startrow=0, startcol=2, index=False)
