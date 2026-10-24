class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        freq={}
        st=[]
        n=len(nums2)
        nge=[]
        for i in range(n-1,-1,-1):
            while st and nums2[i]>=st[-1]:
                st.pop()
            if st:
                freq[nums2[i]]=st[-1]
            else:
                freq[nums2[i]]=-1
            st.append(nums2[i])
        for j in nums1:
            nge.append(freq[j])
        return nge