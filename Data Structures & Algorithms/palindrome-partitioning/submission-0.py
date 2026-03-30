class Solution:
    def palindrome(self,s):
        head=0
        tail=len(s)
        while head<tail:
            if s[head]==s[tail-1]:
                head+=1
                tail-=1
            else:
                return False
        return True

    def partition(self, s: str) -> List[List[str]]:
        res=[]
        curr=[]
        def dfs(s,i):
            if i >=len(s):
                res.append(curr[:])
                return 

            for k in range(i,len(s)):
                temp= s[i:k+1]
                if self.palindrome(temp):
                    curr.append(temp)
                    dfs(s,k+1)
                    curr.pop()
        dfs(s,0)
        return res
            