import click as clk
from numpy import random 
from time import sleep
from os import system, name

class PlayGrid:
 def __init__(self, players):
         self.players = players

class PlayGrid:
 def __init__(self, players):
         self.players = players
         draw_grid()
 def update(self, message):
          pass
 def move(dir, speed):
          pass
 def draw_grid():
     pass

 def empty_grid():
         self.grid = dict()
         str =""
         for row in range(1,10):
             str = ""
             for i in range(1,10):
                 str+=""
             self.grid[row] = str
         return(self.grid)

 def draw_grid():
         self.empty_grid()

 def draw_grid():
         self.empty_grid()
         print_s = "\n"

 def draw_grid():
         empty_grid()
         print_s = "\n"
         for key in self.grid:
             print_s = print_s + self.grid[key] + "\n"
         return(print_s)
 def empty_grid():
         self.grid = dict()
         str = ""
         for row in range(1,10):
             str = ""
             for i in range(1,10):
                 str +=""
         self.grid[row] = str

 def clear():
     if name == 'nt':
         _ = system('cis')
     else:
         _ = system('clear')

 def update(self, message):
         clear()
         grid = self.draw_grid()
         print(grid)
         print(string("\n", message))
 def __init__(self, players):
         self.players = players
         update()

class PlayGrid:
 def __init__(self, players):
         self.players = players
         self.update("Hello")
 def update(self, message):
         clear()
         grid = self.draw_grid()
         print(grid)
         print(string("\n", message))
 def draw_grid(self):
         self.empty_grid()
         print_s = "\n"
         for key in self.grid:
             print_s = print_s + self.grid[key] + "\n"
         return(print_s) 
def empty_grid(self):
        self.grid = dict()
        str = ""
        for row in range(1,10):
            str = ""
            for i in range(1,10):
                str += "'" 
            self.grid[row] = str
