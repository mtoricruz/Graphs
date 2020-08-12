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
    # create graph & empty list for paths of ancestors
    g = Graph()
    paths = []

    # add all vertexes from our ancestors list
    for i in ancestors:
        g.add_vertex(i[0])
        g.add_vertex(i[1])
    
    # add all edges in our graph
    for edge in ancestors:
        g.add_edge(edge[1], edge[0])
    
    # After graph complete, BFT
    # Create empty queue
    q = Queue()
    # add path from starting node to the queue
    q.enqueue([starting_node])
    # create empty set
    visited = set()

    # while queue is not empty
    while q.size() > 0:
        # dequeue the first path
        path = q.dequeue()
        # Grab the last vertex from the path
        vert = path[-1]
        # check if it has parents(neighbors)
        if g.get_neighbors(vert) == set():
            # if not, append to list of paths
            paths.append(path)
        # check if node has been visited
        if vert not in visited:
            # if not, mark visited
            visited.add(vert)
            # for each neighbor of the vert
            for neighbor in g.get_neighbors(vert):
                # make copy of path before adding
                new_path = path.copy()
                # add parent to path
                new_path.append(neighbor)
                # enqueue the new path
                q.enqueue(new_path)

    # To find longest paths, measure lengths of paths
    # keep track of max length of path in paths list
    max_len = max(len(p) for p in paths)
    # create a list of all paths that are in max_len
    longest_paths = [p for p in paths if len(p) == max_len]
    # max len is 1 if starting node has no parents 
    if max_len == 1:
        # return -1
        return -1
    # if there is a path in longest paths list
    if len(longest_paths) == 1:
        # choose the 0th index of the list and return the last index value 
        return longest_paths[0][-1]
    # if there are 2 longest paths
    if len(longest_paths) > 1:
        # lowest stores the 2 parent values in a list
        lowest = [p[-1] for p in longest_paths]
        # return the min value of that list to get the lowest numericID
        return min(lowest)

        

# R