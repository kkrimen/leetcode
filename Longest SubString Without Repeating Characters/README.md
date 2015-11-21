Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.

题意：求一个字符串中没有重复字符的最长子字符串的长度

思路：用一个哈希表来记录每一个字符出现的位置（不带重复），遍历字符串，并及时更新每一个字符在哈希表最后出现的下标（要注意更新条件）