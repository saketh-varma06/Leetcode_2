class Solution {
public:
    int minimizeSum(vector<int>& nums) {
        int ans = INT_MAX, n = nums.size();
        sort(nums.begin(), nums.end());
        ans = min(ans, nums[n-1] - nums[2]);
        ans = min(ans, nums[n-2] - nums[1]);
        ans = min(ans, nums[n-3] - nums[0]);
        return ans;
    }
};