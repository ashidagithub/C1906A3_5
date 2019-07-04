# -*- coding: UTF-8 -*-

# author by : （学员ID)

# 目的：
# 掌握嵌套 if 以及 and 和 or 的用法

# 枚举可能组成三角形的一组数
# 如果该数组可以组成三角形，计算出其面积，并写入文件
print('\n----华丽分割线 练习三 -----')

# 打开文件准备写入
filename = "trialgle-result.txt"
f = open(filename, 'w')  # 先清空文件内容
text2write = "--------清空之前的结果，准备写入新的结果-----\n"
f.write(text2write)

# 变量初始化
count0 = 0  # 总共尝试组合的三角形个数
count1 = 0  # 无法组成三角形的计数器
count2 = 0  # 等腰三角形计数器
count3 = 0  # 等边三角形计数器
count4 = 0  # 不等边三角形计数器

text2write = ""  # 准备写入文件的字符串

area_max = 0            # 最大面积初始值
area_min = 999999999999 # 最小面积初始值
area_total = 0          # 所有三角形的面积

max_len = 5

# 暴力循环尝试
for a in range(1, max_len):
    for b in range(a, max_len):
        for c in range(b, max_len):
            count0 = count0 + 1
            if (a + b > c) and (a + c > b) and (b + c > a):
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
                        text2write = '{0},{1},{2} 正确！可以组成不等边三角形！'.format(a,b,c)
                        print(text2write)
                        # f.write(text2write)
                        count4 = count4 + 1
                        # 以下计算面积并评估最大最小值
                        # 计算半周长
                        p = (a + b + c) / 2
                        # 计算面积
                        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
                        # 记录最大和最小面积的三角形
                        if area > area_max:
                            area_max = area
                        if area < area_min:
                            area_min = area
                        # 汇总所有三角形的面积
                        area_total += area

                        # 写入文件
                        text2write = "在第【%d】次组合时找到第【%d】个不等边三角形，a=(%d),b=(%d),c=(%d), 面积为（%f）\n" \
                                     % (count0, count4, a, b, c, area)
                        f.write(text2write)
                        # --------
            else:
                # print("{0},{1},{2} 错误！某两边之和小于第三边，所以无法组成三角形。".format(a,b,c))
                count1 = count1 + 1

print('------统计结果输出------')
text2write = '总共尝试了 {0} 次组合。'.format(count0)
print(text2write)
f.write(text2write)

text2write = '无法组成三角形的组合有 %d 个，占比%0.2f%%' % (count1, count1/count0*100)
print(text2write)
f.write(text2write)

text2write = '等腰三角形的组合有 %d 个，占比 %0.2f%%'.format(count2,count2/count0*100)
print(text2write)
f.write(text2write)

text2write = '等边三角形的组合有 %d 个，占比 %0.2f%%'.format(count3,count3/count0*100)
print(text2write)
f.write(text2write)

text2write = '不等边三角形的组合有 %d 个，占比 %0.2f%%'.format(count4,count4/count0*100)
print(text2write)
f.write(text2write)

text2write = "最大的三角形面积为（%0.2f），最小的三角形面积为（%0.2f），所有三角形总面积为(%0.2f)，平均面积为（%0.2f）\n" \
             % (area_max, area_min, area_total, area_total/count4)
print(text2write)
f.write(text2write)

# 关闭文件
f.close()
