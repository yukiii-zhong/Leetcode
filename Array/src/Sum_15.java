import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class Sum_15 {
    public List<List<Integer>> threeSum(int[] nums){

        List<List<Integer>> ans = new ArrayList<>();
        Arrays.sort(nums);

        for (int i=0; i<nums.length-2;i++){
            if (i>0 && nums[i] == nums[i-1]) continue;
            int low = i+1, high = nums.length-1, target = -nums[i];
            while (high > low){
                int add = nums[high]+nums[low];
                if (add>target) high--;
                else if (add<target) low++;
                else if (add == target){
                    ans.add(Arrays.asList(i,low,high));
                    low ++;
                    high--;
                    while (low<high && nums[low] == nums[low-1]) low++;
                    while (low<high && nums[high] == nums[high+1]) high--;

                }
            }
        }

        return ans;

    }
}
