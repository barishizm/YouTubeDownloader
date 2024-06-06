import os
from pytube import YouTube, exceptions
from time import time
from customtkinter import *

# Initialize all the settings
set_appearance_mode("System")  # Setting the appearance mode to follow by the app: "System", "Light" or "Dark"
set_default_color_theme("blue")  # Setting the theme of the app to follow

# Create the downloads directory if it doesn't exist
if not os.path.exists("youtube_downloads"):
    os.mkdir("youtube_downloads")

    # Download video function
def download_youtube_video(url):
    try:
        start_time = time()
        download_location = "youtube_downloads/"
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(download_location)
        end_time = time()

        # Showing the download time in a new window
        show_download_status(f"Download successful!\nTotal time taken: {round(end_time - start_time, 3)} seconds")
    except exceptions.RegexMatchError:  # If there's an invalid link or empty link, show an error message
        show_error_message("Please enter a valid YouTube link")