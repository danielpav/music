import os
import soundfile as sf
import sounddevice as sd
import numpy as np

# set the path of the directory containing the audio files
dir_path = "Samples/Deepsky"

# get a list of audio file names in the directory
file_names = [f for f in os.listdir(dir_path) if f.endswith('.wav')]
duration = .25

# loop over the file names and play each file
for file_name in file_names:
    # load the audio file
    file_path = os.path.join(dir_path, file_name)
    audio_data, samplerate = sf.read(file_path)
    numframes = int(duration * samplerate)

    # Set up the stereo audio array
    stereo_audio = np.column_stack((audio_data, audio_data))
    
    # play the audio data
    sd.play(stereo_audio[:numframes], samplerate=samplerate, blocking=True)
    sd.wait()  
