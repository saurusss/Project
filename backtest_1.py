#pandas-datareaer 오류 수정
import datetime
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
#from pandas_datareader import data  
import pandas_datareader as web
import fix_yahoo_finance as yf
yf.pdr_override()
##
import matplotlib.pyplot as plt
from zipline.api import order, symbol
from zipline.algorithm import TradingAlgorithm

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2016, 3, 19)
# data = web.DataReader("AAPL", "yahoo", start, end)
data = web.data.get_data_yahoo("AAPL", start, end)
print(data)
plt.plot(data.index, data['Adj Close'])
plt.show()


# back test
data = data[['Adj Close']]
data.columns = ['AAPL']
data = data.tz_localize('UTC')

def initialize(context):
    pass

def handle_data(context, data):
    order(symbol('AAPL'), 1)

algo = TradingAlgorithm(initialize=initialize, handle_data=handle_data)
result = algo.run(data)

plt.plot(result.index, result.portfolio_value)
plt.show()