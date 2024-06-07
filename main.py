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

# Function to show download status
def show_download_status(message):
    popup = CTkToplevel()
    popup.title("Download Status")
    popup.resizable(False, False)
    popup.geometry("300x150")
    popup.grid_columnconfigure(0, weight=1)
    popup.grid_rowconfigure((0, 1), weight=1)
    msg = StringVar()
    msg.set(message)
    label = CTkLabel(popup, textvariable=msg)
    label.grid(row=0, column=0, padx=20, pady=10)
    button = CTkButton(popup, text="OK", command=popup.destroy)
    button.grid(row=1, column=0, pady=10)
    popup.mainloop()

# Function to show error message
def show_error_message(message):
    error = CTkToplevel()
    error.title("Error")
    error.resizable(False, False)
    error.geometry("300x100")
    error.grid_rowconfigure((0, 1), weight=1)
    error.grid_columnconfigure(0, weight=1)
    error_label = CTkLabel(error, text=message)
    error_label.grid(row=0, column=0, padx=20, pady=10)
    button = CTkButton(error, text="OK", command=error.destroy)
    button.grid(row=1, column=0, pady=10)
    error.mainloop()

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

# Initializing the layout of the app
app = CTk()
app.title("YouTube Downloader")
app.grid_rowconfigure((0, 1), weight=1)
app.grid_columnconfigure((0, 1), weight=1)
app.geometry("400x150")
app.resizable(False, False)
CTkLabel(app, text="Enter YouTube video URL:").grid(row=0, column=0, padx=20, pady=10)
url_entry = CTkEntry(app, width=300)
url_entry.grid(row=0, column=1, padx=20, pady=10)
CTkButton(app, text='Download', command=lambda: download_youtube_video(url_entry.get())).grid(row=1, column=0, columnspan=2, pady=10)
app.mainloop()
