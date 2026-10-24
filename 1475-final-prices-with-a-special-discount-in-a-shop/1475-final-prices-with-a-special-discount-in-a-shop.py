class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        n=len(prices)
        nse=prices.copy()
        st=[]
        for i in range(n-1,-1,-1):
            while st and st[-1]>prices[i]:
                st.pop()
            if st:
                nse[i]=abs(st[-1]-prices[i])
            st.append(prices[i])
        return nse   