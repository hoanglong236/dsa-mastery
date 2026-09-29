int maxArea(int* height, int heightSize) {
    int res = 0;
    int left = 0, right = heightSize - 1;
    while (left < right) {
        int area = 0;
        if (height[left] <= height[right]) {
            area = (right - left) * height[left];
            left++;
        } else {
            area = (right - left) * height[right];
            right--;
        }
        if (res < area) res = area;
    }
    return res;
}