class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col= set()
        posd= set() # (r+c)
        negd= set() # (r-c)

        board = [['.']*n for _ in range(n)] 
        print(board)
        res=[]
        def backtrack(r):
            if r==n:
                copy=[''.join(row) for row in board]
                res.append(copy)
                print(res)
                return

            for c in range(n):
                if c in col or (r+c) in posd or (r-c) in negd:
                    continue
                else:
                    board[r][c]='Q'
                    col.add(c)
                    posd.add(r+c)
                    negd.add(r-c)
                    backtrack(r+1)
                    col.remove(c)
                    posd.remove(r+c)
                    negd.remove(r-c)
                    board[r][c]='.'
        backtrack(0)
        return res
