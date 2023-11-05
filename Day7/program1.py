class Node:
    def __init__(self, name: str, parent: "Node"):
        self.name = name
        self.parent = parent
        self.size = 0
        self.children = []



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
    # cd or ls command
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
   #from ipdb import set_trace; set_trace()
    for node in tree.children:
        tree_traversal(node, values)
    # 
    children_vals = [child.size for child in tree.children]
    values.append(tree.size + sum(children_vals))

sizes = []
open_file("input.txt")
tree_traversal(tree, sizes)

sum = 0
for item in sizes:
    if item <= 100000:
        sum +=item

print(sum)




