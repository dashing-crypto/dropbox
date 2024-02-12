'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
print ('Hello World')

class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

# Creating nodes
node_a = Node('A')
node_b = Node('B')
node_c = Node('C')
node_d = Node('D')

# Building connections
node_a.add_neighbor(node_b)
node_a.add_neighbor(node_c)
node_b.add_neighbor(node_c)
node_b.add_neighbor(node_d)
node_c.add_neighbor(node_d)

#this a uni directional graph

#insted of characters we could have used actual nnode to this above graph
#

