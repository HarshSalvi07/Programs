from collections import deque #Import deque for efficient queue operations (used in BFS)

class Graph:
    def __init__ (self,num_vertices,directed = False):
        #Initializes the graph with number of vertices and whether it's directed
        self.num_vertices = num_vertices
        self.directed = directed
        self.adj_matrix = []  #This will be our adjacency matrix

        #Create a 2D matrix (list of lists) filled with 0s initially
        for i in range (num_vertices):
            row = [0] * num_vertices  #Row of zeroes
            self.adj_matrix.append(row)

    def add_edge(self,r,c):
        #Add an edge from s to d
        if r < 0 or r >= self.num_vertices or c < 0 or c >= self.num_vertices:
            print(f"Error: Vertex {r} or {c} is out of graph bounds.")
            return
        
        self.adj_matrix[r][c] = 1 #Set edge from r to c
        if not self.directed:
            self.adj_matrix[r][c] = 1 #If undirected , also set edge from r to c

    def print_matrix(self):
        #Print the adjacency matrix row by row
        print("Adjacency Matrix: ")
        for row in self.adj_matrix:
            print(row)

    def bfs(self, start):
        #Breadth-First Search using queue
        if start < 0 or start >= self.num_vertices:
            print(f"Error: Start vertex {start} is out of graph bounds.")
            return
    
        visited = [False] * self.num_vertices  #Track visited vertices
        queue = deque()  #Create a queue for BFS

        visited[start] = True  #Mark starting vertex as visited
        queue.append(start)  #Enqueue starting vertex

        print("BFS traversal starting from vertex", start , ":",end= " ")
        while queue:
            vertex = queue.popleft()  #Dequeue a vertex
            print(vertex, end= " ")  #Visit the vertex

            #Visit all neighbors of the current vertex
            for neighbor in range(self.num_vertices):
                