class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1

        while L < R:
            while not self.alphaNumeric(s[L]) and L < R:
                L+= 1
            
            while not self.alphaNumeric(s[R]) and R > L:
                R -= 1
            
            if s[L].lower() != s[R].lower():
                return False
            else:
                L+=1
                R-=1
        
        return True

    

    def alphaNumeric(self, char):
        return ((ord('A') <= ord(char) <= ord('Z')) or
                (ord('a') <= ord(char) <= ord('z')) or
                (ord('0') <= ord(char) <= ord('9')))