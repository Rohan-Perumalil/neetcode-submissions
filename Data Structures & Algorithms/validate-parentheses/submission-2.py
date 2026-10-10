class Solution:
    def isValid(self, s: str) -> bool:
        mapp = {")": "(", "]": "[", "}": "{"}
        stk = []

        for c in s:
            if c in mapp:
                if stk and stk[-1] == mapp[c]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(c)

        return True if not stk else False
