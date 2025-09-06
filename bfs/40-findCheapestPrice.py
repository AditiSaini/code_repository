class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for start,end,price in flights:
            graph[start].append((end,price))
        visited= defaultdict(int) #stores node,level
        min_queue = [(0,src,-1)] #stores distance,node,level
        while min_queue:
            dist,node,level = heapq.heappop(min_queue)
            if node==dst and level<=k:
                return dist
            if level>k:
                continue
            if node in visited and visited[node]<=level:
                continue
            visited[node]=level
            for nei,cost in graph[node]:
                heapq.heappush(min_queue, (dist+cost, nei, level+1))
        return -1