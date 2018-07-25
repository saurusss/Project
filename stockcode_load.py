import pandas as pd
import pickle
# stockcode = pd.read_csv('c:\\TEMP\\stockcode.csv', index_col=0)
# print(stockcode)
stock_df_file ='stockcodefile.data'
f = open(stock_df_file, 'rb')
# Load the object from the file
storedlist = pickle.load(f)
print(storedlist)