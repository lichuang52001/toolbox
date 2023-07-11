import os
import glob

# # Get the path to the folder
# path = "D:\\桌面\test_order_xml"

# # Change the current working directory to the folder
# os.chdir(path)

# Get all the files in the folder and its subfolders
files = glob.glob("**/*")

print(files)

# Iterate over all the files
for file in files:
    # If the file is not a directory
    if not os.path.isdir(file):
        # Check if the file name ends with "order.xml"
        if file.endswith("order.xml"):
            continue
        else:
            # Delete the file
            os.remove(file)

print("All files except 'order' have been deleted.")
