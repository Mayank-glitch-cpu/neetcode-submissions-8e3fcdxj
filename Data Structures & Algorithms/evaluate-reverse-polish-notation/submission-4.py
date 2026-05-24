class Solution:
    def add(self,a,b):
        return a+b
    
    def subtract(self,a,b):
        return b-a

    def divide(self,a,b):
        return int(b/a)

    def mul(self,a,b):
        return a*b 

    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        for op in tokens:
            if op == '+':
                a= stack.pop()
                b= stack.pop()
                stack.append(self.add(a,b))

            elif op == '-':
                a= stack.pop()
                b= stack.pop()
                stack.append(self.subtract(a,b))

            elif op =='*':
                a= stack.pop()
                b= stack.pop()
                stack.append(self.mul(a,b))

            elif op == '/':
                a= stack.pop()
                b= stack.pop()
                stack.append(self.divide(a,b))

            else:
                stack.append(int(op))

        return stack[-1]