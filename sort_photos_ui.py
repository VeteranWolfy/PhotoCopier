import os
import shutil
from tkinter import *
from tkinter.filedialog import askdirectory
from PIL import Image, ImageTk


""" 
--------------------------------- SORT_PHOTOS_UI ---------------------------------
Sort through all photos in source folder.


How to use:
Run python script
Press `y` when on Photo Sorter window and it will move the .jpg and .nef (if it exists) file to the destination folder
Press `n` and the photo will be skipped. 
"""

#SOURCE_FOLDER = r"E:\DCIM\114D5600"
SOURCE_FOLDER=askdirectory(title="Select original photos folder")
DEST_FOLDER = os.path.join(SOURCE_FOLDER, "best_photos")

os.makedirs(DEST_FOLDER, exist_ok=True)


class PhotoSorter:
    def __init__(self, master):
        self.master = master
        master.title("Photo Sorter")

        # Load file list
        self.files = [
            f for f in os.listdir(SOURCE_FOLDER)
            if f.lower().endswith((".jpg", ".png", ".jpeg", ".mov"))
        ]
        self.index = 0

        # UI
        self.canvas = Canvas(master, bg="black")
        self.canvas.pack(fill=BOTH, expand=True)

        # Keyboard bindings
        master.bind("<Left>", self.prev_image)
        master.bind("<Right>", self.next_image)
        master.bind("<y>", self.move_image)
        master.bind("<n>", self.skip_image)

        self.display_image()

    def display_image(self):
        """Show current image or a placeholder for video."""
        file = self.files[self.index]
        path = os.path.join(SOURCE_FOLDER, file)

        if file.lower().endswith(".mov"):
            img = Image.new("RGB", (800, 600), color=(20, 20, 20))
            txt = ImageTk.PhotoImage(img)
            self.canvas.delete("all")
            self.canvas.create_image(400, 300, image=txt)
            self.canvas.create_text(400, 300, text="VIDEO FILE", fill="white", font=("Arial", 32))
            self.current_img = txt
            return

        # Load image
        img = Image.open(path)

        # Resize to window while keeping aspect ratio
        w, h = img.size
        max_w, max_h = 1200, 900
        scale = min(max_w / w, max_h / h, 1)
        img = img.resize((int(w * scale), int(h * scale)), Image.LANCZOS)

        self.photo_image = ImageTk.PhotoImage(img)

        # Display on canvas
        self.canvas.delete("all")
        self.canvas.create_image(600, 450, image=self.photo_image)

    def move_image(self, event=None):
        """Move current image and show next."""
        file = self.files[self.index]
        src = os.path.join(SOURCE_FOLDER, file)
        dst = os.path.join(DEST_FOLDER, file)

        shutil.move(src, dst)

        # Try moving .NEF file as well
        nef_file = file.replace(".JPG", ".NEF")
        if os.path.exists(os.path.join(SOURCE_FOLDER, nef_file)):
            src = os.path.join(SOURCE_FOLDER, nef_file)
            dst = os.path.join(DEST_FOLDER, nef_file)
            shutil.move(src, dst)

        print("Moved:", file)
        self.next_image()

    def skip_image(self, event=None):
        """Keep current image, go next."""
        print("Skipped:", self.files[self.index])
        self.next_image()

    def next_image(self, event=None):
        """Show next image."""
        if self.index < len(self.files) - 1:
            self.index += 1
            self.display_image()
        else:
            print("All photos sorted!")
            self.master.quit()

    def prev_image(self, event=None):
        """Show previous image."""
        if self.index > 0:
            self.index -= 1
            self.display_image()


root = Tk()
root.geometry("1200x900")
app = PhotoSorter(root)
root.mainloop()
