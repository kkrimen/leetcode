Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

题意：给一个字符串，找出并输出其中最长的回文子字符串，其中只存在一个最长的回文子字符串

网上的解法：
1. 预处理字符串，将原始字符串在每个字符之间加上"#"，这样可以不用考虑字符串的奇偶性，然后再前后加上两个哨兵"$"和"@"，防止溢出
2. 定义一个center和一个reach，center指当前发现的最长回文字符串的中心位置，reach则表示这个回文字符串的最右边的位置。
3. 维护一个字典，记录以下表i为中心的单向回文的长度，如：tmpMap[3] = 2，以第四个字符为中心的回文长度是 2*2 = 4。
4. 核心步骤：用于维护第三步中的字典。
    首先在检索i的时候，先找到i在center左边的镜像点mirrori，如果以mirrori为中心的回文串长度在center的边界之内，那么i为中心的回文串也是在center的范围内。
    而如果i在reach的右边或者mirrori为中心的回文串超过了center的边界，那么就需要对i进行拓展，最后得出了所有的tmpMap[i]，就可以得到最长的回文串了。
