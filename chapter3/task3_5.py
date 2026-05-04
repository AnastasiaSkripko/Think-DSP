from thinkdsp import decorate
import matplotlib.pyplot as plt
from thinkdsp import Chirp, Wave
from thinkdsp import PI2, unbias, Chirp, normalize
import numpy as np

class TromboneGliss(Chirp):
    def evaluate(self, ts):
        lengths = np.linspace(1/self.start, 1/self.end, len(ts)) #создаем массив частот из кол-ва ts значений
        freqs = 1 / lengths
        dts = np.diff(ts, prepend=0) #находим разницу между соседними моментами времени
        dphis = PI2 * freqs * dts #приращение фазы, насколько продвинулся сигнал по своему циклу за маленький промежуток времени
        phases = np.cumsum(dphis) 
        cycles = phases / PI2
        frac, _ = np.modf(cycles) #берем только дробную часть
        # unbias(frac) сдвигает сигнал так, чтобы среднее было 0
        # например было [0, 1], стало [-0.5, 0.5]
        ys = normalize(unbias(frac), self.amp)
        return ys
    
signal_1 = TromboneGliss(start=262, end=349)
signal_2 = TromboneGliss(start=349, end=262)

wave_1 = signal_1.make_wave(duration=2, framerate=20000)
wave_2 = signal_2.make_wave(duration=2, framerate=20000)

ys = np.concatenate((wave_1.ys, wave_2.ys))
wave = Wave(ys, framerate=20000)

spectrogram = wave.make_spectrogram(512)
decorate(xlabel='Time(s)', ylabel='Frequency (Hz)')
spectrogram.plot(high=6000)
plt.show()
wave.write(filename='TromboneGliss.wav')
