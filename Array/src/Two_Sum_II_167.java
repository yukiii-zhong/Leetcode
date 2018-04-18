import java.util.Map;
import java.util.HashMap;


public class Two_Sum_II_167 {
    public int[] twoSum(int[] num, int target){
        int i = 0;
        int j = num.length-1;
        int[] ans = new int[2];
        while (true){
            if (target-num[j]<num[i]){
                j--;
            }
            else if (target-num[j] == num[i]){
                ans[0] = i+1;
                ans[1] = j+1;
                break;
            }
            else{
                i++;
            }
        }
        return ans;
    }
}
