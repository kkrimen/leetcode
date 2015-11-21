Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

题意：求一个数组中其中任意两个数的和为指定值，并按数组顺序输出下表

思路：转变想法，可以理解为求数 num1 和 target - num1 在数组中的下表，自然而然想到用一个哈希表，key为数，value为下表
