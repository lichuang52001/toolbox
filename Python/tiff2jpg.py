import os
import cv2
import numpy as np
import datetime

# Set the input and output directories
input_dir = "/home/hp/desktop/cloud_detection_0803/cloud_ground_truth/Natural_False_Color"
output_dir = "/home/hp/desktop/cloud_detection_0803/cloud_ground_truth/Natural_False_Color_jpg"

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop through all files in the input directory
for filename in os.listdir(input_dir):
    # Check if the file is a TIFF image
    if filename.endswith(".TIF"):
        # Read the image using OpenCV
        img = cv2.imread(os.path.join(input_dir, filename))

        img -= img.min()
        img = img/(img.max()-img.min())
        img *= 255
        img_jpg = img.astype(np.uint8)

        jpg_path = os.path.join(output_dir, filename[:-4] + ".jpg")

        # Save the JPEG image to the output directory
        cv2.imwrite(jpg_path, img_jpg)
        print(f'[{datetime.datetime.now()}] | file {jpg_path} is exported')

