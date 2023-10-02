from pydub import AudioSegment
import numpy as np

def triangle_wave(frequency, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    return (2 / np.pi) * np.arcsin(np.sin(2 * np.pi * frequency * t))

def generate_triangle_wave(frequency, duration, sample_rate=44100):
    samples = triangle_wave(frequency, duration, sample_rate)
    samples = (2**15 - 1) * samples / np.abs(samples).max()
    samples = samples.astype(np.int16)
    return samples

frequency = 440 # Hz
duration = 5 # seconds
sample_rate = 44100 # samples per second
samples = generate_triangle_wave(frequency, duration, sample_rate)
segment = AudioSegment(
    samples.tobytes(), 
    frame_rate=sample_rate, 
    sample_width=2, 
    channels=1
)

segment.export("triangle_wave.wav", format="wav")

