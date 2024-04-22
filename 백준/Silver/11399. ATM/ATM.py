N = int(input())
P = list(map(int, input().split()))

P.sort()

l = len(P)
answer = 0
for i, time in enumerate(P):
    answer += time*(l - i)

print(answer)