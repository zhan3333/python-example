import os
str = '//ww3.sinaimg.cn/large/c0679ecajw1fblsmi338sj20og0ogabs.jpg'
fileName = os.path.basename(str)    # c0679ecajw1fblsmi338sj20og0ogabs.jpg
extension = os.path.splitext(str)         # .jpg
print(fileName)
print(extension)