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


def tree_traversal2(treev, values):
    for node in treev.children:
        tree_traversal2(node, values)
    children_vals = [child.size for child in treev.children]
    if treev.size == 0:
        treev.size += sum(children_vals)
    values.append(treev.size + sum(children_vals))

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


def get_size(tree):
    count = 0
    for node in tree.children:
        get_size(node)
    count += node.size



sizes = []
open_file("input.txt")
set_folder_size(tree)

tree_traversal(tree, sizes)
print("Total space in use is: ")
print((sorted(sizes, reverse=True)))

print('Space left is:')
space_left = 70000000 - (sorted(sizes, reverse=True)[0])
print(space_left)

print('Space required is:')
space_required = 30000000 - space_left
print(space_required)

print(f"Finding the smallest directory of size {space_required} or greater . . .")

res_sizes = []

for item in sorted(sizes):
    if item >= space_required:
        print(item)
        break
