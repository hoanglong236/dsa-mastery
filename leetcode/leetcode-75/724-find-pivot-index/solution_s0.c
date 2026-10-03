#include <stdlib.h>

int pivotIndex(int* nums, int numsSize) {
    int* rightPrefix = malloc((size_t) numsSize * sizeof(int));
    if (!rightPrefix) return -1;
    
    int pivotIdx = -1, running = 0;
    for (int i = numsSize - 1; i >= 0; i--) {
        rightPrefix[i] = running;
        running += nums[i];
    }
    running = 0;
    for (int i = 0; i < numsSize; i++) {
        if (running == rightPrefix[i]) {
            pivotIdx = i;
            break;
        }
        running += nums[i];
    }
    free(rightPrefix);
    return pivotIdx;
}