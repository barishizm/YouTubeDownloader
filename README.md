# YouTube Video Downloader

This project is a simple YouTube video downloader application built using Python. The graphical user interface (GUI) is created with customtkinter, and the video downloading functionality is provided by the pytube library. The application allows users to download YouTube videos in the highest available resolution directly to their local Downloads folder.

## Features

- **Simple GUI**: User-friendly interface for entering the YouTube video URL and initiating the download.
- **Highest Resolution Download**: Automatically selects and downloads the highest resolution available for the given video.
- **Multi-threaded Downloading**: The download process runs in a separate thread to keep the application responsive.
- **Error Handling**: Provides informative error messages for invalid URLs and other download issues.

## Installation
### Requirements

- Python 3.x
- Pip package manager

## Required Libraries

- Install the required libraries using pip:

    ```sh
    pip install pytube3 customtkinter
    ```

## Running the Application

- Clone the repository or download the source code.
- Navigate to the project directory.
- Run the application:

## Usage

- Enter a valid YouTube video URL in the text entry field.
- Click the "Download" button.
- The video will be downloaded to your local Downloads folder.
- If the URL is invalid or an error occurs, a message will be displayed with the appropriate information.

## Code Overview
### Main Components

- GUI Initialization: The application window and layout are set up using customtkinter.
- Download Function: Downloads the YouTube video using the pytube library.
- Multi-threading: Ensures the GUI remains responsive during the download process.
- Message Queue: Facilitates communication between the download thread and the main GUI thread for displaying messages.

## Functions

- get_downloads_folder(): Returns the path to the user's Downloads folder.
- show_message(title, message, size="300x150"): Displays a popup message window.
- download_youtube_video(url): Downloads the YouTube video from the provided URL.
- start_download(url): Starts the download process in a separate thread.
- check_queue(): Periodically checks the message queue and displays messages.

## Contributing
Contributions are welcome! If you have any ideas or find bugs, feel free to open an issue or submit a pull request.

### Steps to Contribute
1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -m 'Add some feature').
5. Push to the branch (git push origin feature-branch).
6.Open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

