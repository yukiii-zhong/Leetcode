public class Rotate_Image_48 {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        int t = matrix.length-1;
        for (int i=0;i < (n-1)/2+1;i++){
            for (int j=i;j<n-i-1;j++){
                int temp = matrix[i][j];
                int a =i;
                int b = j;
                for (int k=0; k<4;k++){
                    int temp2 = matrix[b][t-a];
                    matrix[b][t-a] = temp;
                    temp = temp2;

                    int z = a;
                    a = b;
                    b = t-z;
                }
            }

        }
    }
}
