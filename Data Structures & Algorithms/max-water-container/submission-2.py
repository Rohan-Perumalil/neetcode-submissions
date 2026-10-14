class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) -1
        max_area = 0

        while L < R:
            h = min(heights[L], heights[R])
            w = R - L
            area = w * h
            max_area = max(area, max_area)

            if heights[L] > heights[R]:
                R -= 1
            elif heights[L] < heights[R]:
                L += 1
            else:
                L += 1
        
        return max_area