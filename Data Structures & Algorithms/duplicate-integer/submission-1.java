class Solution {
    public boolean hasDuplicate(int[] nums) {
        int len = nums.length;
        int write = 1;

        Set<Integer> hasSeen = new HashSet<>();
        for(int i : nums){
            if(!hasSeen.add(i)){
                return true;
            }
        }
        return false;
    }

    
}