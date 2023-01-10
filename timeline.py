import json
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import numpy as np

# Read the JSON file
with open("audio_data.json", "r") as f:
    data = json.load(f)

# Get the file path and words from the JSON file
file_path = list(data.keys())[0]
words = data[file_path]["words"]

# Read the audio file
fs, audio_data = wav.read(file_path)

# Generate the time axis for the audio signal
duration = len(audio_data) / fs
time = np.linspace(0, duration, len(audio_data))

# Plot the audio signal
plt.plot(time, audio_data)

# Add reference lines for the start and end points of each word
for word in words:
    start = word["start"]
    end = word["end"]
    plt.axvline(x=start+0.05, color='r', linestyle='--')
    plt.axvline(x=end, color='b', linestyle='-')

# Show the plot
plt.show()
