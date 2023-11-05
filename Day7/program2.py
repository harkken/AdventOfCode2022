class Node:
    def __init__(self, name: str, parent: "Node"):
        self.name = name
        self.parent = parent
        self.size = 0
        self.children = []

    def __repr__(self):
        return f'Node("{self.name}",{self.size})'


# creates a new Node for the tree
def create_root_node(name) -> Node:
    return Node(name, parent=None)  


tree = create_root_node("/")
current_node = tree

# open file
def open_file(file_name: str):
   with open(file_name, mode= 'r') as test_file:
      for line in test_file:
        line = line.strip("\n")
        parse_line(line)

# Line processing for each line
def parse_line(line: str):
    select_command(line)


def parse_file(line: str):
    global current_node
    current_node.size += int(line.split(" ")[0])

def select_command(line: str):
    global current_node
    if "$ cd /" in line:
        pass
    if "$ cd .." in line:
        current_node = current_node.parent
    elif "$ cd" in line:
        dirname = line.split("$ cd ")[1]
        for c in current_node.children:
            if c.name == dirname:
                current_node = c
                break
    elif "$ ls" in line:
        pass
    elif "dir" in line: 
        node = create_node(line)
        current_node.children.append(node)
    else:
        parse_file(line)
        

def create_node(line):
    global current_node
    name = line.split("dir ")[1]
    return Node(name, parent=current_node)  


def tree_traversal(tree, values):
    for node in tree.children:
        tree_traversal(node, values) 
    values.append(tree.size)

def set_folder_size(tree):
    if tree.children is None:
        return tree.size
    else:
        tree.size += sum([set_folder_size(child) for child in tree.children])
        return tree.size

sizes = []
open_file("input.txt")
set_folder_size(tree)

tree_traversal(tree, sizes)

space_left = 70000000 - (sorted(sizes, reverse=True)[0])
space_required = 30000000 - space_left

for item in sorted(sizes):
    if item >= space_required:
        print(item)
        break
