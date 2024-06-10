from collections import deque


N, M = map(int, input().split())

maze = []

for _ in range(N):
    buffer = [0 if c=='1' else -1 for c in input()]
    maze.append(buffer)


# queue = [(0, 0, 1)]
queue = deque([(0, 0, 1)])


while queue!=[]:
    pos = queue.popleft()
    x = pos[0]
    y = pos[1]
    d = pos[2]
    
    # maze[y][x] = d
    
    if y==N-1 and x==M-1:
        break
    
    # down
    if y + 1<N and maze[y + 1][x]==0:
        maze[y + 1][x] = d + 1
        queue.append((x, y + 1, d + 1))
    
    # right
    if x + 1<M and maze[y][x + 1]==0:
        maze[y][x + 1] = d + 1
        queue.append((x + 1, y, d + 1))
    
    # up
    if 0<y and maze[y - 1][x]==0:
        maze[y - 1][x] = d + 1
        queue.append((x, y - 1, d + 1))

    # left
    if 0<x and maze[y][x - 1]==0:
        maze[y][x - 1] = d + 1
        queue.append((x - 1, y, d + 1))


print(maze[N - 1][M - 1])

# for line in maze:
#     print(line)