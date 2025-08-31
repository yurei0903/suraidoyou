import librosa
import numpy as np
import soundfile as sf
pitch = 2
y, sr_j = librosa.load("fail_name")
y_shifted = librosa.effects.pitch_shift(y, sr=sr_j, n_steps=pitch)
time = np.arange(0, len(y_shifted)) / sr_j
sf.write("pitch_shift.wav", y_shifted, sr_j)
