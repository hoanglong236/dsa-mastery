int longestSubarray(int* nums, int numsSize) {
    int res = 0;
    int start = 0, zeros = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == 0) zeros++;
        while (zeros > 1) {
            if (nums[start] == 0) zeros--;
            start++;
        }
        if (i - start + 1 > res) res = i - start + 1;
    }
    return res - 1;
}