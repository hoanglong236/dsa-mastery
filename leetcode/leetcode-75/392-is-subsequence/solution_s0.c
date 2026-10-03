#include <stdbool.h>
#include <string.h>

bool isSubsequence(char* s, char* t) {
    int n1 = strlen(s), n2 = strlen(t);
    if (n1 > n2) return false;

    int i = 0;
    for (int j = 0; j < n2; j++) {
        if (s[i] == t[j]) i++;
        if (i == n1) break;
    }
    return i == n1;
}