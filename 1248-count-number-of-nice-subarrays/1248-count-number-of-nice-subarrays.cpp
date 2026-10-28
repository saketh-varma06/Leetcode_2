class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int l=0,r=0,n=nums.size(),cnt=0,ans=0;
        while(r<n){
            if(nums[r]%2!=0){
                cnt++;
            }
            while(cnt>k){
                if(nums[l]%2!=0){
                    cnt--;
                }
                l++;
            }
            if(cnt==k){
                int temp=l;
                while(temp<=r && nums[temp]%2==0){
                    ans++;
                    temp++;
                }
                ans++;
            }
            r++;
        }
        return ans;
    }
};