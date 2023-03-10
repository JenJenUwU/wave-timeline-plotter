import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import numpy as np
#import librosa

# Read the audio files
fs1, data1 = wav.read('./ffmpegdata/data.wav')
fs2, data2 = wav.read('./ffmpegdata/gate.wav')
#fs3, data3 = wav.read('')
#fs4, data4 = wav.read('')

# Make sure the audio files have the same sample rate
assert fs1 == fs2

# Get the duration of the audio files
duration = len(data1) / fs1

# Generate the time axis for the audio signal
time = np.linspace(0, duration, len(data1))

# Plot the audio signals
plt.plot(time, data1, label='Audio 1')
plt.plot(time, data2, label='Audio 2')
#plt.plot(time, data3, label='Audio 3')
#plt.plot(time, data4, label='Audio 4')

# Add a legend and show the plot
plt.legend()
plt.show()
