
class Bubble:
    def __init__(self, arr) :
        self.arr=arr

    def bubble_sort(self):
        flag=True
        while flag:
            flag=False
            for i in range(1,len(self.arr)):
                if self.arr[i-1]>self.arr[i]:
                    tempo=self.arr[i-1]
                    self.arr[i-1]=self.arr[i]
                    self.arr[i]=tempo
                    flag=True
        return self.arr


#a=[2,1,0,3,6,7]
#a = [-3,-10, 100, 2, 1, 50, 0]
a = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(f'The original array is {a}')
ps=Bubble(a)
print(f'Using bubble sort algorithm: { ps.bubble_sort()}')