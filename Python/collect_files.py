# collect files in certain type from a big folder, gather them into a new folder

import os
import shutil

# Specify the directory containing the PDF files
source_dir = './files'

# Specify the directory where the PDF files will be moved
dest_dir = './paper'

# name the file type
filetype = '.pdf'

# Walk through the source directory and its subdirectories
for root, dirs, files in os.walk(source_dir):
    for file in files:
        # Check if the file is a PDF
        if file.endswith('.pdf'):
            # Construct the full path of the file
            file_path = os.path.join(root, file)
            # Move the file to the destination directory
            shutil.move(file_path, dest_dir)
