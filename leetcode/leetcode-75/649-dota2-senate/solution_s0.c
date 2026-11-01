#include <stdlib.h>

char* predictPartyVictory(char* senate) {
    int rteams[10001], dteams[10001];
    int rhead = 0, rtail = 0;
    int dhead = 0, dtail = 0;
    int rcount = 0, dcount = 0;
    int n = 10000;
    for (int i = 0; senate[i] != '\0'; i++) {
        if (senate[i] == 'R') rteams[rtail++] = i + 1;
        else dteams[dtail++] = i + 1;
    }
    rcount = rtail--;
    dcount = dtail--;
    int rsize = rcount, dsize = dcount;
    while (rcount > 0 && dcount > 0) {
        while (rhead < rsize && rteams[rhead] == 0 && rcount > 0)
            rhead = (rhead + 1) % rsize;
        while (dhead < dsize && dteams[dhead] == 0 && dcount > 0)
            dhead = (dhead + 1) % dsize;
        if (rteams[rhead] < dteams[dhead]) {
            rteams[rhead] += n;
            dteams[dhead] = 0;
            dcount--;
        } else {
            rteams[rhead] = 0;
            dteams[dhead] += n;
            rcount--;
        }
        rhead = (rhead + 1) % rsize;
        dhead = (dhead + 1) % dsize;
    }
    char* radiant = "Radiant";
    char* dire = "Dire";
    return rcount > 0 ? radiant : dire;
}