import os
import soundfile as sf
import sounddevice as sd
import numpy as np
from pydub import AudioSegment
from pydub.playback import play

# set the path of the directory containing the audio files
dir_path = "Samples"

# get a list of audio file names in the directory
file_names = ["well.wav", "MaxV-C3MUTGTR.wav","MaxV-THMBASS.wav","Deepsky/8089096.wav", "octave_-0.5.wav", "MaxV -C3DSTGTR.wav", "MaxV-SNARE1.WAV", "octave_0.5.wav",
              "MaxV-C3STREN1.wav", "MaxV-HHCL.WAV"] 
              
file_names01 = ["octave_-0.09999999999999998.wav", "MaxV-C3MUTGTR.wav","MaxV-THMBASS.wav","Deepsky/8089096.wav", "octave_-0.5.wav", "MaxV -C3DSTGTR.wav", "MaxV-SNARE1.WAV", "octave_0.5.wav",
              "MaxV-C3STREN1.wav", "MaxV-HHCL.WAV"] 

file_names02 = ["octave_0.5.wav", "MaxV-C3MUTGTR.wav","MaxV-THMBASS.wav","Deepsky/8089096.wav", "octave_-0.5.wav", "MaxV -C3DSTGTR.wav", "MaxV-SNARE1.WAV", "octave_0.5.wav",
              "MaxV-C3STREN1.wav", "MaxV-HHCL.WAV"] 


file_names2 = ["well.wav", "MaxV-C3MUTGTR.wav","MaxV-THMBASS.wav","DM5Kick46.wav", "octave_-0.5.wav", "MaxV -C3DSTGTR.wav", "MaxV-SNARE1.WAV", "octave_0.5.wav",
              "MaxV-C3STREN1.wav", "MaxV-HHCL.WAV"] 

file_names3 = ["well.wav", "octave_-0.09999999999999998.wav", "octave_-0.19999999999999996.wav", "octave_-0.5.wav", "octave_0.5.wav", "octave_0.20000000000000018.wav", 
               "octave_0.10000000000000009.wav", "octave_1.0.wav", "octave_0.40000000000000013.wav", "octave_0.30000000000000004.wav"] 

beat = .125
sequence = [[3,beat/2],[3, beat/2],[6, beat],[9, beat],[1, beat],[9, beat*2],[6, beat],[3, beat],[8, beat/2],[8, beat/2],[1, beat]
            ,[0, beat], [7, beat], [4, beat/2],[3,beat*1.5],[9, beat],[9,beat]]

sequencea = [[-1,beat/2],[-1, beat/2],[-1, beat],[-1, beat],[1, beat*5],[-1, beat*2],[-1, beat/2],[-1, beat/2],[1, beat]
            ,[-1, beat], [-1, beat], [-1, beat*4.5]]

sequence2 = [[1,beat*2]]*24 + [[8,beat*2]]*8

audio_segments = []

def shift_pitch(audio_segment, octave):
    new_sample_rate = int(audio_segment.frame_rate * (2.0 ** octave))
    shifted_sound = audio_segment._spawn(audio_segment.raw_data, overrides={'frame_rate': new_sample_rate})
    shifted_sound = shifted_sound.set_frame_rate(44100)
    return shifted_sound


# loop over the file names and play each file
def loop(sequence, files, pitch_shift=False):
    file_names = files
    for sample in sequence:
        if sample[0] == -1:
            audio_segments.append(AudioSegment.silent(int(sample[1]*1000)))
            continue    
        # load the audio file
        file_path = os.path.join(dir_path, file_names[sample[0]])
        audio_data = AudioSegment.from_file(file_path, format=file_path[-3:])
        duration = int(sample[1]*1000)
        if sample[0] not in [0,3,6,9] and pitch_shift:
            audio_data = shift_pitch(audio_data, pitch_shift)
        if audio_data.duration_seconds * 1000 < duration:
            audio_segments.append(audio_data)
            audio_segments.append(AudioSegment.silent(duration - int(audio_data.duration_seconds * 1000)))
        else:
            clip = audio_data[:duration]
            audio_segments.append(clip)

for i in range(1):
    loop(sequence, file_names)
loop(sequence, file_names, 0.5)
loop(sequence, file_names)
loop(sequence, file_names, 0.33333333333333333333)
loop(sequence, file_names, 2/3)
loop(sequence, file_names)
loop(sequence, file_names)

output_audio = audio_segments[0]
loops = 1
for i in range(loops):
    if i == 0:
        for audio_segment in audio_segments[1:]:
            output_audio = output_audio.append(audio_segment, crossfade=0)
    else:
        for audio_segment in audio_segments:
            output_audio = output_audio.append(audio_segment, crossfade=0)

output_audio.export("sequence3a.wav", format="wav")