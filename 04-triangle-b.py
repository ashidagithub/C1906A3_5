# -*- coding: UTF-8 -*-

# author by : （学员ID)

# 目的：
# 掌握嵌套 if 以及 and 和 or 的用法

# 练习二
# 枚举1-10 之间，可能组成三角形的一组数
print('\n----华丽分割线 练习二 -----')
count0 = 0  # 总共尝试组合的三角形个数
count1 = 0  # 无法组成三角形的计数器
count2 = 0  # 等腰三角形计数器
count3 = 0  # 等边三角形计数器
count4 = 0  # 不等边三角形计数器

for a in range(1, 11):
    for b in range(1, 11):
        for c in range(1,11):
            count0 = count0 + 1
            if (a + b >= c) and (a + c >= b) and (b + c >= a):
                if (abs(a - b) >= c) or (abs(a - c) >= b) or (abs(b - c) >=a):
                    # print("{0},{1},{2} 错误！某两边之差大于第三边，所以无法组成三角形。".format(a,b,c))
                    count1 = count1 + 1
                else:
                    if (a==b) or (b==c) or (a==c):
                        if (a==b) and (b==c) and (a==c):
                            # print('{0},{1},{2} 正确！可以组成等边三角形。'.format(a,b,c))
                            count3 = count3 + 1
                        else:
                            # print('{0},{1},{2} 正确！可以组成等腰三角形。'.format(a,b,c))
                            count2 = count2 + 1
                    else:
                        print('{0},{1},{2} 正确！可以组成不等边三角形！'.format(a,b,c))
                        count4 = count4 + 1
            else:
                # print("{0},{1},{2} 错误！某两边之和小于第三边，所以无法组成三角形。".format(a,b,c))
                count1 = count1 + 1

print('------统计结果输出------')
print('总共尝试了 {0} 次组合。'.format(count0))
print('无法组成三角形的组合有 {0} 个，占比{1}%'.format(count1, count1/count0*100))
print('等腰三角形的组合有{0}个，占比{1}%'.format(count2,count2/count0*100))
print('等边三角形的组合有{0}个，占比{1}%'.format(count3,count3/count0*100))
print('不等边三角形的组合有{0}个，占比{1}%'.format(count4,count4/count0*100))
