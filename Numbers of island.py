from typing import List
import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        q, visited = collections.deque(), set()
        island = 0

        def DFS(r, c):
            if (r not in range(rows) or c not in range(cols) or grid[r][c] == "0" or (r, c) in visited ):
                return
            
            visited.add((r,c))
            direction = [(1,0),(-1,0),(0,1),(0,-1)]
            for dr, dc in direction:
                r, c = r + dr, c + dc
                DFS(r, c)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    DFS(r, c)
                    island += 1
        return island
        
        """
        # BFS
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        q, visited = collections.deque(), set()
        island = 0

        def BFS(r, c):
            q.append((r,c))
            while q:
                r, c = q.popleft()
                direction = [(1,0),(-1,0),(0,1),(0,-1)]
                for dr, dc in direction:
                    r, c = r + dr, c + dc
                    if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visited):
                        visited.add((r, c))
                        q.append((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    BFS(r, c)
                    island += 1
        return island 

        """

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
a = Solution()
print(a.numIslands(grid))