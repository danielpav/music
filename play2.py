import os
import soundfile as sf
import sounddevice as sd
from pydub import AudioSegment
from pydub.playback import play
import numpy as np

dir_path = "Samples/Deepsky"

file_names = [f for f in os.listdir(dir_path) if f.endswith('.wav')]

# Sample is the index of the sample
class ClipObj:
    def __init__(self, sample, duration, octave):
        # Silence
        if sample == -1:
            self.file_path = -1
        else:
            self.file_path = os.path.join(dir_path, file_names[sample])
        self.duration = duration
        self.octave = octave

def play(arr):
    for clip_obj in arr:
        #Enjoy the silence
        if clip_obj.file_path == -1:
            num_samples = int(clip_obj.duration * 44100)
            silence_waveform = np.zeros(num_samples)
            sd.play(silence_waveform, samplerate=44100, blocking=True)
        else:
            audio_data, samplerate = sf.read(clip_obj.file_path)
            numframes = int(clip_obj.duration * samplerate)
            # Octave shift   
            if clip_obj.octave != 0:
                sound = audio_data[:numframes]
                new_samplerate = int(samplerate * (2.0 ** clip_obj.octave))
                indices = np.round(np.arange(0, len(sound), new_samplerate / samplerate)).astype(int)
                downsampled_frames = int(len(audio_data) / (samplerate / new_samplerate))
                pitch_sound = np.zeros(downsampled_frames)
                pitch_sound[:len(sound)] = sound
                pitch_sound = pitch_sound[indices]
                audio_data = pitch_sound.astype(np.float32)
                samplerate = new_samplerate
            sd.play(audio_data[:numframes], samplerate=samplerate, blocking=True)
