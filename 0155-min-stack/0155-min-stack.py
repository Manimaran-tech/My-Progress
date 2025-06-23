class MinStack(object):

    def __init__(self):
        self.l=[]
        self.min_=[]

    def push(self, val):
        self.l.append(val)
        if not self.min_ or val<=self.min_[-1]:
            self.min_.append(val)
        

    def pop(self):
        val=self.l.pop()
        if val==self.min_[-1]:
            self.min_.pop()
        

    def top(self):
        return self.l[-1]
        

    def getMin(self):
        return self.min_[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()