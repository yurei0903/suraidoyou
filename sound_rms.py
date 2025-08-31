import numpy as np
import librosa
import matplotlib.pyplot as plt

y, sr = librosa.load("fail_name", sr=None)
# RMSを計算
rms = librosa.feature.rms(y=y, frame_length=8192, hop_length=2048)[0]
rms /= np.max(rms)  # 正規化
times = librosa.times_like(rms, hop_length=2048, sr=sr)

# RMSをプロット
plt.figure(figsize=(12, 4))
plt.plot(times, rms, label="RMS")
plt.ylabel("Normalized RMS")
plt.xlabel("Time (s)")
plt.legend()
plt.tight_layout()
plt.show()
