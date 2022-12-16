def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:return []
        m, n = len(matrix),len(matrix[0])
        p_visited = set()
        a_visited = set()
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        def dfs(visited, x,y):
            visited.add((x,y))
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and matrix[nx][ny] >= matrix[x][y]:
                    dfs(visited, nx,ny)
        for i in range(m):
            dfs(p_visited,i,0)
            dfs(a_visited,i,n-1)
        for j in range(n):
            dfs(p_visited,0,j)
            dfs(a_visited,m-1,j)
        return list(p_visited.intersection(a_visited))