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

def check(keystroke, counter, lines_to_check):
  def check_line(line):
    if line[counter - 1].lower() == keystroke:
      return True
    else:
      return False

  new_lines_to_check = {"works": []}

  for work in lines_to_check["works"]:
    matched_lines = list(filter(check_line, work["lines"]))
    new_work = { 
      "name": work["name"],
      "lines": matched_lines
    }
    new_lines_to_check["works"].append(new_work)
  return new_lines_to_check       
      



#generates letter
def generate_keystroke():
  return random.choice(string.ascii_lowercase)
    
while True:
  while any(len(work["lines"]) > 0 for work in lines_to_check["works"]):
    counter+=1
    key = generate_keystroke()
    matched_lines = check(key, counter, lines_to_check)
    lines_to_check = matched_lines
    print(lines_to_check, counter, key)

  # if lines_to_check is empty, reload lines_to_check from file
  # check if match > longestMatch

