class Solution {
public:
    int scoreOfString(string s) {
        int answer = 0;
        for(int i=1; i<s.length(); i++){
            int interval = 0;
            interval = s[i - 1] - s[i];
            interval = abs(interval);
            answer += interval;
        }
        return answer;
    }
};