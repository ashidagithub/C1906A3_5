# -*- coding: UTF-8 -*-

# author by : （学员ID)

# 目的:
# 掌握使用 if 和 for语句

# 实现示例一
print ('\n-----实现示例一-----')
for k in range( 1, 10 ):
    for j in range( 1, 10 ):
        if ( j <= k ):
            s = "{0} x {1} = {2}  ".format(k,j,k*j)
            print(s,end="")
    print()

# 实现示例 二
print ('\n-----实现示例二-----')
for k in range( 1, 10 ):
    for j in range( 1, k+1 ):
        s = "{0} x {1} = {2}  ".format(k,j,k*j)
        print(s,end="")
    print()
