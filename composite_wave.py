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

# Function to generate a sine wave
def generate_sine_wave(frequency, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    samples = np.sin(2 * np.pi * frequency * t)
    samples = (2**15 - 1) * samples / np.abs(samples).max()
    samples = samples.astype(np.int16)
    return samples

# Function to generate a square wave
def generate_square_wave(frequency, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    samples = np.sign(np.sin(2 * np.pi * frequency * t))
    samples = (2**15 - 1) * samples
    samples = samples.astype(np.int16)
    return samples

# Function to generate a composite wave based on proportions of triangle, sine, and square waves
def generate_composite_wave(triangle_prop, sine_prop, square_prop, frequency, duration, sample_rate=44100):
    triangle_samples = generate_triangle_wave(frequency, duration, sample_rate)
    sine_samples = generate_sine_wave(frequency, duration, sample_rate)
    square_samples = generate_square_wave(frequency, duration, sample_rate)

    composite_samples = (
        (triangle_prop * triangle_samples) +
        (sine_prop * sine_samples) +
        (square_prop * square_samples)
    )

    composite_samples = composite_samples / np.abs(composite_samples).max()
    composite_samples = (2**15 - 1) * composite_samples
    composite_samples = composite_samples.astype(np.int16)

    return composite_samples

# Example usage:
triangle_prop = 0.4  # Proportion of triangle wave
sine_prop = 0.3     # Proportion of sine wave
square_prop = 0.3   # Proportion of square wave
frequency = 440     # Hz
duration_ms = 500   # Milliseconds

composite_samples = generate_composite_wave(triangle_prop, sine_prop, square_prop, frequency, duration_ms / 1000)

segment = AudioSegment(
    composite_samples.tobytes(),
    frame_rate=44100,
    sample_width=2,
    channels=1
)

segment.export("composite_wave.wav", format="wav")
  