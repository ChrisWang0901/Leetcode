class Solution:
    """
    Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
     You may assume all four edges of the grid are all surrounded by water.
     """
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
       
        
        rows = len(grid)
        cols = len(grid[0])
        # all the 1s coordinates in the array
        ones = {(r,c) for r in range(rows) for c in range(cols) if grid[r][c] == "1"}
        
        
        count = 0
        
        while ones:
            # add one of the point in ones to queue and do bfs
            queue = collections.deque([ones.pop()]) 
            
            while queue:
                x, y = queue.popleft()
                for i, j in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:
                    
                    if (i,j) in ones:
                        ones.discard((i,j))
                        queue.append((i, j))
                        
            count += 1
            
        return count