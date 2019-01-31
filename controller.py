import string
import random 


longestMatchLength = 0
longestMatch = ""

#need to open and read the file


def book_reder():
  pass
  file = open("./shakespeare/sample1", "r")
  for line in file:
    words = line.split(" ")
    for word in words:
      print(word)

#generates letter
def rand_keystroke_generator(num):
  a = 0
  while a < num:
    return random.choice(string.ascii_letters)
    a += 1
    
    
print( rand_keystroke_generator(10))

