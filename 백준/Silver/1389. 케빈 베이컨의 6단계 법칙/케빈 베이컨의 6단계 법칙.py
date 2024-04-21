N, M = map(int, input().split())

connection = [[] for _ in range(N)]
for _ in range(M):
    friend1, friend2 = map(int, input().split())
    connection[friend1 - 1].append(friend2)
    connection[friend2 - 1].append(friend1)

answer = []



for i in range(N): # i: friend - 1 (friend's index)
    visited = [False for _ in range(N)]
    kevin_bacon = 0
    
    visited[i] = True
    
    depth = 1
    current_depth_friends = connection[i][:]
    next_depth_friends = []
    while 1:
        for friend in current_depth_friends:
            if visited[friend - 1]:
                continue
            kevin_bacon += depth
            visited[friend - 1] = True
            next_depth_friends += connection[friend - 1]
        
        current_depth_friends = next_depth_friends[:]
        next_depth_friends = []
        depth += 1
        
        done = True
        for friend in visited:
            done = done and friend
        if done:
            break
        
    answer.append(kevin_bacon)

print(answer.index(min(answer)) + 1)