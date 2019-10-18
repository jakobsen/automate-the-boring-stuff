"""Adds bullet points to each line of text on the clipboard, ready for pasting
into e.g. Markdown or Wikipedia.

As an example, if the users copy

Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars

and run the script, it will leave

* Lists of animals
* Lists of aquarium life
* Lists of biologists by author abbreviation
* Lists of cultivars

on the clipboard.
"""

import pyperclip

text = pyperclip.paste()
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = "* " + lines[i]
text = '\n'.join(lines)
pyperclip.copy(text)
