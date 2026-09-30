class Node:
    def __init__(self, key: int, val:int):
        self.key, self.val = key, val
        self.prev, self.next = None, None


class LRUCache:

    def __init__(self, capacity: int):
        self.key_to_pointer = {}
        self.left, self.right = Node(0,0), Node(0,0) #left = lru, insert at right
        self.capacity = capacity
        self.left.next , self.right.prev = self.right, self.left
    
    def remove(self, curr:Node):
        previous, nextt = curr.prev, curr.next
        previous.next, nextt.prev = nextt, previous
    
    def insert(self, curr:Node):
        previous, nextt = self.right.prev, self.right
        previous.next, nextt.prev = curr, curr
        curr.prev, curr.next = previous, nextt


    def get(self, key: int) -> int:
        if key not in self.key_to_pointer:
            return -1
        self.remove(self.key_to_pointer[key])
        self.insert(self.key_to_pointer[key])
        return self.key_to_pointer[key].val
        

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_pointer:
            self.remove(self.key_to_pointer[key])
            self.insert(self.key_to_pointer[key])
            self.key_to_pointer[key].val = value
            return
        elif self.capacity == len(self.key_to_pointer):
            lru = self.left.next
            self.remove(self.key_to_pointer[lru.key])
            del self.key_to_pointer[lru.key]
            del lru
            #remove from LHS
        #insert to RHS
        add = Node(key,value)
        self.key_to_pointer[key] = add
        self.insert(add)
        
        


'''from collections import OrderedDict
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
            self.dictionary[key] = value'''
        
