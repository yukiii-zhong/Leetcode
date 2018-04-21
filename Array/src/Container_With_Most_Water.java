public class Container_With_Most_Water {
    public int maxArea(int[] height) {
        int max = 0;
        int i = 0;
        int j = height.length-1;
        while (j>i){
            int container = (j-i)* Math.min(height[i],height[j]);
            max = Math.max(container,max);
            if (height[i]<height[j]){
                i++;
            }
            else {
                j--;
            }
        }
        return max;
    }
}
