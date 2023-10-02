from boilerplate import shift_pitch, loop, export

file_names = [""]
beat = .125

sequence = []

audio_segments = []

loop(sequence, file_names)
export("sequence.wav", loops=1)