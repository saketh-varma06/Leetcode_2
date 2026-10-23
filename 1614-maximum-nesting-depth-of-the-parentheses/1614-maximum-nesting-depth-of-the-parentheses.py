class Solution:
    def maxDepth(self, s: str) -> int:
        cnt=0
        max_dep=0
        for i in range(len(s)):
            if(s[i]=='('):
                cnt+=1
                max_dep=max(max_dep,cnt)
            elif(s[i]==')'):
                cnt-=1
        return max_dep