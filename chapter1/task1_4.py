from thinkdsp import read_wave

def stretch(wave, num):
    # old_Длительность = количество отсчётов / framerate
    # new_длительность = old_длительность × num
    # тогда количество отсчётов / framerate_new = количество отсчётов / framerate_old × num -> framerate_new = num / framerate_old
    wave.ts *= num
    wave.framerate /= num
    wave.write(filename='stretch_sound.wav')

wave = read_wave('120994__thirsk__120-oboe.wav')
stretch(wave, 2)