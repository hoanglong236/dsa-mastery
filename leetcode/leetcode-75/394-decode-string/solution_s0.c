#include <stdlib.h>
#include <string.h>

typedef struct {
    int times;
    char* seq;
    int seqIdx;
} Element;

#define STACK_RANGE 11
#define MAX_STR_LEN 100001

static void freeStack(Element* stack, int n) {
    for (int i = 0; i < n; i++) free(stack[i].seq);
}

char* decodeString(char* s) {
    Element stack[STACK_RANGE];

    int stackIdx = 0;
    stack[stackIdx].times = 1;
    stack[stackIdx].seq = malloc(MAX_STR_LEN * sizeof *stack[stackIdx].seq);
    if (!stack[stackIdx].seq) {
        freeStack(stack, 1);
        return NULL;
    }
    stack[stackIdx].seqIdx = 0;
    int times = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] >= '0' && s[i] <= '9') {
            times = times * 10 + (s[i] - '0');
        } else if (s[i] == '[') {
            stackIdx++;
            stack[stackIdx].times = times;
            stack[stackIdx].seq = malloc(MAX_STR_LEN * sizeof *stack[stackIdx].seq);
            if (!stack[stackIdx].seq) {
                freeStack(stack, stackIdx);
                return NULL;
            }
            stack[stackIdx].seqIdx = 0;
            times = 0;
        } else if (s[i] == ']') {
            Element last = stack[stackIdx];
            int n = last.seqIdx; 
            for (int j = 0; j < last.times - 1; j++) {
                memcpy(last.seq + last.seqIdx, last.seq, n);
                last.seqIdx += n;
            }
            stackIdx--;
            memcpy(stack[stackIdx].seq + stack[stackIdx].seqIdx, last.seq, last.seqIdx);
            stack[stackIdx].seqIdx += last.seqIdx;
            free(last.seq);
        } else {
            stack[stackIdx].seq[stack[stackIdx].seqIdx++] = s[i];
        }
    }
    stack[0].seq[stack[0].seqIdx] = '\0';
    return stack[0].seq;
}