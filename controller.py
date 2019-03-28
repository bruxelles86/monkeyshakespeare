import string
import random
import os
import json

counter = 0
longestMatchLength = 0
longestMatch = ""

required_letters = list(string.ascii_letters)
#  created a method to load json object from sample
def load_book():
  with open('./shakespeare/samples.json') as f:
    lines_to_check = json.load(f)
    return lines_to_check

def check(keystroke, counter, lines_to_check):
  def check_line(line):
    if any(leter.lower() == keystroke for leter in line):        
      return True
    else:
      return False

  #refactored code below to reduce lengthy varaibles
  new_lines_to_check = { "works": []}

  for work in lines_to_check["works"]: 
    new_lines_to_check["works"].append({
      "name": work["name"],
      "lines": list(filter(check_line, work["lines"]))
    })
       
  return new_lines_to_check

# generates letter --we need to work on this whether to generate
# a single leter or a combination of letters that a monkey can type i.e 'xlm'
# maybe generate random word length as well 
def monkey_typed_word():
  return f"{generate_keystroke()}{generate_keystroke()}{generate_keystroke()}" 

def generate_keystroke():
  return random.choice(string.ascii_lowercase)
    
while True:
  word = monkey_typed_word()
  print("the word is", word)
  lines_to_check = load_book()
  counter+=1
  print("started again", counter)

  while any(len(work["lines"]) > 0 for work in lines_to_check["works"]):
    key = generate_keystroke()
    matched_lines = check(key, counter, lines_to_check)      
    lines_to_check = matched_lines
    print(lines_to_check, counter, key)

  
  # if lines_to_check is empty, reload lines_to_check from file
  # check if match > longestMatch

