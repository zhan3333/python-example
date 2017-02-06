from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import requests
import os

# 脚本实现了煎蛋图片的自动下载
# anchor zhan
# 访问页面
# 下载图片
# 翻页
# 记录已下载图片
initUrl = 'http://jandan.net/ooxx/page-'     # 初始页面
saveDir = './ooxx'                           # 保存文件夹
downPage = {max: 2312, min: 2000}                    # 访问页码


def get_pic_url(html):
    # 从html中获取到需要的图片url
    soup = BeautifulSoup(html, "html.parser")
    rows = soup.find_all("a", class_="view_img_link")
    picUrls = []
    for row in rows:
        url = row['href']
        picUrls.append(url)
    return picUrls


def down_pic_by_url(url):
    # 根据图片地址，下载图片到执行文件夹
    dirName = nowPage                               # 储存文件夹名称
    savePath = saveDir + '/' + dirName.__str__()    # 储存文件夹
    fileExtensionName = get_pic_url_file_extension_name(url)    # 文件扩展名
    fileName = get_pic_url_file_name(url)           # 文件名
    fileSavePath = savePath + '/' + fileName
    # 判断文件是否已经存在
    if os.path.isfile(fileSavePath):
        print('file %s already exist!' % fileSavePath)
        return
    r = requests.get('http:' + url)
    if not os.path.isdir(savePath):
        os.mkdir(savePath)

    f = open(savePath + '/' + fileName, 'wb')
    f.write(r.content)
    f.close()
    # i = Image.open(BytesIO(r.content))
    # i.save(savePath + '/' + fileName)        # 保存文件



def get_pic_url_file_name(url:str):
    # 获取url对应的文件名
    return os.path.basename(url)


def get_pic_url_file_extension_name(url:str):
    # 获取url对应文件的扩展名
    return os.path.splitext(url)[1]

# 开始运行

# 检测文件夹是否存在
if not os.path.isdir(saveDir):
    os.mkdir(saveDir)
print('Has %s page wait access.' % (downPage[max] - downPage[min]))
for pageKey, page in enumerate(range(downPage[min], downPage[max])):
    print('Access page is %s' % pageKey)
    nowPage = page                          # 当前使用页码
    mainUrl = initUrl + page.__str__()      # 爬取页面地址
    print('now page url is ', mainUrl)
    r = requests.get(mainUrl)
    picUrls = get_pic_url(r.content)        # 页面获取到的图片地址
    print('has %s url wait down' % picUrls.__len__())
    for key, url in enumerate(picUrls):
        print('%s pic is download...' % key)
        down_pic_by_url(url)
        print('%s pic is down over!' % key)