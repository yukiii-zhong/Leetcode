import java.util.ArrayList;
import java.util.List;

public class Pascals_Triangle_118 {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        if (numRows == 0) return ans;
        List<Integer> row1 = new ArrayList<Integer>();
        row1.add(1);
        ans.add(row1);
        if (numRows == 1) return ans;
        for (int i = 1; i < numRows; i++){
            List<Integer> theRow = new ArrayList<>();
            List<Integer> prevRow = ans.get(i-1);
            theRow.add(1);
            for (int j = 1;j<i;j++) {
                theRow.add(prevRow.get(j-1) + prevRow.get(j));
            }
            theRow.add(1);
            ans.add(theRow);
        }
        return ans;
    }
}
