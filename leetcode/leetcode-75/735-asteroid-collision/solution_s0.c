#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* asteroidCollision(int* asteroids, int asteroidsSize, int* returnSize) {
    int* stack = malloc((size_t) asteroidsSize * sizeof *stack);
    if (!stack) {
        *returnSize = 0;
        return NULL;
    }

    int j = -1;
    for (int i = 0; i < asteroidsSize; i++) {
        while (j >= 0 && -asteroids[i] > stack[j] && stack[j] > 0) j--;
        if (j == -1 || stack[j] < 0) stack[++j] = asteroids[i];
        else {
            if (-asteroids[i] == stack[j]) j--;
            else if (-asteroids[i] < stack[j] && asteroids[i] < 0);
            else stack[++j] = asteroids[i];
        }
    }

    *returnSize = j + 1;
    return stack;
}