class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int answer = 0;
        for(auto customer: accounts){
            int totalMoney = 0;
            for(auto money: customer){
                totalMoney += money;
            }
            answer = answer<totalMoney ? totalMoney : answer;
        }
        return answer;
    }
};