from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import requests
import os

# 访问页面
# 下载图片
# 翻页
# 记录已下载图片
initUrl = 'http://jandan.net/pic/page-'
saveDir = './pic'
downPage = [2623, 2600]

def get_pic_url(html):
    soup = BeautifulSoup(html, "html.parser")
    rows = soup.find_all("a", class_="view_img_link")
    picUrls = []
    for row in rows:
        url = row['href']
        picUrls.append(url)
    print('urls is ', picUrls)
    return picUrls


def down_pic_by_url(url):
    r = requests.get('http:' + url)
    fileExtensionName = get_pic_url_file_extension_name(url)    # 文件扩展名
    fileName = get_pic_url_file_name(url)   # 文件名
    dirName = nowPage
    savePath = saveDir + '/' + dirName.__str__()
    if not os.path.isdir(savePath):
        os.mkdir(savePath)
    if (fileExtensionName == '.gif'):
        # 文件为gif
        print(url, ' is gif')
    else:
        i = Image.open(BytesIO(r.content))
        i.save(savePath + '/' + fileName)        # 保存文件


def get_pic_url_file_name(url:str):
    return os.path.basename(url)
# 获取url对应的文件名


def get_pic_url_file_extension_name(url:str):
    return os.path.splitext(url)[1]
# 获取url对应文件的扩展名

# 检测文件夹是否存在
if not os.path.isdir(saveDir):
    os.mkdir(saveDir)


for page in range(downPage[1], downPage[0]):
    nowPage = page                          # 当前使用页码
    mainUrl = initUrl + page.__str__()      # 爬取页面地址
    print('url is ', mainUrl)
    r = requests.get(mainUrl)
    picUrls = get_pic_url(r.content)        # 页面获取到的图片地址
    for url in picUrls:
        down_pic_by_url(url)