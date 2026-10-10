from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_t = defaultdict(int)
        freq_s = defaultdict(int)

        for i in range(len(s)):
            freq_t[t[i]] += 1
            freq_s[s[i]] += 1
        
        

        return freq_t == freq_s