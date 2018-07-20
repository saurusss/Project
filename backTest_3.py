#pandas-datareaer 오류 수정
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
#from pandas_datareader import data  
import pandas_datareader as web
import fix_yahoo_finance as yf
yf.pdr_override()
##
import datetime
import matplotlib.pyplot as plt
from zipline.api import order, symbol
from zipline.algorithm import TradingAlgorithm

# start = datetime.datetime(2010, 1, 1)
# end = datetime.datetime(2016, 3, 19)
# data = web.DataReader("AAPL", "yahoo", start, end)
# data = web.data.get_data_yahoo("AAPL", start, end)

def print_menu():
    print()
    menu0 = input("종목코드(6자리): ")
    menu1 = input("KS or KQ : ")
    menu2 = input("start date : ")
    menu3 = input("end date : ")
    menu = [menu0, menu1, menu2, menu3]
    return menu

def query_gs(code):
    # start_date = '1996-05-06' #startdate를 1996년으로 설정해두면 가장 오래된 데이터부터 전부 가져올 수 있다.
    # tickers = '067160.KQ' #  아프리카tv ticker(종목코드)
    # afreeca = pdr.data.get_data_yahoo(tickers, start_date)
    # print(afreeca)
    #tickers = '035420.KS' #  네이버의 ticker(종목코드)
    tickers = '.'.join(code[:2])
    gs = web.data.get_data_yahoo(tickers, code[2], code[3])
    return gs

menu = print_menu()             #종목 입력
data = query_gs(menu)           #주가 조회


print(data)
plt.plot(data.index, data['Adj Close'])
plt.show()


# back test
data = data[['Adj Close']]
data.columns = [menu[0]]
data = data.tz_localize('UTC')

def initialize(context):
    context.i = 0
    context.sym = symbol('AAPL')
    context.hold = False

def handle_data(context, data):
    context.i += 1
    if context.i < 20:
        return
    buy = False
    sell = False

    ma5 = data.history(context.sym, 'price', 5, '1d').mean()
    ma20 = data.history(context.sym, 'price', 20, '1d').mean()

    if ma5 > ma20 and context.hold == False:
        order_target(context.sym, 100)
        context.hold = True
        buy = True
    elif ma5 < ma20 and context.hold == True:
        order_target(context.sym, -100)
        context.hold = False
        sell = True

    record(AAPL=data.current(context.sym, "price"), ma5=ma5, ma20=ma20, buy=buy, sell=sell)

algo = TradingAlgorithm(initialize=initialize, handle_data=handle_data)
result = algo.run(data)

plt.plot(result.index, result.portfolio_value)
plt.show()

plt.plot(result.index, result.ma5)
plt.plot(result.index, result.ma20)
plt.legend(loc='best')


plt.plot(result.ix[result.buy == True].index, result.ma5[result.buy == True], '^')
plt.plot(result.ix[result.sell == True].index, result.ma5[result.sell == True], 'v')
plt.show()