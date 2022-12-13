#include<iostream>

#include<vector>

using namespace std;

int island_perimeter(vector<vector<int>>& grid) {

    int rows = grid.size();
    int cols = grid[0].size();
    int no_of_islands = 0;
    int adjacent_islands = 0;
    
    for(int i=0;i<rows;i++)
    {
        for(int j=0;j<cols;j++)
        {
            if(grid[i][j]==1)
            {
                no_of_islands++;
                if(j-1>=0 && grid[i][j-1]==1)
                    adjacent_islands++;
                if(i-1>=0 && grid[i-1][j]==1)
                    adjacent_islands++;
            }
        }
    }

    return (no_of_islands*4)-(adjacent_islands*2);
        
}

int main()
{
    vector<vector<int>> grid = {{0,1,0,0},{1,1,1,0},{0,1,0,0},{1,1,0,0}};
    return 0;
}