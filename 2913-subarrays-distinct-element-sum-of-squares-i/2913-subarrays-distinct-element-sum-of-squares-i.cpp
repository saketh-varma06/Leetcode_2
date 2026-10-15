class Solution {
public:
    int sumCounts(vector<int>& nums) {
        int cnt=0,l=0,r=0,n=nums.size(),ans=0;
        unordered_map<int,int>mpp;
        while(l<n){
            r=l;
            cnt=0;
            mpp.clear(); 
            while(r<n){
                mpp[nums[r]]++;
                if(mpp[nums[r]]==1){
                    cnt++;
                }
                ans+=cnt*cnt;
                r++;
            }
            l++;       
        }
        return ans;
    }
};