"""Multiple clipboard manager. Save content from the clipboard under keywords
and retrieve them.
USAGE:
python mcb.py save <keyword> – Saves clipboard to keyword
python mcb.py <keyword> – Places content of keyword in clipboard. If keyword
is not found, nothing happens.
python mcb.py list – See all saved keywords.
"""

import sys
import shelve
import pyperclip


if __name__ == "__main__":
    mcbShelf = shelve.open("mcb")
    if len(sys.argv) == 3 and sys.argv[1].lower() == "save":
        if sys.argv[2].lower() in mcbShelf.keys():
            response = input(
                "Warning! This key already exists. Overwrite content? (y/n) ")
            while True:
                if response.lower().strip()[0] == 'y':
                    break
                elif response.lower().strip()[0] == 'n':
                    print("Program aborted.")
                    exit(0)
                else:
                    response = input("Please enter a valid response. (y/n) ")
        mcbShelf[sys.argv[2].lower()] = pyperclip.paste()
        print(f"Clipboard content successfully saved under"
              f" '{sys.argv[2].lower()}'")
    elif len(sys.argv) == 2:
        if sys.argv[1].lower() == "list":
            print("The following keywords are stored:")
            for key in mcbShelf.keys():
                print(key)
        else:
            if sys.argv[1].lower() in mcbShelf.keys():
                pyperclip.copy(mcbShelf[sys.argv[1].lower()])
                print("Content successfully copied to clipboard.")
            else:
                print("Key not found.")
    mcbShelf.close()
