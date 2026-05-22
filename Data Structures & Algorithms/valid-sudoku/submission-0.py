class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in range(9):
            seen = set()
            for col in range(9):
                ele = board[row][col]
                if ele == ".":
                    continue
                if ele in seen:
                    return False
                seen.add(ele)
        
        for col in range(9):
            seen = set()
            for row in range(9):
                ele = board[row][col]
                if ele == ".":
                    continue
                if ele in seen:
                    return False
                seen.add(ele)
        
        for row_block in range(0,9,3):
            for col_block in range(0,9,3):
                seen = set()
                for row in range(row_block,row_block+3):
                    for col in range(col_block, col_block+3):
                        ele = board[row][col]
                        if ele == ".":
                            continue
                        if ele in seen:
                            return False
                        seen.add(ele)
        return True
        