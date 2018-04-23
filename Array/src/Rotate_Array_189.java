public class Rotate_Array_189 {
    public void rotate(int[] nums, int k) {
        int n = nums.length, count = 0;
        for (int start=0;count<n;start++){
            int temp = nums[start];
            int i = start;
            do{
                int a = (i+k)%n;
                int temp2 = nums[a];
                nums[a] = temp;
                temp = temp2;
                i = a;
                count++;
            }  while (i != start);
        }

    }

    public void rotate2(int[] nums, int k){
        
    }
}
