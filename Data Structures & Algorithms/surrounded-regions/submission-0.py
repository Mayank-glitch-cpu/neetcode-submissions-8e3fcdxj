class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows,cols = len(board), len(board[0])
        
        def capture(r,c):
            if (r<0 or c<0 or
                r==rows or c==cols or 
                board[r][c]!='O'):
                return

            board[r][c]='T'
            capture(r-1,c)
            capture(r+1,c)
            capture(r,c-1)
            capture(r,c+1)

        # capture all the unsurrounded regions  ['O' --> 'T']
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=='O' and (r in [0,rows-1] or c in [0,cols-1]):
                    capture(r,c)
                
        # change all the O's to X's

        for r in range(rows):
            for c in range(cols):
                if board[r][c] =='O':
                    board[r][c]= 'X'

        # again change all the T's to O's
        for r in range(rows):
            for c in range(cols):
                if board[r][c] =='T':
                    board[r][c]= 'O'
