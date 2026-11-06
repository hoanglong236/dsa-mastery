#include <stdbool.h>

bool canPlaceFlowers(int* flowerbed, int flowerbedSize, int n) {
    int i = 0;
    while (i < flowerbedSize && n > 0) {
        if (flowerbed[i] == 1) {
            i += 2;
        } else if (i == flowerbedSize - 1 || flowerbed[i + 1] != 1) {
            n--;
            i += 2;
        } else {
            i++;
        }
    }
    return n == 0;
}