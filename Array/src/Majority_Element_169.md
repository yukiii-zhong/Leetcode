## Solution1: Use Map (Actualy a slow method)

The only purpose to use this method is to practice the use of map.

### Map, hashmap

原理： 映射Map <key, value> pair

EX: Map: theMap, key: num, value: an integer

1. `void` Put value : `theMap.put(num,1)`
2. `boolean` Judge whether key exists: `theMap.containsKey(num)`
3. get value according to the key: `theMap.get(num)`

#### Map. Entry

1. `for (Map.Entry<Integer,Integer> entry: map.entrySet())`
2. `entry.getValue()`
3. `entry.getKey`

```java
import java.util.map;

public int majorityElement(int[] nums){
    Map<Integer,Integer> counts = new HashMap<Integer, Integer>;
    for(int num: nums){
        if (!counts.containsKey(num)){
            counts.put(num,1)
        }
        else{
            counts.put(num, counts.get(num)+1);
        }
    }
    Map.Entry<Integer, Integer> majorityEntry = null;
    for (Map.Entry<Integer, Integer> entry: counts.entrySet()){
        if(majorityEntry == null || entry.getValue() > majorityEntry.getValue()){
            majorityEntry = entry;
        }
    }
    return majorityEntry.getKey();
}
```

 



## Solution2: Sort

### Algorithm

1. Exists **more than** $n/2$ times
2. The majority always exist

So:

When the array is sorted, the middle one must be the majority number

$[1,2,3,4,5]$

$[1,2,3,4]$

### Sort an array

```java
import java.util.Arrays;
...
int[] nums = {1,5,3,2,4};
Arrays.sort(nums);
//Now, Array is sorted:{1,2,3,4,5}
```



