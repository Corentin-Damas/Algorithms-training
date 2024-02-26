import random
class RandomizedSet:
    def __init__(self):
        self.map = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val not in self.map:
            self.map[val] = len(self.arr)
            self.arr.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        # The last elmenet swap place of the removed element to get a continuous indexing
        idx = self.map[val]
        last = self.arr[-1]
        self.arr[idx] = last
        self.map[last] = idx
        self.arr.pop()
        del self.map[val]
        return True    


    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

instruct = ["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]
info = [[],[1],[2],[2],[],[1],[2],[]]
