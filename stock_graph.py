#pandas-datareaer 오류 수정
import datetime
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
##
#from pandas_datareader import data  
import pandas_datareader as pdr
import fix_yahoo_finance as yf
yf.pdr_override()
import matplotlib.pyplot as plt

def query_gs(code):
    start_date = '1996-05-06' #startdate를 1996년으로 설정해두면 가장 오래된 데이터부터 전부 가져올 수 있다.
    # tickers = '067160.KQ' #  아프리카tv ticker(종목코드)
    # afreeca = pdr.data.get_data_yahoo(tickers, start_date)
    # print(afreeca)
    #tickers = '035420.KS' #  네이버의 ticker(종목코드)
    tickers = '.'.join(code[:2])
    gs = pdr.data.get_data_yahoo(tickers, code[2])
    return gs

def print_menu():
    print()
    menu1 = input("종목코드(6자리): ")
    menu2 = input("KS or KQ) : ")
    menu3 = input("start date : ")
    menu = [menu1, menu2, menu3]
    return menu

menu = print_menu()
gs = query_gs(menu)
print(gs)
# 주가 이동평균 계산
ma5 = gs['Adj Close'].rolling(window=5).mean()
gs.insert(len(gs.columns), "MA5", ma5)

ma20 = gs['Adj Close'].rolling(window=20).mean()
gs.insert(len(gs.columns), "MA20", ma20)

ma60 = gs['Adj Close'].rolling(window=60).mean()
gs.insert(len(gs.columns), "MA60", ma60)
ma120 = gs['Adj Close'].rolling(window=120).mean()
gs.insert(len(gs.columns), "MA120", ma120)

plt.plot(gs.index, gs['Adj Close'], label="Adj Close")
plt.plot(gs.index, gs['MA5'], label="MA5")
plt.plot(gs.index, gs['MA20'], label="MA20")
plt.plot(gs.index, gs['MA60'], label="MA60")
plt.plot(gs.index, gs['MA120'], label="MA120")
plt.legend(loc='best')
plt.grid()
plt.show()

# def print_menu():
#     print()
#     menu[0] = input("종목코드 6자리": ")
#     menu[1] = input("KS or KQ) : ")
#     return menu

# def run():
#         while 1:
#         tickers = print_menu()
#         print(tickers)

# if __name__ == "__main__":
#     run()