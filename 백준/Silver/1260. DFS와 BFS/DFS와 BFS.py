N, M, V = map(int, input().split())

visited = [False for _ in range(N)]
connected_nodes = [set() for _ in range(N)]

for _ in range(M):
    node1, node2 = map(int, input().split())
    connected_nodes[node1 - 1].add(node2)
    connected_nodes[node2 - 1].add(node1)
    
for i in range(len(connected_nodes)):
    temp = sorted(list(connected_nodes[i]))
    connected_nodes[i] = temp



# dfs
def get_dfs_result(visited, connected_nodes, V):
    visited = visited[:]
    connected_nodes = connected_nodes[:]
    V = V

    stack = []
    answer = []


    stack = connected_nodes[V - 1][:]
    visited[V - 1] = True
    answer.append(V)
    while stack!=[]:
        temp = stack.pop(0)

        if visited[temp - 1]:
            continue

        stack = connected_nodes[temp - 1] + stack
        visited[temp - 1] = True
        answer.append(temp)

    return answer




# bfs
def get_bfs_result(visited, connected_nodes, V):
    visited = visited[:]
    connected_nodes = connected_nodes[:]
    V = V

    queue = []
    answer = []
    
    
    queue = connected_nodes[V - 1][:]
    visited[V - 1] = True
    answer.append(V)
    while queue!=[]:
        temp = queue.pop(0)

        if visited[temp - 1]:
            continue

        queue = queue + connected_nodes[temp - 1]
        visited[temp - 1] = True
        answer.append(temp)

    return answer



print(" ".join(map(str, (get_dfs_result(visited, connected_nodes, V)))))
print(" ".join(map(str, (get_bfs_result(visited, connected_nodes, V)))))