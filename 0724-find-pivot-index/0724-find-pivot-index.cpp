class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int total=0;
        for(int num:nums){
            total+=num;
        }
        int prefix_sum=0;
        for(int i=0;i<nums.size();i++){
            int suffix_sum=total-prefix_sum-nums[i];
            if(prefix_sum==suffix_sum){
                return i;
            }
            prefix_sum+=nums[i];
        }
        return -1;
    }
};