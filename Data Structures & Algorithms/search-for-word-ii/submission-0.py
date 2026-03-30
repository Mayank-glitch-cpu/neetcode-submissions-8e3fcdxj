class Trienode():
    def __init__(self):
        self.child={}
        self.isend= False

    def add(self, words):
        for word in words:
            curr = self
            for c in word:
                if c not in curr.child:
                    curr.child[c] = Trienode()
                curr = curr.child[c]
            curr.isend = True
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root= Trienode()
        root.add(words)
        res, visit = set(), set()
        row , col = len(board), len(board[0])

        def dfs(r,c,node,word):
            curr= node
            if (r < 0 or c< 0 or
                r>=row or c>=col or
                (r,c) in visit or board[r][c] not in node.child):
                return 

            visit.add((r,c))
            node=node.child[board[r][c]]
            word+=board[r][c]
            if node.isend:
                res.add(word)

            dfs(r-1,c,node,word)
            dfs(r+1,c,node,word)
            dfs(r,c-1,node,word)
            dfs(r,c+1,node,word)
            visit.remove((r,c))
        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r,c,root,"")
        return list(res)
    


            
       
