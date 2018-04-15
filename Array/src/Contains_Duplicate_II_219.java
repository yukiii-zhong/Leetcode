import java.util.HashSet;
import java.util.Set;

public class Contains_Duplicate_II_219 {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Set<Integer> set = new HashSet<Integer>();
        for (int i=0; i<nums.length;i++){
            if (set.contains(nums[i])) return true;
            set.add(nums[i]);
            if (set.size()>k) set.remove(nums[i-k]);
        }
        return false;
    }
}
