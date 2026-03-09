class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int minDif = INT_MAX;
        int output;
        sort(nums.begin(), nums.end());
        for(int i = 0; i < size(nums); i++){

            int l = i+1, r = size(nums)-1;
            while(l < r){
                int sum = nums[i]+nums[l]+nums[r];
                int dif = abs(sum-target);
                if(dif < minDif){
                    minDif = dif;
                    output = sum;
                }
                if(sum < target) l++;
                else if (sum > target) r--;
                else{
                    return sum;
                }
            }
        }
        return output;
    }
};