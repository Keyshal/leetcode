class Solution:

    def dfs(self,gride,r,c,m,n):
        if 0<=r<m and 0<=c<n:
            pass
        else:
            return
        if gride[r][c]!="1":
            return
        gride[r][c]="2"
        self.dfs(gride,r-1,c,m,n)
        self.dfs(gride,r+1,c,m,n)
        self.dfs(gride,r,c-1,m,n)
        self.dfs(gride,r,c+1,m,n)



    def numIslands(self, grid: List[List[str]]) -> int:
        # grid = [
        # ["1", "1", "1", "1", "0"],
        # ["1", "1", "0", "1", "0"],
        # ["1", "1", "0", "0", "0"],
        # ["0", "0", "0", "0", "0"]
        # ]
        m=len(grid)
        n=len(grid[0])
        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    self.dfs(grid, i, j, m, n)
                    count=count+1
        return count
