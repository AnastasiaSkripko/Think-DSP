from thinkdsp import UncorrelatedGaussianNoise
from scipy.stats import linregress
from thinkdsp import decorate, PI2
import matplotlib.pyplot as plt
import numpy as np
import timeit
import scipy.fftpack

signal = UncorrelatedGaussianNoise()
noise = signal.make_wave(duration=1.0, framerate=16384)

loglog = dict(xscale='log', yscale='log')
def plot_bests(ns, bests):    
    decorate(**loglog) 
    plt.plot(ns, bests)
    plt.show() 

    x = np.log(ns)
    y = np.log(bests)
    t = linregress(x,y)
    slope = t[0]
    return slope

def analyze1(ys, fs, ts):
    args = np.outer(ts, fs) # создаёт матрицу размером len(ts) × len(fs)
    M = np.cos(PI2 * args)
    amps = np.linalg.solve(M, ys)
    return amps

def analyze2(ys, fs, ts):
    args = np.outer(ts, fs)
    M = np.cos(PI2 * args)
    amps = np.dot(M, ys) / 2
    return amps

def run_speed_test(ns, func):
    results = []
    for N in ns:
        ts = (0.5 + np.arange(N)) / N
        freqs = (0.5 + np.arange(N)) / 2
        ys = noise.ys[:N]    
        # Измеряем время выполнения func
        # timeit.timeit() возвращает время в секундах
        timer = timeit.Timer(lambda: func(ys, freqs, ts))
        result = timer.timeit(number=1)  # выполняем 1 раз    
        results.append(result)
    return results

def scipy_dct(ys, freqs, ts):
    return scipy.fftpack.dct(ys, type=3)

ns = 2 ** np.arange(6, 13)
bests = run_speed_test(ns, analyze1)
slope = plot_bests(ns, bests)
print(slope)

bests2 = run_speed_test(ns, analyze2)
slope2 = plot_bests(ns, bests2)
print(slope2)

bests3 = run_speed_test(ns, scipy_dct)
slope3 = plot_bests(ns, bests3)
print(slope3)

plt.plot(ns, bests, label='analyze1')
plt.plot(ns, bests2, label='analyze2')
plt.plot(ns, bests3, label='fftpack.dct')
decorate(xlabel='Wave length (N)', ylabel='Time (s)', **loglog)
plt.show()