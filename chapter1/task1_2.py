from thinkdsp import decorate
import matplotlib.pyplot as plt
from thinkdsp import read_wave

def filter_wave(wave, start, duration):
    segment = wave.segment(start, duration)
    spectrum = segment.make_spectrum()
    filtered = spectrum.make_wave()
    filtered.normalize()
    filtered.apodize()
    filtered.plot()
    decorate(xlabel='Time (s)')
    plt.show()

wave = read_wave('120994__thirsk__120-oboe.wav')
filter_wave(wave, 0, 0.5)
