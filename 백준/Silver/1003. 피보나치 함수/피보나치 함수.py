rng = int(input())

arr = [[1, 0], [0, 1]]

for _ in range(rng):
  n = int(input())
  for i in range(len(arr), n+1):
    arr.append([arr[i-1][0] + arr[i-2][0], arr[i-1][1] + arr[i-2][1]])

  print(f"{arr[n][0]} {arr[n][1]}")