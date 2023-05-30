import os
import shutil
import argparse
from tqdm import tqdm

def scan_and_save_jpg_files(input_path, output_path, ite):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Get the total number of files
    total_files = sum(len(files) for _, _, files in os.walk(input_path))

    # Initialize the progress bar
    progress_bar = tqdm(total=total_files, desc="Copying Files", unit="file")

    # Iterate over all files and directories in the input path
    for root, dirs, files in os.walk(input_path):
        for file in files:
            # Check if the file is a JPEG image
            if file.lower().endswith('.jpg'):
                # Get the full path of the input file
                input_file_path = os.path.join(root, file)
                
                # Get the relative path of the input file
                # relative_path = os.path.relpath(input_file_path, input_path)
                
                # Construct the output file path
                # output_file_path = os.path.join(output_path, relative_path)
                output_file_path = os.path.join(output_path, file)
                
                # Create the output directory structure if it doesn't exist
                output_dir = os.path.dirname(output_file_path)
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)
                
                # Copy only CERTAIN JPG to the output path
                if "PAN" not in output_file_path and "MUX" not in output_file_path and "thumb" not in output_file_path:
                    shutil.copy(input_file_path, output_file_path)
                    print("No.", ite, "Copied:", output_file_path)
                    ite += 1

                # Update the progress bar
                progress_bar.update(1)
    
    # Close the progress bar
    progress_bar.close()

# main program
parser = argparse.ArgumentParser(description='Walk through ALL files in the INPUT PATH, COPY ALL JPGs without PAN/MUX/thumb to the OUTPUT PATH ')
parser.add_argument('--inpath', type=str, help='the input path')
parser.add_argument('--outpath', type=str, help='the output path')

args = parser.parse_args()
input_path = args.inpath
output_path = args.outpath

ite = 1

scan_and_save_jpg_files(input_path, output_path, ite)
