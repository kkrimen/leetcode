You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

题意：数字以逆序存于链表中，求两个数字的和并以链表的形式返回

思路：根据题意，思路比较清晰，只要利用两个指针指向两个链表，并将其每一位进行相加，需要进位则进位