class Solution:
    def mySqrt(self, x: int) -> int:

        if x == 1:
            return x
        
        if x == 0:
            return x

        L, R = 1 , x
        result = 0

        while L <= R:
            mid = (L + R) // 2
            mid_squared = mid * mid
            
            if mid_squared <= x:
                result = mid
                L = mid +1
            else:
                R = mid - 1

        return result

                 

            