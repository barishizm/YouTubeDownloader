import os
from pytube import YouTube, exceptions
from time import time
from customtkinter import *
import threading
import queue

# Initialize all the settings
set_appearance_mode("System")  # Setting the appearance mode to follow by the app: System, Light or Dark.
set_default_color_theme("blue")  # Setting the theme of the app to follow.

# a queue for communicating between threads.
message_queue = queue.Queue()

# Function to get the users Downloads folder path.
def get_downloads_folder():
    return os.path.join(os.path.expanduser("~"), "Downloads")

# show messages
def show_message(title, message, size="300x150"):
    popup = CTkToplevel()
    popup.title(title)
    popup.resizable(False, False)
    popup.geometry(size)
    popup.grid_columnconfigure(0, weight=1)
    popup.grid_rowconfigure((0, 1), weight=1)
    label = CTkLabel(popup, text=message)
    label.grid(row=0, column=0, padx=20, pady=10)
    button = CTkButton(popup, text="OK", command=popup.destroy)
    button.grid(row=1, column=0, pady=10)
    popup.mainloop()

# Download video functions
def download_youtube_video(url):
    try:
        start_time = time()
        download_location = get_downloads_folder()
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(download_location)
        end_time = time()
        message_queue.put(("Download Status",
                           f"Download successful!\nTotal time taken: {round(end_time - start_time, 3)} seconds"))
    except exceptions.RegexMatchError:
        message_queue.put(("Error", "Please enter a valid YouTube link", "300x100"))
    except Exception as e:
        message_queue.put(("Error", f"An error occurred: {str(e)}", "300x100"))

# handle download in a separate thread
def start_download(url):
    threading.Thread(target=download_youtube_video, args=(url,)).start()

# periodically check the message queue and show messages
def check_queue():
    try:
        while True:
            message = message_queue.get_nowait()
            show_message(*message)
    except queue.Empty:
        pass
    finally:
        app.after(100, check_queue)

# Initialize the layout of the app
app = CTk()
app.title("YouTube Downloader")
app.grid_rowconfigure((0, 1), weight=1)
app.grid_columnconfigure((0, 1), weight=1)
app.geometry("400x150")
app.resizable(False, False)

CTkLabel(app, text="Enter YouTube video URL:").grid(row=0, column=0, padx=20, pady=10)
url_entry = CTkEntry(app, width=300)
url_entry.grid(row=0, column=1, padx=20, pady=10)
CTkButton(app, text='Download', command=lambda: start_download(url_entry.get())).grid(
    row=1, column=0, columnspan=2, pady=10
)

# check the queue
app.after(100, check_queue)

app.mainloop()
