import os
import soundfile as sf
import sounddevice as sd
from pydub import AudioSegment
from pydub.playback import play

dir_path = "Samples/Deepsky"

file_names = [f for f in os.listdir(dir_path) if f.endswith('.wav')]

# Sample is the index of the sample
class ClipObj:
    def __init__(self, sample, duration, octave):
        self.file_path = os.path.join(dir_path, file_names[sample])
        self.duration = duration
        self.octave = octave

def play(arr):
    for clip_obj in arr:
        audio_data, samplerate = sf.read(clip_obj.file_path)
        sound = AudioSegment.from_file(clip_obj.file_path, format="wav")
        numframes = int(clip_obj.duration * samplerate)
        if clip_obj.octave != 0:
            print("here")
            new_samplerate = int(sound.frame_rate * (2.0 ** clip_obj.octave))
            pitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_samplerate})
            pitch_sound = pitch_sound.set_frame_rate(44100)
            pitch_sound.play()
        else:
            sd.play(audio_data[:numframes], samplerate=samplerate, blocking=True)

