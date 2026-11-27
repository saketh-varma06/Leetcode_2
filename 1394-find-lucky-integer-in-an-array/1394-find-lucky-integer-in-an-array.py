class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        dicti={}
        for i in range(len(arr)):
            dicti[arr[i]]=dicti.get(arr[i],0)+1
        ans=-1
        for key,values in dicti.items():
            if key==values:
                ans=max(ans,key)
        return ans