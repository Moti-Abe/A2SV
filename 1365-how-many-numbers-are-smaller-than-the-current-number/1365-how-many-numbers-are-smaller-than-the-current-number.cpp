class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int>res;
        for(int i = 0; i < size(nums); i++){
            int count = 0;
            for(int  j = 0; j < size(nums); j++){
                if(i != j &&  nums[j] <nums[i])
                count++;
            }
            res.push_back(count);
        }
        return res;
    }
};