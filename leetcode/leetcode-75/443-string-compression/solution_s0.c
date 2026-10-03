int compress(char* chars, int charsSize) {
    int slow = 0;
    char lastChar = chars[0];
    int lastCharCount = 0;
    for (int fast = 0; fast < charsSize + 1; fast++) {
        if (fast == charsSize || chars[fast] != lastChar) {
            chars[slow++] = lastChar;
            if (lastCharCount > 1) {
                int left = slow;
                while (lastCharCount > 0) {
                    chars[slow++] = '0' + lastCharCount % 10;
                    lastCharCount /= 10;
                }
                int right = slow - 1;
                while (left < right) {
                    char tmp = chars[left]; chars[left] = chars[right]; chars[right] = tmp;
                    left++;
                    right--;
                }
            }
            if (fast < charsSize) {
                lastChar = chars[fast];
                lastCharCount = 1;
            }
        } else {
            lastCharCount += 1;
        }
    }
    return slow;
}