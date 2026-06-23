class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visit= set()
        rows= len(board)
        cols= len((board)[0])
        def dfs(r,c,i):
            if (r<0 or c<0 or
                r>= rows or c>= cols or
                (r,c) in visit or board[r][c]!= word[i]):
                return False

            if i== len(word)-1:
                return True
                
            visit.add((r,c))

            res= (dfs(r-1,c,i+1) or
                    dfs(r+1,c, i+1) or
                    dfs(r, c-1, i+1) or
                    dfs(r, c+1, i+1))

            visit.remove((r,c))
            return res

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r,c,0):
                        return True
        return False