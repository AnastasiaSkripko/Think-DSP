from thinkdsp import read_wave
from thinkdsp import decorate
import matplotlib.pyplot as plt
import numpy as np

def compress(dct, thresh=1):
    count = 0
    for i, amp in enumerate(dct.amps):
        if np.abs(amp) < thresh:
            dct.hs[i] = 0
            count += 1
    n = len(dct.amps)
    print(count, n, 100 * count / n, sep='\t')

wave = read_wave('chapter6/100475__iluppai__saxophone-weep.wav')
segment = wave.segment(start=1.2, duration=0.5)
segment.normalize()
seg_dct = segment.make_dct()

seg_dct.plot(high=4000)
decorate(xlabel='Frequency (Hz)', ylabel='DCT')
plt.show()

compress(seg_dct, thresh=10)
seg_dct.plot(high=4000)
plt.show()

from thinkdsp import Spectrogram

def make_dct_spectrogram(wave, seg_length):
    window = np.hamming(seg_length)
    i, j = 0, seg_length
    step = seg_length // 2
    spec_map = {}   # map from time to Spectrum
    while j < len(wave.ys):
        segment = wave.slice(i, j)
        segment.window(window)
        # the nominal time for this segment is the midpoint
        t = (segment.start + segment.end) / 2
        spec_map[t] = segment.make_dct()
        i += step
        j += step
    return Spectrogram(spec_map, seg_length)

spectro = make_dct_spectrogram(wave, seg_length=1024)
for t, dct in sorted(spectro.spec_map.items()):
    compress(dct, thresh=0.2)

wave2 = spectro.make_wave()
wave2.write(filename='wave2.wav')