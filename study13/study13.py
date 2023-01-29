#py学习记录13：文件目录操作
"""
利用 os 和 shutil 两个库可以实现基本的文件目录操作

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
"""
#第一种，只获取清单
file_list = []
dirs_list = []

for (dirpath, dirnames, filenames) in os.walk('C:/Users/likes/Desktop/temp') :
    file_list += filenames
    dirs_list += dirnames

print(file_list)
print(dirs_list)

#第二种，获取完整路径
for (dirpath, dirnames, filenames) in os.walk('C:/Users/likes/Desktop/temp'):
    for fn in filenames:
        # 把 dirpath 和 每个文件名拼接起来 就是全路径
        fpath = os.path.join(dirpath, fn)

        print(fpath)
"""


#9.目录下的所有文件和子目录名,获取当前目录下的列表
"""
targetDir = r'C:/Users/likes/Desktop/temp_2'
file_list = os.listdir(targetDir)

print(file_list)
"""


#10.查找指定扩展名文件和目录
import glob

exec_list = glob.glob('C:/Users/likes/Desktop/temp_2/temp2/*.txt')
print(exec_list)