from collections import deque
def bfs_of_graph(v,adj_list):
    visitd = [False] * (v + 1)
    bfs_resut = []
    queue = deque([1])
    visitd[1] = True
    
    while queue:
        node = queue.popleft()
        bfs_resut.append(node)
        
        for neighbour in adj_list[node]:
            if not visitd[neighbour]:
                visitd[neighbour] = True
                queue.append(neighbour)
                
    return bfs_resut

if __name__ == "__main__":
    v = 5          
    adj_list = {
        1: [2, 3],
        2: [1, 5],
        3: [1, 4, 6],
        4: [3],
        5: [2, 7],
        6: [3, 7],
        7: [5, 6]
        }
    v = len(adj_list)
    result = bfs_of_graph(v, adj_list)
    print("BFS traversal of the graph is:", result)