import sounddevice as sd
import numpy as np

# Get list of available devices
devices = sd.query_devices()
print(devices)

# Select the default output device
device_idx = None  # Replace with the index of the device you want to test
for i, device in enumerate(devices):
    if device['max_output_channels'] > 0 and 'M4' in device['name']:
        device_idx = i
        break

if device_idx is None:
    print('No default output device found!')
    exit()

# Generate a 1 kHz sine wave
duration = 5  # seconds
sample_rate = 44100
t = np.linspace(0, duration, duration * sample_rate, False)
audio_data = 0.5 * np.sin(2 * np.pi * 1000 * t)

# Play the audio through the selected device
print(f"Playing audio through device {device_idx}...")
sd.play(audio_data, sample_rate, device=device_idx)
sd.wait()
print("Done!")
