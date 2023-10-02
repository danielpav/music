import numpy as np
import sounddevice as sd
from scipy import signal

# Generate a signal
fs = 44100  # sample rate (Hz)
t = np.linspace(0, 1, fs, False)
sig1 = np.sin(2 * np.pi * 100 * t) + np.sin(2 * np.pi * 200 * t)
sig2 = np.sin(2 * np.pi * 300 * t) + np.sin(2 * np.pi * 600 * t)
sig3 = np.sin(2 * np.pi * 300 * t) + np.sin(2 * np.pi * 1000 * t)
sig = np.concatenate((sig1, sig2, sig3))

# Design the low-pass filter
nyquist_freq = fs / 2
cutoff_freq = 1000  # Hz
order = 5
b, a = signal.butter(order, cutoff_freq / nyquist_freq, "low")

# Apply the low-pass filter to the signal
filtered_sig = signal.filtfilt(b, a, sig)

device = 6
sd.play(filtered_sig, samplerate=fs, blocking=True, device=device)   
sd.wait()