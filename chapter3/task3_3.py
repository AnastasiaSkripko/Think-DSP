from thinkdsp import PI2, unbias, Chirp, normalize
from thinkdsp import decorate
import numpy as np
import matplotlib.pyplot as plt

class SawtoothChirp(Chirp):
    def evaluate(self, ts):
        freqs = np.linspace(self.start, self.end, len(ts)) #создаем массив частот из кол-ва ts значений
        dts = np.diff(ts, prepend=0) #находим разницу между соседними моментами времени
        dphis = PI2 * freqs * dts #приращение фазы, насколько продвинулся сигнал по своему циклу за маленький промежуток времени
        phases = np.cumsum(dphis) 
        cycles = phases / PI2
        frac, _ = np.modf(cycles) #берем только дробную часть
        # unbias(frac) сдвигает сигнал так, чтобы среднее было 0
        # например было [0, 1], стало [-0.5, 0.5]
        ys = normalize(unbias(frac), self.amp)
        return ys
    
signal = SawtoothChirp(start=2500, end=3000)
wave = signal.make_wave(duration=1, framerate=20000)
spectrum = wave.make_spectrum(512)
decorate(xlabel='Frequency (Hz)')
spectrum.plot()
plt.show()
wave.write(filename='signal_2.wav')