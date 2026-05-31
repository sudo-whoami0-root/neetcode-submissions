class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> hasSeen = new HashSet<>();
        for(int i : nums){
            if(!hasSeen.add(i)){
                return true;
            }
        }
        return false;
    }

    
}