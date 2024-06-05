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