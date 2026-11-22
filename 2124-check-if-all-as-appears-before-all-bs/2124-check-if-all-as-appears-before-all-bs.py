class Solution:
    def checkString(self, s: str) -> bool:
        ans=s
        ans="".join(sorted(ans))
        return s==ans