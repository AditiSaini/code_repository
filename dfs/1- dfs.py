def dfs_iterative(adj, source, end):
    stack = [source]
    visited = set()
    while len(stack)>0:
        cur_data = stack.pop()
        visited.add(cur_data)
        for data in adj[cur_data]:
            if data == end:
                return True
            if data not in visited:
                stack.append(data)
    return False

def dfs(adj, source, end):
    visited = set()
    current = source
    return dfs_recurse(adj, current, end, visited)

def dfs_recurse(adj, current, end, visited):
    if current == end:
        return True
    visited.add(current)
    for data in adj[current]:
        if data not in visited:
            found = dfs_recurse(adj, data, end, visited)
            if found:
                return True
    return False
    

def add_edge(adj, s, t):
    # Add edge from vertex s to t
    adj[s].append(t)
    # Due to undirected Graph
    adj[t].append(s)
    
if __name__ == "__main__":
    V = 5

    # Create an adjacency list for the graph
    adj = [[] for _ in range(V)]

    # Define the edges of the graph
    edges = [[1, 2], [1, 0], [2, 0], [2, 3], [2, 4]]

    # Populate the adjacency list with edges
    for e in edges:
        add_edge(adj, e[0], e[1])

    source = 1
    end = 3
    print(dfs(adj, source, end))
