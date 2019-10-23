"""Copies an entire folder and its contents into a ZIP file whose name
increments.
Note that with only minor changes, shutil.make_archive() could be used
instead, accomplishing the same thing with less code.
"""

import zipfile
import shutil
import os


def backUpToZip(folder):
    folder = os.path.relpath(folder)
    # Determine the filename
    number = 1
    while True:
        zipFileName = f"{folder}_{number}.zip"
        if not os.path.exists(zipFileName):
            break
        number += 1

    # Create the ZIP file
    print(f"Creating {os.path.relpath(zipFileName)} ...")
    backupZip = zipfile.ZipFile(zipFileName, 'w')

    for foldername, subfolders, filenames in os.walk(folder):
        print(f"Currently adding items from  {os.path.relpath(foldername)}")
        backupZip.write(foldername)
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith(".zip"):
                continue
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    # shutil.make_archive(zipFileName, 'zip', folder)
    print("Done.")


if __name__ == "__main__":
    backUpToZip("delicious")
