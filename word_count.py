"""
This module counts the number of words in a file.
"""

import re

# FILE_PATH = 'youtube_transcript.html'
FILE_PATH = 'transcript.txt'
CHUNK_SIZE = 100000  # number of characters to read in each chunk
WORD_COUNT = 0

with open(FILE_PATH, 'r', encoding='utf-8') as file:

    while True:
        chunk = file.read(CHUNK_SIZE)
        if not chunk:
            # end of file
            break
        # extract the text from the HTML chunk using regular expressions
        text = re.sub('<[^<]+?>', '', chunk)
        # split the text into words and count them
        WORD_COUNT += len(text.split())

print(f"The number of words in the HTML file is: {WORD_COUNT}")
