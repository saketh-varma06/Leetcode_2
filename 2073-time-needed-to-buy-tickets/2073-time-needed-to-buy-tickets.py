class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        count=0
        q=[]
        for i in range(len(tickets)):
            q.append(i)
        while q:
            cur=q.pop(0)
            tickets[cur]-=1
            count+=1
            if tickets[cur]>0:
                q.append(cur)
            if tickets[cur]==0 and cur==k:
                return count