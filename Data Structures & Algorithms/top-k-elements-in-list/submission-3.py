import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        max_heap = []
        result = []

        for num in nums:
            freq[num] += 1
        
        for key, value in freq.items():
            heapq.heappush(max_heap, (-value, key))
        

        for i in range(k):
            result.append(heapq.heappop(max_heap)[1])
        
        return result
