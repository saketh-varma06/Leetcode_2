class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        time=0
        while(True):
            for i in range(len(tickets)):
                if(tickets[i]>0):
                    tickets[i]-=1
                    time+=1
                    if(tickets[k]==0):
                        return time