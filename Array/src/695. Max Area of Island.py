class Solution:

    # Method2 is out of time limit
    def maxAreaOfIsland2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxi = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                sum = self.dfs(i,j,grid,[])
                maxi = max(sum,maxi)
        return maxi

    def dfs(self,i,j,grid,set):
        sum = 0

        if grid[i][j] == 0:
            return sum

        # When grid[i][j] == 1
        if (i,j) not in set:
            set.append((i,j))
            sum +=1

            if i-1 >=0:
                sum += self.dfs(i-1,j,grid,set)

            if j-1 >= 0:
                sum += self.dfs(i,j-1,grid,set)

            if i+1 < len(grid):
                sum += self.dfs(i+1,j,grid,set)

            if j+1 < len(grid[0]):
                sum += self.dfs(i, j+1,grid,set)

        return sum

    def maxAreaOfIsland(self, grid):

        seen = set()
        ans = 0

        def area(r,c):

            if not (0<=r<len(grid) and 0<=c < len(grid[0])):
                return 0
            if grid[r][c] == 0 or (r,c) in seen:
                return 0

            seen.add((r,c))

            return 1 + area(r-1,c)+area(r+1,c)+area(r,c-1)+area(r,c+1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in seen:
                    ans = max(ans,area(r,c))

        return ans