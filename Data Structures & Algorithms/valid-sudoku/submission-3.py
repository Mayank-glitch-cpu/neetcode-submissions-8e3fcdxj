class Solution:
    def transpose_matrix(self,matrix):
        return [list(row) for row in zip(*matrix)]
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # first check for rows 
        h_row= {}
        h_col={}
        for r in range(len(board)):
            for num in board[r]:
                if num!='.':
                    if num in h_row:
                        return False
                    h_row[num]=r # here key is num and value is row for this hash rows
            # print('hash row',r,' ',h_row)
            h_row={}

        transposed_board= self.transpose_matrix(board)
        # print(transposed_board)
        for c in range(len(transposed_board)):
        # print('hash col',h_col)_board)):
            for num in transposed_board[c]:
                if num!='.':
                    if num in h_col:
                        return False
                    h_col[num]=c # here key is num and value is col for this hash rows
            # print('hash col',c,' ',h_col)
            h_col={}
        ################# Lets solve for squares now#####################
        square_index=[i for i in range(len(board))]
        start_row=[]
        start_col=[]
        h_square={}
        for s_index in square_index:
            start_row=(s_index//3)*3
            start_col=(s_index%3)*3
            for i in range(start_row,start_row+3):
                for j in range(start_col,start_col+3):
                    if board[i][j] !='.':
                        if board[i][j] in h_square:
                            return False # print('violate in square',' ',s_index)
                        h_square[board[i][j]]= s_index
            # print('Sqaure',s_index,' ',h_square)
            h_square={}
        return True
