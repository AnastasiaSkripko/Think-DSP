from thinkdsp import read_wave
from thinkdsp import decorate
import matplotlib.pyplot as plt

wave = read_wave('chapter3/87778__marcgascon7__vocals.wav')
spectrogram = wave.make_spectrogram(512)
decorate(xlabel='Time(s)', ylabel='Frequency (Hz)')
spectrogram.plot(high=3000)
plt.show()