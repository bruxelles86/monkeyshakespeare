import multiprocessing
from flask import Flask
from flask import render_template
from flask import jsonify

app = Flask(__name__)

def get_matched_words():
  with open("./data.txt") as f:
    content = f.read()
    matches = content.split(",")
    return matches

@app.route('/')
def index():
  return render_template('index_monkey.html')  

@app.route('/matches')
def display_longest_match():
  return render_template('match.html', data=get_matched_words())

@app.route('/match')
def get_match():
  data = get_matched_words()  
  return  jsonify(data)

