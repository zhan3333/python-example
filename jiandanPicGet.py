from bs4 import BeautifulSoup
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
downPage = {max: 2342, min: 2341}                    # 访问页码


def get_pic_urls(html):
    # 从html中获取到需要的图片url数组
    soup = BeautifulSoup(html, "html.parser")
    rows = soup.find_all("a", class_="view_img_link")
    pic_urls = []
    for row in rows:
        pic_url = row['href']
        pic_urls.append(pic_url)
    return pic_urls


def down_pic_by_url(pic_url):
    # 根据图片地址，下载图片到执行文件夹
    save_dir_name = nowPage                               # 储存文件夹名称
    save_path = saveDir + '/' + save_dir_name.__str__()    # 储存文件夹
    file_name = get_pic_url_file_name(pic_url)           # 文件名
    file_save_path = save_path + '/' + file_name
    # 判断文件是否已经存在
    if os.path.isfile(file_save_path):
        print('file %s already exist!' % file_save_path)
        return
    r = requests.get('http:' + pic_url)
    if not os.path.isdir(save_path):
        os.mkdir(save_path)
    # 写入文件
    f = open(save_path + '/' + file_name, 'wb')
    f.write(r.content)
    f.close()


def get_pic_url_file_name(full_url: str):
    # 获取url对应的文件名
    return os.path.basename(full_url)


# 开始运行

# 检测文件夹是否存在
if not os.path.isdir(saveDir):
    os.mkdir(saveDir)
print('Has %s page wait access.' % (downPage[max] - downPage[min]))
for page_num, page in enumerate(range(downPage[min], downPage[max])):
    print('Access page is %s' % page_num)
    nowPage = page                          # 当前使用页码
    mainUrl = initUrl + page.__str__()      # 爬取页面地址
    print('now page url is ', mainUrl)
    r = requests.get(mainUrl)
    picUrls = get_pic_urls(r.content)        # 页面获取到的图片地址
    print('has %s url wait down' % picUrls.__len__())
    for key, url in enumerate(picUrls):
        print('%s pic is download...' % key)
        down_pic_by_url(url)
        print('%s pic is down over!' % key)