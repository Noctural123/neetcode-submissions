class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // Declaring
        HashMap<Integer, Integer> map = new HashMap<>();
        ArrayList<Integer>[] freq = new ArrayList[nums.length + 1];

        // Initializing array indices
        for(int i = 0; i < freq.length; i++){
            freq[i] = new ArrayList<>();
        }

        // Populating Map
        for(Integer num: nums){
            map.put(num, map.getOrDefault(num,0) + 1);
        }

        // Populating Frequency
        for(Map.Entry<Integer, Integer> entry: map.entrySet()){
            Integer num = entry.getKey();
            Integer occurences = entry.getValue();

            freq[occurences].add(num);
        }

        // Initializing result array and index.
        int[] result = new int[k];
        int index = 0;

        // Traverse backwards through frequency
        for(int i = freq.length-1; i > 0; i--){
            for(Integer num: freq[i]){
                result[index++] = num;

                if(index == k){
                    return result;
                }
            }
        }

        return result;

        
        
    }
}
