"""
cd / =  start
$ = command

command is 

 - create the tree
 - tree folding

 - Groups/ Classes/ Expressions

 - Command 
 - directory
 - file

 - Command 
    - ls 
    - cd 

 - File
   - <num> file name
 
 - Directory 
   - dir <dir_name>

- build the directory tree where dirs are nodes
"""
from enum import Enum

class Command(Enum):
    ls_command = "ls"
    cd_command = "cd"

class Node:
    """
    Node class to hold our dirs
    """
    def __init__(self, data):
        self.data = data
        self.children = [] # other nodes, dirs or files

class File:
    """
    class to hold file instances
    """
    def __init__(self, name, size):
        self.name = name
        self.size = size

class Dir:
    def __init__(self, name):
        self.name = name

        
start_node = Node(Dir('/'))

with open("input.txt", "r") as file:
    node = start_node
    for line in file:
        line = line.strip()
        # cmd
        if '$' in line:
            # dir
            if 'cd' in line:
                # set the current node to be a level 
                # deeper
                dir_name = line.split()[1]
                cur_dir = Dir(dir_name)
                cur_node = Node(cur_dir)
                
            # list
            elif 'ls' in line:  

            #node = start_node.children[]
