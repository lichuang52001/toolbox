# # # # # # # # # # # # # # # # # # 
# Function: scan all folders and subfolders, save .jpg files in a output path
# # # # # # # # # # # # # # # # # # 


import os
import shutil

def scan_and_save_jpg_files(input_path, output_path, ite):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Iterate over all files and directories in the input path
    for root, dirs, files in os.walk(input_path):
        for file in files:
            # Check if the file is a MUX.JPEG image
            if file.lower().endswith('mux.jpg'):
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

                shutil.copy(input_file_path, output_file_path)                
                print("No.", ite, "Copied:", output_file_path)
                ite += 1

                
                # Copy the input file to the output path
                # if "PAN" not in output_file_path and "MUX" not in output_file_path and "thumb" not in output_file_path:
                #     shutil.copy(input_file_path, output_file_path)
                #     print("No.", ite, "Copied:", output_file_path)
                #     ite += 1
                    # print(f"Copied: {output_file_path}")




# def delete_files_containing_PAN(folder_path):
#     # Iterate over all files in the folder
#     for filename in os.listdir(folder_path):
#         file_path = os.path.join(folder_path, filename)
        
#         # Check if the filename contains "PAN"
#         if "PAN" in filename:
#             # Check if the path is a file
#             if os.path.isfile(file_path):
#                 # Delete the file
#                 os.remove(file_path)
#                 # print(f"Deleted: {file_path}")

# def delete_files_containing_MUX(folder_path):
#     # Iterate over all files in the folder
#     for filename in os.listdir(folder_path):
#         file_path = os.path.join(folder_path, filename)
        
#         # Check if the filename contains "MUX"
#         if "MUX" in filename:
#             # Check if the path is a file
#             if os.path.isfile(file_path):
#                 # Delete the file
#                 os.remove(file_path)
#                 # print(f"Deleted: {file_path}")

# def delete_files_containing_thumb(folder_path):
#     # Iterate over all files in the folder
#     for filename in os.listdir(folder_path):
#         file_path = os.path.join(folder_path, filename)
        
#         # Check if the filename contains "thumb"
#         if "thumb" in filename:
#             # Check if the path is a file
#             if os.path.isfile(file_path):
#                 # Delete the file
#                 os.remove(file_path)
#                 # print(f"Deleted: {file_path}")

# Example usage
input_path = '/HDFS/ARCHIVE/SV2-02/LEVEL1A/PMS/2023'
output_path = '/home/yarn/lichuang/cloud_detection_0613/SV2-02_MUX_JPGs'

ite = 1

scan_and_save_jpg_files(input_path, output_path, ite)
# delete_files_containing_MUX(output_path)
# delete_files_containing_PAN(output_path)
# delete_files_containing_thumb(output_path)

