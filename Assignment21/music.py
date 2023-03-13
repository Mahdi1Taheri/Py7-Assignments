import pysynth

# Define the notes and their durations
notes = (("c", -10), ("b", 10), ("e", 15), ("g", 20), ("g", 20), ("a", 20), ("b", 20))

# Generate the melody
pysynth.make_wav(notes, fn="melody1.wav")