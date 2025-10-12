from collections import deque 

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.order = deque(maxlen=capacity)
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.order.remove(key)
            self.order.append(key)
            self.cache[key]=value
        else:
            if len(self.cache)>=self.capacity:
                lru = self.order.popleft()
                del self.cache[lru]
            self.order.append(key)
            self.cache[key]=value




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

#Leetcode Link: https://leetcode.com/problems/lru-cache/