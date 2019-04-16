import string
import random
import os
import json

import socket
import threading
import sys
from monkey import Monkey

class Server:
  #create a socket object
  soket = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
  connections = []

  def __init__(self):
    self.soket.bind(('0.0.0.0', 4545))
    self.soket.listen(1)

  def handler(self, c, a ):
    longestMatch = ''
    while True:
      lines_to_check = self.load_book()
      counter = 0
      while any(len(work["lines"]) > 0 for work in lines_to_check["works"]):
        key = self.generate_keystroke()
        counter+=1
        matched_lines = self.check(key, counter, lines_to_check)      
        lines_to_check = matched_lines
        if len(longestMatch) < counter: 
          for work in lines_to_check["works"]: 
            for line in work["lines"]:
              longestMatch = line[0:counter]

        for connection in self.connections:
          connection.send(bytes(longestMatch, 'utf-8'))
          
      data = c.recv(1024)
      if len(data) < 1:
        print(str(a[0]) + ':' + str(a[1]), "Disconnected")
        self.connections.remove(c)
        c.close()
        break

      print(longestMatch, counter, key, len(data))

  def run(self):
    while True:
      c, a = self.soket.accept()
      cThread = threading.Thread(target=self.handler, args=(c, a))
      cThread.daemon = True
      cThread.start()
      self.connections.append(c)
      print(str(a[0]) + ':' + str(a[1]), "connected")
  
  def load_book(self):
    with open('./shakespeare/samples.json') as f:
      return json.load(f)

  def check(self, keystroke, counter, lines_to_check):
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

class Client:
  soket = socket.socket( socket.AF_INET, socket.SOCK_STREAM)

  def __init__(self, address):
    self.soket.connect((address, 4545))

    iThread = threading.Thread(target=self.sendMsg)
    iThread.daemon = True
    iThread.start()

    while True:
      data = self.soket.recv(1024)
      if not data:
        break
      print(str(data, 'utf-8'))

  def sendMsg(self):
    while True:
      self.soket.send(bytes(input(""), 'utf-8'))

# to distingush server or client
if len(sys.argv) > 1:
  client = Client(sys.argv[1])
else:
  server = Server()
  server.run()
  




