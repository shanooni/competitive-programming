from random import random


class RandomizedSet:

    def __init__(self):
        self.randomList = []

    def insert(self, val: int) -> bool:
        if val not in self.randomset:
            self.randomset.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.randomset:
            self.randomset.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.randomset)