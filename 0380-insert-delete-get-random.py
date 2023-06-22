from random import randint

class RandomizedSet:

    def __init__(self):
        self.arr_indeces = {}
        self.arr = []
        self.n_items = 0
        

    def insert(self, val: int) -> bool:
        if val in self.arr_indeces:
            return False
        
        self.arr_indeces[val] = self.n_items
        if len(self.arr) == self.n_items:
            self.arr.append(val)
        else:
            self.arr[self.n_items] = val
        self.n_items += 1 
        return True


    def remove(self, val: int) -> bool:
        if val not in self.arr_indeces:
            return False
        
        i = self.arr_indeces[val]
        new_val = self.arr[self.n_items - 1]
        self.arr_indeces[new_val] = i
        self.arr[i] = new_val
        del self.arr_indeces[val]
        self.n_items -= 1
        return True
        

    def getRandom(self) -> int:
        return self.arr[randint(0, self.n_items - 1)]

