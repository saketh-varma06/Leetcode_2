class Solution {
public:
    long long minSumSquareDiff(vector<int>& nums1, vector<int>& nums2, int k1, int k2) {
        int i = 0;
        long long sum = 0;
        long long k = (long long)k1 + k2;
        vector<int> diff(nums1.size());

        while (i < nums1.size()) {
            diff[i] = abs(nums1[i] - nums2[i]);
            sum += diff[i];
            i++;
        }

        if (sum <= k) {
            return 0;
        }

        int low = 0;
        int high = *max_element(diff.begin(), diff.end());

        while (low < high) {
            int mid = low + (high - low) / 2;
            long long need = 0;
            i = 0;

            while (i < diff.size()) {
                if (diff[i] > mid) {
                    need += diff[i] - mid;
                }
                i++;
            }

            if (need <= k) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }

        long long used = 0;
        i = 0;

        while (i < diff.size()) {
            if (diff[i] > low) {
                used += diff[i] - low;
                diff[i] = low;
            }
            i++;
        }

        k -= used;
        i = 0;

        while (i < diff.size() && k > 0) {
            if (diff[i] == low && diff[i] > 0) {
                diff[i]--;
                k--;
            }
            i++;
        }

        i = 0;
        sum = 0;

        while (i < diff.size()) {
            sum += 1LL * diff[i] * diff[i];
            i++;
        }

        return sum;
    }
};