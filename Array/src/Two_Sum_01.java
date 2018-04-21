import java.util.HashMap;
import java.util.Map;

public class Two_Sum_01 {
    public int[] twoSum(int[] nums, int target) {
        for (int i=0; i<nums.length;i++){
            if (nums[i] <=target){
                for (int j=i+1; j<nums.length; j++){
                    if (nums[i]+nums[j] == target){
                        return new int[] {i,j};
                    }
                }
            }
        }
        throw new IllegalArgumentException("No two sum solution");
    }

    public int[] twoSum2(int[] nums, int target){
        Map<Integer, Integer> seen = new HashMap<>();
        int[] ans = new int[2];
        for (int i = 0; i<nums.length;i++){
            if (seen.containsKey(target - nums[i])){
                ans[1] = i;
                ans[0] = seen.get(target-nums[i]);
                break;
            }
            else{
                seen.put(nums[i],i);
            }
        }
        return ans;
    }
}
