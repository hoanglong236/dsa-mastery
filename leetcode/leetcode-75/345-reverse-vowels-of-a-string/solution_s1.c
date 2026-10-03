#include <string.h>
#include <stdbool.h>

static bool isVowelCaseInsensitive(char c) {
    return c == 'a' || c == 'A'
        || c == 'e' || c == 'E'
        || c == 'i' || c == 'I'
        || c == 'o' || c == 'O'
        || c == 'u' || c == 'U';
}

char* reverseVowels(char* s) {
    int n = strlen(s);
    int left = 0, right = n - 1;
    while (left < right) {
        while (left < right && !isVowelCaseInsensitive(s[left]))
            left++;
        while (left < right && !isVowelCaseInsensitive(s[right]))
            right--;
        char t = s[left]; s[left] = s[right]; s[right] = t;
        left++;
        right--;
    }
    return s;
}