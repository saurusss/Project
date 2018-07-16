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

#Average 산출
def ma(gss,calcT):
    for i in calcT:
        maN =  gss['Adj Close'].rolling(window=i).mean()
        maC = 'MA' + str(i)
        gs.insert(len(gs.columns), maC, maN)
        #print(gs)

def make_graph(calcT):
    for i in calcT:
        plt.plot(gs.index, gs['MA'+str(i)], label='MA'+str(i))

menu = print_menu()             #종목 입력
gs = query_gs(menu)             #주가 조회
# calcT = [5, 20, 60, 120]      #이동평균 산출 종류 지정
calcT = [60, 120]               #이동평균 산출 종류 지정
ma(gs, calcT)                   #이동평균 산출

# draw Graph 
plt.plot(gs.index, gs['Adj Close'], label="Adj Close")
#plt.plot(gs.index, gs['Volume'], label="Volume")
make_graph(calcT)
plt.legend(loc='best')
plt.grid()
plt.show()

# def run():
#         while 1:
#         tickers = print_menu()
#         print(tickers)

# if __name__ == "__main__":
#     run()