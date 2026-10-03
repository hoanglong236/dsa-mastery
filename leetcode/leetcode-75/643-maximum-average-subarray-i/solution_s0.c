#include <limits.h>

double findMaxAverage(int* nums, int numsSize, int k) {
    int maxWindowSum = INT_MIN;
    int running = 0, start = 0;
    for (int i = 0; i < numsSize; i++) {
        running += nums[i];
        if (i >= k - 1) {
            if (running > maxWindowSum) maxWindowSum = running;
            running -= nums[start];
            start++;
        }
    }
    return (double) maxWindowSum / k;
}