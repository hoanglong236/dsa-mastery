#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

static int int_cmp(const void *a, const void *b) {
    int x = *(const int *) a;
    int y = *(const int *) b;
    return (x > y) - (x < y);
}

bool closeStrings(char* word1, char* word2) {
    int* freq1 = calloc(26, sizeof *freq1);
    int* freq2 = calloc(26, sizeof *freq2);
    if (!freq1 || !freq2) {
        free(freq1); free(freq2);
        return false;
    }
    for (int i = 0; word1[i] != '\0'; i++) freq1[word1[i] - 'a']++;
    for (int i = 0; word2[i] != '\0'; i++) freq2[word2[i] - 'a']++;
    for (int i = 0; i < 26; i++) {
        if ((freq1[i] == 0) != (freq2[i] == 0)) {
            free(freq1); free(freq2);
            return false;
        }
    }
    qsort(freq1, 26, sizeof *freq1, int_cmp);
    qsort(freq2, 26, sizeof *freq2, int_cmp);
    bool res = memcmp(freq1, freq2, 26 * sizeof *freq1) == 0;
    free(freq1); free(freq2);
    return res;
}