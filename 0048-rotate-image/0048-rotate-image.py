class Solution:
    def rotate(self, mat: list[list[int]]) -> None:
        
        n = len(mat)
        for i in range(n):
            for j in range(i):
                mat[i][j],mat[j][i] = mat[j][i],mat[i][j]
            
        for i in range(n):
            mat[i].reverse()
        