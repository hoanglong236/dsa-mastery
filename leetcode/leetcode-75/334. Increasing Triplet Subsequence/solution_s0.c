#include <stdbool.h>

bool increasingTriplet(int* nums, int numsSize) {
    int i = 0, j = 0;
    int pivot = 0;
    for (int k = 1; k < numsSize; k++) {
        if (nums[i] >= nums[k]) {
            if (i < pivot && nums[pivot] < nums[k]) {
                i = pivot;
                j = k;
            } else pivot = k;
        } else {
            if (nums[i] >= nums[j] || nums[j] >= nums[k]) j = k;
            else return true;
        }
    }
    return false;
}