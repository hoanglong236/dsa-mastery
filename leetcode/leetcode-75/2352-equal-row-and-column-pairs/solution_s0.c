#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#define FNV_OFFSET 14695981039346656037ULL      // offset basis (unsigned long long)
#define FNV_PRIME 1099511628211ULL              // FNV prime

#define CAP 401                                 // prime > 2 * max gridSize (200)

typedef struct {
    int* key;
    int value;
    unsigned long long hashValue;
    bool used;
} Slot;

static Slot table[CAP];

static unsigned long long hashRow(int* row, int rowSize) {
    unsigned long long h = FNV_OFFSET;
    for (int i = 0; i < rowSize; i++) {
        unsigned int v = (unsigned int) row[i];
        for (int b = 0; b < 4; b++) {       // int has 4 bytes (almost)
            h ^= (v >> (b * 8)) & 0xFF;     // extract last 1 byte (1 byte = 8 bits)
            h *= FNV_PRIME;
        }
    }
    return h;
}

static void put(int* row, int rowSize, int value) {
    unsigned long long h = hashRow(row, rowSize);
    int idx = (int) (h % CAP);
    size_t nmem = (size_t) rowSize * sizeof *row;
    while (table[idx].used) {
        if (table[idx].hashValue == h && memcmp(table[idx].key, row, nmem) == 0) {
            table[idx].value = value;
            return;
        }
        idx = (idx + 1) % CAP;
    }
    table[idx].key = row;
    table[idx].value = value;
    table[idx].hashValue = h;
    table[idx].used = true;
}

static bool get(int* row, int rowSize, int* out) {
    unsigned long long h = hashRow(row, rowSize);
    int idx = (int) (h % CAP);
    size_t nmem = (size_t) rowSize * sizeof *row;
    while (table[idx].used) {
        if (table[idx].hashValue == h && memcmp(table[idx].key, row, nmem) == 0) {
            *out = table[idx].value;
            return true;
        }
        idx = (idx + 1) % CAP;
    }
    *out = 0;
    return false;
}

static void increment(int* row, int rowSize) {
    int oldValue = 0;
    get(row, rowSize, &oldValue);
    put(row, rowSize, ++oldValue);
}

int equalPairs(int** grid, int gridSize, int* gridColSize) {
    memset(table, 0, sizeof table);
    int res = 0;

    for (int i = 0; i < gridSize; i++) {
        increment(grid[i], gridSize);
    }
    int *vertical = malloc((*gridColSize) * sizeof *vertical);
    if (!vertical) return 0;

    for (int i = 0; i < gridSize; i++) {
        int out = 0;
        for (int j = 0; j < (*gridColSize); j++) {
            vertical[j] = grid[j][i];
        }
        get(vertical, gridSize, &out);
        res += out;
    }

    free(vertical);
    return res;
}