class Solution {
public:
    int romanToInt(string s) {
        int answer = 0;

        map<char, int> roman;
        roman['I'] = 1;
        roman['V'] = 5;
        roman['X'] = 10;
        roman['L'] = 50;
        roman['C'] = 100;
        roman['D'] = 500;
        roman['M'] = 1000;

        for(int i=0; i<s.size(); i++){
            int val = roman[s[i]];
            if(i+1<s.size() && val<roman[s[i+1]]){
                val = roman[s[i+1]] - val;
                i++;
            }
            answer += val;
        }

        return answer;
    }
};