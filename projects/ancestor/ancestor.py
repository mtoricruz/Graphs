from util import Stack, Queue
from graph import Graph
# U
# If > 1 ancestor for 'earliest' return the lowest numericID 
# Way to check if node has no parent, mark as earliest ancestor and 
# return that node
# P
# if starting_node has no ancestors:
# if input individual not in ancestors return -1


# E
def earliest_ancestor(ancestors, starting_node):
    q = Queue()
    q.enqueue(starting_node)
    paths = []
    visited = set()
    if starting_node not in ancestors:
        return -1

    while q.size() > 0:
        v = q.dequeue()

        if v not in visited:
            visited.add(v)

            for neighbor in self.get_neighbors(v):
                q.enqueue(neighbor)

        

# R