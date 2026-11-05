#include <stdlib.h>
#include <string.h>

#define STACK_LEVELS 10 // level <= 30 / 3 = 10
#define MAX_STR_LEN 100001

char* decodeString(char* s) {
    int stackTimes[STACK_LEVELS];
    int stackSeqStartIndices[STACK_LEVELS];

    char* seq = malloc(MAX_STR_LEN * sizeof *seq);
    if (!seq) return NULL;

    int times = 0, stackIdx = 0, seqIdx = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] >= '0' && s[i] <= '9') {
            times = times * 10 + (s[i] - '0');
        } else if (s[i] == '[') {
            stackIdx++;
            stackTimes[stackIdx] = times;
            stackSeqStartIndices[stackIdx] = seqIdx;
            times = 0;
        } else if (s[i] == ']') {
            int copySize = seqIdx - stackSeqStartIndices[stackIdx];
            char* src = seq + stackSeqStartIndices[stackIdx];
            for (int k = 0; k < stackTimes[stackIdx] - 1; k++) {
                memcpy(seq + seqIdx, src, copySize);
                seqIdx += copySize;
            }
            stackIdx--;
        } else
            seq[seqIdx++] = s[i];
    }
    seq[seqIdx] = '\0';
    return seq;
}