#include <string.h>
#include <stdlib.h>

char* reverseWords(char* s) {
    int n = (int) strlen(s);
    char* res = malloc(n + 1);
    if (!res) return NULL;

    int k = 0, len = 0;
    for (int i = n - 1; i > -1; i--) {
        if (s[i] == ' ') {
            if (len > 0) {
                if (k > 0) res[k++] = ' ';
                memcpy(res + k, s + i + 1, len);
                k += len;
                len = 0;
            }
        } else len++;
    }
    if (len > 0) {
        if (k > 0) res[k++] = ' ';
        memcpy(res + k, s, len);
        k += len;
    }
    res[k] = '\0';
    return res;
}