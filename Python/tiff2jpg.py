import os
import cv2
import numpy as np

# Set the input and output directories
input_dir = "./input"
output_dir = "./output"

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop through all files in the input directory
for filename in os.listdir(input_dir):
    # Check if the file is a TIFF image
    if filename.endswith(".tiff"):
        # Read the image using OpenCV
        img = cv2.imread(os.path.join(input_dir, filename))

        img -= img.min()
        img = img/(img.max()-img.min())
        img *= 255
        img_jpg = img.astype(np.uint8)

        # Save the JPEG image to the output directory
        cv2.imwrite(os.path.join(output_dir, filename[:-5] + ".jpg"), img_jpg)

