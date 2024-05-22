def dfs(k, dungeons):
    temp = []
    for i in range(len(dungeons)):
        if k<dungeons[i][0]:
            continue
        else:
            dungeons_temp = dungeons[:]
            a, b = dungeons_temp.pop(i)
            temp.append(dfs(k - b, dungeons_temp))
    if temp==[]:
        return 0
    return max(temp) + 1

def solution(k, dungeons):
    answer = dfs(k, dungeons)
    # answer = -1
    return answer