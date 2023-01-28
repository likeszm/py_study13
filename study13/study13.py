#py学习记录13：文件目录操作
"""


"""

import os
import shutil


#1.创建文件夹
"""
os.makedirs('C:/Users/likes/Desktop/temp', exist_ok = True)
"""

#2.删除文件或文件夹
"""
os.remove('C:/Users/likes/Desktop/temp/新建文本文档.txt')

shutil.rmtree('C:/Users/likes/Desktop/temp')
"""

#3.复制文件
"""
shutil.copyfile('C:/Users/likes/Desktop/temp/temp2/1.txt','C:/Users/likes/Desktop/temp/temp2/2.txt')
"""

#4.复制目录
"""
shutil.copytree('C:/Users/likes/Desktop/temp', 'C:/Users/likes/Desktop/temp_2')
"""

#5.修改文件名文件夹名
"""
os.rename('C:/Users/likes/Desktop/temp/temp2/1.txt' , 'C:/Users/likes/Desktop/temp/temp2/1_test.txt')

#文件夹名修改失败，暂未解决，报错为 PermissionError: [WinError 5] 拒绝访问。
os.rename('C:/Users/likes/Desktop/temp' , 'C:/Users/likes/Desktop/temp_3')
"""

#6.判断文件或文件夹是否存在 以及类型

"""
anser1 = os.path.exists('C:/Users/likes/Desktop/temp/temp2/1.txt')
anser2 = os.path.exists('C:/Users/likes/Desktop/temp/temp2/1_test.txt')

print(f'anser1 = {anser1}, anser2 = {anser2}')
"""

"""
anser1 = os.path.isfile('C:/Users/likes/Desktop/temp/temp2/1_test.txt')
anser2 = os.path.isdir('C:/Users/likes/Desktop/temp/temp2')

print(f'anser1 = {anser1}, anser2 = {anser2}')
"""


#7.当前文件目录

"""
#获取当前的工作目录
directory = os.getcwd()
print(f'directory = {directory}')
"""

"""
os.chdir('C:/Users/likes/Desktop/temp')
"""


#8.递归遍历所有文件



#9.目录下的所有文件和子目录名

#10.查找指定扩展名文件和目录

