class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=re.sub(r'[^a-zA-Z0-9]','',s)
        s=s.lower()
        print(s)
        head=0
        tail=-1
        n=len(s)
        if s=='':
            return True
        while head<=n//2 and abs(tail)<=(n//2)+1:
            if s[head]==s[tail]:
                head+=1
                tail-=1
            else:
                return False
        return True        