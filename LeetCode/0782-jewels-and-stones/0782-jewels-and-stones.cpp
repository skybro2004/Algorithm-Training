class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        int answer = 0;
        for(int stoneIndex=0; stoneIndex<stones.size(); stoneIndex++){
            for(int jewelIndex=0; jewelIndex<jewels.size(); jewelIndex++){
                if(stones[stoneIndex]==jewels[jewelIndex]){
                    answer += 1;
                    break;
                }
            }
        }
        return answer;
    }
};