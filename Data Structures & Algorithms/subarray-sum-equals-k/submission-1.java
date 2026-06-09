class Solution {
    public int subarraySum(int[] nums, int k) {
    int sum = 0, result = 0;
    Map<Integer, Integer> preSum = new HashMap<>();
    preSum.put(0, 1);  // Initialize with sum 0 occurring once
    
    for (int num : nums) {
        sum += num;  // Update running sum
        
        // If we've seen (sum-k) before, we found subarray(s) with sum k
        if (preSum.containsKey(sum - k)) {
            result += preSum.get(sum - k);
        }
        
        // Update the frequency of current prefix sum
        if(preSum.containsKey(sum)){
            int currSum=preSum.get(sum);
            preSum.put(sum, currSum+1);
        }
        else{
            preSum.put(sum,1);
        }
    }
    return result;
    }
}
