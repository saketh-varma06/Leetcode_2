class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        st=[]
        cnt=1
        for i in range(len(target)):
            while cnt<target[i]:
                st.append("Push")
                st.append("Pop")
                cnt+=1
            st.append("Push")
            cnt+=1
        return st