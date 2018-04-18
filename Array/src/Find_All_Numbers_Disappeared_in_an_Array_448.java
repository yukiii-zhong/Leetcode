import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class Find_All_Numbers_Disappeared_in_an_Array {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> ans = new ArrayList<>();
        int n =nums.length;
        if (n==0) return ans;
        Arrays.sort(nums);
        numGap(-1,nums[0],ans);

        for (int i=0; i< n-1; i++){
            numGap(nums[i],nums[i+1],ans);
        }
        numGap(nums[n-1],n,ans);
        return ans;
    }

    private void numGap(int small, int large, List<Integer> ans){
        if (large > small+1){
            for (int i = small +1; i<large;i++){
                ans.add(i);
            }
        }
    }
}
