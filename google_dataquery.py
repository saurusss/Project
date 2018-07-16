import pandas as pd 
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader as web
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as numpy
import seaborn as sns


import warnings
warnings.simplefilter(action = "ignore", category = FutureWarning)

from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

#%matplotlib inline

#plt.rcParams['axes.unicode_minus'] = False
#plt.rc('figure', figsize=(10, 6))

start = datetime(2015, 1, 1)
end = datetime.now()
print(end)

ka = web.data.get_data_google('KRX:003490', start, end)

print(ka.head(10))