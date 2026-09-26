#include <stdbool.h>

bool canPlaceFlowers(int* flowerbed, int flowerbedSize, int n) {
    int plantPlots = 0, emptyPlots = 0;
    for (int i = 0; i < flowerbedSize; i++) {
        if (flowerbed[i] == 1) {
            emptyPlots--;
            if (emptyPlots > 0) plantPlots += (emptyPlots + 1) / 2;
            emptyPlots = -1;
        } else {
            emptyPlots++;
        }
    }
    if (emptyPlots > 0) plantPlots += (emptyPlots + 1) / 2;
    return plantPlots >= n;
}