public class Best_Time_to_Buy_and_Sell_Stock_121 {
    public static int maxProgit(int[] prices){
        if (prices.length == 0 || prices.length == 1){
            return 0;
        }

        int maxDiff = 0;
        int min = prices[0];
        for (int p:prices){
            if (p<min){
                min = p;
            }
            else{
                maxDiff = Math.max(maxDiff,(p-min));
            }
        }
        return maxDiff;

    }


}
