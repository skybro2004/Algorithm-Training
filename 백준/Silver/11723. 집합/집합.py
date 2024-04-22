import sys

arr = [False for _ in range(21)]

M = int(input())

for _ in range(M):
    raw_input = sys.stdin.readline()
    raw_input = raw_input.split() + [-1]
    command = raw_input[0]
    x = int(raw_input[1])
    match command:
        case "add":
            arr[x] = True
        case "remove":
            arr[x] = False
        case "check":
            if arr[x]:
                print(1)
            else:
                print(0)
        case "toggle":
            if arr[x]:
                arr[x] = False
            else:
                arr[x] = True
        case "all":
            arr = [True for _ in range(21)]
        case "empty":
            arr = [False for _ in range(21)]