# Пилообразный сигнал линейно нарастает от –1 до 1, а затем резко падает до –1 и повторяется
# Напишите класс, называемый SawtoothSignal, расширяющий signal и предоставляющий evaluate для оценки пилообразного сигнала

from thinkdsp import PI2, unbias, Sinusoid, normalize
from thinkdsp import decorate
import numpy as np
import matplotlib.pyplot as plt

class SawtoothSignal(Sinusoid):
    def evaluate(self, ts):
        # ts - последовательность моментов времени, в которых оценивается сигнал
        cycles = self.freq * ts + self.offset / PI2
        frac , _ = np.modf(cycles) # np.modf возвращает 2 массива: дробную и целую части. Второй игнорируется
        ys = 2*(frac - 0.5)
        ys = normalize(unbias(ys), self.amp) # unbias смещает сигнал так, что он центрируется по 0, normalize нормализует до заданной амплитуды amp
        return ys

signal = SawtoothSignal(200)
decorate(xlabel='Time (s)')
signal.plot()
plt.show()

wave = signal.make_wave(duration=0.5, framerate=10000)
spectrum = wave.make_spectrum()
spectrum.plot()
decorate(xlabel='Frequency (Hz)')
plt.show()

from numpy.fft import rfftfreq

hs = np.fft.rfft(wave.ys)                       # NumPu-массив комплексных чисел, представляющих амплитуду и фазу каждой частотной компоненты в сигнале
fs = rfftfreq(len(wave.ys), 1/wave.framerate)   # массив, содержащий частоты, соответствующие hs
magnitude = np.absolute(hs)                     # амплитуда на каждой частоте
print("Частоты:", fs)
print("Амплитуда:", magnitude)