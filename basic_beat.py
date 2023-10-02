from boilerplate import shift_pitch, loop, export, main
from sequences import *
from klangfarben import *

main(basic_beat_hihat, file_names, "basic_beat_hihat", loops=4, swings=[.65, .50])
main(basic_beat_snare, file_names, "basic_beat_snare", loops=4)
main(basic_beat_kick, file_names, "basic_beat_kick", loops=4)