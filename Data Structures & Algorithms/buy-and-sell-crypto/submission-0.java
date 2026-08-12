class Solution {
    public int maxProfit(int[] prices) {
        int left = 0;
        int right = 1;
        int maxProf = 0;

        while(right < prices.length){
            if(prices[left] < prices[right]){
                maxProf = Math.max(maxProf, prices[right] - prices[left]);
            }
            else{
                left = right;
            }
            right++;
        }

        return maxProf;
    }
}
