class Solution:
    def makeGood(self, s: str) -> str:
        st=[]
        for i in range(len(s)):
            while st and abs(ord(st[-1])-ord(s[i]))==32:
                st.pop()
                break
            else:
                st.append(s[i])
        return "".join(st)