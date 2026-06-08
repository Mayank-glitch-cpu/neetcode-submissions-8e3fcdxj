class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out= []
        stack= []
        def backtrack(openB, closeB):
            if openB == closeB == n:
                out.append(''.join(stack))

            if openB < n:
                stack.append('(')
                backtrack(openB+1, closeB)
                stack.pop()

            if closeB < openB:
                stack.append(')')
                backtrack(openB, closeB + 1)
                stack.pop()

        backtrack(0,0)
        return out

        