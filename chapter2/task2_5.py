from thinkdsp import TriangleSignal
from thinkdsp import decorate
import matplotlib.pyplot as plt

def mod_spectrum(spectrum):
    # hs NumPu-массив комплексных чисел, представляющих амплитуду и фазу каждой частотной компоненты в сигнале
    # fs массив, содержащий частоты, соответствующие hs
    spectrum.hs[0] = 0;
    for i in range(1, len(spectrum.hs)):
        spectrum.hs[i] /= spectrum.fs[i]

signal = TriangleSignal(440)
wave = signal.make_wave(duration=0.5, framerate=44100)
wave.write(filename='wave1.wav')

spectrum = wave.make_spectrum()
decorate(xlabel='Frequency (Hz)')
spectrum.plot(high=10000)
plt.show()

mod_spectrum(spectrum)
decorate(xlabel='Frequency (Hz)')
spectrum.plot(high=10000)
plt.show()

wave_2 = spectrum.make_wave()
wave_2.write(filename='wave2.wav')