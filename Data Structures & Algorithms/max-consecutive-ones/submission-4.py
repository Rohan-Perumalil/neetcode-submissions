class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = count = 0
        for num in nums:
            if num == 0:
                result = max(result, count)
                count = 0
            else:
                count +=1
        
        return max(result, count)