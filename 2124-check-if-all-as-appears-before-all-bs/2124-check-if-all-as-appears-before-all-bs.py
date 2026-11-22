class Solution:
    def checkString(self, s: str) -> bool:
        ans=s
        ans="".join(tuple(sorted(ans)))
        return s==ans