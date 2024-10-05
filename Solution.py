from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # Function to reverse a portion of the list from left_ptr to right_ptr
        def reverse(left_Ptr: int, right_Ptr: int) -> None:
            while left_Ptr < right_Ptr:
                # Swap elements at left_ptr and right_ptr
                nums[left_Ptr], nums[right_Ptr] = nums[right_Ptr], nums[left_Ptr]
                # Move pointers towards the center
                left_Ptr += 1
                right_Ptr -= 1

        # Step 1: Reverse the entire list
        reverse(0, len(nums) - 1)
        
        # Step 2: Reverse the first k elements (0 to k-1)
        reverse(0, k - 1)
        
        # Step 3: Reverse the remaining elements (k to end)
        reverse(k, len(nums) - 1)

# Time Complexity: O(n)
# - Each of the three reverse operations takes O(n) time in total.
# Space Complexity: O(1)
# - The rotation is done in place, so no additional space proportional to the input size is used.