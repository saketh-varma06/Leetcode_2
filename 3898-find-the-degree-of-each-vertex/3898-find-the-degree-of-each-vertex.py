class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        n=len(matrix)
        ans=[]
        for i in range(n):
            degree=0
            for j in range(n):
                if(matrix[i][j]==1):
                    degree+=1
            ans.append(degree)
        return ans