import string
import random
import os
import json

class Monkey:
  def __init__(self, book_path):    
    self.longestMatch = ""
    self.book_path = book_path
      
  required_letters = list(string.ascii_letters)
  longestMatch = ""

  def load_book(self):
    with open(f'{self.book_path}') as f:
      return json.load(f)

  def check(self,keystroke, counter, lines_to_check):
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

  def generate_keystroke(self):
    return random.choice(string.ascii_lowercase)

  def run(self, load_book, generate_keystroke, check):
    while True:
      lines_to_check = self.load_book()
      counter = 0
      while any(len(work["lines"]) > 0 for work in lines_to_check["works"]):
        counter+=1
        matched_lines = self.check(generate_keystroke, counter, lines_to_check)      
        lines_to_check = matched_lines
        if len(self.longestMatch) < counter: 
          for work in lines_to_check["works"]: 
            for line in work["lines"]:
              self.longestMatch = line[0:counter]
              print(self.longestMatch)
  
  def print_longest_match(self):
    # print(self.longestMatch)
    return self.longestMatch 






# #########################################

# class Monk:
#   def generate_keystroke(self):
#     return random.choice(string.ascii_lowercase)

# class server:

#   def__init__(self, keystroke):
#     self.counter = 0




#   def load_book(self, path):
#     with open(f'{path}') as f:
#       return json.load(f)

#   def filter_matched_lines(self,line,keystroke,counter):
#     def check_line(line):
#       if counter <= len(line):
#         if line[counter - 1].lower() == keystroke:   
#           return True
#         else: 
#           return False
#       return False
#     list(filter(check_line, line))


#   def check_for_matched_lines(self, lines_to_check):
#     matched_lines = {"works": []}
#     for work in lines_to_check["works"]: 
#       matched_lines["works"].append({
#         "name": work["name"],
#         "lines": self.filter_matched_lines(work["lines"])
#       })    
#     return matched_lines



# # if lines_to_check is empty, reload lines_to_check from file
# # check if match > longestMatch

