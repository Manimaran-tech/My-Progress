import random

class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.array = []

    def insert(self, val: int) -> bool:
        if val in self.array:
            return False
        self.array.append(val)
        self.map[val] = len(self.array) - 1

    def remove(self, val: int) -> bool:
        if val not in self.array:
            return False
        index = self.map[val]
        last = self.array[-1]
        self.array[index]= last
        self.map[last] = index
        self.array.pop()
        del self.map[val]
         
        return True

    def getRandom(self) -> int:
        return random.choice(self.array)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()