import numpy as np


class Bubble:
    def __init__(self, arr) :
        self.arr=arr

    def show(self):
        for i in range(len(self.arr)):
            print(self.arr[i])

    def bubble_sort(self):
        flag=True
        while flag:
            flag=False
            for i in range(1,len(self.arr)-1):
                if self.arr[i-1]>self.arr[i]:
                    tempo=self.arr[i-1]
                    self.arr[i-1]=self.arr[i]
                    self.arr[i]=tempo
                    flag=True
        return self.arr





a=[2,1,0,3,6,7]
ps=Bubble(a)
#ps.show()
print(ps.bubble_sort())