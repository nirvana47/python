"""
This module contains code to extract text from a specific segment of a YouTube transcript HTML file.
"""

import re

# Open the HTML file and read its contents
with open('youtube_transcript.html', 'r', encoding='utf-8') as f:
    html_file = f.read()

# Define a regular expression to match HTML tags
tag_regex = re.compile(r'<[^>]+>')

# Define a regular expression to match timestamps of the format x:xx, xx:xx, or x:xx:xx
timestamp_regex = re.compile(r'^(?:\d{1,2}:)?\d{1,2}:\d{2}$')

# Remove HTML tags from the HTML file and extract the text
text = tag_regex.sub('', html_file)

# Split the text into lines and remove empty and timestamp-only lines
lines = [line.strip() for line in text.splitlines() if line.strip() and not timestamp_regex.match(line.strip())]

# Delete the first 200 lines of text
lines = lines[208:-380]

# Join the lines into a single string
text = '\n'.join(lines)

# Replace &amp; with &
text = text.replace('&amp;', '&')

# Save the extracted text to a text file
with open('transcript.txt', 'w', encoding='utf-8') as f:
    f.write(text)


# import re

# # Open the HTML file and read its contents
# with open('youtube_transcript.html', 'r', encoding='utf-8') as f:
#     html_file = f.read()

# # Define a regular expression to match HTML tags
# tag_regex = re.compile(r'<[^>]+>')

# # Remove HTML tags from the HTML file and extract the text
# text = tag_regex.sub('', html_file)

# # Save the extracted text to a text file
# with open('transcript.txt', 'w', encoding='utf-8') as f:
#     f.write(text)
