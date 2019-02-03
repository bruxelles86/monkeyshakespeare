import string
import random
import os

counter = 0
longestMatchLength = 0
longestMatch = ""

#need to open and read the file
required_letters = list(string.ascii_letters)

def book_reader(keystroke):
  directory = "./shakespeare"
  for filename in os.listdir(directory):
    file = open(os.path.join(directory, filename), "r")
    for line in file:
      characters = list(line)
      chars_letters_only = [char for char in characters if char in required_letters]
      if (len(chars_letters_only) < counter):
        continue
      if (chars_letters_only[counter-1] == keystroke):
        print(chars_letters_only[counter-1], "found on count", counter)

#generates letter
def generate_keystroke():
  return random.choice(string.ascii_lowercase)
    
while True:
  counter += 1
  key = generate_keystroke()
  book_reader(key)