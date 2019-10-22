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

if __name__ == "__main__":
    regex = re.compile(sys.argv[1])
    matches = []
    # Begin with the case that we only get a regex
    if (len(sys.argv) == 2 or
            (len(sys.argv) == 3 and sys.argv[2].lower() == "copy")):
        for filename in os.listdir('.'):
            if filename.endswith(".txt"):
                f = open(filename, 'r')
                text_to_search = f.read()
                for groups in regex.findall(text_to_search):
                    matches.append(groups)
                f.close()
        print("The following matches were found:")
        print('\n'.join(matches))
        if len(sys.argv) == 3 and sys.argv[2].lower() == "copy":
            pyperclip.copy('\n'.join(matches))
            print("Matches copied to clipboard")

    if len(sys.argv) == 3 and sys.argv[2].lower() != "copy":
        for filename in os.listdir(sys.argv[2]):
            if filename.endswith(".txt"):
                f = open(sys.argv[2] + "/" + filename, 'r')
                text_to_search = f.read()
                for groups in regex.findall(text_to_search):
                    matches.append(groups)
                f.close()
        print("The following matches were found:")
        print('\n'.join(matches))

    if len(sys.argv) == 4 and sys.argv[3].lower == "copy":
        for filename in os.listdir(sys.argv[2]):
            if filename.endswith(".txt"):
                f = open(sys.argv[2] + "/" + filename, 'r')
                text_to_search = f.read()
                for groups in regex.findall(text_to_search):
                    matches.append(groups)
                f.close()
            print("The following matches were found:")
            print('\n'.join(matches))
            pyperclip.copy('\n'.join(matches))
            print("Matches copied to clipboard")
