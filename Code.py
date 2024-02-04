from textblob import TextBlob
from pdfminer.high_level import extract_text
import os
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

# Ask the user to select a directory.
open_file = filedialog.askdirectory()

# Check if a directory was selected.
if open_file:
    new_names = []
    count = 0

    # Loop through each file in the selected directory.
    for filename in os.listdir(open_file):
        if filename.lower().endswith('.pdf'):  # Check if it's a PDF file.
            full_filename = os.path.join(open_file, filename)
            text = extract_text(full_filename)

            blob = TextBlob(text)
            # Find the first 10-digit number.
            std_id = [v for (v, t) in blob.tags if t == 'CD' and v.isdigit() and len(v) == 10]

            # If a 10-digit number is found, prepare to rename the file.
            if std_id:
                new_names.append(std_id[0])
                new_filename = os.path.join(open_file, std_id[0] + '.pdf')
                try:
                    os.rename(full_filename, new_filename)
                    count += 1
                except OSError as e:
                    print(f"Error renaming {filename}: {e}")

    # Print the results.
    print(f'{count} files renamed')
    res = os.listdir(open_file)
    print(res)
else:
    print("No directory selected.")
