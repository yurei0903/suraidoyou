import librosa
import numpy as np
import soundfile as sf
hayasa = 1.5
y, sr_j = librosa.load("fail_name")
y_shifted = librosa.effects.time_stretch(y, rate=hayasa)
time = np.arange(0, len(y_shifted)) / sr_j
sf.write("time_stretch.wav", y_shifted, sr_j)
