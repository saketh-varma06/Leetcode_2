class Solution {
public:
    int minimumSumSubarray(vector<int>& nums, int l, int r) {
        int left=0,right=0,sum=0,ans=INT_MAX;
        while(right<nums.size()){
            sum+=nums[right];
            if((right-left+1)>r){
                sum-=nums[left];
                left++;
            }
            for(int i=left ;i<=right;i++){
                int len=(right-i+1);
                if(len>=l && len<=r){
                    int curr=sum;
                    for(int j=left;j<i;j++){
                        curr-=nums[j];
                    }
                    if(curr>0)
                        ans=min(ans,curr);
                }
            }
            right++;
        }
        return ans==INT_MAX ? -1 : ans;
    }
};