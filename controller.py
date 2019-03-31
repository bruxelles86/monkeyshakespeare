import string
import random
import os
import json


counter = 0
longestMatch = ""

required_letters = list(string.ascii_letters)

#  created a method to load json object from sample

def load_book():
  with open('./shakespeare/samples.json') as f:
    return json.load(f)


def check(keystroke, counter, lines_to_check):
  def check_line(line):
    if counter <= len(line):
      if line[counter - 1].lower() == keystroke:   
        return True
      else: 
        return False
    return False


  #refactored code below to reduce lengthy varaibles
  new_lines_to_check = {"works": []}

  for work in lines_to_check["works"]: 
    new_lines_to_check["works"].append({
      "name": work["name"],
      "lines": list(filter(check_line, work["lines"]))
    })    
  return new_lines_to_check

def generate_keystroke():
  return random.choice(string.ascii_lowercase)
    
while True:
  lines_to_check = load_book()
  counter = 0
  while any(len(work["lines"]) > 0 for work in lines_to_check["works"]):
    key = generate_keystroke()
    counter+=1
    matched_lines = check(key, counter, lines_to_check)      
    lines_to_check = matched_lines
    if len(longestMatch) < counter: 
      for work in lines_to_check["works"]: 
        for line in work["lines"]:
          longestMatch = line[0:counter]

    print(longestMatch, counter, key)

  
  # if lines_to_check is empty, reload lines_to_check from file
  # check if match > longestMatch