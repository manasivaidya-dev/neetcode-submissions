from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dictionary = OrderedDict()
        

    def get(self, key: int) -> int:
        if key not in self.dictionary:
            return -1
        else:
            val = self.dictionary[key]
            del self.dictionary[key]
            self.dictionary[key] = val
            return self.dictionary[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.dictionary:
            del self.dictionary[key]
            self.dictionary[key] = value
        else:
            if len(self.dictionary) == self.capacity:
                self.dictionary.popitem(last = False)
            self.dictionary[key] = value
        
