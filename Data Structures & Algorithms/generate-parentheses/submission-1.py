class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res= []

        def backtrack(openB, closedB):
            if openB == closedB == n:
                res.append(''.join(stack))

            if openB < n:
                stack.append("(")
                backtrack(openB +1, closedB)
                stack.pop()

            if closedB < openB:
                stack.append(")")
                backtrack(openB, closedB+1)
                stack.pop()

        backtrack(0,0)
        return res