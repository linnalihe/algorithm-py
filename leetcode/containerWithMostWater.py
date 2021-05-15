# Medium

# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

# Notice that you may not slant the container.

# Example 1:

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1
# Example 3:

# Input: height = [4,3,2,1,4]
# Output: 16
# Example 4:

# Input: height = [1,2,1]
# Output: 2


# Constraints:

# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104

# area is the difference in index position * max of index values

# brute force is a nested for loop that will check each pair and
# keep track of the maxArea found

# start from the left and right and move inward
# this will maximize the diff in index position
# move right pointer if it is shorter else left pointer

# Runtime: 676 ms, faster than 86.83% of Python3 online submissions for Container With Most Water.
# Memory Usage: 27.8 MB, less than 11.38% of Python3 online submissions for Container With Most Water.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(height)-1
        while left < right:
            shorter = height[left] if height[left] < height[right] else height[right]
            area = (right-left)*shorter
            if area > maxArea:
                maxArea = area

            if shorter == height[left]:
                left += 1

            else:
                right -= 1
        return maxArea
