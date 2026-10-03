int pivotIndex(int* nums, int numsSize) {
    int pivotIdx = -1, total = 0, running = 0;
    for (int i = 0; i < numsSize; i++) total += nums[i];
    for (int i = 0; i < numsSize; i++) {
        if (running == total - nums[i] - running) return i;
        running += nums[i];
    }
    return -1;
}