public class Move_Zeroes_283 {
    public void moveZeroes(int[] nums) {
        int moveStep = 0;
        int countNotZero = 0;
        for (int i=0; i<nums.length;i++){
            if(nums[i] !=0){
                nums[i-moveStep] = nums[i];
                countNotZero++;
            }
            else{
                moveStep ++;
            }
        }
        for(int i = countNotZero; i<nums.length;i++){
            nums[i] = 0;
        }

    }
}