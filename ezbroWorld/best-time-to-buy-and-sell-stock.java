class Solution {
    public int maxProfit(int[] prices) {
        int min = prices[0], maxProfit = 0; 
        for(int i =1 ; i<prices.length;i++){
            if(min > prices[i]){
                min = prices[i];
            }
            else{
                maxProfit = Math.max(maxProfit, prices[i]-min);
            }
        }
        return maxProfit;
    }
}
