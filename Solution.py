from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # Normalize k in case it's larger than the length of nums
        k = k % len(nums) if nums else 0

        # Rotate the list k times
        for _ in range(k):
            # Store the last element to move it to the front
            last_Element = nums[-1]

            # Shift all elements to the right by one position
            for index in range(len(nums) - 1, 0, -1):
                nums[index] = nums[index - 1]

            # Place the last element at the front
            nums[0] = last_Element

# Time Complexity: O(k * n)
# - The outer loop runs k times, and for each iteration, we shift n elements.
# - In the worst case, if k is close to n, this can approach O(n^2).

# Space Complexity: O(1)
# - The rotation is done in place, so no extra space proportional to the input size is used.