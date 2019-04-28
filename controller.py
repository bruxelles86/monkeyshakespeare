import string
import random
import os
import json

longestMatch = ""

def load_book():
  with open('./shakespeare/samples.json') as f:
    return json.load(f)

def check_for_any_match(keystroke, counter, lines_to_check):
  def check_line(line):
    if counter <= len(line):
      if line[counter - 1].lower() == keystroke:   
        return True
      else: 
        return False
    return False

  new_lines_to_check = {"works": []}

  for work in lines_to_check["works"]: 
    new_lines_to_check["works"].append({
      "name": work["name"],
      "lines": list(filter(check_line, work["lines"]))
    })    
  return new_lines_to_check

def generate_keystroke():
  return random.choice(string.ascii_lowercase)

def save_matched_lines(line):
  f = open('./data.txt', "a+")
  f.write(line + ",")
  f.close()

while True:    
  lines_to_check = load_book()
  counter = 0

  while any(len(work["lines"]) > 0 for work in lines_to_check["works"]):
    key = generate_keystroke()
    counter+=1
    matched_lines = check_for_any_match(key, counter, lines_to_check)      
    lines_to_check = matched_lines  

    for work in lines_to_check["works"]: 
      for line in work["lines"]:
        if len(f'{line[0:counter]}') > len(longestMatch):
          longestMatch = line[0:counter]
          print(f"deep inside :- {key}:{counter} - {longestMatch}")
          
          if len(longestMatch) > 3:
            save_matched_lines(longestMatch)