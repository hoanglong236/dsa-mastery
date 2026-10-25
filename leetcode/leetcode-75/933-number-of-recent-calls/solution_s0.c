#include <stdlib.h>

#define MAX_CALL 10001

typedef struct {
    int* calls;
    int callsSize;
    int queueStartIdx;
} RecentCounter;


RecentCounter* recentCounterCreate() {
    RecentCounter* obj = malloc(sizeof(RecentCounter));
    obj->callsSize = 0;
    obj->queueStartIdx = 0;
    obj->calls = calloc(MAX_CALL, sizeof *obj->calls);
    return obj;
}

int recentCounterPing(RecentCounter* obj, int t) {
    obj->calls[obj->callsSize++] = t;
    int start = t - 3000;
    int i = 0;
    while (obj->calls[obj->queueStartIdx] < start) obj->queueStartIdx++;
    return obj->callsSize - obj->queueStartIdx;
}

void recentCounterFree(RecentCounter* obj) {
    free(obj->calls);
    obj->callsSize = 0;
    obj->queueStartIdx = 0;
}

/**
 * Your RecentCounter struct will be instantiated and called as such:
 * RecentCounter* obj = recentCounterCreate();
 * int param_1 = recentCounterPing(obj, t);
 
 * recentCounterFree(obj);
*/