import java.util.Arrays;

public class Missing_Number_268 {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int expectedsum = (0+n)*(n+1)/2;
        int actSum = 0;

        for (int i=0; i<n; i++){
            actSum +=nums[i];
        }
        return expectedsum-actSum;
    }
}
