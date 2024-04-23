"""import sys
input = sys.stdin.readline



def is_in_list(arr, n):
    # print("="*10)
    # print(arr, n)
    while 1:
        # print(arr)
        pivot= arr[(len(arr) - 1)//2]
        # print(front, pivot, back)
        
        if pivot<n:
            arr = arr[(len(arr) + 1)//2:]
            if arr==[]:
                return False
        elif n<pivot:
            arr = arr[:(len(arr) - 1)//2]
            if arr==[]:
                return False
        else:
            return True

N = int(input())
A = list(sorted(map(int, input().split())))
M = int(input())
arr = list(map(int, input().split()))

for n in arr:
    if is_in_list(A, n):
        print(1)
    else:
        print(0)"""
        
import sys
input = sys.stdin.readline



N = int(input())
A = set(sorted(map(int, input().split())))
M = int(input())
arr = list(map(int, input().split()))

for n in arr:
    if n in A:
        print(1)
    else:
        print(0)