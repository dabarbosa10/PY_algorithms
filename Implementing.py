class SumTwo:
    def __init__(self, num_a, target):
        self.num_a=num_a
        self.target=target
        
    def brute_force(self):
        for i in range(len(self.num_a)):
            for j in range(i+1, len(self.num_a)):
                if self.num_a[i]+self.num_a[j]==self.target:
                    return [i,j]
        return []

    def sot(self):
        div={}
        for i in range(len(self.num_a)):
            diff=self.target-self.num_a[i]
            if diff in div:
                return [div[diff],i]
            else:
                div[self.num_a[i]]=i
        return []

ls=[2,4,9,6,5]
ta=14
sm=SumTwo(ls, ta)
val=sm.brute_force()
s1=sm.sot()
print(val)
print('Using Hashing: ')
print(s1)