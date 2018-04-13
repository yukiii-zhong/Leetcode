public class Maximum_Subarray_53 {
    public int maxSubArray(int[] nums) {
        int max = nums[0];
        int sum = nums[0];
        for (int i=1; i < nums.length; i++){
            sum = nums[i] + ((sum>0) ? sum: 0);
            max = Math.max(max,sum);
        }
        return max;
    }

}
