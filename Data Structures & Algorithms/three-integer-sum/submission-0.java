class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        HashSet<List<Integer>> set = new HashSet<>();
        int curr = 0;
        int p1 = 1;
        int p2 = 2;

        while(curr != nums.length-2){
            if(nums[curr] + nums[p1] + nums[p2] == 0){
                List<Integer> list = new ArrayList<>();
                list.add(nums[curr]);
                list.add(nums[p1]);
                list.add(nums[p2]);
                Collections.sort(list);
                set.add(list);
            }
            p2++;
            if(p2 == nums.length){
                p1++;
                p2 = p1+1;
            }
            if(p1 == nums.length-1){
                curr++;
                p1 = curr+1;
                p2 = p1+1;
            }
        }

        List<List<Integer>> result = new ArrayList<>(set);
        return result;
    }
}
