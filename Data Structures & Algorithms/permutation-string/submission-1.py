from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1 = self.get_frequency(s1)
        L = 0

        for R in range(len(s2)):
            if s2[R] not in freq_s1:
                R += 1
            
            L = R
            R += len(s1)

            if freq_s1 == self.get_frequency(s2[L:R]):
                return True
        
        return False
    

    def get_frequency(self, string):
        frequency_map = defaultdict(int)
        
        for char in string:
            frequency_map[char] += 1
        
        return frequency_map


            