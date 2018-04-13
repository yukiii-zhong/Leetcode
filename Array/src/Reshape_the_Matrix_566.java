import java.util.LinkedList;
import java.util.Queue;

public class Reshape_the_Matrix_566 {

    public int[][] matrixReshape(int[][] nums, int r, int c){

        // track the index of new matrix
        int a=0;
        int b=-1;

        int[][] answer = new int[r][c];

        // 不符合条件的，直接 Run out, it doesn't need to go through the iteration
        if (nums.length == 0 || r * c != nums.length * nums[0].length) return nums;

        for (int i=0; i<nums.length;i++){
            for(int j=0;j< nums[i].length;j++){
                b++;
                if (b==c){
                    b=0;
                    a +=1;
                }
                if (a> r-1 || b>c-1) return nums;
                answer[a][b] = nums[i][j];
            }
        }
        return answer;
    }

    public int[][] matrixReshape2(int[][] nums, int r, int c) {
        int[][] ans = new int[r][c];
        if (nums.length == 0 || r * c != nums.length * nums[0].length)
            return nums;
        int count = 0;

        Queue< Integer > queue = new LinkedList< >();
        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < nums[0].length; j++) {
                queue.add(nums[i][j]);
            }
        }
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                ans[i][j] = queue.remove();
            }
        }

        return ans;
    }

    public int[][] matrixReshape3(int[][] nums, int r, int c) {
        int[][] ans = new int[r][c];
        if (nums.length == 0 || r * c != nums.length * nums[0].length)
            return nums;
        int count = 0;

        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < nums[0].length; j++) {
                ans[count / c][count % c] = nums[i][j];
                count++;
            }
        }
        return ans;
    }

}
