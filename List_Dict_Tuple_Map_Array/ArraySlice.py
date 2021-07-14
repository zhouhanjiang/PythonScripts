#!/usr/bin/python
# -*- coding: utf-8 -*-


from __future__ import division

'''
__Author__:zhouhanjiang
学习Python中的X[:,0]、X[:,1]、X[:,:,0]、X[:,:,1]、X[:,m:n]和X[:,:,m:n]
'''

import numpy as np

def Array_Slice_Test():
    '''
    简单的小实验
    '''
    #二维列表
    data_list=[[1,2,3],
               [1,2,1],
               [3,4,5],
               [4,5,6],
               [5,6,7],
               [6,7,8],
               [6,7,9],
               [0,4,7],
               [4,6,0],
               [2,9,1],
               [5,8,7],
               [9,7,8],
               [3,7,9]]
    # data_list.toarray()
    data_list=np.array(data_list)
    # [ list0[n] list1[n] ...... listm[n] ]
    #二维数组:m*n
    #其中,m为二维数组的长度,n为listX的长度
    # [ [1 2 3] [1 2 1] ...]
    print 'data_list：'+str(data_list)
    #取m索引=0对应的List0[n](列表)
    print 'X[0,:]结果输出为：'
    print data_list[0,:] #[1 2 3]
    #取m索引=1对应的List1[n](列表)
    print 'X[1,:]结果输出为：'
    print data_list[1,:] #[1 2 1]
    #取m索引=Y对应的ListY[n],再切片取listY[n][m,n)的值的组成列表(一维)
    print 'X[Y,m:n]结果输出为：'
    print data_list[0,0:1] #[1]
    print data_list[1,0:2] #[1 2]
    #取所有listX[n]中索引=0的切片的新列表(一维)
    print 'X[:,0]结果输出为：'
    print data_list[:,0] #[1 1 3 4 5 6 6 0 4 2 5 9 3]
    #取所有listX[n]中索引=1的切片的新列表(一维)
    print 'X[:,1]结果输出为：'
    print data_list[:,1] #[2 2 4 5 6 7 7 4 6 9 8 7 7]
    #取所有listX[n]中索引=2的切片的新列表(一维)
    print 'X[:,2]结果输出为：'
    print data_list[:,2] #[3 1 5 6 7 8 9 7 0 1 7 8 9]
    #取所有listX[n]中索引区间[m,n)切片的新列表组成的列表(二维)
    print 'X[:,m:n]结果输出为：'
    print data_list[:,0:1] #[[1][1]...]
    print data_list[:,0:2] #[[1 2][1 2]...]


    #三维列表
    data_list=[[[1,2],[1,0],[3,4],[7,9],[4,0]],
               [[1,4],[1,5],[3,6],[8,9],[5,0]],
               [[8,2],[1,8],[3,5],[7,3],[4,6]],
               [[1,1],[1,2],[3,5],[7,6],[7,8]] ,
               [[9,2],[1,3],[3,5],[7,67],[4,4]],
               [[8,2],[1,9],[3,43],[7,3],[43,0]],
               [[1,22],[1,2],[3,42],[7,29],[4,20]],
               [[1,5],[1,20],[3,24],[17,9],[4,10]],
               [[11,2],[1,110],[3,14],[7,4],[4,2]]]
    data_list=np.array(data_list)
    # [[[list00][list01]...[list0p]]   [[list10][list11]...[list1p]]  ......   [[list(n-1)0][list(n-1)1]...[list(n-1)p]] ]
    #三维矩阵:m*n*p
    #其中m为三维矩阵的长度
    #n为n*p二维数组的长度
    #p为ListXY列表的长度
    # [ [[  1   2][  1   0][  3   4][  7   9][  4   0]]  [[  1   2][  1   0][  3   4][  7   9][  4   0]] ...]
    print 'data_list：'+str(data_list)
    #取三维矩阵中索引号=m的二维数组,即[[listm0],[listm1],...,[listmp]]
    print 'X[m,:,:]结果输出为：'
    print data_list[0,:,:] #[[1 2][1 0][3 4][7 9][4 0]]
    print data_list[0,1,:] #[1 0]
    print data_list[0,1,0] #[1 ]
    print data_list[1,:,:] #[[1 4][1 5][3 6][8 9][5 0]]
    print data_list[1,1,:] #[1 5]
    print data_list[1,1,1] #[ 5]
    #取所有二维数组n*p中listnX组成的新二维数组
    print 'X[:,n,:]结果输出为：'
    print data_list[:,0,:] #[[ 1  2][ 1  4] [ 8  2][ 1  1][ 9  2][ 8  2][ 1 22][ 1  5][11  2]]
    print data_list[:,0,0] #[ 1  1  8  1  9  8  1  1 11]
    print data_list[:,0,1] #[ 2  4  2  1  2  2 22  5  2]
    print data_list[:,1,:] #[[  1   0][  1   5][  1   8][  1   2][  1   3][  1   9][  1   2][  1  20][  1 110]]
    print data_list[:,1,0] #[1 1 1 1 1 1 1 1 1]
    print data_list[:,1,1] #[  0   5   8   2   3   9   2  20 110]
    #取所有二维矩阵n*p中listXY索引为p的值组成的新二维数组
    print 'X[:,:,p]结果输出为：'
    print data_list[:,:,0] #[[ 1  1  3  7  4][ 1  1  3  8  5]...]
    #取三维矩阵中第二维的所有数据
    print data_list[:,:,1] #[[  2   0   4   9   0][  4   5   6   9   0]...]
    #取三维矩阵中第m维到第n-1维的所有数据
    print 'X[:,:,m:n]结果输出为：'
    print data_list[:,:,0:1] #[ [[ 1][ 1][ 3][ 7][ 4]] ...]
    print data_list[:,:,0:2] #[[[  1   2][  1   0][  3   4][  7   9][  4   0]]...]


if __name__ == '__main__':
    Array_Slice_Test()
