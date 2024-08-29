class Solution {
public:
    int removeStones(vector<vector<int>>& stones) {
        int answer = stones.size();

        map<int, vector<int>> hash_row;
        map<int, vector<int>> hash_col;
        
        for(auto stone: stones){
            hash_row[stone[0]].push_back(stone[1]);
            hash_col[stone[1]].push_back(stone[0]);
        }

        for(auto stone: stones){
            if(hash_row[stone[0]].size()==0) continue;
            dfs(hash_row, hash_col, {stone[0], stone[1]});
            answer--;
        }
    
        return answer;
    }

    void dfs(map<int, vector<int>>& hash_row, map<int, vector<int>>& hash_col, pair<int, int> coord){
        vector<int> temp_col = hash_row[coord.first];
        hash_row[coord.first].clear();
        for(auto col: temp_col){
            if(col==coord.second) continue;
            dfs(hash_row, hash_col, {coord.first, col});
        }

        vector<int> temp_row = hash_col[coord.second];        
        hash_col[coord.second].clear();
        for(auto row: temp_row){
            if(row==coord.first) continue;
            dfs(hash_row, hash_col, {row, coord.second});
        }

        return;
    }
};