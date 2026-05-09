from thinkdsp import SquareSignal
from thinkdsp import decorate
import matplotlib.pyplot as plt

signal = SquareSignal(1100)
wave = signal.make_wave(duration=0.5, framerate=10000)
spectrum = wave.make_spectrum()
spectrum.plot()
decorate(xlabel='Frequency (Hz)')
plt.show()

wave.write(filename='SquareSignal_1100.wav')