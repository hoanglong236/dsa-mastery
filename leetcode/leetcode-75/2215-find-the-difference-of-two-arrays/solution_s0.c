#include <stdlib.h>
#include <stdbool.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** findDifference(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize, int** returnColumnSizes) {
    
    int** res = malloc(2 * sizeof *res);
    if (!res) {
        *returnSize = 0;
        return NULL;
    }
    *returnColumnSizes = calloc(2, sizeof **returnColumnSizes);
    if (!(*returnColumnSizes)) {
        free(res);
        *returnSize = 0;
        return NULL;
    }

    const int OFFSET = 1000;
    const int RANGE_SIZE = 2001;
    bool* seen1 = calloc(RANGE_SIZE, sizeof *seen1);
    bool* seen2 = calloc(RANGE_SIZE, sizeof *seen2);
    res[0] = malloc((size_t) nums1Size * sizeof (*res)[0]);
    res[1] = malloc((size_t) nums2Size * sizeof (*res)[1]);
    if (!seen1 || !seen2 || !res[0] || !res[1]) {
        free(res[0]); free(res[1]);
        free(seen1); free(seen2);
        free(*returnColumnSizes); free(res);
        *returnSize = 0;
        return NULL;
    }
    for (int i = 0; i < nums1Size; i++) seen1[nums1[i] + OFFSET] = true;
    for (int i = 0; i < nums2Size; i++) seen2[nums2[i] + OFFSET] = true;
    for (int i = 0; i < RANGE_SIZE; i++) {
        if (seen1[i] && !seen2[i])
            res[0][(*returnColumnSizes)[0]++] = i - OFFSET;
        if (!seen1[i] && seen2[i])
            res[1][(*returnColumnSizes)[1]++] = i - OFFSET;
    }

    free(seen1); free(seen2);
    *returnSize = 2;
    return res;
}