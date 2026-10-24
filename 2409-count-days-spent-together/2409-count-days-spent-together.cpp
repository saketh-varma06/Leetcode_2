class Solution {
public:
    int countDaysTogether(string arriveAlice, string leaveAlice, string arriveBob, string leaveBob) {
        int alicearrmon=stoi(arriveAlice.substr(0,2));
        int alicearrdate=stoi(arriveAlice.substr(3,2));
        int aliceleamon=stoi(leaveAlice.substr(0,2));
        int aliceleadate=stoi(leaveAlice.substr(3,2));
        int bobarrmon=stoi(arriveBob.substr(0,2));
        int bobarrdate=stoi(arriveBob.substr(3,2));
        int bobleamon=stoi(leaveBob.substr(0,2));
        int bobleadate=stoi(leaveBob.substr(3,2));
        vector<int>days={31,28,31,30,31,30,31,31,30,31,30,31};
        int alice_start=accumulate(days.begin(),days.begin()+alicearrmon-1,0)+alicearrdate;
        int alice_end=accumulate(days.begin(),days.begin()+aliceleamon-1,0)+aliceleadate;
        int bob_start=accumulate(days.begin(),days.begin()+bobarrmon-1,0)+bobarrdate;
        int bob_end=accumulate(days.begin(),days.begin()+bobleamon-1,0)+bobleadate;
        int start=max(alice_start,bob_start);
        int end=min(alice_end,bob_end);
        return max(0,end-start+1);
    }
};