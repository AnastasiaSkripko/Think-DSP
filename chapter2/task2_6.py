from thinkdsp import SawtoothSignal
from thinkdsp import decorate
import matplotlib.pyplot as plt

signal = SawtoothSignal(100)
wave = signal.make_wave(duration=0.5, framerate=10000)
spectrum = wave.make_spectrum()
decorate(xlabel='Frequency (Hz)')
spectrum.plot(high=2000)
plt.show()

for i in range(1, len(spectrum.hs)):
    spectrum.hs[i] *= (1 / i)

decorate(xlabel='Frequency (Hz)')
spectrum.plot(high=2000)
plt.show()