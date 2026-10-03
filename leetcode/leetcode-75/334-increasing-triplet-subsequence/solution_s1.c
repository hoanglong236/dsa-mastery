#include <limits.h>
#include <stdbool.h>

bool increasingTriplet(int* nums, int numsSize) {
    int first = INT_MAX, second = INT_MAX;
    for (int k = 0; k < numsSize; k++) {
        if (nums[k] <= first) first = nums[k];
        else if (nums[k] <= second) second = nums[k];
        else return true;
    }
    return false;
}