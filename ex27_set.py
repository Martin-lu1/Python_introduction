# 0. 请问集合的唯一作用是什么呢？
# 答：集合几乎所有的作用就是确保里边包含的元素的唯一性，
# 就像世界上没有两片完全相同的树叶一样，集合内不可能存在两个相同的元素！
#
# 1. 如果你希望创建的集合是不变的，应该怎么做？
# 答：frozenset()
set1 = {1,2,3,4,5}
set2 = frozenset([1,2,3,4,5])
set1.remove(2)
print(set1)
# set2.remove(2) # 报错
# print(set2)

# 2. 请问如何确定一个集合里边有多少个元素？
# 答：没错，len()函数正好可以满足你此刻的需求^_^
print(len(set1))
# 3. 请目测以下代码会打印什么内容？
# num_set = set([1, 2, 3, 4, 5])
# print(num_set[0])
#
# 答：会报错，因为集合是无序的。
#
# 4. 请问 set1 = {[1, 2]} 和 set1 = set([1, 2]) 执行的结果一样吗？
# 答：不一样，set1 = set([1, 2]) 会生成一个集合{1, 2}，
# 但set1 = {[1, 2]}却会报错。
#
# set1 = {[1, 2]}
# Traceback (most recent call last):
#   File "<pyshell#17>", line 1, in <module>
#     set1 = {[1, 2]}
# TypeError: unhashable type: 'list'
# 从报错信息上我们看到“列表不是可哈希类型”，没错，列表是可变的，
# 它怎么可以哈希呢？！咦，等等，这句话好像在那听过……呃，
# 敢情集合跟字典的存储方式一样的丫！
#
# 其实你再想想就会觉得很有道理，利用哈希函数计算，相同的元素得到的哈希值
# （存放地址）是相同的，所以在集合中所有相同的元素都会覆盖掉，
# 因此有了集合的唯一性。
#
# 然后你继续接着想就觉得更有道理了，通过哈希函数计算的地址不可能是按顺序排放的，
# 所以集合才强调是无序的！
#
# 5. 打开你的IDLE，输入set1 = {1, 1.0}，你发现了什么？
# 答：没错， 集合内容是{1.0}，其实你弄懂了上一题，这一题一样容易：
# 因为在Python的哈希函数会将相同的值的元素计算得到相同的地址，
# 所以1和1.0是等值的^_^
#
# 6. 请问如何给集合添加和删除元素？
# 答：使用add()方法可以为集合添加元素，使用remove()方法可以删除集合中
# 已知的元素。
#
#num1.add(6)
#num1
# {0, 1, 2, 3, 4, 5, 6}
#num1.remove(6)
#num1
# {0, 1, 2, 3, 4, 5}
# 动动手
# 0. 自学扩展：自己花点时间看下这个表格
# （http://bbs.fishc.com/thread-45276-1-1.html），今后会用上的^_^
# 由于集合类型不是我们教学的重点，所以课堂中小甲鱼仅强调基本的使用方法，
# 这里帮大家把Python集合类型的所有内置方法做成一个总结表，
# 以便供大家使用时参考。
#
# 集合类型内建方法总结
#
# 集合（s）.方法名
#
# 等价符号
#
# 方法说明
#
# s.issubset(t)	s <= t	子集测试（允许不严格意义上的子集）：
# s 中所有的元素都是 t 的成员
#  	s < t	子集测试（严格意义上）：s != t
# 而且 s 中所有的元素都是 t 的成员
# s.issuperset(t)	s >= t	超集测试（允许不严格意义上的超集）：
# t 中所有的元素都是 s 的成员
#  	s > t	超集测试（严格意义上）：s != t
# 而且 t 中所有的元素都是 s 的成员
# s.union(t)	s | t	合并操作：s "或" t 中的元素
# s.intersection(t)	s & t	交集操作：s "与" t 中的元素
# s.difference	s - t	差分操作：在 s 中存在，在 t 中不存在的元素
# s.symmetric_difference(t)	s ^ t	对称差分操作：s "或" t 中的元素，
# 但不是 s 和 t 共有的元素
# s.copy()	 	返回 s 的拷贝（浅复制）
# 以下方法仅适用于可变集合
#
#  	 
# s.update	s |= t	将 t 中的元素添加到 s 中
# s.intersection_update(t)	s &= t	交集修改操作：
# s 中仅包括 s 和 t 中共有的成员
# s.difference_update(t)	s -= t	差修改操作：
# s 中包括仅属于 s 但不属于 t 的成员
# s.symmetric_difference_update(t)	s ^= t
# 对称差分修改操作：s 中包括仅属于 s 或仅属于 t 的成员
# s.add(obj)	 	加操作：将 obj 添加到 s
# s.remove(obj)	 	删除操作：将 obj 从 s 中删除，如果 s 中不存在 obj，
# 将引发异常
# s.discard(obj)	 	丢弃操作：将 obj 从 s 中删除，
# 如果 s 中不存在 obj，也没事儿^_^
# s.pop()	 	弹出操作：移除并返回 s 中的任意一个元素
# s.clear()	 	清除操作：清除 s 中的所有元素
# 1.本节课回顾
#num = {}
#type(num)
# <class 'dict'>
#num2 = {1, 2, 3, 4}
#type(num2)
# <class 'set'>
#
# 大括号并不是字典的特权，在Python里，如果用大括号括起一堆没有映射关系的数字时，
# 这一堆数字就是集合。
#
# 集合的特点：（唯一）
#
#num = {1, 1, 2, 2, 3, 4}
#num
# {1, 2, 3, 4}
#
# 集合和字典一样，都是无序的，不支持index。
#
# 如何创建一个集合：
#
# 一种是直接把一堆元素用大括号括起来
#
# 一种是使用工厂函数set()
#
#set1 = set([1, 2, 2, 3, 4])
#set1
# {1, 2, 3, 4}
#set1 = set('I love you')
#set1
# {'I', 'v', 'e', 'o', 'y', 'u', ' ', 'l'}
#
# 搞搞看：去除列表中重复的元素：
#
# [0, 1, 2, 3, 4, 5, 5, 3, 1]
#
# 如果没学习集合，我们会：
#
#num = [0, 1, 2, 3, 4, 5, 5, 3, 1]
#temp = []
#for each in num:
#     if each not in temp:
#         temp.append(each)
#
#         
#temp
# [0, 1, 2, 3, 4, 5]
#
# 使用集合，如下：
#
#num = [0, 1, 2, 3, 4, 5, 5, 3, 1]
#num = list(set(num))
#num
# [0, 1, 2, 3, 4, 5]
#
# 但是要注意，使用集合得到的是无序的。
#
# 如何访问集合中的值：
#
# 可以使用for把集合中的数据一个个读取出来
#
# 可以通过in 和 not in 判断一个元素是否在集合中已经存在。
#
# 内置函数 add() 和 remove()
#
#num = {0, 1, 2, 3, 4, 5}
#num.add(6)
#num
# {0, 1, 2, 3, 4, 5, 6}
#
#num.remove(1)
#num
# {0, 2, 3, 4, 5, 6}
#
# 不可变集合
#
# frozen：冰冻的，冻结的
#
# frozenset() 定义不可变集合
#
#num = frozenset((1, 2, 3, 4, 5))
#num
# frozenset({1, 2, 3, 4, 5})
#num.add(0)
# Traceback (most recent call last):
#   File "<pyshell#34>", line 1, in <module>
#     num.add(0)
# AttributeError: 'frozenset' object has no attribute 'add'
