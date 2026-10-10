#include <stdbool.h>
#include <stdlib.h>

bool uniqueOccurrences(int* arr, int arrSize) {
    const int OFFSET = 1000;
    const int FREQ_RANGE_SIZE = 2001;
    const int UNIQUE_FREQ_RANGE_SIZE = 1001;
    int *freq = calloc(FREQ_RANGE_SIZE, sizeof *freq);
    bool *uniqueFreq = calloc(UNIQUE_FREQ_RANGE_SIZE, sizeof *uniqueFreq);
    if (!freq || !uniqueFreq) {
        free(freq); free(uniqueFreq);
        return false;
    }

    for (int i = 0; i < arrSize; i++) freq[arr[i] + OFFSET] += 1;
    bool res = true;
    for (int i = 0; i < FREQ_RANGE_SIZE; i++) {
        if (freq[i] > 0) {
            if (uniqueFreq[freq[i]]) {
                res = false;
                break;
            }
            uniqueFreq[freq[i]] = true;
        }
    }

    free(freq); free(uniqueFreq);
    return res;
}