from gtts import gTTS
import os

# Reading the input file and setting up the text
fh = open("test.txt", "r")
myText = fh.read().replace("\n", " ")

# Setting up the language
language = "en"

# Setting up the output
output = gTTS(text=myText, tld="com", lang=language, slow=True)

# Saving the output file and closing the input file
output.save("output.mp3")
fh.close()

# Reading the output file
os.system("start output.mp3")
