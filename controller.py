import string
import random
import os
import json
from flask import Flask
from flask import (
  Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import threading 


app = Flask(__name__)

longestMatch = ""
data= []

if __name__ == '__main__':
  appThread = threading.Thread(target=app.run)
  appThread.daemon = True
  appThread.run()
 
  # mThread.join()

@app.route('/')
def index():  
  return render_template('index_monkey.html')
  # return (f'Hello, Monkey World!{result} : {data}')

@app.route('/matches')
def longest_match():
  result = monkey_typing()
  return f'{data} : {result}'


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

  new_lines_to_check = {"works": []}

  for work in lines_to_check["works"]: 
    new_lines_to_check["works"].append({
      "name": work["name"],
      "lines": list(filter(check_line, work["lines"]))
    })    
  return new_lines_to_check

def generate_keystroke():
  return random.choice(string.ascii_lowercase)
    
def monkey_typing():
  global longestMatch
  global data
  while True:    
    lines_to_check = load_book()
    counter = 0
    while any(len(work["lines"]) > 0 for work in lines_to_check["works"]):
      key = generate_keystroke()
      counter+=1
      matched_lines = check(key, counter, lines_to_check)      
      lines_to_check = matched_lines      
      for work in lines_to_check["works"]: 
        for line in work["lines"]:
          if len(longestMatch) < len(f'{line[0:counter]}'):
            longestMatch = line[0:counter]
            print(f"{key}:{counter} - {longestMatch}")

            if len(longestMatch) > 3:
              data.append(longestMatch)

            return longestMatch
      # return "No longest much found"
      
      
          
  


  
  # if lines_to_check is empty, reload lines_to_check from file
  # check if match > longestMatch