
# MP3-Track-Extractor

MP3-Track-Extractor is a Python script that allows you to extract track information (title and duration) from a folder of MP3 files. It's a handy tool for organizing and cataloging your music collection or analyzing the contents of a directory.

## Features

- Extracts track title and duration (in minutes and seconds) from MP3 files.
- Supports both Windows and Unix-like file paths.
- Simple to use and customize.

## Usage
Clone the Repository:
   ```
   git clone https://github.com/your-username/MP3-Track-Extractor.git
   ```

## Navigate to the repository directory.
Open a command prompt or terminal
Run the script with
   ```
   python main.py
   ```
## Enter the file location of the folder containing your MP3 files.
The script will automatically remove any quotes and format the file path correctly.
View Results:

The script will display track information in the format "Track Number. Title Duration" (e.g., "01. Track Name 03:45").
It will also save this information to a file named mp3_info.txt in the same directory.

## Requirements
Python 3.x
eyed3 library (install it with ``` pip install eyed3 ```)
## Contributing
Contributions and improvements are welcome. Please feel free to fork the repository and submit pull requests.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Author
GullySL
