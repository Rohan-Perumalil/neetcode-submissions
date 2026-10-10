class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        double = 2* len(nums)
        new_arr = [0] * double
        new_arr = nums + nums
        return new_arr

