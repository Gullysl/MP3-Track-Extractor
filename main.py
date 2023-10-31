import os
import eyed3

# Ask the user for the file location
folder_path = input("Enter the file location of your MP3 files: ")

# Remove any quotes around the file location
folder_path = folder_path.strip('\'"')

# Replace any forward slashes with backslashes (for Windows compatibility)
folder_path = folder_path.replace('/', '\\')

# Initialize a list to store the title and track length information
mp3_info_list = []

# Iterate through the files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".mp3"):
        mp3_file = os.path.join(folder_path, filename)
        audiofile = eyed3.load(mp3_file)

        if audiofile is not None:
            title = audiofile.tag.title

            # Calculate track length in minutes and seconds
            track_length_seconds = int(audiofile.info.time_secs)
            track_length_minutes = track_length_seconds // 60
            track_length_seconds = track_length_seconds % 60

            mp3_info_list.append((title, track_length_minutes, track_length_seconds))

# Print the information to the console in the specified format
for i, (title, minutes, seconds) in enumerate(mp3_info_list, start=1):
    print(f"{i:02d}. {title} {minutes:02d}:{seconds:02d}")

# You can also save this information to a file if needed
with open('mp3_info.txt', 'w') as file:
    for i, (title, minutes, seconds) in enumerate(mp3_info_list, start=1):
        file.write(f"{i:02d}. {title} {minutes:02d}:{seconds:02d}\n")
