import pandas as pd
from thinkdsp import Wave, decorate
import matplotlib.pyplot as plt
import numpy as np

def serial_corr(wave, lag=1):
    N = len(wave)
    y1 = wave.ys[lag:]
    y2 = wave.ys[:N-lag]
    corr = np.corrcoef(y1, y2)[0, 1]
    return corr

def autocorr(wave):
    lags = np.arange(len(wave.ys)//2)
    corrs = [serial_corr(wave, lag) for lag in lags]
    return lags, corrs

df = pd.read_csv('chapter5/BTC_USD_2013-10-01_2020-03-26-CoinDesk.csv', 
                 parse_dates=[0])
ys = df['Closing Price (USD)']
ts = df.index
wave = Wave(ys, ts, framerate=1)
wave.plot()
decorate(xlabel='Time (days)')
plt.show()

lags, corrs = autocorr(wave)
plt.plot(lags, corrs)
decorate(xlabel='Lag', 
         ylabel='Correlation')
plt.show()