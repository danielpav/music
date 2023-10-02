# Description: This file contains the functions for the effects that can be applied to the audio
import numpy as np
import soundfile as sf

def shift_pitch(audio_segment, octave):
    new_sample_rate = int(audio_segment.frame_rate * (2.0 ** octave))
    shifted_sound = audio_segment._spawn(audio_segment.raw_data, overrides={'frame_rate': new_sample_rate})
    shifted_sound = shifted_sound.set_frame_rate(44100)
    return shifted_sound


def apply_flanger(audio, depth, frequency, feedback):
    num_samples, num_channels = audio.shape
    delay_line_length = int(depth * 0.001 * 44100)  # Convert depth from milliseconds to samples

    # Initialize the delay line buffer with zeros
    delay_line_buffer = np.zeros((delay_line_length, num_channels))

    output_audio = np.zeros_like(audio)

    for i in range(num_samples):
        # Calculate the current delay time based on the modulation frequency
        current_delay = int(depth * 0.5 * np.sin(2 * np.pi * frequency * i / 44100))

        for channel in range(num_channels):
            # Get the delayed sample from the buffer
            delayed_sample = delay_line_buffer[current_delay % delay_line_length, channel]

            # Apply the flanger effect
            output_audio[i, channel] = audio[i, channel] + feedback * delayed_sample

            # Update the delay line buffer with the current sample
            delay_line_buffer[i % delay_line_length, channel] = audio[i, channel]

    return output_audio
