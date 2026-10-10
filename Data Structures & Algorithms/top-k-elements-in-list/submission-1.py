from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        max_heap = []

        for num in nums:
            freq[num] += 1
        
        for key, value in freq.items():
            heapq.heappush(max_heap, (-value, key))

        result = []
        for i in range(k):
            result.append(heapq.heappop(max_heap)[1])

        return result
        
        

"""
 Create a frequency map for amount of times number shows
 add them to Max Heap
 pop k elements
 """