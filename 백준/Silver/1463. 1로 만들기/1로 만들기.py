N = int(input())


dp = [-1 for _ in range(N)]
dp[0] = 0

for i in range(N):
    if dp[i]!=-1:
        continue
    
    temp = [dp[i - 1]]
    if (i+1)%3==0:
        temp.append(dp[(i+1)//3 - 1])
    if (i+1)%2==0:
        temp.append(dp[(i+1)//2 - 1])
    dp[i] = min(temp) + 1

print(dp[-1])