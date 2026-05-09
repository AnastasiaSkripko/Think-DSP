from thinkdsp import read_wave
from thinkdsp import decorate
import matplotlib.pyplot as plt

wave = read_wave('chapter4/132736__ciccarelli__ocean-waves.wav')
segment = wave.segment(start=2, duration=1.0)
spectrum = segment.make_spectrum()

segment_2 = wave.segment(start=3, duration=1.0)
spectrum_2 = segment_2.make_spectrum()
spectrum_2.plot_power()

spectrum.plot_power()
decorate(xlabel='Frequency (Hz)',
         ylabel='Power')
spectrum_2.plot_power()
decorate(xlabel='Frequency (Hz)',
         ylabel='Power')
plt.show()