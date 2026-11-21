class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic={}
        for char in s:
            dic[char]=dic.get(char,0)+1
        ans=-1
        for i in range(len(s)):
            if(dic[s[i]]==1):
                ans=i
                break
        return ans