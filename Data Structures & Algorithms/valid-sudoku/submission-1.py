class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        seen = set()

        for row in range(9):
            for col in range(9):
                ele = board[row][col]
                if ele == ".":
                    continue
    
                row_key = (ele, "at_row", row)
                col_key = (ele, "at_col", col)
                blk_key = (ele, "at_blk", row//3,col//3)

                if row_key in seen or col_key in seen or blk_key in seen:
                    return False
                
                seen.add(row_key)
                seen.add(col_key)
                seen.add(blk_key)

        return True
