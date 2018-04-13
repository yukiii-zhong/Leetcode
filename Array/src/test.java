public class test {
    public static void main(String[] args){
        int[][] Matrix0 = {{1,2},{3,4}};
        int[][] Matrix1 = {{1,2,3,4},{5,6}};

        // Test
        Reshape_the_Matrix_566 R1 = new Reshape_the_Matrix_566();
        printMatrix(R1.matrixReshape(Matrix0,1,4));


    }
    public static void printMatrix(int[][] matrix){
        for (int i=0; i< matrix.length;i++){
            for(int j=0; j< matrix[i].length; j++){
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }

}
