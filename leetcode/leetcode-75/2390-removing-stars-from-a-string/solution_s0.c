#include <string.h>
#include <stdlib.h>

char* removeStars(char* s) {
    int n = strlen(s);
    char* res = malloc((size_t) (n + 1) * sizeof *res);
    if (!res) return NULL;

    int j = 0;
    for (int i = 0; i < n; i++) {
        if (s[i] != '*') res[j++] = s[i];
        else j--;
    }
    res[j] = '\0';
    return res;
}