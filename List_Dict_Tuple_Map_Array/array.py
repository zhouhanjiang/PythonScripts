#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: array.py
# Author: zhouhanjiang@xunlei.com
# Create: 2021/07/14 10:03
# LastMod: 2021/07/14 10:03

"""
    array.py
"""

import os
# import time

from Utils.logger import get_logger

logger = get_logger(
        os.path.basename(os.path.abspath(__file__)),
        os.path.abspath(__file__),
        level="INFO",
        log_file_max_bytes=1024 * 1024)

# import builtins as __builtin__


def print(*args, **kwargs):
    """
        overwrite print
    """
    # My custom print() function.
    # Adding new arguments to the print function signature
    # is probably a bad idea.
    # Instead consider testing if custom argument keywords
    # are present in kwargs
    # __builtin__.print('My overridden print() function!')
    # return __builtin__.print(*args, **kwargs)
    return logger.info(*args, **kwargs)


'''
__Author__:zhouhanjiang
学习Python中的X[:,0]、X[:,1]、X[:,:,0]、X[:,:,1]、X[:,m:n]和X[:,:,m:n]
'''


class ArraySlice:
    """
        ArraySlice
    """
    def __init__(self):
        import numpy as np
        # 二维列表
        self.d2_list = [[1, 2, 3], [1, 2, 1], [3, 4, 5], [4, 5, 6], [5, 6, 7],
                        [6, 7, 8], [6, 7, 9], [0, 4, 7], [4, 6, 0], [2, 9, 1],
                        [5, 8, 7], [9, 7, 8], [3, 7, 9]]
        self.n_d2_array = np.array(self.d2_list)
        # print("self.n_d2_array="+str(self.n_d2_array))

        # 三维列表
        self.d3_list = [[[1, 2], [1, 0], [3, 4], [7, 9], [4, 0]],
                        [[1, 4], [1, 5], [3, 6], [8, 9], [5, 0]],
                        [[8, 2], [1, 8], [3, 5], [7, 3], [4, 6]],
                        [[1, 1], [1, 2], [3, 5], [7, 6], [7, 8]],
                        [[9, 2], [1, 3], [3, 5], [7, 67], [4, 4]],
                        [[8, 2], [1, 9], [3, 43], [7, 3], [43, 0]],
                        [[1, 22], [1, 2], [3, 42], [7, 29], [4, 20]],
                        [[1, 5], [1, 20], [3, 24], [17, 9], [4, 10]],
                        [[11, 2], [1, 110], [3, 14], [7, 4], [4, 2]]]
        self.n_d3_array = np.array(self.d3_list)
        # print("self.n_d3_array=" + str(self.n_d3_array))

    def __del__(self):
        pass
    
    def n_d2_arry_test(self):
        """
           n_d2_arry_test
        """
        # 二维数组:m*n
        # 其中,m为二维数组的长度,n为listX的长度

        # 取m索引=0对应的List0[n](列表)
        # [1 2 3]
        print('X[0, :]结果输出为：' + str(self.n_d2_array[0, :]))
        # 取m索引=Y对应的ListY[n],再切片取listY[n][m,n)的值的组成列表(一维)
        # [1]
        print('X[0, 0:1]结果输出为：' + str(self.n_d2_array[0, 0:1]))
        # [1 2]
        print('X[0, 0:2]结果输出为：' + str(self.n_d2_array[0, 0:2]))
        # [1 2 3]
        print('X[0, 0:3]结果输出为：' + str(self.n_d2_array[0, 0:3]))
        # 超限截断
        # [1 2 3]
        print('X[0, 0:4]结果输出为：' + str(self.n_d2_array[0, 0:4]))

        # 取m索引=1对应的List1[n](列表)
        # [1 2 1]
        print('X[1, :]结果输出为：' + str(self.n_d2_array[1, :]))
        # 取m索引=Y对应的ListY[n],再切片取listY[n][m,n)的值的组成列表(一维)
        # [1]
        print('X[1, 0:1]结果输出为：' + str(self.n_d2_array[1, 0:1]))
        # [1 2]
        print('X[1, 0:2]结果输出为：' + str(self.n_d2_array[1, 0:2]))
        # [1 2 1]
        print('X[1, 0:3]结果输出为：' + str(self.n_d2_array[1, 0:3]))
        # 超限截断
        # [1 2 1]
        print('X[1, 0:4]结果输出为：' + str(self.n_d2_array[1, 0:4]))

        # 取所有listX[n]中索引=0的切片的新列表(一维)
        # [1 1 3 4 5 6 6 0 4 2 5 9 3]
        print('X[:, 0]结果输出为：' + str(self.n_d2_array[:, 0]))
        # 取所有listX[n]中索引=1的切片的新列表(一维)
        # [2 2 4 5 6 7 7 4 6 9 8 7 7]
        print('X[:, 1]结果输出为：' + str(self.n_d2_array[:, 1]))
        # 取所有listX[n]中索引=2的切片的新列表(一维)
        # [3 1 5 6 7 8 9 7 0 1 7 8 9]
        print('X[:, 2]结果输出为：' + str(self.n_d2_array[:, 2]))
        # 取所有listX[n]中索引=4的切片的新列表(一维)
        # 超限告警: index 4 is out of bounds for axis 1 with size 3
        # print('X[:, 4]结果输出为：' + str(self.n_d2_array[:, 4]))

        # 取所有listX[n]中索引区间[m,n)切片的新列表组成的列表(二维)
        # [[1]
        #  [1]
        #  [3]
        #  [4]
        #  [5]
        #  [6]
        #  [6]
        #  [0]
        #  [4]
        #  [2]
        #  [5]
        #  [9]
        #  [3]]
        print('X[:, 0:1]结果输出为：' + str(self.n_d2_array[:, 0:1]))
        # [[1 2]
        #  [1 2]
        #  [3 4]
        #  [4 5]
        #  [5 6]
        #  [6 7]
        #  [6 7]
        #  [0 4]
        #  [4 6]
        #  [2 9]
        #  [5 8]
        #  [9 7]
        #  [3 7]]
        print('X[:, 0:2]结果输出为：' + str(self.n_d2_array[:, 0:2]))
        # [[1 2 3]
        #  [1 2 1]
        #  [3 4 5]
        #  [4 5 6]
        #  [5 6 7]
        #  [6 7 8]
        #  [6 7 9]
        #  [0 4 7]
        #  [4 6 0]
        #  [2 9 1]
        #  [5 8 7]
        #  [9 7 8]
        #  [3 7 9]]
        print('X[:, 0:3]结果输出为：' + str(self.n_d2_array[:, 0:3]))
        # 超限截断
        # [[1 2 3]
        #  [1 2 1]
        #  [3 4 5]
        #  [4 5 6]
        #  [5 6 7]
        #  [6 7 8]
        #  [6 7 9]
        #  [0 4 7]
        #  [4 6 0]
        #  [2 9 1]
        #  [5 8 7]
        #  [9 7 8]
        #  [3 7 9]]
        print('X[:, 0:4]结果输出为：' + str(self.n_d2_array[:, 0:4]))

    def n_d3_arry_test(self):
        """
           n_d3_arry_test
        """
        # 三维矩阵:m*n*p
        # 其中m为三维矩阵的长度
        # n为n*p二维数组的长度
        # p为ListXY列表的长度

        # 取三维矩阵中索引号=0的二维数组,即[[list00],[list01],...,[list0p]]
        # [[1, 2], [1, 0], [3, 4], [7, 9], [4, 0]]
        print('X[0, :, :]结果输出为：' + str(self.n_d3_array[0, :, :]))
        # [1 0]
        print('X[0, 1, :]结果输出为：' + str(self.n_d3_array[0, 1, :]))
        # 1
        print('X[0, 1, 0]结果输出为：' + str(self.n_d3_array[0, 1, 0]))

        # 取三维矩阵中索引号=1的二维数组,即[[list00],[list01],...,[list0p]]
        # [[1, 4], [1, 5], [3, 6], [8, 9], [5, 0]]
        print('X[1, :, :]结果输出为：' + str(self.n_d3_array[1, :, :]))
        # [1 5]
        print('X[1, 1, :]结果输出为：' + str(self.n_d3_array[1, 1, :]))
        # 1
        print('X[1, 1, 0]结果输出为：' + str(self.n_d3_array[1, 1, 0]))

        # 取所有二维数组n*p中listnX组成的新二维数组
        # [[ 1  2]
        #  [ 1  4]
        #  [ 8  2]
        #  [ 1  1]
        #  [ 9  2]
        #  [ 8  2]
        #  [ 1 22]
        #  [ 1  5]
        #  [11  2]]
        print('X[:, 0, :]结果输出为：' + str(self.n_d3_array[:, 0, :]))
        # [ 1  1  8  1  9  8  1  1 11]
        print('X[:, 0, 0]结果输出为：' + str(self.n_d3_array[:, 0, 0]))
        # [ 2  4  2  1  2  2 22  5  2]
        print('X[:, 0, 1]结果输出为：' + str(self.n_d3_array[:, 0, 1]))
        # 超限报警
        # index 2 is out of bounds for axis 2 with size 2
        # print('X[:, 0, 2]结果输出为：' + str(self.n_d3_array[:, 0, 2]))
        # [[  1   0]
        #  [  1   5]
        #  [  1   8]
        #  [  1   2]
        #  [  1   3]
        #  [  1   9]
        #  [  1   2]
        #  [  1  20]
        #  [  1 110]]
        print('X[:, 1, :]结果输出为：' + str(self.n_d3_array[:, 1, :]))
        # [1 1 1 1 1 1 1 1 1]
        print('X[:, 1, 0]结果输出为：' + str(self.n_d3_array[:, 1, 0]))
        # [  0   5   8   2   3   9   2  20 110]
        print('X[:, 1, 1]结果输出为：' + str(self.n_d3_array[:, 1, 1]))
        # 超限报警
        # index 2 is out of bounds for axis 2 with size 2
        # print('X[:, 1, 2]结果输出为：' + str(self.n_d3_array[:, 1, 2]))

        # 取所有二维矩阵n*p中listXY索引为p的值组成的新二维数组
        # [[ 1  1  3  7  4]
        #  [ 1  1  3  8  5]
        #  [ 8  1  3  7  4]
        #  [ 1  1  3  7  7]
        #  [ 9  1  3  7  4]
        #  [ 8  1  3  7 43]
        #  [ 1  1  3  7  4]
        #  [ 1  1  3 17  4]
        #  [11  1  3  7  4]]
        print('X[:, :, 0]结果输出为：' + str(self.n_d3_array[:, :, 0]))
        #  [[[ 1][ 1][ 3][ 7][ 4]]
        #   [[ 1][ 1][ 3][ 8][ 5]]
        #   [[ 8][ 1][ 3][ 7][ 4]]
        #   [[ 1][ 1][ 3][ 7][ 7]]
        #   [[ 9][ 1][ 3][ 7][ 4]]
        #   [[ 8][ 1][ 3][ 7][43]]
        #   [[ 1][ 1][ 3][ 7][ 4]]
        #   [[ 1][ 1][ 3][17][ 4]]
        #   [[11][ 1][ 3][ 7][ 4]]]
        print('X[:, :, 0:1]结果输出为：' + str(self.n_d3_array[:, :, 0:1]))
        # [[[1 2][1 0][3 4][7 9][4 0]]
        #  [[1 4][1 5][3 6][8 9][5 0]]
        #  [[8 2][1 8][3 5][7 3][4 6]]
        #  [[1 1][1 2][3 5][7 6][7 8]]
        #  [[9 2][1 3][3 5][7  67][4 4]]
        #  [[8 2][1 9][3 43][7 3][43 0]]
        #  [[1  22][1 2][3 42][7  29][4 20]]
        #  [[1 5][1  20][3 24][17 9][4 10]]
        #  [[11 2][1 110][3 14][7 4][4 2]]]
        print('X[:, :, 0:2]结果输出为：' + str(self.n_d3_array[:, :, 0:2]))
        # 超限截断
        # [[[1 2][1 0][3 4][7 9][4 0]]
        #  [[1 4][1 5][3 6][8 9][5 0]]
        #  [[8 2][1 8][3 5][7 3][4 6]]
        #  [[1 1][1 2][3 5][7 6][7 8]]
        #  [[9 2][1 3][3 5][7  67][4 4]]
        #  [[8 2][1 9][3 43][7 3][43 0]]
        #  [[1  22][1 2][3 42][7  29][4 20]]
        #  [[1 5][1  20][3 24][17 9][4 10]]
        #  [[11 2][1 110][3 14][7 4][4 2]]]
        print('X[:, :, 0:3]结果输出为：' + str(self.n_d3_array[:, :, 0:3]))
        # [[  2   0   4   9   0]
        #  [  4   5   6   9   0]
        #  [  2   8   5   3   6]
        #  [  1   2   5   6   8]
        #  [  2   3   5  67   4]
        #  [  2   9  43   3   0]
        #  [ 22   2  42  29  20]
        #  [  5  20  24   9  10]
        #  [  2 110  14   4   2]]
        print('X[:, :, 1]结果输出为：' + str(self.n_d3_array[:, :, 1]))
        # []
        print('X[:, :, 1:1]结果输出为：' + str(self.n_d3_array[:, :, 1:1]))
        # [[[2][0][4][9][0]]
        #  [[4][5][6][9][0]]
        #  [[2][8][5][3][6]]
        #  [[1][2][5][6][8]]
        #  [[2][3][5][67][4]]
        #  [[2][9][43][3][0]]
        #  [[22][2][42][29][20]]
        #  [[5][20][24][9][10]]
        #  [[2][110][14][4][2]]]
        print('X[:, :, 1:2]结果输出为：' + str(self.n_d3_array[:, :, 1:2]))


if __name__ == '__main__':
    a_s = ArraySlice()
    # a_s.n_d2_arry_test()
    a_s.n_d3_arry_test()
