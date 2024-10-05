# 189. Rotate Array

__Type:__ Medium <br>
__Topics:__ Array, Math, Two Pointers <br>
__Companies:__ Amazon, Google, Microsoft, Bloomberg, Accenture, Meta, Apple, Infosys, tcs, Adobe, Uber, Yahoo, Zoho, Walmart Labs, Goldman Sachs, TikTok, Oracle, Flipkart, Cisco
__Leetcode Link:__ [189. Rotate Array](https://leetcode.com/problems/rotate-array/description/)
<hr>

### Question:
Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.
<hr>

### Examples:

__Example 1:__

__Input:__ nums = [1,2,3,4,5,6,7], k = 3 <br>
__Output:__ [5,6,7,1,2,3,4] <br>
__Explanation:__ <br>
rotate 1 steps to the right: [7,1,2,3,4,5,6] <br>
rotate 2 steps to the right: [6,7,1,2,3,4,5] <br>
rotate 3 steps to the right: [5,6,7,1,2,3,4]

__Example 2:__

__Input:__ nums = [-1,-100,3,99], k = 2 <br>
__Output:__ [3,99,-1,-100] <br>
__Explanation:__ <br>
rotate 1 steps to the right: [99,-1,-100,3] <br>
rotate 2 steps to the right: [3,99,-1,-100]
<hr>

### Constraints:

- <code>1 <= nums.length <= 10<sup>5</sup> </code>
- <code>-2<sup>31</sup> <= nums[i] <= 2<sup>31</sup> - 1</code>
- <code>0 <= k <= 10<sup>5</sup></code>
<hr>

### Hints:
- The easiest solution would use additional memory and that is perfectly fine.
- The actual trick comes when trying to solve this problem without using any additional memory. This means you need to use the original array somehow to move the elements around. Now, we can place each element in its original location and shift all the elements around it to adjust as that would be too costly and most likely will time out on larger input arrays.
- One line of thought is based on reversing the array (or parts of it) to obtain the desired result. Think about how reversal might potentially help us out by using an example.
- The other line of thought is a tad bit complicated but essentially it builds on the idea of placing each element in its original position while keeping track of the element originally in that position. Basically, at every step, we place an element in its rightful position and keep track of the element already there or the one being overwritten in an additional variable. We can't do this in one linear pass and the idea here is based on cyclic-dependencies between elements.