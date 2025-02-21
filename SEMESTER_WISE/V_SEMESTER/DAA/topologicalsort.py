from collections import deque
def dfs(node, vis, st, adj):
    vis[node] = True
    
    for neighbour in adj[node]:
        if not vis[neighbour]:
            dfs(neighbour, vis, st, adj)
            
    st.append(node)
    
def topo_sort(v, adj):
    vis = [False] * v        
    st = deque()
    
    for i in range(v):
        if not vis[i]:
            dfs(i, vis, st, adj)
    return list(reversed(st))
if __name__ == "__main__":
    v =6
    adj = {
        0: [],
        1: [],
        2: [3],
        3: [1],
        4: [0, 1],
        5: [0, 2]
        }
    v = len(adj)
    result = topo_sort(v, adj)
    print("Topological sort of the graph is:", result)
    print("Topological sort:", " ".join(map(str, result)))