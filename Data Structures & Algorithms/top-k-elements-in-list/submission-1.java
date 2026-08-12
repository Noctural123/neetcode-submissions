class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        // Map of num, occurences
        HashMap<Integer, Integer> map = new HashMap<>();

        // Created list of type Integer lists to implement bucket sorting
        List<Integer>[] freq = new List[nums.length+1];

        // Initialized ArrayList for each index in freq
        for(int i = 0; i < freq.length; i++){
            freq[i] = new ArrayList<>();
        }

        // Populate map with num, occurences from nums array.
        for(Integer num: nums){
            map.put(num, map.getOrDefault(num,0) + 1);
        }

        // Populating frequency list with each index being the occurences and the value at each index holds an array containing
        // the numbers with that amount of occurences.
        for( Map.Entry<Integer, Integer> entry: map.entrySet()){
            Integer num = entry.getKey();
            Integer occurences = entry.getValue();

            freq[occurences].add(num);
        }

        // Initialize result list of size k.
        int[] res = new int[k];
        int index = 0;

        // Loop through frequency list backwards and populate res array until index equal to k. Once index is equal to k, return res.
        for(int i = freq.length-1; i >= 0; i--){
            for(Integer num: freq[i]){
                res[index++] = num;

                if(index == k){
                    return res;
                }
            }
        }

        return res;
    }
}
