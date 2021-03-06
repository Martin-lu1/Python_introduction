# 0.
# 请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！
# 介绍跟Python的文件相关且十分有用的模块。模块是什么？
# 模块是一个包含你定义的函数和变量的文件，后缀是.py，
# 模块可以做到被别的程序所引入，以使用该模块中的函数等功能。
#
# OS模块（Operating System操作系统）
#
# 对于文件系统的访问来说，Python一般是提供OS模块来实现就可以了，
# 我们所知道常用的操作系统有：Windows，Mac OS，Linux，UNIX等，
# 这些操作系统底层由于文件系统的访问工作原理不同，
# 因此你可能就要针对不同的系统来考虑使用哪些文件系统模块....
# 这样的做法是非常不友好且麻烦的，因为这样就意味着当你的程序运行环境一改变，
# 你就要相应的去修改大量的代码来应付。但是我们的Python是跨平台的，
# 所以Python就有了这个OS模块。
#
# 有了OS模块，我们不需要关心什么操作系统下使用什么模块，
# OS模块会帮你选择正确的模块并调用。
#
# os模块中关于文件 / 目录常用的函数使用方法
# 函数名       使用方法
# getcwd()    返回当前工作目录
# chdir(path) 改变工作目录
# listdir(path='.') 列举指定目录中的文件名（'.'表示当前目录，'..'表示上一级目录）
# mkdir(path) 创建单层目录，如该目录已存在抛出异常
# makedirs(path) 递归创建多层目录，如该目录已存在抛出异常，注意：'E:\\a\\b' 和
# 'E:\\a\\c' 并不会冲突
# remove(path) 删除文件
# rmdir(path) 删除单层目录，如该目录非空则抛出异常
# removedirs(path) 递归删除目录，从子目录到父目录逐层尝试删除，遇到目录非空则抛出异常
# rename(old, new) 将文件old重命名为new
# system(command) 运行系统的shell命令
# walk(top) 遍历top路径以下所有的子目录，返回一个三元组：(路径, [包含目录],
# [包含文件])【具体实现方案请看：第30讲课后作业 ^ _ ^】
# 以下是支持路径操作中常用到的一些定义，支持所有平台
# os.curdir 指代当前目录（'.'）
# os.pardir 指代上一级目录（'..'）
# os.sep 输出操作系统特定的路径分隔符（Win下为 '\\'，Linux下为 '/'）
# os.linesep 当前平台使用的行终止符（Win下为'\r\n'，Linux下为 '\n'）
# os.name 指代当前使用的操作系统（包括：'posix','nt', 'mac', 'os2', 'ce', 'java'）
# os.path模块中关于路径常用的函数使用方法
# 函数名            使用方法
#
# basename(path)    去掉目录路径，单独返回文件名
# dirname(path)     去掉文件名，单独返回目录路径
# join(path1[, path2[, ...]])    将path1, path2各部分组合成一个路径名
# split(path) 分割文件名与路径，返回(f_path, f_name) 元组。如果完全使用目录，
# 它也会将最后一个目录作为文件名分离 且不会判断文件或者目录是否存在
# splitext(path) 分离文件名与扩展名，返回(f_name, f_extension)元组
# getsize(file) 返回指定文件的尺寸，单位是字节
# getatime(file) 返回指定文件最近的访问时间（浮点型秒数，
# 可用time模块的gmtime()或localtime() 函数换算）
# getctime(file) 返回指定文件的创建时间（浮点型秒数，
# 可用time模块的gmtime()或localtime() 函数换算）
# getmtime(file) 返回指定文件最新的修改时间（浮点型秒数，可用time模块的gmtime()
# 或localtime() 函数换算）
# 以下为函数返回 True 或 False
#
# exists(path) 判断指定路径（目录或文件）是否存在
# isabs(path) 判断指定路径是否为绝对路径
# isdir(path) 判断指定路径是否存在且是一个目录
# isfile(path) 判断指定路径是否存在且是一个文件
# islink(path) 判断指定路径是否存在且是一个符号链接（在windows上即为快捷方式）
# ismount(path) 判断指定路径是否存在且是一个挂载点
# samefile(path1, paht2) 判断path1和path2两个路径是否指向同一个文件
# 动动手
# 0.
# 编写一个程序，统计当前目录下每个文件类型的文件数，程序实现如图：
import os
import sys
all_files = os.listdir(os.curdir)
type_file = dict()
for each in all_files:
    if os.path.isdir(each):
        type_file.setdefault('文件夹',0) # 设置默认字典关键字
        type_file['文件夹'] += 1
    f_name,f_extension = os.path.splitext(each)
    if f_extension in type_file:
        type_file[f_extension] += 1
    else:
        type_file[f_extension] = 1
# print(type_file)
####################################################################
#
# import os
#
all_files = os.listdir(os.curdir)  # 使用os.curdir表示当前目录更标准
type_dict = dict()

for each_file in all_files:
    if os.path.isdir(each_file):
        type_dict.setdefault('文件夹', 0)
        type_dict['文件夹'] += 1
    else:
        ext = os.path.splitext(each_file)[1]
        type_dict.setdefault(ext, 0)
        type_dict[ext] += 1

# for each_type in type_dict.keys():
#     print('该文件夹下共有类型为【%s】的文件 %d 个' % (each_type, type_dict[each_type]))
# 2.打印当前文件夹文件及大小
# import os
#
# all_files = os.listdir(os.curdir)  # 使用os.curdir表示当前目录更标准
# file_dict = dict()
#
# for each_file in all_files:
#     if os.path.isfile(each_file):
#         file_size = os.path.getsize(each_file)
#         file_dict[each_file] = file_size
#
# for each in file_dict.items():
#     print('%s【%dBytes】' % (each[0], each[1]))
# 2.
# 编写一个程序，用户输入文件名以及开始搜索的路径，搜索该文件是否存在。
# 如遇到文件夹，则进入文件夹继续搜索，程序实现如图：
# import os
# def search_file1(start_dir,target):
#     os.chdir(start_dir)
#     for each in os.listdir(os.curdir):
#         if each == target:
#             print(os.getcwd() + os.sep + each)
#         else:
#             if os.path.isdir(each):
#                 search_file1(each,target)
#                 os.chdir(os.pardir)
# start_dir = input('请输入待查找的初始目录：')
# target = input('请输入需要查找的目标文件：')
# search_file1(start_dir, target)
#############################################
# import os
# def search_file(start_dir, target):
#     os.chdir(start_dir)
#     for each_file in os.listdir(os.curdir):
#         if each_file == target:
#             print(os.getcwd() + os.sep + each_file)  # 使用os.sep是程序更标准
#         if os.path.isdir(each_file):
#             search_file(each_file, target)  # 递归调用
#             os.chdir(os.pardir)  # 递归调用后切记返回上一层目录
#             print(os.getcwd() + os.sep )
# start_dir = input('请输入待查找的初始目录：')
# target = input('请输入需要查找的目标文件：')
# search_file(start_dir, target)
# 3.
# 编写一个程序，用户输入开始搜索的路径，查找该路径下（包含子文件夹内）
# 所有的视频格式文件（要求查找mp4 rmvb, avi的格式即可），
# 并把创建一个文件（vedioList.txt）存放所有找到的文件的路径，程序实现如图：
# import os
# vedioList = []
# def search_vedio(start_dir):
#     os.chdir(start_dir)
#     for each in os.listdir(os.curdir):
#         if os.path.isdir(each):
#             search_vedio(each)
#             os.chdir(os.pardir)
#         else:
#             f_name,f_extension =  os.path.splitext(each)
#             if f_extension in ['.mp4','.rmvb','.avi']:
#                 vedioList.append(os.getcwd() + os.sep + each)
# start = input("请输入开始搜索的文件夹：")
# search_vedio(start)
# print(vedioList)
##############################################################
#
# import os
#
#
# def search_file(start_dir, target):
#     os.chdir(start_dir)
#
#     for each_file in os.listdir(os.curdir):
#         ext = os.path.splitext(each_file)[1]
#         if ext in target:
#             vedio_list.append(os.getcwd() + os.sep + each_file + os.linesep)  # 使用os.sep是程序更标准
#         if os.path.isdir(each_file):
#             search_file(each_file, target)  # 递归调用
#             os.chdir(os.pardir)  # 递归调用后切记返回上一层目录
#
#
# start_dir = input('请输入待查找的初始目录：')
# program_dir = os.getcwd()
#
# target = ['.mp4', '.avi', '.rmvb']
# vedio_list = []
#
# search_file(start_dir, target)
#
# f = open(program_dir + os.sep + 'vedioList.txt', 'w')
# f.writelines(vedio_list)
# f.close()
# 4.
# 编写一个程序，用户输入关键字，查找当前文件夹内（如果当前文件夹内包含文件夹，
# 则进入文件夹继续搜索）所有含有该关键字的文本文件（.txt后缀），
# 要求显示该文件所在的位置以及关键字在文件中的具体位置（第几行第几个字符），
# 程序实现如图：
import os
location = {}
def keyWord(start_dir,word):
    os.chdir(start_dir)
    for each in os.listdir(os.curdir):
        if os.path.isdir(each):
            keyWord(each,word)
            os.chdir(os.pardir)
        else:
            if os.path.splitext(each)[1] == '.txt':
                file = open(each,encoding='utf8')
                count = 0
                for each_line in file:
                    count += 1
                    if word in each_line:
                        # 解决字典变列表问题
                        location.setdefault(os.getcwd() + os.sep + each,"第" + str(count) + "行第" + str(each_line.index(word) + 1) + "个字符")
                        # 要求字典非空，否则会被视作列表
                        # location[os.getcwd() + os.sep + each] = "第" + str(count) + "行第" + str(each_line.index(word) + 1) + "个字符"
                file.close()
start = input("请输入要查找的文件夹：")
Word = input("请输入要查找的词：")
keyWord(start,Word)
for each_loc in location:
    print(each_loc,location[each_loc])
'''列表属性测试'''
# location = {1:2}
# def loc():
#    for each in range(10):
#        location[each] = each
# loc()
# print(location)
###################3#################################
# import os
#
#
# def print_pos(key_dict):
#     keys = key_dict.keys()
#     keys = sorted(keys)  # 由于字典是无序的，我们这里对行数进行排序
#     for each_key in keys:
#         print('关键字出现在第 %s 行，第 %s 个位置。' % (each_key, str(key_dict[each_key])))
#
#
# def pos_in_line(line, key):
#     pos = []
#     begin = line.find(key)
#     while begin != -1:
#         pos.append(begin + 1)  # 用户的角度是从1开始数
#         begin = line.find(key, begin + 1)  # 从下一个位置继续查找
#
#     return pos
#
#
# def search_in_file(file_name, key):
#     f = open(file_name)
#     count = 0  # 记录行数
#     key_dict = dict()  # 字典，用户存放key所在具体行数对应具体位置
#
#     for each_line in f:
#         count += 1
#         if key in each_line:
#             pos = pos_in_line(each_line, key)  # key在每行对应的位置
#             key_dict[count] = pos
#
#     f.close()
#     return key_dict
#
#
# def search_files(key, detail):
#     all_files = os.walk(os.getcwd())
#     txt_files = []
#
#     for i in all_files:
#         for each_file in i[2]:
#             if os.path.splitext(each_file)[1] == '.txt':  # 根据后缀判断是否文本文件
#                 each_file = os.path.join(i[0], each_file)
#                 txt_files.append(each_file)
#
#     for each_txt_file in txt_files:
#         key_dict = search_in_file(each_txt_file, key)
#         if key_dict:
#             print('================================================================')
#             print('在文件【%s】中找到关键字【%s】' % (each_txt_file, key))
#             if detail in ['YES', 'Yes', 'yes']:
#                 print_pos(key_dict)
#
#
# key = input('请将该脚本放于待查找的文件夹内，请输入关键字：')
# detail = input('请问是否需要打印关键字【%s】在文件中的具体位置（YES/NO）：' % key)
# search_files(key, detail)
