import os
for folderName, subfolders, filenames in os.walk("delicious"):
    print(f"The current folder is {folderName}")

    for subfolder in subfolders:
        print(f"SUBFOLDER OF {folderName}: {subfolder}")

    for filename in filenames:
        print(f"FILE INSIDE {folderName}: {filename}")

    print("")
