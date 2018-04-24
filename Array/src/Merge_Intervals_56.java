import java.util.*;

public class Merge_Intervals_56 {

    private class IntervalComparator implements Comparator<Interval> {
        public int compare(Interval a, Interval b){
            return a.start<b.start ? -1: a.start==b.start ? 0:1;
        }
    }

    public List<Interval> merge(List<Interval> intervals){
        Collections.sort(intervals,new IntervalComparator());

        // Another way of sorting.
        Collections.sort(intervals, new Comparator<Interval>(){
            public int compare(Interval a,Interval b){
                return a.start - b.start;
            }
        });




        LinkedList<Interval> ans = new LinkedList<>();

        for (Interval interval: intervals){
            if (ans.isEmpty() || ans.getLast().end < interval.start){
                ans.add(interval);
            }
            else{
                ans.getLast().end = Math.max(ans.getLast().end,interval.end);
            }
        }

        return ans;
    }
}
