public class Toeplitz_Matrix_766 {
    public boolean isToeplitzMatrix(int[][] matrix) {
        int a = matrix.length;
        int b = matrix[0].length;

        if (a==1 || b==1) return true;

        for (int i = 0; i< a-1;i++){
            for(int j=0; j<b-1; j++){
                if(matrix[i][j] != matrix[i+1][j+1]) return false;
            }
        }

        return true;

    }
}
