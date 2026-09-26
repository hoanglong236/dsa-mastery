#include <stdbool.h>
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* kidsWithCandies(int* candies, int candiesSize, int extraCandies, int* returnSize) {
    bool* res = malloc((size_t) candiesSize * sizeof(bool));
    if (!res) {
        *returnSize = 0;
        return NULL;
    }

    int max = 0;
    for (int i = 0; i < candiesSize; i++)
        if (candies[i] > max) max = candies[i];
    for (int i = 0; i < candiesSize; i++)
        res[i] = (candies[i] + extraCandies) >= max;

    *returnSize = candiesSize;
    return res;
}