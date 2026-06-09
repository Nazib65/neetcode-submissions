class Solution {
    public int subarraySum(int[] nums, int k) {
        int sum=0, res=0;
        Map<Integer, Integer> prefixSums= new HashMap<>();
        prefixSums.put(0,1);

        for(int num: nums){
            sum+=num;
            
            int diff= sum-k;
            if(prefixSums.containsKey(diff)){
                res+=prefixSums.get(diff);
            }
            prefixSums.put(sum, prefixSums.getOrDefault(sum,0)+1);
        }
        return res;
    }
}