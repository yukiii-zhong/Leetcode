import java.util.Arrays;

public class Missing_Number_268 {
    public int missingNumber(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        if (nums[n-1] != n) return n;
        for (int i=0; i<nums.length;i++){
            if (nums[i] == i+1) return i;
        }
        throw new IllegalArgumentException("No missing Number");
    }
}
