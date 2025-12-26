# PhotoCopier
A script to make sorting through photos quicker and easier.

# How to use
Run the executables found in the `dist` folder. 
Suggestion is the `sort_photos_ui.exe`. This will prompt you to select the folder containing the photos you want to sort. You can then use the `left` and `right` arrow keys to navigate and press `y` or `n` to move the photo to a `best_photos` folder located in the same folder as the originally selected folder. 

This approach simplifies the process as now no python is needed to be run.


# Note for creating executables.
Run: `python -m PyInstaller --onefile sort_photos_ui.py`
