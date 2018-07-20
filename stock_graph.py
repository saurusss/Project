#pandas-datareaer 오류 수정
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
##
#from pandas_datareader import data  
import pandas_datareader as pdr
import fix_yahoo_finance as yf
yf.pdr_override()

import matplotlib.pyplot as plt
import datetime

def print_menu():
    '''종목 입력'''
    print()
    menu1 = input("종목코드(6자리): ")
    menu2 = input("KS or KQ) : ")
    menu3 = input("start date : ")
    menu = [menu1, menu2, menu3]
    return menu
    
def query_gs(code):
    '''주식가격 조회'''
    start_date = '1996-05-06' #startdate를 1996년으로 설정해두면 가장 오래된 데이터부터 전부 가져올 수 있다.
    # tickers = '067160.KQ' #  아프리카tv ticker(종목코드)
    # afreeca = pdr.data.get_data_yahoo(tickers, start_date)
    # print(afreeca)
    #tickers = '035420.KS' #  네이버의 ticker(종목코드)
    tickers = '.'.join(code[:2])
    gs = pdr.data.get_data_yahoo(tickers, code[2])
    return gs


#Average 산출
def ma(gss,calcT):
    '''average 산출'''
    for i in calcT:
        maN =  gss['Adj Close'].rolling(window=i).mean()
        maC = 'MA' + str(i)
        gs.insert(len(gs.columns), maC, maN)
        #print(gs)

menu = print_menu()
gs = query_gs(menu)
# calcT = [5, 20, 60, 120]
calcT = [60, 120]
ma(gs, calcT)


# ma5 = ma(gs, 5)
# ma20 =ma(gs, 20)
# ma60 = ma(gs,60)
# ma120 = ma(gs,120)

# 주가 이동평균 계산
# ma5 = gs['Adj Close'].rolling(window=5).mean()
# gs.insert(len(gs.columns), "MA5", ma5)

# ma20 = gs['Adj Close'].rolling(window=20).mean()
# gs.insert(len(gs.columns), "MA20", ma20)

# ma60 = gs['Adj Close'].rolling(window=60).mean()
# gs.insert(len(gs.columns), "MA60", ma60)
# ma120 = gs['Adj Close'].rolling(window=120).mean()
# gs.insert(len(gs.columns), "MA120", ma120)

plt.plot(gs.index, gs['Adj Close'], label="Adj Close")


def make_graph(calcT):
    for i in calcT:
        plt.plot(gs.index, gs['MA'+str(i)], label='MA'+str(i))

make_graph(calcT)
# plt.plot(gs.index, gs['MA5'], label="MA5")
# plt.plot(gs.index, gs['MA20'], label="MA20")
# plt.plot(gs.index, gs['MA60'], label="MA60")
# plt.plot(gs.index, gs['MA120'], label="MA120")
plt.legend(loc='best')
plt.grid()
plt.show()

# def run():
#         while 1:
#         tickers = print_menu()
#         print(tickers)

# if __name__ == "__main__":
#     run()