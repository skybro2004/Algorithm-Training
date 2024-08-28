class Solution {
public:
    bool isStrictlyPalindromic(int n) {
        bool answer = true;

        for(int base=2; base<=n-2; base++){
            int temp = n;
            vector<int> convertedNumber;
            while(temp!=0){
                convertedNumber.push_back(temp%base);
                temp = temp/base;
            }
            int size = convertedNumber.size();
            for(int i=0; i<size/2; i++){
                if(convertedNumber[i]==convertedNumber[size-1-i]) continue;
                answer = false;
                break;
            }
            if(!answer) break;
        }

        return answer;
    }
};