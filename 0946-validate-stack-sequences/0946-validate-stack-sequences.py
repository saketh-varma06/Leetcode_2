class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        st=[]
        j=0
        for i in range(len(pushed)):
            st.append(pushed[i])
            while st and j<len(popped) and st[-1]==popped[j]:
                st.pop()
                j+=1
        return len(st)==0