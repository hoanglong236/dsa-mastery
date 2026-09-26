#include <string.h>
#include <stdlib.h>

static int gcdOfInts(int a, int b) {
    while (a != b) {
        if (a > b) a = a - b;
        else b = b - a;
    }
    return a;
}

char* gcdOfStrings(char* str1, char* str2) {
    int n1 = strlen(str1), n2 = strlen(str2);
    int i = 0, j = 0;
    while (i < n1 && j < n2) {
        if (str1[i++] != str2[j++]) return "";
    }

    int gcd = gcdOfInts(n1, n2);
    for (i = 0; i < n1; i++)
        if (str1[i] != str1[i % gcd]) return "";
    for (j = 0; j < n2; j++)
        if (str2[j] != str2[j % gcd]) return "";

    char* res = malloc(gcd + 1);
    memcpy(res, str1, gcd);
    res[gcd] = '\0';
    return res;
}