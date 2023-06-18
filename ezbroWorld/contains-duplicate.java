class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>();
        boolean isDuple = false;
        
        for (int i =0 ; i<nums.length ; i++){
            if(set.contains(nums[i])){
                isDuple = true;
                break;
            }
            else{
                set.add(nums[i]);
            }
        }
        return isDuple;
    }
}
