class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(i, j, n, m):
            x, y = i, j
            for delta in deltas:
                nx = x + delta[0]
                ny = y + delta[1]
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1" and visited[nx][ny]:
                    visited[nx][ny] = False
                    dfs(nx, ny, n, m)
            return
        n = len(grid[0])
        m = len(grid)
        visited = [[True for _ in range(n)] for _ in range(m)]
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and visited[i][j]:
                    visited[i][j] = False
                    dfs(i, j, n, m)
                    cnt += 1
        return cnt     
                
