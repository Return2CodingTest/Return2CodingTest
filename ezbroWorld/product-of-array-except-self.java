class Solution {
    public int[] productExceptSelf(int[] nums) {
        int length = nums.length;
        int[] leftToRight = new int[length];
        int[] rightToLeft = new int[length];
        int[] outputs = new int[length];

        Arrays.fill(leftToRight,1);
        Arrays.fill(rightToLeft,1);
        
        for(int i = 1; i<length;i++){
            leftToRight[i] = leftToRight[i-1] * nums[i-1];
        }
        
        for(int j = length-2 ; j>-1;j--){
            rightToLeft[j] = rightToLeft[j+1] * nums[j+1];
        }
        
        for(int i =0; i<length;i++){
            outputs[i] = leftToRight[i] * rightToLeft[i];
        }
                
        return outputs;
    }
}
