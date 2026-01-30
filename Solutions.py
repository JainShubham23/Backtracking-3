# Problem1 N Queens(https://leetcode.com/problems/n-queens/)
# Time Complexity : O(n^2)
# Space Complexity : O(n!)
# Did this code successfully run on Leetcode :yes
# Any problem you faced while coding this :no

class Solution(object):

    def solveNQueens(self, n):
        
        def helper(board, row):
            """
            Backtracking function to place queens row by row.
            """
            # Base case: all rows filled, add solution to result
            if row == n:
                solution = []
                for i in range(n):
                    sb = []
                    for j in range(n):
                        sb.append("Q" if board[i][j] else ".")  # 'Q' if queen, '.' if empty
                    solution.append("".join(sb))
                result.append(solution)
                return

            # Try placing a queen in each column of the current row
            for j in range(n):
                if isValid(board, row, j):
                    board[row][j] = True      # choose: place queen
                    helper(board, row + 1)    # explore: move to next row
                    board[row][j] = False     # unchoose: remove queen (backtrack)


        def isValid(board, i, j):
            """
            Check if placing a queen at position (i, j) is valid:
            - No other queen in the same column
            - No other queen in the upper-left diagonal
            - No other queen in the upper-right diagonal
            """
            # Check column
            r = i
            while r >= 0:
                if board[r][j]:
                    return False
                r -= 1

            # Check upper-left diagonal
            r, c = i, j
            while r >= 0 and c >= 0:
                if board[r][c]:
                    return False
                r -= 1
                c -= 1

            # Check upper-right diagonal
            r, c = i, j
            while r >= 0 and c < n:
                if board[r][c]:
                    return False
                r -= 1
                c += 1

            # No conflicts found
            return True


        # Initialize result list to store all valid board configurations
        result = []

        # Initialize empty board (False = no queen)
        board = [[False] * n for _ in range(n)]

        # Start backtracking from row 0
        helper(board, 0)

        # Return all valid solutions
        return result




# Problem2 Word Search(https://leetcode.com/problems/word-search/)
# Time Complexity : O(M N L^4)
# Space Complexity : O(L)
# Did this code successfully run on Leetcode :yes
# Any problem you faced while coding this :no

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        ## iterate on the grid going from first element to last element
        ## Visit the element and insert into visited
        ## if we get all the char of the word, at the new position we go ahead, else we backtrack


        ## getting the ROWS and COLS
        ROWS,COLS = len(board),len(board[0])
        ## maintaining a set 
        visited = set()
        def dfs(r,c,i):
            ## base case
            if i == len(word):
                return True
            ## boundary condition - return False 
            if (r<0 or r>=ROWS or c<0 or c>=COLS or word[i] != board[r][c] or ((r,c)) in visited):
                return False
            ## Choosing the option
            visited.add((r,c))
            ## check in all the direction if I can find the next char
            for dr,dc in ((1,0),(0,1),(-1,0),(0,-1)):
                row,col = r+dr, c+dc
                if dfs(row,col,i+1):
                    return True   
            ## backtracking and removing from the visited          
            visited.remove((r,c))
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        return False

       