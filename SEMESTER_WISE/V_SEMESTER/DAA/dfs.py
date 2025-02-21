def dfs_of_graph(v, adj_list):
    visited = [False] * (v + 1)
    dfs_result = []
    
    def dfs(node):
        visited[node] = True
        dfs_result.append(node)
        
        for neighbour in adj_list.get(node, []):
            if not visited[neighbour]:
                dfs(neighbour)
    dfs(1)
    return dfs_result

if __name__ == "__main__":
    adj_list ={
        1: [2, 3],
        2: [1, 5],
        3: [1, 4, 6],
        4: [3],
        5: [2, 7],
        6: [3, 7],
        7: [5, 6]
        }       
    v = len(adj_list)
    result = dfs_of_graph(v, adj_list)
    print("DFS traversal of the graph is:", result)
# Output: DFS traversal of the graph is: [1, 2, 5, 7, 6, 3, 4]
                    