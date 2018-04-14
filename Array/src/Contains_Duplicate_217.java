import java.util.HashSet;
import java.util.Set;
import java.util.Arrays;

public class Contains_Duplicate_217 {
    public boolean containsDuplicate1(int[] nums) {
        Set existed = new HashSet();
        for (int i: nums){
            if (existed.contains(i)){
                return true;
            }
            else {
                existed.add(i);
            }
        }
        return false;
    }
    public boolean containsDuplicate2(int[] nums){
        if (nums.length == 0 || nums.length == 1){
            return false;
        }
        Arrays.sort(nums);
        for (int i=0; i<nums.length-1;i++){
            if (nums[i] == nums[i+1]) return true;
        }
        return false;
    }

}
