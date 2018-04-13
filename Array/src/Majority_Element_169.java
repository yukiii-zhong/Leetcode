import java.util.HashMap;
import java.util.Map;

public class Majority_Element_169 {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> counts = countNums(nums);
        Map.Entry<Integer,Integer> majorityEntry = null;
        for (Map.Entry <Integer,Integer> entry: counts.entrySet()){
            if (majorityEntry == null || entry.getValue() > majorityEntry.getValue()){
                majorityEntry = entry;
            }
        }

        return majorityEntry.getKey();

    }

    private Map<Integer,Integer> countNums(int[] nums){
        Map<Integer,Integer> counts= new HashMap<Integer, Integer>();
        for(int num: nums){
            if (!counts.containsKey(num)){
                counts.put(num,1);
            }
            else{
                counts.put(num, counts.get(num) +1);
            }
        }
        return counts;
    }
}