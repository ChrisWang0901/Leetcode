class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        use dynamic programming bottom up
        time : O(m * n)
        space : O(1)
        """
        # fill the first row and first column
        for i in range(len(grid) - 1):
            grid[i + 1][0] += grid[i][0]

        for j in range(len(grid[0]) - 1):
            grid[0][j + 1] += grid[0][j]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]
