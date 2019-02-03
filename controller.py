import string
import random
import os


longestMatchLength = 0
longestMatch = ""

#need to open and read the file
required_letters = list(string.ascii_letters)
def book_reader():
  directory = "./shakespeare"
  for filename in os.listdir(directory):
    file = open(os.path.join(directory, filename), "r")
    for line in file:
      characters = list(line)
      print([char for char in characters if char in required_letters])

  #   open("./shakespeare/sample1", "r")

#generates letter
# def rand_keystroke_generator(num):
#   a = 0
#   while a < num:
#     return random.choice(string.ascii_letters)
#     a += 1
    
    
# print( rand_keystroke_generator(10))
book_reader()

