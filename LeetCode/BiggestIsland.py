class Solution:
    
    def countIslands(self, matrix):
        biggestIsland = 0
    # TODO: Write your code here
        rows = len(matrix)
        columns = len(matrix[0])
    #print('row:',row,'\ncolumn',column);
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j]==1:
                    area = self.find_isvalid_island(i,j,matrix)
                    if(area>biggestIsland):
                        biggestIsland = area                        
        return biggestIsland;

    def find_isvalid_island(self,i,j,matrix):
        if(i<0 or i >= len(matrix) or j <0 or j >= len(matrix[0])):
            return 0
        if matrix[i][j]==0:
            return 0
        matrix[i][j]=0
        area = 1;
        area+=self.find_isvalid_island(i,j+1,matrix)
        area+=self.find_isvalid_island(i,j-1,matrix)
        area+=self.find_isvalid_island(i+1,j,matrix)
        area+=self.find_isvalid_island(i-1,j,matrix)
        return area;


def main():
    s = Solution()
    matriks = [[1,0,0,1,0],
               [0,1,1,1,1],
               [1,0,0,0,1], 
               [0,0,0,1,1]]
    #matriks = [[1,0],[1,1]]
    print(s.countIslands(matriks))
    
main()