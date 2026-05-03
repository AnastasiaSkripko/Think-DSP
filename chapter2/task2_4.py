from thinkdsp import TriangleSignal
from thinkdsp import decorate
import matplotlib.pyplot as plt

signal = TriangleSignal(440)
wave = signal.make_wave(duration=0.01, framerate=44100)
decorate(xlabel='Time (s)')
wave.plot()
plt.show()

spectrum = wave.make_spectrum()
print(spectrum.hs[0])

spectrum.hs[0] = 100

wave_2 = spectrum.make_wave()
decorate(xlabel='Time (s)')
wave_2.plot()
plt.show()