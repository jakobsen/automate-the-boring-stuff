"""Convert dates from American format (MM-DD-YYYY) to European style
format (DD-MM-YYYY) in the name of files in the current working directory
or a subdirectory of the current working directory.
"""

import shutil
import os
import re

datePattern = re.compile(r"""
    ^(.*?)          # any text preceding the date
    ((0|1)?\d)-     # month number
    ((0|1|2|3)?\d)- # day number
    ((19|20)\d\d)   # year
    (.*?)$          # any text after the date
""", re.VERBOSE)

for amerFilename in os.listdir("."):
    mo = datePattern.search(amerFilename)
    if mo is None:
        continue

    # Get different parts of the filename
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    euroFilename = (beforePart +
                    dayPart +
                    "-" +
                    monthPart +
                    "-" +
                    yearPart +
                    afterPart)

    absWorkingDirectory = os.path.abspath(".")
    amerFilename = os.path.join(absWorkingDirectory, amerFilename)
    euroFilename = os.path.join(absWorkingDirectory, euroFilename)
    print(f"Renaming {amerFilename} to {euroFilename}")
    # Uncomment after testing:
    # shutil.move(amerFilename, euroFilename)