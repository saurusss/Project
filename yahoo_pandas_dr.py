#pandas-datareaer 오류 수정
import datetime
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
##
#from pandas_datareader import data  
import pandas_datareader as pdr
import fix_yahoo_finance as yf
yf.pdr_override()

start_date = '1996-05-06' #startdate를 1996년으로 설정해두면 가장 오래된 데이터부터 전부 가져올 수 있다.

tickers = '067160.KQ' #1 아프리카tv와 네이버의 ticker(종목코드)
afreeca = pdr.data.get_data_yahoo(tickers, start_date)

tickers = '035420.KS' #1 아프리카tv와 네이버의 ticker(종목코드)
naver = pdr.data.get_data_yahoo(tickers, start_date)

print(naver)
print(afreeca)