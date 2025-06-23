import os
import shutil

# Use raw strings for Windows paths
source_folder = r"C:\Users\POOJA\Documents\Images"
destination_folder = r"C:\Users\POOJA\Downloads\Exchange Image"

# Create destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

print("Scanning for .jpg files...")

files_found = False

for filename in os.listdir(source_folder):
    print("Found:", filename)  # Debug line to show all files
    if filename.lower().endswith('.jpg'):
        files_found = True
        src_path = os.path.join(source_folder, filename)
        dest_path = os.path.join(destination_folder, filename)
        shutil.move(src_path, dest_path)
        print(f"Moved: {filename}")

if not files_found:
    print("No .jpg files found in the source folder.")
else:
    print("\nAll .jpg files moved successfully.")
