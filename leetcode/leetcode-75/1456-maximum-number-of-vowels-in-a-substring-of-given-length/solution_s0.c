#include <string.h>

static int isVowel(char ch) {
    return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ? 1 : 0;
}

int maxVowels(char* s, int k) {
    int count = 0;
    for (int i = 0; i < k; i++) count += isVowel(s[i]);

    int res = count, n = strlen(s);
    for (int i = k; i < n && res < k; i++) {
        count += isVowel(s[i]) - isVowel(s[i - k]);
        if (count > res) res = count;
    }
    return res;
}