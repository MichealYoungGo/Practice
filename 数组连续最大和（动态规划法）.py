# -*- coding: utf-8 -*-
# @Time    : 2018/11/30 0030 上午 9:45
# @Author  : 杨宏兵
# @File    : 数组连续最大和（动态规划法）.py
# @Software: PyCharm
def maxSubArrey(arr):
    if arr == None or len(arr) < 1:
        print('参数不合法')
        return
    n = len(arr)
    End = [None] * n
    All = [0] * n
    End[n-1] = arr[n-1]
    All[n-1] = arr[n-1]
    End[0] = All[0] = arr[0]
    i = 1
    while i < n:
        End[i] = max(End[i-1]+arr[i], arr[i])
        All[i] = max(End[i], All[i-1])
        i += 1
    return All[n-1]

if __name__ == '__main__':
    arr = [1, -2, 4, 8, -4, 7, -1, -5]
    print('连续最大和为'+str(maxSubArrey(arr)))