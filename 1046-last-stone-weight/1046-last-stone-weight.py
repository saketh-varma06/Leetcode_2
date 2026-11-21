class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        while len(stones)>1:
            stones=sorted(stones)
            for i in range(len(stones)-1,0,-1):
                if(stones[i]!=stones[i-1]):
                    stones[i-1]=stones[i]-stones[i-1]
                    stones.pop(i)
                else:
                    stones.pop(i)
                    stones.pop(i-1)
                break
        return stones[0] if stones else 0