"""RegexSearch. Search all *.txt-folders in a specified folder
using the supplied regex, and print all matches. If no folder is
specified, the program runs in the current working directory.
The user may also choose to specify that the results should be placed on the
clipboard.
Usage:
python re.py "<regex>" - Search all *.txt-files in the current directory and
                         print the results
python re.py "<regex>" "<path>" - Search all *.txt-files in the speicified directory
                                  for the specified regex and print the results.
python re.py "<regex>" copy - Search all *.txt-files in the current directory and
                              print the results and place them in the clipboard
python re.py "<regex>" "<path>" copy - Search all *.txt-files in the speicified directory
                                       for the specified regex and print the results
                                       and place them in the clipboard
"""

import os
import sys
import re
import pyperclip


def search_txt_files(regex, path, copy):
    regex = re.compile(regex)
    matches = []
    for filename in os.listdir(path):
        if filename.endswith("txt"):
            f = open(os.path.join(path, filename), 'r')
            text_to_search = f.read()
            for groups in regex.findall(text_to_search):
                matches.append(groups)
            f.close()
    if len(matches) == 0:
        print("No matches were found.")
        exit(0)
    else:
        print("The following matches were found:")
        print('\n'.join(matches))
        if copy:
            pyperclip.copy('\n'.join(matches))
            print("Matches copied to clipboard")
        exit(0)


if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) == 4:
        search_txt_files(sys.argv[1], sys.argv[2], True)
    elif len(sys.argv) == 3 and sys.argv[2].lower() == "copy":
        search_txt_files(sys.argv[1], ".", True)
    elif len(sys.argv) == 3 and sys.argv[2].lower() != "copy":
        search_txt_files(sys.argv[1], sys.argv[2], False)
    elif len(sys.argv) == 2:
        search_txt_files(sys.argv[1], ".", False)
    else:
        print("Invalid arguments. Please see below.")
        print(__doc__)
