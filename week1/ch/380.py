import random
class RandomizedSet:

    def __init__(self):
        self.store_dict = dict()

    def insert(self, val: int) -> bool:
        if val in self.store_dict:
            return False
        else:
            self.store_dict[val] = 1
            return True

    def remove(self, val: int) -> bool:
        if val in self.store_dict:
            del self.store_dict[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(list(self.store_dict.keys()))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
