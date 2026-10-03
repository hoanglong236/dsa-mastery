#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int x = *(const int *) a;
    int y = *(const int *) b;
    return (x > y) - (x < y);
}

int maxOperations(int* nums, int numsSize, int k){
    qsort(nums, (size_t) numsSize, sizeof(int), cmp_int);
    int res = 0;
    int left = 0, right = numsSize - 1;
    int running = 0;
    while (left < right) {
        running = nums[left] + nums[right];
        if (running == k) {
            res++;
            left++;
            right--;            
        }
        else if (running < k) left++;
        else right--;
    }
    return res;
}