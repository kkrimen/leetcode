There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

题意：求两个数组中的中位数，要求算法的复杂度为O(log(m+n))

思路：用二分法，数组A取x，则在B中应该取k-x，对比两个值大小，若有A[x] < b[k-x]，则可以舍弃A在x位置左边的部分，B在k-x右边的部分，同时更新k值，一直迭代直到A或者B的大小为0或者k值为1,可以直接求出第k个值得大小。
注意要考虑奇偶数的情况。