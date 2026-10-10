class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s)- 1

        while L < R:
            while L < R and not self.isAlphaNum(s[L]):
                L+=1
            
            while R > L and not self.isAlphaNum(s[R]):
                R -= 1

            if s[L].lower() != s[R].lower():
                return False
            
            L, R = L + 1, R - 1

        return True

    def isAlphaNum(self, character: str) -> bool:
        char = ord(character)
        return (
            (char >= ord("a") and char <= ord("z"))
            or (char >= ord("A") and char <= ord("Z"))
            or (char >= ord("0") and char <= ord("9"))
        )
