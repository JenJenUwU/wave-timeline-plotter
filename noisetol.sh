#!/bin/bash

# Detect silence in the audio and set the output to the SILENCEINFO variable
SILENCEINFO=$(ffmpeg -i ffmpegdata/data.wav -af silencedetect=n=-50dB:d=0.05 -f null - 2>&1)
# Extract the first line of the silence information
SILENCEPOINTS=$(echo $SILENCEINFO | sed -n '1p')
# Use the silence points to trim the input file and create a new file called "trimmed.mp4"
ffmpeg -i ffmpegdata/data.wav -to $SILENCEINFO ffmpegdata/trimmed.wav