from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_t = defaultdict(int)
        freq_s = defaultdict(int)

        for char1 in s:
            freq_s[char1] += 1

        for char2 in t:
            freq_t[char2] += 1
        

        return freq_t == freq_s