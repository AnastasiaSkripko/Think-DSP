from thinkdsp import decorate
import matplotlib.pyplot as plt
import numpy as np
from thinkdsp import read_wave

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

def estimate_fundamental(segment, low=70, high=150):
    lags, corrs = autocorr(segment)
    lag = np.array(corrs[low:high]).argmax() + low
    period = lag / segment.framerate
    frequency = 1 / period
    return frequency

wave = read_wave('chapter5/28042__bcjordan__voicedownbew.wav')
wave.normalize()
spectrogram = wave.make_spectrogram(seg_length=1024)
spectrogram.plot(high=4200)
decorate(xlabel='Time (s)', 
         ylabel='Frequency (Hz)')
plt.show()

duration = 0.01
step = 0.05
starts = np.arange(0.0, 1.4, step)

ts = []
freqs = []

for start in starts:
    ts.append(start + step/2)
    segment = wave.segment(start=start, duration=duration)
    freq = estimate_fundamental(segment)
    freqs.append(freq)

wave.make_spectrogram(2048).plot(high=900)
plt.plot(ts, freqs, color='white')
decorate(xlabel='Time (s)', 
         ylabel='Frequency (Hz)')
plt.show()