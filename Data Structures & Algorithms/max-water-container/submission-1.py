class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) - 1
        max_area = 0

        while L < R:
            w = min(heights[R], heights[L])
            h = R - L
            area = w * h
            max_area = max(area, max_area)

            if heights[L] < heights[R]:
                L += 1
            elif heights[L] > heights[R]:
                R -= 1
            else:
                L+=1
        
        return max_area