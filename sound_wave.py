# librosaをインポート
import librosa
# numpyをインポート（配列を生成するため）
import numpy as np
# matplotlibをインポート（グラフ描画するため）
import matplotlib.pyplot as plt

# 音楽ファイルのパスを設定（例："/foldername/filename.mp3"）
file_name = "ra.wav"
# loadメソッドでy=音声信号の値（audio time series）、sr=サンプリング周波数（sampling rate）を取得
y, sr = librosa.load(file_name)
# 時間 = yのデータ数 / サンプリング周波数(#サンプリング周波数は1秒間に何回標本化を行うかを示す値)
print("サンプリング周波数:", sr)
time = np.arange(0, len(y)) / sr


plt.plot(time, y)
plt.xlabel("Time(s)")
plt.ylabel("Sound Amplitude")

# グラフを表示
plt.show()
