# -*- coding: UTF-8 -*-

# author by : （学员ID)

# 目的:
# 掌握使用 if 和 for语句
# 验证费马大定理 2

import math

# 定义解的上限
limit = 100

# 定义计数器
count = 0

# 定义幂
n = 3

# 打开记录文件
# 写文件
filename = "flt-b-result.txt"
f = open(filename, 'w')  # write 方式第一次写一行
s = '----方程组 a^{0}+b^{1}=c^{2} 的所有正整数解及解的总个数, a,b,c均小于 {3}\n'.format(n,n,n,limit)
f.write(s)

# 如果 j 和 k 的平方和，再开根为整数，则找到解
for j in range(1, limit+1):
    for k in range(j, limit+1):
        sum = math.pow(j,n) + math.pow(k,n)
        sroot = math.pow(sum, 1/n)
        if (sroot % 1)==0:
        # if (sroot % 1)<0.001:
            count = count + 1
            s = '找到解：%d^%d + %d^%d = %d^%d\n' % (j,n,k,n,sroot,n)
            print (s)
            f.write(s)

# 输出解的总个数
s = '总计找到 {0} 个解'.format(count)
print(s)
f.write(s)

# 关闭文件
f.close()
