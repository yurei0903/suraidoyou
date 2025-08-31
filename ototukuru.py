import numpy as np
import soundfile as sf

rate = 48000
duration = 3.0
# linespace:0秒からduration秒まで、rate*duration個の等間隔な数値を生成(numpy.ndarray型)
t = np.linspace(0., duration, int(rate * duration))
# 正弦波を生成
n = 0
x = np.sin(2.0 * np.pi * 440.0 * 2**(n / 12) * t)
sf.write("ra.wav", x, rate)
