import numpy as np
from scipy.signal import stft
import matplotlib.pyplot as plt

# 1. Simulate IQ Signal (1 MHz sample rate)
fs = 1e6
t = np.linspace(0, 0.01, int(fs * 0.01))
iq_data = np.exp(1j * 2 * np.pi * 100e3 * t) + 0.2 * (np.random.randn(len(t)) + 1j * np.random.randn(len(t)))

# 2. STFT Spectral Analysis
f, t_spec, Zxx = stft(iq_data, fs=fs, nperseg=256)

# 3. Save Output Plot
plt.pcolormesh(t_spec * 1e3, f / 1e3, np.abs(Zxx), shading='gouraud')
plt.title('STFT Spectrogram of Simulated IQ Signal')
plt.xlabel('Time (ms)')
plt.ylabel('Frequency (kHz)')
plt.savefig('spectrogram.png')
print("Pipeline executed successfully!")
