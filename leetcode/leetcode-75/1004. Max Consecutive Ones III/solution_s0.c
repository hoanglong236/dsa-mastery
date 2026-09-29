int longestOnes(int* nums, int numsSize, int k) {
    int res = 0;
    int start = 0, flipped = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == 0) {
            if (flipped == k) {
                while (nums[start] == 1) start++;
                start++;
            } else flipped++;
        }
        if (i - start + 1 > res) res = i - start + 1; 
    }
    return res;
}