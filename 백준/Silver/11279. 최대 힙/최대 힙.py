import sys


def swap(arr, i1, i2):
    arr[i1], arr[i2] = arr[i2], arr[i1]



class MaxHeap:
    def __init__(self):
        self.arr = [0]

    def add(self, number):
        self.arr.append(number)
        index1 = len(self.arr) - 1
        total_depth = int((len(self.arr) - 1)**(1/2))
        while index1!=1:
            index2 = index1//2
            if self.arr[index2]<self.arr[index1]:
                swap(self.arr, index1, index2)
                index1 = index2
            else:
                break

    def remove(self):
        if len(self.arr)==1:
            return 0
        temp = self.arr.pop(1)
        self.arr.insert(1, self.arr.pop())
        parent_index = 1
        while 1:
            # print(self.arr)

            childeren_index = []

            try:
                child_index = parent_index*2
                self.arr[child_index]
            except IndexError:
                pass
            else:
                if self.arr[parent_index]<self.arr[child_index]:
                    childeren_index.append(child_index)

            try:
                child_index = parent_index*2 + 1
                self.arr[child_index]
            except IndexError:
                pass
            else:
                if self.arr[parent_index]<self.arr[child_index]:
                    childeren_index.append(child_index)

            if len(childeren_index)==2:
                if self.arr[childeren_index[0]]<self.arr[childeren_index[1]]:
                    swap(self.arr, parent_index, childeren_index[1])
                    parent_index = childeren_index[1]
                else:
                    swap(self.arr, parent_index, childeren_index[0])
                    parent_index = childeren_index[0]
            elif len(childeren_index)==1:
                swap(self.arr, parent_index, childeren_index[0])
                parent_index = childeren_index[0]
            else:
                break
            
        return temp



M = int(input())

# ans = []
heap = MaxHeap()
for _ in range(M):
    x = int(sys.stdin.readline())
    if x==-1:
        # print(ans)
        continue
    if x:
        heap.add(x)
    else:
        print(heap.remove())
    # print(heap.arr)
# print(ans)