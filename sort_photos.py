### Sort photos using a simple method

# 1. Open first photo in folder
# 2. User selects move or stay
# 3. If move, move to folder
# 4. If stay, open next photo
# 5. Repeat until all photos are sorted


# TOOD: Works but only does one file type at a time. And slow and inefficient as it opens and closes photos app everytime.

import os
import subprocess

def sort_photos(folder_path):
    
    # Get all photos in the folder
    photos = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.png','.mov'))]

    for photo in photos:
        # TODO: Remove this if not needed
        # program = r"C:\Program Files\WindowsApps\Microsoft.Windows.Photos_2025.11110.18001.0_x64__8wekyb3d8bbwe\Photos.exe"
        subprocess.Popen(["start", os.path.join(folder_path, photo)],shell=True)
        
        # Ask user if they want to move or stay
        move_photos = input("Move to best photos folder? (y/n): ")
        
        # Kill photos process
        subprocess.run(["taskkill", "/IM", "Photos.exe", "/F"],
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL)


        if move_photos == 'y':
            os.rename(os.path.join(folder_path, photo), os.path.join(folder_path, 'best_photos', photo))


if __name__ == "__main__":
    # path to folder containing photos
    folder_path = r"E:\DCIM\114D5600"
    sort_photos(folder_path)
