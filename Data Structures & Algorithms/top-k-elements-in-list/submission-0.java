class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        List<Integer>[] freq = new List[nums.length+1];

        for(int i = 0; i < freq.length; i++){
            freq[i] = new ArrayList<>();
        }

        for(Integer num : nums){
            map.put(num, map.getOrDefault(num, 0)+1);
        }

        for(Map.Entry<Integer, Integer> entry : map.entrySet()){
            Integer num = entry.getKey();
            Integer count = entry.getValue();
            freq[count].add(num);
        }

        int[] result = new int[k];
        int index=0;
        for(int i = freq.length-1; i> 0 && index<k; i--){
            for(Integer num: freq[i]){
                result[index++] = num;

                if(index==k){
                    return result;
                }
            }
        }

        return result;
    }
}
