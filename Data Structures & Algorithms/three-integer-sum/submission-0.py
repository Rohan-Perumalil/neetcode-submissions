class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        n = len(nums)

        for i in range(n - 2):
            L, R = i + 1, n - 1
            
            while L < R:
                summ = nums[L] + nums[R] + nums[i]
                if summ == 0:
                    ans.add((nums[L], nums[R], nums[i]))
                    R -= 1
                    L += 1
                elif summ > 0:
                    R -= 1
                else:
                    L += 1
        
        return [list(triplet) for triplet in ans]
