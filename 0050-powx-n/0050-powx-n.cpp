class Solution {
public:
    double myPow(double x, int n) {
        long long N=n;
        if(N<0){
            N=-N;
        }   
        if(n==0){
            return 1;
        }
        double half=myPow(x,N/2);
        double ans;
        if(N%2==0)            ans= half*half;
        else                  ans= half*half*x;
        if(n<0)               return 1/ans;
        else                  return ans;
    }   
};