class Solution {
public:
    // const vector<pair<int, int>> directions = {
    //     {-1, 0}, // UP
    //     {0, 1},  // RIGHT
    //     {1, 0},  // DOWN
    //     {0, -1}  // LEFT
    // };
    int countSubIslands(vector<vector<int>>& grid1, vector<vector<int>>& grid2) {
        int answer = 0;
        int m = grid1.size();
        int n = grid1[0].size();

        vector<pair<int, int>> subIsland;

        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(grid2[i][j]==0) continue;

                subIsland = getIslandCoords(grid1, grid2, i, j, m, n);

                bool flag = true;
                for(auto coord: subIsland){
                    flag = flag && grid1[coord.first][coord.second];
                    if(!flag) break;
                }
                if(flag) answer++;
            }
        }

        return answer;
    }

    vector<pair<int, int>> getIslandCoords(vector<vector<int>>& grid1, vector<vector<int>>& grid2, int y, int x, int m, int n){
        vector<pair<int, int>> coords;

        queue<pair<int, int>> q;
        q.push({y, x});

        while(!q.empty()){
            pair<int, int> coord = q.front();
            q.pop();

            if(grid2[coord.first][coord.second]==0) continue;

            coords.push_back(coord);
            grid2[coord.first][coord.second] = 0;

            if(0<coord.first){
                q.push({coord.first - 1, coord.second});
            }
            if(coord.first<m-1){
                q.push({coord.first + 1, coord.second});
            }
            if(0<coord.second){
                q.push({coord.first, coord.second - 1});
            }
            if(coord.second<n-1){
                q.push({coord.first, coord.second + 1});
            }
        }
        return coords;
    }
};