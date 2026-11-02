class Solution {
public:
    int minMoves2(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int n=nums.size(),median=0;
        if(n%2!=0){
            median=nums[n/2];
        }
        else{
            median=(nums[n/2-1]+nums[n/2])/2;
        }
        long long sum=0;
        for(int i=0;i<nums.size();i++){
            sum+=abs(nums[i]-median);
        }
        return sum;
    }
};