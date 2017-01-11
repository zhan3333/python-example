import os
print(os.getcwd())  # 获取当前工作目录
print(os.name)      # 获取正在使用的平台  nt: windows， posix:linux
# os.mkdir('testOsDir')     # 创建文件夹
# os.rmdir('testOsDir')     # 删除文件夹
if not os.path.isdir('testOsDir'):
    os.mkdir('testOsDir')

