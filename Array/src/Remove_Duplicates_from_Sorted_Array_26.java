// Notes: It's a sorted array.

public class Remove_Duplicates_from_Sorted_Array_26 {
    public int removeDuplicates(int[] nums){
        if (nums.length ==0 || nums.length ==1) return nums.length;
        int j = 1;
        for (int i=1; i<nums.length;i++){
            if(nums[i] != nums[i-1]) {
                nums[j] =nums[i];
                j++;
            }
        }
        return j;
    }
}
