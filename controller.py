import string
import random
import os
import json

counter = 0
longestMatchLength = 0
longestMatch = ""

required_letters = list(string.ascii_letters)

with open('./shakespeare/samples.json') as f:
  lines_to_check = json.load(f)
  print(lines_to_check)


def check(keystroke, count, lines_to_check):
  for work in lines_to_check["works"]:
    for line in work["lines"]:
      

  # directory = "./shakespeare"
  # for filename in os.listdir(directory):
  #   file = open(os.path.join(directory, filename), "r")
  #   for line in file:
  #     characters = list(line)
  #     chars_letters_only = [char for char in characters if char in required_letters]
  #     if (len(chars_letters_only) < count):
  #       continue
  #     if (chars_letters_only[count-1] == keystroke):
  #       print(chars_letters_only[count-1], "found on count", count)

#generates letter
def generate_keystroke():
  return random.choice(string.ascii_lowercase)
    
while True:
  while any(len(work["lines"]) > 0 for work in lines_to_check["works"]):
    counter += 1
    key = generate_keystroke()
    check(key, counter, lines_to_check)

  # if lines_to_check is empty, reload lines_to_check from file
  # check if match > longestMatch

