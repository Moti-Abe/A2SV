class Solution {
public:
    int timeRequiredToBuy(vector<int>& tickets, int k) {
        int sum = 0;
        for(int i = 0; i < size(tickets); i++){
            if(tickets[i] >= tickets[k]){
                if(i <= k)
                sum += tickets[k];
                else
                sum += tickets[k]-1;
            }
            else
            sum += tickets[i];
        }
        return sum;
    }
};