class Solution {
public:
    vector<vector<int>> largestLocal(vector<vector<int>>& grid) {
        vector<vector<int>> answer;
        // pivot 정하기
        for(int row=0; row<grid.size()-2; row++){
            vector<int> answer_row;
            for(int col=0; col<grid.size()-2; col++){
                // pivot으로부터 3x3 범위 탐색
                int max = 0;
                for(int i=row; i<row+3; i++){
                    for(int j=col; j<col+3; j++){
                        max = grid[i][j]<max ? max : grid[i][j];
                    }
                }
                answer_row.push_back(max);
            }
            answer.push_back(answer_row);
        }
        return answer;
    }
};