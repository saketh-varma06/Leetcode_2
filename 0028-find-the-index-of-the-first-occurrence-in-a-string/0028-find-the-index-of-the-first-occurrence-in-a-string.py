class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l=0
        r=0
        ans=-1
        while(r<len(needle) and l<len(haystack)):
            if(needle[r]==haystack[l]):
                l+=1
                r+=1
            else:
                l=l-r+1
                r=0
            if(r==len(needle)):
                ans=l-r
        return ans