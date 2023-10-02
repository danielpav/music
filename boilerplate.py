import os
import soundfile as sf
import sounddevice as sd
import numpy as np
from pydub import AudioSegment
from pydub.playback import play
from effects import *
from klangfarben import *
from sequences import *

audio_segments = []
beat = .50 # seconds

def swing(sequence, eighth_swing=.50, sixteenth_swing=.50 ):
    cursor = 0
    for i in range(len(sequence)): 
        if cursor < 1/2:
            if cursor + sequence[i][1] <= 1/2:
                sequence[i][1] *= eighth_swing*2
                print(sequence[i][1])
            else:
                print(cursor)
                sequence[i][1] = ((1/2 - cursor)/sequence[i][1])*eighth_swing*2 + (cursor + sequence[i][1] - 1/2)*((1.0-eighth_swing)*2)
                print("ie", sequence[i][1])
        else:
            if cursor + sequence[i][1] <= 1:
                sequence[i][1] *= (1.0-eighth_swing)*2
            else:
                sequence[i][1] = 1.0 - cursor
                print("here", sequence[i][1])
        cursor += sequence[i][1]
        if .99 < cursor < 1:
            print(".99")
            sequence[i][1] += 1 - cursor
            cursor = 1
        if cursor >= 1:
            cursor -= 1
        print("cursor: " + str(cursor))
    return sequence

# loop over the file names and add each file to audio_segments
def loop(sequence, files, swings=False, pitch_shift=False):
    file_names = files
    [eighth_swing, sixteenth_swing] = swings
    sequence = swing(sequence, eighth_swing)
    for sample in sequence:
        if sample[0] == -1:
            audio_segments.append(AudioSegment.silent(int(sample[1]*beat*1000)))
            continue    
        # load the audio file
        file_path = os.path.join(dir_path, file_names[sample[0]])
        audio_data = AudioSegment.from_file(file_path, format=file_path[-3:])
        duration = int(sample[1]*beat*1000)
        if sample[0] not in [0,3,6,9] and pitch_shift:
            audio_data = shift_pitch(audio_data, pitch_shift)
        if audio_data.duration_seconds * 1000 < duration:
            audio_segments.append(audio_data)
            audio_segments.append(AudioSegment.silent(duration - int(audio_data.duration_seconds * 1000)))
        else:
            clip = audio_data[:duration]
            audio_segments.append(clip)

def export(name, loops=1):
    output_audio = audio_segments[0]
    for i in range(loops):
        if i == 0:
            for audio_segment in audio_segments[1:]:
                output_audio = output_audio.append(audio_segment, crossfade=0)
        else:
            for audio_segment in audio_segments:
                output_audio = output_audio.append(audio_segment, crossfade=0)

    output_audio.export(f"Out/{name}.wav", format="wav")

def main(sequence, files, name, loops=1, swings=False, pitch_shift=False):
    loop(sequence, files, swings, pitch_shift)
    export(name, loops)