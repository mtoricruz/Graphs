"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('nonexistent vertex')

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        # Create empty queue
        q = Queue()

        # Add starting vert ID
        q.enqueue(starting_vertex)

        # Create set for visited verts
        visited = set()

        # While queue is not empty
        while q.size() > 0:
            # Dequeue a vert
            v = q.dequeue()

            # if not visited
            if v not in visited:
                print(v)
                # Mark as visited
                visited.add(v)

                # add all neighbors to the queue
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        # Create an empty stack
        s = Stack()
        # Add starting vert ID
        s.push(starting_vertex)
        # create set for visited verts
        visited = set()

        # while stack is not empty
        while s.size() > 0:
            # pop a vert
            v = s.pop()
            # if not visited
            if v not in visited:
                print(v)
                # mark as visited
                visited.add(v)

                # add all neighbors to the stack
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # breakpoint()
        if visited is None:
            visited = set()
        
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)
        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and 
        q = Queue()
        # enqueue A PATH TO the starting vertID
        q.enqueue([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # Grab the last vertex from the PATH
            # -1 grabs the last item in the list
            last = path[-1]
            # If that vertex has not been visited..
            if last not in visited:
                # CHECK IF IT'S THE TARGET
                if last == destination_vertex:
                    # IF SO, RETURN PATH
                    return path
                # Mark it as visited...
                else:
                    visited.add(last)
                # Then add A PATH TO its neighbors to the back of the queue
            for neighbor in self.get_neighbors(last):
                # COPY THE PATH
                new_path = path.copy()
                # APPEND THE NEIGHBOR TO THE BACK
                new_path.append(neighbor)
                q.enqueue(new_path)

                

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])
        visited = set()

        while s.size() > 0:
            path = s.pop()
            last = path[-1]
            if last not in visited:
                if last == destination_vertex:
                    return path
                else:
                    visited.add(last)
            for neighbor in self.get_neighbors(last):
                new_path = path.copy()
                new_path.append(neighbor)
                s.push(new_path)
            

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
