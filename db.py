import librosa
import matplotlib.pyplot as plt

# Load the audio file
filename = './ffmpegdata/data.wav'
y, sr = librosa.load(filename)

# Calculate the dB level of the audio
db = librosa.amplitude_to_db(y)

# Plot the dB level over time
plt.figure()
times = librosa.samples_to_time(range(len(db)), sr=sr)
plt.plot(times, db)
plt.xlabel('Time (sec)')
plt.ylabel('Amplitude (dB)')
plt.show()