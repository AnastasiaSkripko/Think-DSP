from thinkdsp import read_wave
from thinkdsp import decorate
import matplotlib.pyplot as plt

wave = read_wave('chapter3/72475__rockwehrmann__glissup02.wav')
spectrogram = wave.make_spectrogram(512)
decorate(xlabel='Time(s)', ylabel='Frequency (Hz)')
spectrogram.plot(high=7500)
plt.show()