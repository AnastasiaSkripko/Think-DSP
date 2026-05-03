from thinkdsp import CosSignal, SinSignal
from thinkdsp import decorate
import matplotlib.pyplot as plt

def plt_spectrum(wave, start, duration):
    segment = wave.segment(start, duration)
    spectrum = segment.make_spectrum()
    spectrum.plot(high=1500)
    decorate(xlabel='Frequency (Hz)')
    plt.show()

cos_sig = CosSignal(freq=522, amp=1.0, offset=0) #нота до
cos_sig.plot()
decorate(xlabel='Time (s)')
plt.show()

sin_sig = SinSignal(freq=1044, amp=0.5, offset=0)
sin_sig.plot()
decorate(xlabel='Time (s)')
plt.show()

mix = sin_sig + cos_sig
mix.plot()
decorate(xlabel='Time (s)')
plt.show()
wave = mix.make_wave(duration=0.5, start=0, framerate=11025)

wave.write(filename='my_mixed_sound.wav')

plt_spectrum(wave, 0, 0.5)