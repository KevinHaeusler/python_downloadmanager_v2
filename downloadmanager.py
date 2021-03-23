import os
import shutil
import re

download_folder = r'C:\Users\Kevin Haeusler\Downloads'
download_files = os.listdir(download_folder)
downloading_file = ''
# Set Destination Folders
exe_folder = r'C:\Users\Kevin Haeusler\Downloads\EXE'
misc_folder = r'C:\Users\Kevin Haeusler\Downloads\MISCELLANEOUS'
pdf_folder = r'C:\Users\Kevin Haeusler\Downloads\PDF'
pictures_folder = r'C:\Users\Kevin Haeusler\Downloads\PICTURES'
videos_folder = r'C:\Users\Kevin Haeusler\Downloads\VIDEOS'
zip_folder = r'C:\Users\Kevin Haeusler\Downloads\ZIP'
# Exclude Destination Folders
excluded_folders = ["EXE", "MISCELLANEOUS", "PDF", "PICTURES", "VIDEOS", "ZIP"]
# Set Log File

def move_file(file, extension):
    if file not in excluded_folders:
        if re.match('^.*\.(jpe?g|gif|png|bmp)$', extension):
            destination_folder = pictures_folder
        elif re.match('^.*\.(mp4|mkv|wmv|m4v|mov|avi|flv|webm|flac|mka|m4a|aac|ogg)$', extension):
            destination_folder = videos_folder
        elif re.match('^.*\.(zip|rar|tar|7z)$', extension):
            destination_folder = zip_folder
        elif re.match('^.*\.(exe)$', extension):
            destination_folder = exe_folder
        elif re.match('^.*\.(pdf)$', extension):
            destination_folder = pdf_folder
        else: 
            destination_folder = misc_folder
        shutil.move(os.path.join(download_folder, file), os.path.join(destination_folder, file))
    

for file in download_files:
    extension = os.path.splitext(file)[1].lower()
    move_file(file, extension)
