#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

static bool isVowelCaseInsensitive(char c) {
    return c == 'a' || c == 'A'
        || c == 'e' || c == 'E'
        || c == 'i' || c == 'I'
        || c == 'o' || c == 'O'
        || c == 'u' || c == 'U';
}

char* reverseVowels(char* s) {
    int n = strlen(s);
    int* vowelIndices = malloc((size_t) n * sizeof(int));
    if (!vowelIndices) {
        return NULL;
    }

    int i = 0, j = 0;
    for (i = 0; i < n; i++)
        if (isVowelCaseInsensitive(s[i])) vowelIndices[j++] = i;
    i = 0;
    j = j - 1;
    while (i < j) {
        char t = s[vowelIndices[i]];
        s[vowelIndices[i]] = s[vowelIndices[j]];
        s[vowelIndices[j]] = t;
        i++;
        j--;
    }
    free(vowelIndices);
    return s;
}