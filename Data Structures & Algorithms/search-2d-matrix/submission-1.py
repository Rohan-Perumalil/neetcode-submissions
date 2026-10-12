class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        

        m, n = len(matrix), len(matrix[0])
        total = n * m

        L, R = 0, total -1

        while L <= R:
            mid = (L+R) // 2
            mid_i = mid // n
            mid_j = mid % n

            value = matrix[mid_i][mid_j]

            if value == target: return True
            elif target > value: L = mid + 1
            else: R = mid - 1

        return False 