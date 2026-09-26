#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
    int* res = malloc(numsSize * sizeof(int));
    if (!res) return NULL;

    int running = 1;
    for (int i = 0; i < numsSize; i++) {
        res[i] = running;
        running *= nums[i];
    }
    running = 1;
    for (int i = numsSize - 1; i > -1; i--) {
        res[i] *= running;
        running *= nums[i];
    }

    *returnSize = numsSize;
    return res;
}