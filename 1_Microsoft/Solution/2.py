# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

# Only numbers 1 through 9 are used.
# Each number is used at most once.
# Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

 class Solution {
 	vector<vector<int>> ans;
 	void dfs(vector<int>& temp, int target, int index, int sum, int k){
         if(sum==target && k==0){
             ans.push_back(temp);
             return;
         }
         if(sum>target){
             return;
         }
         for(int i=index; i<=9; i++){
             if(i>target){
                 break;
             }
             temp.push_back(i);
             dfs(temp,target,i+1,sum+i,k-1);
             temp.pop_back();
         }

 	}
 public:
 	vector<vector<int>> combinationSum3(int k, int n) {
 		vector<int> temp;
 		dfs(temp, n, 1, 0, k);
 		return ans;
 	}
 };
