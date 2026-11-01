class Solution {
public:
    int minMoves(vector<int>& nums){
        long long cnt=0;
        int el=nums[0];
        for(int i=0;i<nums.size();i++){
            el=min(el,nums[i]);
            cnt+=nums[i];
        }
        return cnt-(1LL*nums.size()*el);
    }
};