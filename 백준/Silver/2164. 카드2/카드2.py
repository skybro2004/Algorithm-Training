from collections import deque

N = int(input())

queue = deque(range(1, N+1))

for _ in range(N-1):
    temp = queue.popleft()
    queue.append(queue.popleft())
print(queue[0])