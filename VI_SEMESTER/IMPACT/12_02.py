from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v, visited, stack):
        visited[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, stack)
        stack.append(v)

    def transpose(self):
        g = Graph(self.V)
        for i in self.graph:
            for neighbor in self.graph[i]:
                g.add_edge(neighbor, i)
        return g

    def dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=" ")
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited)

    def print_sccs(self):
        stack = []
        visited = [False] * self.V

        # Fill vertices in stack according to their finishing times
        for i in range(1, self.V):
            if not visited[i]:
                self.dfs(i, visited, stack)

        # Create a reversed graph
        gr = self.transpose()

        # Mark all the vertices as not visited (For the second DFS)
        visited = [False] * self.V

        # Now process all vertices in order defined by Stack
        while stack:
            i = stack.pop()
            if not visited[i]:
                gr.dfs_util(i, visited)
                print("")

# Initialize the graph
g = Graph(19)  # Adjusted for 1-based index
edges = [(1, 2), (2, 3), (3, 7), (7, 14), (14, 15), (4, 1), (5, 4), (2, 5), 
         (3, 6), (6, 5), (15, 16), (16, 13), (13, 17), (17, 11), (11, 6), 
         (17, 18), (18, 9), (9, 4)]
for u, v in edges:
    g.add_edge(u, v)

# Print strongly connected components
print("Strongly Connected Components:")
g.print_sccs()
