class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []

        for char in operations:
            if char == "+":
                stk.append(stk[-1] + stk[-2])
            elif char == "C":
                stk.pop()
            elif char == "D":
                stk.append(stk[-1] * 2)
            else:
                stk.append(int(char))
        
        return sum(stk)