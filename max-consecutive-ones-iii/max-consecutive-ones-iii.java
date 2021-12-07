class Solution {
    // Using sliding window to reduce the time complexity
    public int longestOnes(int[] A, int K) {
        // The left integer
        int left = 0;
        // Number of zeros
        int zeros = 0;
        // The result answer
        int ans = 0;
        for (int right = 0; right < A.length; right++) {
            // If this is zero
            if (A[right] == 0) {
                // Increment the number of zeros
                zeros++;
            }
            // If the number of zeros is greater than the limit
            // Sliding window to remove the first zero of previous window
            // and add the next zero to the current window
            while (zeros > K) {
                // If the next left is zero
                if (A[left++] == 0) {
                    // decrement the number of zero
                    zeros--;
                }
            }
            // Record the max
            ans = Math.max(ans, right - left + 1);
        }
        return ans;
    }
}