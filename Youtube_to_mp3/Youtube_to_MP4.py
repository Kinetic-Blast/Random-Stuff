from pytube import YouTube
import os

# Ask the user for the YouTube video URL
video_url = input("Enter the YouTube video URL: ")

# Create a YouTube object
yt = YouTube(video_url)

# Get the highest resolution audio stream
audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').desc().first()

# Download the audio stream
output_path = 'downloads/'
audio_stream.download(output_path=output_path)

print(f'Download and conversion complete! MP3 saved at: {output_path}')
