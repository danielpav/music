from play2 import ClipObj
import os
import math
import numpy as np
import soundfile as sf
from pydub import AudioSegment

e = math.e
sample_rate = 44100
bpm = 120
bps = bpm/60
measure_samples = sample_rate * 2
measure_ms = 1000 * 2
slide_length_ms = measure_ms 
segment_length_ms = 100
num_segments = int(slide_length_ms/segment_length_ms)

file_paths = [os.path.join("Samples/Deepsky", f) for f in os.listdir("Samples/Deepsky") if f.endswith('.wav')]

audio_segments = []
mod_arr = np.linspace(1, 1/e, num_segments)

audio_data = AudioSegment.from_file(file_paths[0], format=file_paths[0][-3:])
#audio_data = AudioSegment.from_file("/home/daniel/projects/DAW/octave_-0.19999999999999996.wav", format="wav")
audio_data = audio_data[100:]

for i in range(num_segments):
    clip = audio_data._spawn(audio_data.raw_data, overrides={'frame_rate': int(sample_rate * mod_arr[i])})
    clip.set_frame_rate(44100)
    audio_segments.append(clip[:segment_length_ms])


output_audio = audio_segments[0]
for audio_segment in audio_segments[1:]:
    output_audio = output_audio.append(audio_segment, crossfade=0)

output_audio.export("e_slide3.wav", format="wav")