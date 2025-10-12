class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.time = 0 
        self.cache = {}
        self.heap = []
        self.freq = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        #Operations for LFU
        self.freq[key]+=1
        self.time+=1
        heapq.heappush(self.heap, (self.freq[key], self.time, key))
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity==0:
            return 
        self.time+=1
        if key in self.cache:
            #Operations for LFU
            self.cache[key]= value
            self.freq[key]+=1
            heapq.heappush(self.heap, (self.freq[key], self.time, key))
        else:
            if len(self.cache)>=self.capacity:
                #Evict from cache 
                while self.heap:
                    freq, time, lfu = heapq.heappop(self.heap)
                    print(freq, lfu)
                    if self.freq.get(lfu, None)==freq:
                        del self.cache[lfu]
                        del self.freq[lfu]
                        break                
            self.freq[key]=1
            heapq.heappush(self.heap, (self.freq[key], self.time, key))
            self.cache[key]= value

    
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Leetcode Link: https://leetcode.com/problems/lfu-cache/