from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1 = self.get_frequency(s1)
        L = 0

        for R in range(len(s2)):
            if s2[R] not in s1:
                R += 1
                        
            L = R
            R += len(s1)
            w = str(s2[L:R])
            freq_window = self.get_frequency(w)

            if freq_window == freq_s1:
                return True
        
        return False


    

    def get_frequency(self, string):
        freq_map = defaultdict(int)
        for c in string:
            freq_map[c] += 1
        
        return freq_map




            