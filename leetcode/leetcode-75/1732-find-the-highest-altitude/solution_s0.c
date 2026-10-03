int largestAltitude(int* gain, int gainSize) {
    int res = 0, prefix = 0;
    for (int i = 0; i < gainSize; i++) {
        prefix += gain[i];
        if (prefix > res) res = prefix;
    }
    return res;
}